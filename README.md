# 🛍️ Botique-Ollama

> Offline e-commerce chatbot powered by Ollama & Llama 3.2.
> Compares zero-shot vs one-shot prompting on 20 customer queries.
> Private, local & free — no cloud, no API keys needed.

---

## 📌 Overview

Botique-Ollama is a fully offline AI customer support chatbot for a
fictional e-commerce store called **Botique**. It uses Meta's **Llama 3.2 1B**
model served locally via **Ollama** — no data ever leaves your machine.

It compares two prompt engineering strategies:
- **Zero-Shot** — instructions only, no examples
- **One-Shot** — instructions with one example

---

## 🗂️ Project Structure
```
botique-ollama/
├── prompts/
│   ├── zero_shot_template.txt
│   └── one_shot_template.txt
├── eval/
│   └── results.md
├── chatbot.py
├── setup.md
├── report.md
└── README.md
```

---

## ⚙️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.8+ | Scripting |
| Ollama | Local LLM server |
| Llama 3.2 1B | AI model |
| Requests | API calls |

---

## 🚀 Quick Start
```bash
# 1. Clone the repo
git clone https://github.com/vikram0678/botique-ollama.git
cd botique-ollama

# 2. Pull the model
ollama pull llama3.2:1b

# 3. Install dependencies
pip install requests

# 4. Run the chatbot
python chatbot.py
```

---

## 📊 Results Summary

| Method | Avg Relevance | Avg Coherence | Avg Helpfulness |
|--------|---------------|---------------|-----------------|
| Zero-Shot | 4.45 | 4.90 | 4.05 |
| One-Shot | 3.40 | 3.90 | 3.05 |

✅ **Zero-Shot outperformed One-Shot** across all criteria.

---

## 🔍 Key Findings

- Zero-Shot gave consistent helpful responses on all 20 queries
- One-Shot failed on 4 queries with *"I can't help with that"*
- Both methods handled simple queries equally well
- One-Shot struggled with sensitive topics like payment security

---

## ⚠️ Limitations

- No real-time order data access
- Model may hallucinate store policies
- Slow on CPU hardware
- No conversation memory between queries

---

## 📄 Docs

- Full evaluation → [eval/results.md](eval/results.md)
- Full report → [report.md](report.md)
- Setup guide → [setup.md](setup.md)

---

## 👤 Author

**Vikram** — [@vikram0678](https://github.com/vikram0678)