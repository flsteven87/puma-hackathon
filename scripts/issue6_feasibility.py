"""Reproduce issue-6 aggregate source checks without emitting building identities.

Inputs are local original downloads, kept outside Git. See the topic's broad
discovery audit for URLs, dates, terms, reference rule and interpretation limits.
Requires pdftotext; the optional archive check uses only Python's standard library.
"""

import argparse
from collections import Counter, defaultdict
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import unicodedata
import xml.etree.ElementTree as ET


SOURCE_HASHES = {
    "organisations": "a6e3883a772aa0caee72b754c495a28a98116e99e6c0404879f84818bb1ed245",
    "unregistered": "0b75c68c602dafc21858e374ac6183ca212fab28c913b19250403b3f147d7225",
}
FIELDS = ["執照號碼", "核發日期", "行政區代碼（編碼）", "行政區", "管委會名稱", "管委會設置地址"]
ARCHIVE_MANIFEST_SHA256 = "d5bf4cfc5b8d41d8310be784dd1c810d48343df6ad83f2fbf2c1e497c7e04233"
LIST_ROW = re.compile(
    r"^\s*(\d+)\s+(\d{3}使字第\d{4}號)\s+(\S+區)\s+(.+?)\s+(\d+)\s+(\d+)\s+(\d+)\s*$",
    re.MULTILINE,
)


def checked_bytes(path, source):
    data = path.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest != SOURCE_HASHES[source]:
        raise ValueError(f"{source}: source changed; audit the new release before comparing")
    return data


def address_key(address):
    """Only width/space/city-prefix normalization; never geocode or fuzzy-match."""
    value = unicodedata.normalize("NFKC", address)
    return re.sub(r"\s+", "", re.sub(r"^(臺北市|台北市)", "", value))


def official_comparison(org_path, list_path):
    reader = csv.DictReader(io.StringIO(checked_bytes(org_path, "organisations").decode("utf-8-sig")))
    if reader.fieldnames != FIELDS:
        raise ValueError("Unexpected organisation CSV fields")
    raw_rows = list(reader)
    if any(None in row or any(value is None for value in row.values()) for row in raw_rows):
        raise ValueError("Malformed CSV row")
    org_rows = [row for row in raw_rows if any(value.strip() for value in row.values())]
    checked_bytes(list_path, "unregistered")
    text = subprocess.run(
        ["pdftotext", "-layout", str(list_path), "-"], check=True, capture_output=True, text=True
    ).stdout
    listed = [match.groups() for match in LIST_ROW.finditer(text)]
    if [int(row[0]) for row in listed] != list(range(1, len(listed) + 1)) or not listed:
        raise ValueError("PDF rows are missing, repeated or out of sequence")
    list_ids = {row[1] for row in listed}
    if len(list_ids) != len(listed):
        raise ValueError("Repeated permit IDs in the scoped list")
    org_by_permit = defaultdict(list)
    for row in org_rows:
        org_by_permit[row["執照號碼"]].append(row)
    overlaps = [row for row in listed if row[1] in org_by_permit]
    comparisons = [
        (listed_row, org_row)
        for listed_row in overlaps
        for org_row in org_by_permit[listed_row[1]]
    ]
    permit_counts = Counter(row["執照號碼"] for row in org_rows)
    return {
        "source_sha256": SOURCE_HASHES,
        "reference_rule": "Exact use-permit ID intersection; it does not establish a shared building or management scope",
        "organisation_csv": {
            "raw_rows": len(raw_rows),
            "entirely_blank_rows": len(raw_rows) - len(org_rows),
            "nonempty_rows": len(org_rows),
            "distinct_nonempty_rows": len({tuple(row.values()) for row in org_rows}),
            "distinct_permit_ids": len(org_by_permit),
            "repeated_permit_id_groups": sum(count > 1 for count in permit_counts.values()),
            "missing_fields_in_nonempty_rows": {
                field: sum(not row[field].strip() for row in org_rows) for field in FIELDS
            },
        },
        "scoped_unregistered_list": {
            "rows": len(listed), "distinct_permit_ids": len(list_ids),
            "minimum_storeys": min(int(row[4]) for row in listed),
            "maximum_storeys": max(int(row[4]) for row in listed),
        },
        "permit_id_intersection": {
            "permit_ids": len(overlaps), "record_pairs": len(comparisons),
            "district_disagreements": sum(row[2] != org["行政區"] for row, org in comparisons),
            "different_representative_addresses": sum(
                address_key(row[2] + row[3]) != address_key(org["管委會設置地址"])
                for row, org in comparisons
            ),
            "organisation_names_ending_in_manager_label": sum(
                org["管委會名稱"].endswith("管理負責人") for _, org in comparisons
            ),
            "action": "Verify identity, management scope, organisation type and current record before transferring status",
        },
        "nonintersecting_list_permit_ids": len(list_ids - org_by_permit.keys()),
        "nonintersection_meaning": "No matching registration row in this snapshot; not proof that no organisation exists",
        "simulated_inputs": 0,
    }


