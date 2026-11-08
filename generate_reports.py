#!/usr/bin/env python3
"""Generate a separate weekly client status report from the PSI TPM tracker."""
import argparse
from pathlib import Path
from datetime import datetime
from openpyxl import load_workbook

def clean(value):
    return "" if value is None else str(value).strip()

def generate_reports(input_file: Path, output_dir: Path):
    wb = load_workbook(input_file, data_only=True)
    if "Summary" not in wb.sheetnames or "Risks and Issues" not in wb.sheetnames:
        raise ValueError("Workbook must contain 'Summary' and 'Risks and Issues' tabs.")
    summary = wb["Summary"]
    risks_ws = wb["Risks and Issues"]
    projects = []
    for row in summary.iter_rows(min_row=2, values_only=True):
        if not row or not clean(row[0]):
            continue
        projects.append({
            "project": clean(row[0]), "client": clean(row[1]),
            "rag": clean(row[2]) or "Not set", "milestone": clean(row[3]) or "Not set",
            "date": clean(row[4]) or "Not set", "problem": clean(row[5]) or "No issue recorded"
        })
    risk_rows = []
    for row in risks_ws.iter_rows(min_row=2, values_only=True):
        if not row or not clean(row[0]):
            continue
        risk_rows.append({
            "id": clean(row[0]), "project": clean(row[1]), "description": clean(row[2]),
            "probability": clean(row[3]), "impact": clean(row[4]), "owner": clean(row[5]),
            "action": clean(row[6]), "due": clean(row[7]) or "Not set", "status": clean(row[8]) or "Open"
        })
    output_dir.mkdir(parents=True, exist_ok=True)
    generated = []
    for p in projects:
        project_risks = [r for r in risk_rows if r["project"].casefold() in (p["project"].casefold(), "both")]
        lines = [
            f"# Weekly Status Report – {p['client']} ({p['project']})",
            "",
            f"- **Reporting date:** {datetime.now().strftime('%d %b %Y')}",
            f"- **Overall status:** {p['rag']}",
            f"- **Next milestone:** {p['milestone']} – {p['date']}",
            f"- **Main issue:** {p['problem']}",
            "",
            "## Risks and issues",
        ]
        if project_risks:
            for r in project_risks:
                lines += [
                    f"### {r['id']} – {r['description']}",
                    f"- Probability / impact: {r['probability']} / {r['impact']}",
                    f"- Owner: {r['owner']}",
                    f"- Action: {r['action']}",
                    f"- Due: {r['due']} | Status: {r['status']}",
                    ""
                ]
        else:
            lines.append("No risks recorded for this project.")
        lines += [
            "## TPM note",
            "This is an automatically generated draft. The TPM must validate dates, status, client-safe wording and actions before sending.",
            ""
        ]
        safe_name = "".join(ch.lower() if ch.isalnum() else "_" for ch in p["project"]).strip("_")
        path = output_dir / f"{safe_name}_weekly_status.md"
        path.write_text("\n".join(lines), encoding="utf-8")
        generated.append(path)
    return generated

def main():
    parser = argparse.ArgumentParser(description="Generate weekly client status reports from PSI tracker.")
    parser.add_argument("--input", required=True, help="Path to T5_Project_Tracker.xlsx")
    parser.add_argument("--output", default="reports", help="Output folder (default: reports)")
    args = parser.parse_args()
    for report in generate_reports(Path(args.input), Path(args.output)):
        print(f"Created: {report}")

if __name__ == "__main__":
    main()
