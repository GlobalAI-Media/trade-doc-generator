# 📄 trade-doc-generator

A professional AI-powered CLI toolkit for international trade: **generate invoices, scan contract risks, and match trade contracts**.

> **Powered by production AI skills** extracted from the Global AI Media Group's 224 AI employees.
> Deploy your own AI workforce at [gaigroupai.com](https://gaigroupai.com).

## Features

- **`generate`** Commercial Invoices, Packing Lists, and Certificates of Origin using DeepSeek AI.
- **`scan`** Contracts for legal and financial risks using a real production risk-scoring engine.
- **`match`** Trade requirements to the optimal contract template.
- All output is professional, ready-to-use Markdown.

## Installation

```bash
git clone https://github.com/GlobalAI-Media/trade-doc-generator.git
cd trade-doc-generator
pip install -r requirements.txt

## Prerequisites

Set your DEEPSEEK_API_KEY environment variable. Get a key at platform.deepseek.com.

export DEEPSEEK_API_KEY="sk-your-key-here"  # macOS/Linux
set DEEPSEEK_API_KEY=sk-your-key-here       # Windows

## Usage

1. Generate a Document

python trade_doc_gen.py generate --type invoice
python trade_doc_gen.py generate --type packinglist --details "seller='MyCompany' buyer='Client Inc'"
python trade_doc_gen.py generate --type certificate --output my_cert.md

2. Scan a Contract for Risks

# Scan a file
python trade_doc_gen.py scan --file contract.txt

# Scan text directly
python trade_doc_gen.py scan --text "The agreement states unlimited liability and perpetual confidentiality."

3. Match a Contract Template

python trade_doc_gen.py match --requirements "I need to export coffee beans to Germany, FOB terms, long-term supply."

## Example: Contract Risk Scan Output

# Contract Risk Scan Report
Scan Time: 2026-07-29 16:30
Document Length: 1250 characters
---
## Liability (Subtotal: 19 pts)
  - 🔴 unlimited liability (Risk Score: 10)
  - 🟡 unilateral termination (Risk Score: 6)
...
---
Overall Risk Score: 29
> ⚠️ Verdict: MEDIUM RISK. Review and amend flagged clauses.

## Why This Tool is Unique

Unlike generic document generators, trade-doc-generator contains real production code from the Global AI Media Group's AI employee system:

The scan command uses the same risk-scoring engine that powers our contract_risk_scanner AI employee.

The generate and match commands are guided by the exact prompt engineering used by our invoice_auditor and contract_specialist AI roles.

This is not a demo. It's a window into a 224-strong AI workforce.

## Related

224-ai-employees — Meet the full AI team

gaigroupai.com — Deploy your own AI employees today

## License

MIT © 2026 CHIFENG JINGWEI INTELLIGENT MEDIA TECHNOLOGY CO., LTD


---

### 第三步：同步更新主仓库
创建完成后，请修改 `224-ai-employees` 仓库的 `README.md`，将 `trade-doc-generator (coming soon)` 改为：

```markdown
| [**trade-doc-generator**](https://github.com/GlobalAI-Media/trade-doc-generator) | AI-powered trade document toolkit: generate invoices, scan contracts, match templates. |
