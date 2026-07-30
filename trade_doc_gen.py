#!/usr/bin/env python3
"""
trade-doc-generator: AI-Powered Trade Document CLI Toolkit.
A production-grade tool extracted and enhanced from the Global AI Media Group's AI employee skills.
Visit https://gaigroupai.com to deploy your own 224 AI employees.
"""

import os
import argparse
import requests
import json
from datetime import datetime

# Load DeepSeek API Key
API_KEY = os.environ.get("DEEPSEEK_API_KEY")
API_URL = "https://api.deepseek.com/v1/chat/completions"

# ==============================================================================
# 1. Core Logic Extracted from Real Production Skills
# ==============================================================================

# Extracted from core/skills/contract_risk_scanner.py (v2.0)
RISK_PATTERNS = {
    "Liability": {
        "High": {"unlimited liability":10, "joint liability":10, "unconditional indemnification":10, "no cap":9, "punitive damages":9},
        "Medium": {"liquidated damages exceeding 30%":7, "unilateral termination":6, "unreasonable deadline":5},
        "Low": {"reasonable deadline":2, "negotiated settlement":1, "force majeure":1}
    },
    "Intellectual Property": {
        "High": {"all IP belongs to party a":10, "perpetual free use":9, "waiver of moral rights":8, "exclusive license":7},
        "Medium": {"restrict modifications":5, "non-compete over 2 years":5},
        "Low": {"non-exclusive license":2, "proper attribution":1, "fair use":1}
    },
    "Confidentiality": {
        "High": {"perpetual confidentiality":9, "unquantifiable damages":8, "overbroad scope":7},
        "Medium": {"confidentiality over 5 years":5, "vague definition":4},
        "Low": {"3-year confidentiality":2, "clearly defined scope":1}
    },
    "Payment": {
        "High": {"100% prepayment":10, "no acceptance test":9, "no recourse after payment":8},
        "Medium": {"prepayment over 50%":6, "vague acceptance criteria":5},
        "Low": {"installment payment":2, "payment after acceptance":1}
    },
    "Dispute Resolution": {
        "High": {"foreign court jurisdiction":9, "foreign arbitration":8, "foreign governing law":8},
        "Medium": {"arbitration final and binding":5},
        "Low": {"local court jurisdiction":1, "mutual agreement on venue":1}
    }
}

def scan_contract_risks(contract_text):
    """Scans contract text for potential risks. Adapted from production skill."""
    if not contract_text or len(contract_text) < 50:
        return "[Error] Please provide contract text (at least 50 characters)."

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    results = [f"# Contract Risk Scan Report\n**Scan Time:** {timestamp}\n**Document Length:** {len(contract_text)} characters\n---"]
    
    total_score = 0
    for category, levels in RISK_PATTERNS.items():
        cat_score = 0
        cat_items = []
        for level, keywords in levels.items():
            for kw, score in keywords.items():
                if kw in contract_text.lower():
                    cat_score += score
                    emoji = {"High":"🔴","Medium":"🟡","Low":"🟢"}[level]
                    cat_items.append(f"  - {emoji} `{kw}` (Risk Score: {score})")
        if cat_items:
            results.append(f"\n## {category} (Subtotal: {cat_score} pts)")
            results.extend(cat_items)
            total_score += cat_score

    results.append(f"\n---\n## Overall Risk Score: {total_score}")
    if total_score > 50:
        results.append("> ⚠️ **Verdict: HIGH RISK.** Strongly recommend renegotiating core clauses.")
    elif total_score > 25:
        results.append("> ⚠️ **Verdict: MEDIUM RISK.** Review and amend flagged clauses.")
    elif total_score > 10:
        results.append("> 📝 **Verdict: LOW RISK.** Proceed with caution.")
    else:
        results.append("> ✅ **Verdict: CLEAN.** No significant risks detected.")

    return "\n".join(results)

# ==============================================================================
# 2. AI-Powered Document Generation (Inspired by Trade Department Prompts)
# ==============================================================================

