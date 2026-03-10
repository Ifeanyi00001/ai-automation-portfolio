# seed_pinecone.py
# Run once to populate Pinecone with initial legal precedents.
# Requirements: pip install pinecone openai
# Usage: python seed_pinecone.py

from pinecone import Pinecone
from openai import OpenAI

# ── CONFIG ─────────────────────────────────────────
PINECONE_API_KEY = "YOUR_PINECONE_API_KEY"
PINECONE_INDEX_HOST = "YOUR_PINECONE_INDEX_HOST"  # e.g. https://legal-xxxx.svc.pinecone.io
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
NAMESPACE = "case-precedents"
# ───────────────────────────────────────────────────

pc = Pinecone(api_key=PINECONE_API_KEY)
openai_client = OpenAI(api_key=OPENAI_API_KEY)
index = pc.Index(host=PINECONE_INDEX_HOST)

# ── ADD YOUR REAL CASE SUMMARIES HERE ──────────────
precedents = [
    {
        "case_name": "Smith v. Johnson Construction (2022)",
        "summary": "Breach of contract. Contractor failed to complete renovation within agreed timeline. Force majeure clause was overly broad. Court sided with plaintiff. Award: $145,000. Key lesson: always define specific triggering events in force majeure clauses."
    },
    {
        "case_name": "Greenfield LLC v. Apex Tech (2021)",
        "summary": "NDA + trade secret misappropriation. Defendant argued 'reasonable steps' were not taken. Court enforced NDA. Injunction granted. Key lesson: document your IP protection measures — access logs, encryption policies, employee training records."
    },
    {
        "case_name": "Martinez v. City of Houston (2023)",
        "summary": "Personal injury, municipal liability, slip-and-fall on public property. Government immunity waiver applied under Texas Tort Claims Act. Damages capped at $100,000. Key lesson: file notice of claim within 6-month window."
    },
    {
        "case_name": "Harbor Properties v. Eastside Zoning Board (2020)",
        "summary": "Administrative law, zoning variance denial. Property developer appealed denial of conditional use permit for mixed-use development. Administrative record incomplete — board failed to cite specific findings. Reversed and remanded."
    },
    {
        "case_name": "Chen v. Pacific Shipping Co. (2023)",
        "summary": "Maritime law, cargo damage claim. Carrier argued act-of-God defense for storm damage. Court found carrier failed to properly stow cargo per Carriage of Goods by Sea Act (COGSA). $230,000 awarded to shipper."
    }
]
# ───────────────────────────────────────────────────

print(f"📦 Seeding {len(precedents)} precedents into Pinecone namespace '{NAMESPACE}'...")
vectors = []
for i, p in enumerate(precedents):
    full_text = f"CASE: {p['case_name']}\nSUMMARY: {p['summary']}"
    response = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=full_text
    )
    embedding = response.data[0].embedding
    vectors.append({
        "id": f"case-{i:04d}",
        "values": embedding,
        "metadata": {
            "case_name": p["case_name"],
            "summary": p["summary"]
        }
    })
    print(f"  ✅ Embedded: {p['case_name']}")

index.upsert(vectors=vectors, namespace=NAMESPACE)
print(f"\n✅ Done! {len(vectors)} precedents seeded successfully.")
print(f"   Pinecone namespace: {NAMESPACE}")
print(f"   Vector dimension: 1536")
