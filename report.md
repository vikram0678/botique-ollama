# 📊 Botique-Ollama — Evaluation Report

---

## 1. Introduction

This project evaluates the feasibility of using a local Large
Language Model (LLM) for e-commerce customer support.

Using **Ollama** and **Llama 3.2 1B**, the chatbot runs entirely
offline — no cloud APIs, no data privacy risks, and no cost.

The core goal is to compare two prompt engineering strategies:
- **Zero-Shot Prompting** — model gets instructions only
- **One-Shot Prompting** — model gets instructions + one example

---

## 2. Methodology

### 2.1 Queries
20 customer support queries were adapted from the
**Ubuntu Dialogue Corpus** into e-commerce scenarios.

Example adaptation:
- Original: *"My wifi driver is not working after the update."*
- Adapted: *"My discount code is not working at checkout."*

### 2.2 Prompt Templates

**Zero-Shot Template:**
- Role assignment only
- No examples provided
- Model relies entirely on instructions

**One-Shot Template:**
- Same role assignment
- One example query-response pair included
- Model guided by the example format and tone

### 2.3 Scoring Rubric

Each response was manually scored on three criteria:

| Criteria | Description | Scale |
|----------|-------------|-------|
| Relevance | Does it address the query? | 1-5 |
| Coherence | Is it clear and grammatical? | 1-5 |
| Helpfulness | Is it useful and actionable? | 1-5 |

---

## 3. Results & Analysis

### 3.1 Average Scores

| Method | Avg Relevance | Avg Coherence | Avg Helpfulness |
|--------|-------------|---------------|-----------------|
| Zero-Shot | **4.45** | **4.90** | **4.05** |
| One-Shot | 3.40 | 3.90 | 3.05 |

### 3.2 Key Observations

**Zero-Shot performed better overall.**

Zero-Shot gave consistent, relevant responses across all 20
queries. It scored especially high on coherence (4.90 avg),
meaning the responses were almost always grammatically correct
and easy to read.

**One-Shot had critical failures.**

On 4 out of 20 queries (Q3, Q13, Q18, Q20), the One-Shot model
responded with *"I can't help with that request"* — scoring 1
across all criteria. This was unexpected since One-Shot is
supposed to improve performance.

**Good Example — Zero-Shot (Q12):**
> Query: *"I forgot my account password. How do I reset it?"*  
> Response: Clear step-by-step instructions including
> Forgot Password link, email entry, and reset link.  
> Scores: Relevance 5, Coherence 5, Helpfulness 5 ✅

**Bad Example — One-Shot (Q18):**
> Query: *"Are my payment details saved securely?"*  
> Response: *"I can't help with that request."*  
> Scores: Relevance 1, Coherence 2, Helpfulness 1 ❌

**Both methods performed equally well on simple queries** like
order tracking, password reset, and leaving reviews — scoring
5/5/5 in most cases.

---

## 4. Conclusion & Limitations

### Conclusion

Zero-Shot prompting proved more reliable than One-Shot for
this e-commerce customer support task. The single example in
the One-Shot template may have confused the model on queries
that didn't closely match the example topic.

Llama 3.2 1B is **partially suitable** for basic customer
support — it handles simple, common queries well but struggles
with sensitive or complex topics.

### Limitations

- **No real-time data** — model cannot access actual orders
- **Hallucination risk** — model invents policies that may not exist
- **Slow on CPU** — takes several seconds per response
- **Small model** — 1B parameters limits reasoning ability
- **No memory** — each query is independent, no conversation history

### Next Steps

1. Add **RAG (Retrieval Augmented Generation)** to ground
   responses in real policy documents
2. Use a **larger model** like Llama 3.2 3B for better quality
3. Build a **Streamlit UI** for live chat interaction
4. Add **few-shot prompting** with 3-5 examples
5. Implement **conversation memory** for multi-turn support