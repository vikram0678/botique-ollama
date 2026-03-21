import requests
import json
import os

# ── Constants 
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME      = "llama3.2:1b"
RESULTS_FILE    = "eval/results.md"
ZERO_SHOT_FILE  = "prompts/zero_shot_template.txt"
ONE_SHOT_FILE   = "prompts/one_shot_template.txt"

# ── 20 E-commerce Queries 
QUERIES = [
    "How do I track the shipping status of my recent order?",
    "My discount code is not working at checkout.",
    "How do I cancel an order I just placed?",
    "I received the wrong item in my package.",
    "How long does standard delivery usually take?",
    "Can I change my delivery address after placing an order?",
    "My payment was deducted but I got no order confirmation.",
    "How do I return a damaged product?",
    "Is it possible to exchange an item for a different size?",
    "Why has my order been stuck on processing for 3 days?",
    "How do I apply a gift card to my order?",
    "I forgot my account password. How do I reset it?",
    "Can I place an order without creating an account?",
    "How do I unsubscribe from your promotional emails?",
    "Do you offer free shipping on all orders?",
    "My refund has not been credited back to my account yet.",
    "How do I leave a review for a product I purchased?",
    "Are my payment details saved securely on your platform?",
    "Can I track my order without logging into my account?",
    "My package shows delivered but I never received it.",
]

# ── Load Template  
def load_template(filepath):
    with open(filepath, "r") as f:
        return f.read()

# ── Query Ollama  ─
def query_ollama(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(
            OLLAMA_ENDPOINT,
            json=payload,
            timeout=120
        )
        response.raise_for_status()
        return json.loads(response.text).get("response", "").strip()
    except requests.exceptions.RequestException as e:
        print(f"  [ERROR] {e}")
        return "Error: Could not get response."

# ── Main  
def main():
    print("🛍️  Botique-Ollama Chatbot Starting...\n")

    # Load templates
    zero_template = load_template(ZERO_SHOT_FILE)
    one_template  = load_template(ONE_SHOT_FILE)

    os.makedirs("eval", exist_ok=True)

    with open(RESULTS_FILE, "w") as f:

        # Write header
        f.write("# Botique Evaluation Results\n\n")
        f.write("## Scoring Rubric\n\n")
        f.write("- **Relevance (1-5):** Does the response address the query?\n")
        f.write("- **Coherence (1-5):** Is it grammatically correct and clear?\n")
        f.write("- **Helpfulness (1-5):** Is it useful and actionable?\n\n")
        f.write("---\n\n")
        f.write("## Results Table\n\n")
        f.write("| Query # | Customer Query | Prompting Method | Response | Relevance | Coherence | Helpfulness |\n")
        f.write("|---------|---------------|-----------------|----------|-----------|-----------|-------------|\n")

        for i, query in enumerate(QUERIES, start=1):
            print(f"[{i}/20] {query}")

            # Zero-Shot
            print("  ⏳ Zero-shot...")
            zero_prompt    = zero_template.replace('"{query}"', f'"{query}"')
            zero_response  = query_ollama(zero_prompt)
            print("  ✅ Done")

            # One-Shot
            print("  ⏳ One-shot...")
            one_prompt     = one_template.replace('"{query}"', f'"{query}"')
            one_response   = query_ollama(one_prompt)
            print("  ✅ Done\n")

            # Clean text for table
            q  = query.replace("|", "-")
            zr = zero_response.replace("\n", " ").replace("|", "-")[:250]
            or_ = one_response.replace("\n", " ").replace("|", "-")[:250]

            # Write rows
            f.write(f"| {i} | {q} | Zero-Shot | {zr} | | | |\n")
            f.write(f"| {i} | {q} | One-Shot  | {or_} | | | |\n")
            f.flush()

    print("✅ All 20 queries done!")
    print("📄 Open eval/results.md and fill in your scores.")

if __name__ == "__main__":
    main()