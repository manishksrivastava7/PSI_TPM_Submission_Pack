# Weekly Status Report – Nirmal Finance (Kavach)

- **Reporting date:** 05 Nov 2026
- **Overall status:** RED
- **Next milestone:** UAT readiness / conditional UAT – 2026-11-12
- **Main issue:** 4/50 incorrect EMI results; 2 early call terminations; provider IP approval pending; AI cost +40%.

## Risks and issues
### K1 – Wrong EMI amount in 4 of 50 test calls
- Probability / impact: High / Critical
- Owner: Arjun + Meera; Sana verifies
- Action: Reproduce failures; trace source data/prompt/model; fix; regression against all failed and boundary cases. Block release until pass.
- Due: 2026-11-11 | Status: Open

### K2 – 2 calls ended at approximately 40 seconds
- Probability / impact: Medium / High
- Owner: Arjun + Dev; Sana verifies
- Action: Inspect provider timeout, session limits and application logs; run >40-second regression calls.
- Due: 2026-11-11 | Status: Open

### K3 – New telephony IPs need client network approval (3 working days)
- Probability / impact: High / Critical
- Owner: Dev + Nirmal network approver
- Action: Submit IP list Monday; obtain named approver; daily chase; connectivity test immediately after approval.
- Due: 2026-11-11 | Status: In progress

### K4 – AI cost is 40% above budget
- Probability / impact: High / High
- Owner: Meera; TPM reports to Group CTO
- Action: Break down cost per call/model/token/retry; compare configuration and test volume; propose optimization; report root cause by Wednesday.
- Due: 2026-11-11 | Status: Open

### K5 – Meera unavailable Wednesday–Friday
- Probability / impact: High / High
- Owner: TPM + Meera
- Action: Complete investigation and written handover by Tuesday 5 PM; document model/prompt/config and pending hypotheses.
- Due: 2026-11-10 | Status: Open

### X1 – Shared QA / backend / frontend / DevOps capacity conflict
- Probability / impact: Medium / High
- Owner: TPM + workstream leads
- Action: Time-box Arjun's Ledger fix; reserve Kavach QA and release capacity; do not start birthday feature in current sprint.
- Due: 2026-11-09 | Status: Open

## TPM note
This is an automatically generated draft. The TPM must validate dates, status, client-safe wording and actions before sending.
