# Setup Guide

## Requirements
- Python 3.8+
- Ollama installed on your machine

## Step 1 — Install Ollama
Download from https://ollama.com and install for your OS.

## Step 2 — Pull the Model
```bash
ollama pull llama3.2:1b
```

## Step 3 — Clone 
```bash
git clone https://github.com/vikram0678/botique-ollama.git
cd botique-ollama
```

## Step 4 — Run the Chatbot
Make sure Ollama is running, then:
```bash
python chatbot.py
```

## Step 5 — Score the Results
Open `eval/results.md` and manually fill in
the Relevance, Coherence, Helpfulness scores (1-5).