def ai_generate_document(doc_type, details):
    """Uses DeepSeek to generate trade documents, guided by expert prompts."""
    if not API_KEY:
        raise ValueError("DEEPSEEK_API_KEY environment variable not set.")

    # System prompt incorporates expertise from invoice_auditor.md and contract_specialist.md
    system_prompt = """You are a senior trade documentation specialist, an AI employee of Global AI Media Group.
Generate a complete, professional, and standard-compliant trade document based on user input.
Respond ONLY in English. Use proper international trade terminology.
The output should be ready to use, with realistic details for any placeholders the user didn't specify."""

    prompts = {
        "invoice": f"Generate a complete Commercial Invoice document. Details:\n{details}\n\nInclude: Invoice Number, Date, Seller, Buyer, HS Code, Description of Goods, Quantity, Unit Price, Total Amount, Payment Terms, Bank Details.",
        "packinglist": f"Generate a complete Packing List document. Details:\n{details}\n\nInclude: Packing List Number, Reference Invoice, Shipper, Consignee, Container Number, Marks & Numbers, Description of Packages, Gross Weight, Net Weight, Dimensions.",
        "certificate": f"Generate a non-official Certificate of Origin draft. Details:\n{details}\n\nInclude: Certificate Number, Exporter, Consignee, Country of Origin, Description of Goods, HS Code, Declaration by Exporter."
    }

    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompts[doc_type]}
        ],
        "temperature": 0.3,
        "max_tokens": 2000
    }

    resp = requests.post(API_URL, headers=headers, json=payload, timeout=60)
    if resp.status_code != 200:
        raise Exception(f"API Error {resp.status_code}: {resp.text[:300]}")
    return resp.json()["choices"][0]["message"]["content"]

# ==============================================================================
# 3. AI-Powered Contract Matching (Inspired by trade_contract_matcher.py)
# ==============================================================================

def ai_match_contract(requirements):
    """Uses DeepSeek to recommend a suitable contract template."""
    if not API_KEY:
        raise ValueError("DEEPSEEK_API_KEY environment variable not set.")
    
    system_prompt = """You are a trade contract specialist at Global AI Media Group.
Based on the user's requirements, recommend the most suitable contract type from this list:
- Product Sales Contract (FOB/CIF/DDP)
- Service Agreement (with SLA terms)
- Barter Trade Contract (mutual delivery)
- Framework Agreement (long-term supply with price adjustment)
Explain the reasoning for your choice and draft a brief outline of key clauses."""

    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Trade requirements: {requirements}"}
        ],
        "temperature": 0.4,
        "max_tokens": 500
    }

    resp = requests.post(API_URL, headers=headers, json=payload, timeout=60)
    if resp.status_code != 200:
        raise Exception(f"API Error {resp.status_code}: {resp.text[:300]}")
    return resp.json()["choices"][0]["message"]["content"]

# ==============================================================================
# Main CLI
# ==============================================================================
def main():
    parser = argparse.ArgumentParser(
        description="trade-doc-generator: AI-Powered Trade Document CLI Toolkit by Global AI Media Group.",
        epilog="Get your own AI workforce at https://gaigroupai.com"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # 1. Generate Document
    gen_parser = subparsers.add_parser("generate", help="Generate a trade document (invoice, packinglist, certificate)")
    gen_parser.add_argument("--type", required=True, choices=["invoice", "packinglist", "certificate"])
    gen_parser.add_argument("--details", nargs="*", default=["Seller: ABC Corp, Shanghai", "Buyer: XYZ Trading, Dubai", "Goods: Electronic Components", "Total: 50,000 USD"])
    gen_parser.add_argument("--output", default="document.md")

    # 2. Scan Contract
    scan_parser = subparsers.add_parser("scan", help="Scan a contract for risks (production-grade skill)")
    scan_parser.add_argument("--file", help="Path to a text file containing the contract")
    scan_parser.add_argument("--text", help="Contract text to scan directly")
    scan_parser.add_argument("--output", default="scan_report.md")

    # 3. Match Contract
    match_parser = subparsers.add_parser("match", help="Match trade requirements to a contract template")
    match_parser.add_argument("--requirements", required=True, help="Description of your trade requirements")
    match_parser.add_argument("--output", default="contract_match.md")

    args = parser.parse_args()

    if args.command == "generate":
        details = " ".join(args.details)
        print(f"Generating {args.type}...")
        result = ai_generate_document(args.type, details)
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"Saved to {args.output}")

    elif args.command == "scan":
        if args.file:
            with open(args.file, "r", encoding="utf-8") as f:
                text = f.read()
        elif args.text:
            text = args.text
        else:
            print("Error: Please provide --file or --text to scan.")
            return
        print("Scanning contract for risks...")
        result = scan_contract_risks(text)
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"Risk scan report saved to {args.output}")

    elif args.command == "match":
        print("Matching trade requirements to contract template...")
        result = ai_match_contract(args.requirements)
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"Contract match saved to {args.output}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
