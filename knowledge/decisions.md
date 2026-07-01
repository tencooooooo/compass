# Decisions

## v0.3 - Company profiles and knowledge base

- `collectors/companies/fetch_company_profiles.py` を追加し、企業情報取得を価格取得と分離した。
- 企業情報は再取得しやすく、履歴管理より鮮度を優先するため、`storage/raw/companies/{ticker}.json` に毎回上書き保存する。
- 価格以外のrawデータも増えるため、企業情報の保存先は `storage/raw/companies/` にした。
- logging方式は価格collectorと同じ仕組みにし、collectorが増えても実行結果を `logs/YYYY-MM-DD.log` に集約できるようにした。
- 投資方針、スコアリング設計、用語、セクター、ロードマップ、設計判断を `knowledge/` に分離した。
- `knowledge/` はAIの学習データではなく、分析時に参照する「人間が育てるナレッジ」として扱う。

## v0.4 - Financial data and data model direction

- `collectors/financials/fetch_financials.py` を追加し、決算データ取得を独立したcollectorにした。
- 決算データは `storage/raw/financials/{ticker}.json` に毎回上書き保存する。まずは最新の主要指標をAIが読みやすい単一JSONにまとめる。
- 価格、企業情報、決算のrawデータは現時点では種類別ディレクトリに保存する。
- 将来的にはAIが銘柄単位で読み込みやすいよう、`storage/entities/{ticker}/company.json`, `financials.json`, `prices.csv`, `news.json` へ統一する方針をREADMEに明記した。
- 決算分析ルール、成長企業パターン、投資指標辞書を `knowledge/` に追加した。

## v0.5 - News and event database

- `collectors/news/fetch_news.py` を追加し、yfinanceから銘柄ごとに最大20件のニュースを取得する。
- ニュースは `storage/raw/news/{ticker}.json` に毎回上書き保存する。
- `collectors/news/build_event_database.py` を追加し、保存済みニュースと価格CSVを結び付けて `storage/events/{ticker}_events.json` を作成する。
- イベントDBはAI分析ではなく、ニュース発生日と価格・出来高の事実を保存する土台として扱う。
- ニュース発生日が非取引日の場合、価格は発生日以降の最初の取引日を参照する。
- ニュース分類、市場心理、イベントパターンを `knowledge/` に追加した。

## v0.6 - Company analysis reports

- `analyzers/company_analysis/generate_company_report.py` を追加し、保存済みデータから銘柄ごとのMarkdownレポートを生成する。
- レポート出力先は `reports/company_analysis/{ticker}.md` とした。
- プロンプトは `prompts/company_analysis_prompt.md` に分離し、Pythonコードに直接書かない方針にした。
- `knowledge/company_analysis_guidelines.md`, `knowledge/report_template.md`, `knowledge/analysis_principles.md` を追加した。
- レポートは「事実、整理、考察、調査優先度」の順に構成し、買い・売り・目標株価などの投資判断は出さない。
- GitHub Actionsでデータ収集後に企業分析レポートを自動生成するようにした。

## v0.7 - Comparative analysis reports

- `analyzers/comparative_analysis/generate_comparison_report.py` を追加し、複数銘柄を横断比較するMarkdownレポートを生成する。
- 出力先は `reports/comparative_analysis/` とし、初期レポートは `market_overview.md`, `mega_tech_comparison.md`, `semiconductor_comparison.md`, `sector_technology.md` とした。
- 比較分析用プロンプトは `prompts/comparative_analysis_prompt.md` に分離した。
- `knowledge/comparative_analysis_guidelines.md`, `knowledge/peer_group_definitions.md`, `knowledge/ranking_principles.md` を追加した。
- v0.6の個別企業レポートから強み、注目ポイント、調査優先度を抽出して比較表に使う。
- 比較分析は投資判断ではなく、追加調査候補を整理するための補助として扱う。

## v1.0-alpha - Project philosophy milestone

- 新しい分析機能は追加せず、研究プロジェクトとしての思想と運用方針を整理した。
- `MANIFEST.md` を追加し、目的、価値観、禁止事項、長期ゴールを明文化した。
- `PROJECT_PHILOSOPHY.md` を追加し、Knowledge、Explainable AI、長期投資、理由重視、人間とAIの役割分担を整理した。
- `docs/future_architecture.md`, `docs/development_principles.md`, `docs/release_strategy.md` を追加し、将来構成、開発原則、リリース方針を分離した。
- `knowledge/investment_philosophy.md`, `knowledge/ai_design_principles.md`, `knowledge/future_features.md` を追加し、AIが将来参照する思想メモを拡張した。
- 実際のGit tagやGitHub Releaseは作成せず、READMEに推奨手順のみ記載した。

## v1.0-alpha - Compass rebranding

- プロジェクトブランドを Compass へ変更した。
- 旧名称はREADMEのHistory、CHANGELOG、Project Historyに履歴として残す。
- Growth Hunter は将来追加予定の成長株スクリーニングエンジン名として残す。
- `knowledge/brand_identity.md` と `docs/branding.md` を追加し、ブランド定義、命名理由、将来のブランド構成を記録した。
- README、MANIFEST、PROJECT_PHILOSOPHY、settings、Workflow、prompts、docs、Knowledgeの現行ブランド表記をCompassへ統一した。

## Compass Research 01 - Explainable Scoring Engine

