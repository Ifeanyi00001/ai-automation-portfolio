# 🎧 Customer Support Triage Engine
**Sector:** Support | **Build Time:** ~3.5 hours | **Difficulty:** ⭐⭐⭐⭐

## One-Line Pitch
> Uses a Pinecone knowledge base to auto-resolve 40% of Tier-1 support tickets without any human involvement.

## ROI
- 40% Ticket Deflection Rate
- \–\ Per Human Ticket → \.05 AI Resolution

## Stack
\
8n\ · \Zendesk\ · \Pinecone\ · \OpenAI\ · \Claude 3.5 Sonnet\ · \Slack\

## Setup
1. Copy \.env.example\ to \.env\ and fill in your API keys.
2. Import \workflow.json\ into your n8n instance.
3. Seed your Pinecone index with your help center articles.
4. Activate the workflow.
