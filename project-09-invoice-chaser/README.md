# 💰 AI Invoice & Payment Chaser Engine
**Sector:** Finance | **Build Time:** ~4 hours | **Difficulty:** ⭐⭐⭐⭐

## One-Line Pitch
> Monitors Xero daily for overdue invoices and runs a 3-tier automated escalation: friendly email → firm email + SMS → Slack escalation.

## ROI
- \,000/year Recovered in AR Staff Time
- Reduces DSO (Days Sales Outstanding) by 30%

## Stack
\
8n\ · \Xero\ · \Claude 3.5 Sonnet\ · \Twilio\ · \Airtable\ · \Gmail\ · \Slack\

## Setup
1. Copy \.env.example\ to \.env\ and fill in your API keys.
2. Import \workflow.json\ into your n8n instance.
3. Create your Airtable chase log base using the schema in the documentation.
4. Activate the workflow — it runs automatically on weekdays at 9AM.
