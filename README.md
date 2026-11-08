# PSI TPM Weekly Status Report Generator

A small Python utility that reads the two-tab PSI project tracker (Excel) and creates one Markdown weekly status report per client/project.

## Requirements
- Python 3.9+
- Install dependencies: `python -m pip install -r requirements.txt`

## Run
From this folder:

```bash
python generate_reports.py --input ../T5_Project_Tracker.xlsx --output reports
```

Expected output:
- `reports/kavach_weekly_status.md`
- `reports/ledger_weekly_status.md`

## Input format
The workbook must contain:
- `Summary`: Project, Client, RAG Status, Next milestone, Milestone date, Main problem
- `Risks and Issues`: ID, Project, Description, Probability, Impact, Owner, Action / mitigation, Due date, Status

Risks with project value `Both` are included in each client's report. Blank optional fields are displayed as `Not set` or a safe fallback rather than causing a crash.

## AI use disclosure
AI assistance: ChatGPT was used to help structure the requirements, draft the initial Python implementation, and review test scenarios. The final logic, input columns, output content and sample results were checked manually against the tracker.

## Prompts used
1. "Design a small Python tool for a Technical Program Manager that reads an Excel project tracker with Summary and Risks and Issues tabs and generates one client-specific weekly status report per project."
2. "Generate robust Python code using openpyxl. Validate required worksheet names, handle blank cells safely, filter risks by project, include shared risks marked Both, and output Markdown files."
3. "Review the code for edge cases: empty rows, missing optional values, unexpected project names and output directory creation. Keep the TPM responsible for validating the generated client-facing report."

## One AI error and correction
Initial AI-generated logic treated every risk row as relevant to every project. I corrected it to include only risks whose project matches the current project, plus shared risks explicitly marked `Both`. I also added safe handling for blank dates and fields, and a required-sheet check.

## Sample output / manual verification
Run the command above. Verify that:
- Kavach report includes K1–K5 and shared X1, but no Ledger-only L1–L3.
- Ledger report includes L1–L3 and shared X1, but no Kavach-only K1–K5.
- Each report contains the milestone, RAG status, main issue, owners, actions and due dates.

## Important
The tool creates a first-draft report; it does not decide whether a status is safe to send. The TPM must validate facts, dates, risk wording and client confidentiality before distribution.