def archive_audit(directory):
    """Read original archived XML directly; filenames are not year filters."""
    by_permit = defaultdict(list)
    manifests = []
    for path in sorted(directory.glob("*.xml")):
        manifests.append((path.name, hashlib.sha256(path.read_bytes()).hexdigest()))
        for _, element in ET.iterparse(path, events=("end",)):
            if element.tag != "執照":
                continue
            values = {
                "issue": (element.findtext("發照日期") or "").strip(),
                "type": (element.findtext("建造類別") or "").strip(),
                "structure": (element.findtext("構造種類") or "").strip(),
                "floors": tuple((node.text or "").strip() for node in element.findall("建物資訊/地上層數")),
                "completion": (element.findtext("竣工日期") or "").strip(),
                "addresses": tuple((node.text or "").strip() for node in element.findall("全建築地點/建築地點")),
                "lots": tuple((node.text or "").strip() for node in element.findall("全地段地號/地段地號")),
            }
            by_permit[element.attrib.get("號碼", "").strip()].append(values)
            element.clear()
    if not manifests or "" in by_permit:
        raise ValueError("No archived XML files or missing permit identifier")
    manifest_digest = hashlib.sha256(
        json.dumps(manifests, ensure_ascii=False, separators=(",", ":")).encode()
    ).hexdigest()
    if manifest_digest != ARCHIVE_MANIFEST_SHA256:
        raise ValueError("Archived source set changed; audit it before comparing")
    duplicates = [rows for rows in by_permit.values() if len(rows) > 1]
    digest_counts = Counter(digest for _, digest in manifests)
    records = [row for rows in by_permit.values() for row in rows]
    return {
        "xml_files": len(manifests), "records": len(records), "distinct_permit_ids": len(by_permit),
        "duplicate_permit_id_groups": len(duplicates),
        "conflicting_extracted_field_groups": sum(
            len({json.dumps(row, sort_keys=True, ensure_ascii=False) for row in rows}) > 1
            for rows in duplicates
        ),
        "identical_file_digest_groups": sum(count > 1 for count in digest_counts.values()),
        "archive_file_manifest_sha256": manifest_digest,
        "records_with_completion": sum(bool(row["completion"]) for row in records),
        "records_with_positive_integer_floor": sum(
            bool(row["floors"]) and all(value.isdigit() and int(value) > 0 for value in row["floors"])
            for row in records
        ),
        "current_building_survival": "not checked",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--organisations", type=Path, required=True)
    parser.add_argument("--unregistered", type=Path, required=True)
    parser.add_argument("--archive-dir", type=Path)
    args = parser.parse_args()
    result = official_comparison(args.organisations, args.unregistered)
    if args.archive_dir:
        result["historical_archive"] = archive_audit(args.archive_dir)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