- `engines/scoring_engine/` を追加し、点数、理由、Evidence、Confidenceを同時に出力する設計にした。
- スコアは Growth, Financial Health, Valuation, Momentum, News の5カテゴリ、各20点、合計100点とした。
- `reports/scoring/company_scores.csv`, `company_scores.json`, `explanations/{ticker}.md` を生成する。
- 厳密な売上成長率など、現時点で時系列財務が不足する項目は理由とConfidenceへ反映する。
- スコアはランキングや投資判断ではなく、追加調査候補を整理するための説明可能な補助情報として扱う。

## Compass Research 02 - Market Intelligence Engine

- `engines/market_intelligence/` を追加し、市場、セクター、市場心理を整理する基盤を作成した。
- `reports/market/market_summary.md`, `sector_summary.md`, `market_dashboard.json` を生成する。
- 入力には価格、企業情報、決算、ニュース、Event Database、Knowledge、Scoring結果、比較分析レポートを使用する。
- Growth Hunterはまだ実装せず、将来Growth Hunterが参照する市場・セクター文脈を先に整備する。
- 企業ランキングは生成せず、市場構造の理解を優先する。

## Compass Research 03 - Discovery Engine

- `engines/discovery/` を追加し、追加調査候補を説明可能な形で抽出する基盤を作成した。
- Discovery Scoreは投資判断ではなく、候補発見のための補助指標として扱う。
- 入力には価格、企業情報、決算、ニュース、Events、企業分析、比較分析、Scoring、Market Intelligence、Knowledgeを使用する。
- 出力は `reports/discovery/discovery_candidates.md`, `discovery_candidates.json`, `candidate_details/{ticker}.md` とした。
- Growth Hunterはまだ実装せず、Discovery Engineをその土台として位置づけた。

## Compass Research 04 - Backtesting & Validation Engine

- `engines/validation/` を追加し、Discovery候補を保存済み価格データと突き合わせて検証する基盤を作成した。
- 検証期間は 1w, 1m, 3m, 6m, 1y とし、期間未完了の候補は断定せずNeutralとして扱う。
- 出力は `reports/validation/validation_summary.md`, `validation_history.csv`, `validation_history.json` とした。
- ベンチマークは保存済みのSPYまたはS&P500価格データがある場合のみ使用する。
- Validationは自動学習ではなく、将来のLearning Engineが参照する履歴と根拠を蓄積するための土台として位置づけた。

## Compass Research 05 - Slack Notification Engine

- `integrations/slack/` を追加し、GitHub Actionsの最後にDaily Research Briefを送信できるようにした。
- Slack Incoming Webhook URLは `SLACK_WEBHOOK_URL` としてGitHub Secretsで管理し、コードや設定ファイルには保存しない。
- Secrets未設定の場合はSlack通知のみスキップし、Workflow全体は失敗させない。
- 通知は詳細レポートではなく、実行結果、Discovery、Market Summary、Important News、Validation、Artifact名に絞る。
- 失敗時は `always()` の通知ステップから最低限の障害情報を送る設計にした。

## Compass Research 06 - Notification Engine

- `engines/notification/` を追加し、重要イベントの検知と通知ルーティングをDaily Reportから分離した。
- Slackへ直接依存せず、`NotificationRouter` から `SlackConnector` を呼ぶ設計にした。
- 初期イベントはDiscovery Alert、Score Change Alert、Market Trend Alert、Important News Alert、Validation Alert、Workflow Failureとした。
- 通知履歴は `storage/notifications/notification_history.json` に保存し、重複通知防止に使用する。
- GitHub Actions cacheで `storage/notifications/` を復元し、前回スコアと市場トレンドを比較できるようにした。
- 将来Discord、Teams、LINE、Email、Push通知へ拡張できる構成にした。

## Compass Core 01 - Memory Engine

- `core/memory/` を追加し、Memory API、Provider Interface、LocalProviderを分離した。
- 現在はLocal JSONのみを実装し、将来S3、Postgres、Supabaseへ移行できる構造にした。
- Memory保存先は `memory/companies`, `memory/sectors`, `memory/discoveries`, `memory/validations`, `memory/market`, `memory/lessons` とした。
- GitHub ActionsではValidation後にMemoryを更新し、その後Notification Engineを実行する順序にした。
- `memory/` はGit管理対象外とし、Actions cacheで復元し、Artifactへ含める運用にした。

## Compass Core 02 - Feedback Engine

- `core/feedback/` を追加し、Feedback Engine、Feedback Analyzer、Improvement Detectorを分離した。
- Discovery Memory、Validation Memory、Company Memory、Sector Memory、Knowledge、Scoring結果をFeedback入力にした。
- 出力は `reports/feedback/feedback_summary.md`, `improvement_candidates.md`, `feedback_history.json` とした。
- FeedbackはLearning Engineではなく、Knowledge更新候補を人間へ提示する層とした。
- GitHub ActionsではMemory更新後にFeedback Engineを実行し、その後Notification Engineを実行する順序にした。

## Compass Core 03 - Decision Engine

- `core/decision/` を追加し、Decision Engine、Proposal Generator、Review Managerを分離した。
- Feedback HistoryとImprovement Candidatesから人間レビュー用Proposalを生成する設計にした。
- 出力は `reports/proposals/proposal_YYYY-MM-DD.md`, `proposal_index.json`, `reports/knowledge_updates/candidate_YYYY-MM-DD.md` とした。
- Proposal statusはPending、Approved、Rejected、DeferredでJSON管理する。
- Decision EngineはKnowledge、Scoring、Ruleを自動更新しない。Knowledge変更権限は人間が持つ。
- GitHub ActionsではFeedback後にDecision Engineを実行し、その後Notification Engineを実行する順序にした。
