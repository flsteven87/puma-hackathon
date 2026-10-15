# 臺北市政問題研究

我們從市民的實際困擾出發，研究臺北市政問題，釐清現行做法、公開資料與資訊缺口。

研究起點是[市政 debug松](https://puma.taipei/hackathon)，由沈伯洋競選辦公室主辦。本專案獨立維護，與主辦單位沒有合作關係。

## 先看這兩份報告

- [研究總覽](https://flsteven87.github.io/puma-hackathon/research-report.html)：研究方法、活動規則、七個題目的進度。
- [老屋韌性研究報告](https://flsteven87.github.io/puma-hackathon/topics/issue-6-building-resilience.html)：第 6 題「危老耐震如何查」，目前研究得最完整的一題。

報告是中文閱讀版。每個結論的出處、日期和限制，都寫在對應的研究文件裡。

## 目前進度

更新於 2026-10-15。老屋韌性研究已完成原始來源查找、必要欄位可行性評估，以及兩份官方清冊的可重現比對。

- 5,489 個清冊使照號碼與 9,657 個組織報備使照號碼，有 3 組重疊；代表地址皆不同，仍需確認建物身分與管理範圍，不能直接當成建物狀態矛盾。
- 社群保存檔補到 71,690 筆歷史使照紀錄，包含早年建物屬性；重複、缺值與現況未確認的限制仍保留。
- 目前這個資料查核例子不需要模擬輸入；選案效益與安全成效尚未驗證。

詳見[真實資料發現](https://flsteven87.github.io/puma-hackathon/topics/issue-6-building-resilience.html#real-data-check)與[完整資料稽核及重現方法](docs/topics/issue-6-building-resilience.md#broad-discovery-and-real-input-feasibility-audit-2026-10-15)。公開版提供研究與閱讀報告；文件提及的本機互動原型不在本版的發布範圍。

## 七個題目

| 題號 | 官方題目 | 研究文件 | 狀態 |
| --- | --- | --- | --- |
| 1 | 把三千棵樹種回來 | [行道樹](docs/topics/issue-1-trees.md) | 初步整理 |
| 2 | 找回消失的垃圾桶 | [公共垃圾桶](docs/topics/issue-2-bins.md) | 初步整理 |
| 3 | 鼠患四處跑，衛生安全怎麼辦 | [鼠患](docs/topics/issue-3-rats.md) | 初步整理 |
| 4 | 內湖尖峰車流好比停車場 | [內湖交通](docs/topics/issue-4-neihu-traffic.md) | 初步整理 |
| 5 | 公車路網如何即時反應需求 | [公車路網](docs/topics/issue-5-buses.md) | 初步整理 |
| 6 | 危老耐震如何查，風險評級怎麼找 | [老屋韌性](docs/topics/issue-6-building-resilience.md) | 真實清冊查核已重現；個案連結與效益待驗證 |
| 7 | 自由題：你看見的市政 bug | [自由題](docs/topics/issue-7-free-topic.md) | 初步整理 |

方法、跨題比較和資料集索引都在[研究主文件](docs/research.md)。專有名詞見[名詞表](CONTEXT.md)。

## 我們怎麼做研究

1. **記住官方痛點。** 每題開始時，逐字記下官方題目的痛點，之後都從這句話出發，不靠轉述。
2. **找真正的困擾。** 主辦單位建議的做法只是方向；我們從市民實際遇到的問題往回推。
3. **每個說法都附來源。** 寫明出處、取得日期、怎麼查的，以及有什麼限制。
4. **猜測和事實分開寫。** 還沒驗證的想法標成假設，不當成結論。

完整步驟見[研究流程](docs/research.md#topic-research-playbook)。

## 這份研究還不能說明的事

- 這是研究底稿，不是驗證過的產品提案，也不是官方指引。
- 我們還沒觀察過實際使用者操作，任何「能幫上忙」的說法都還是假設。
- 資料查閱截至 2026-10-15，各來源描述的時間點不同。引用前，請回原始來源確認最新內容。

## 資料與授權

- 本專案的原創文字與分析採 [CC BY 4.0](LICENSE) 授權。
- 引用的政府資料、論文、引文和商標不在此授權內，仍依各自原本的條款。
- 我們只放來源連結和彙總結果，不轉載原始資料、市民陳情內容或個人資料。有些來源的條款不明或禁止轉載；公開看得到，不代表可以再利用。

引用格式如下，並請附上 commit 和查閱日期：

> Puma Hackathon Research contributors. *Puma Hackathon Research*. 2026. https://github.com/flsteven87/puma-hackathon

## 使用的 AI 與工具

- **AI 研究助手：** 各題的深入調查由 GPT-6.1-Sol 執行，GPT-6-Luna 協助找來源，GPT-6-Astra 與 Claude Opus 5.5 審查研究方法。AI 產出只是線索，結論都回到原始來源核對。
- **資料搜尋：** 用 [Twinkle Hub](https://hub.twinkleai.tw/zh-TW) 搜尋政府開放資料，也直接查政府網站、研究論文、社區組織和營運單位的公開資料。
- **檢查工具：** `scripts/` 提供官方題目原文擷取、真實資料彙總比對、文件連結檢查與桌機／手機截圖工具。`issue6_feasibility.py` 只輸出彙總，不列出姓名、地址或使照號碼。HTML 正文依版面自然換行。

閱讀本專案不需要任何帳號。

## 歡迎指正

發現錯誤、反例或無法重現的地方，歡迎開 issue 或 pull request。請附上原始網址、查閱日期、你看了什麼、怎麼查的，並把「看到的事實」和「推論」分開寫。請不要放入個人資料或帳號密碼。
