# 🦙 Run Ollama On Your Own Machine

> Build and run powerful AI models locally — no cloud, no cost, complete privacy.

![Ollama Banner](https://img.shields.io/badge/Ollama-Local%20AI-blue?style=for-the-badge&logo=ollama)
![Model](https://img.shields.io/badge/Model-qwen2.5%3A0.5b-green?style=for-the-badge)
![Model](https://img.shields.io/badge/Model-gemma3%3A1b-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

---

## 📌 Project Overview

This project walks through setting up **Ollama** on your local machine to run open-source large language models (LLMs) entirely offline. By the end, you'll have a working local AI assistant, understand model parameters, and even create your own custom AI persona — all without relying on any cloud service.

**Project Link:** [View on NextWork](http://learn.nextwork.org/projects/ai-ollama-setup)  
**Author:** pavitrasunkari@gmail.com

---

## 🚀 What You'll Build

- ✅ A locally running AI powered by **Ollama**
- ✅ Chat with open-source models like `qwen2.5:0.5b` and `gemma3:1b`
- ✅ Understand the difference between local AI and cloud AI
- ✅ A custom AI persona (e.g., a **Coding Tutor**)
- ✅ Hands-on understanding of **RAG (Retrieval-Augmented Generation)**

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| [Ollama](https://ollama.com) | Framework to run LLMs locally |
| `qwen2.5:0.5b` | Lightweight open-source AI model (500M parameters) |
| `gemma3:1b` | Google's lightweight open-source model (1B parameters) |
| Terminal / CLI | Running Ollama commands |

---

## 📋 Prerequisites

- A computer running **macOS**, **Linux**, or **Windows (WSL)**
- At least **4GB of RAM** (8GB+ recommended)
- Internet connection for initial model download
- Basic comfort using the terminal/command line

---

## ⚙️ Setup & Installation

### Step 1 — Install Ollama

Head to [https://ollama.com](https://ollama.com) and download the installer for your operating system. Follow the on-screen instructions.

### Step 2 — Verify Installation

Open your terminal and run:

```bash
ollama serve
```

You should see the message:

```
Ollama is running
```

### Step 3 — Pull Your First AI Model

Download a lightweight model to get started:

```bash
ollama pull qwen2.5:0.5b
```

> 💡 `0.5b` means the model has **500 million parameters** — small enough to run smoothly on most machines.

To see all your downloaded models:

```bash
ollama list
```

### Step 4 — Chat with Your Local AI

```bash
ollama run qwen2.5:0.5b
```

Try asking it something:

```
>>> What is the capital of India?
```

**Example Response:**
> The capital of India is **New Delhi**. It was chosen due to its historical significance, political importance, cultural associations with the Indian subcontinent, and accessibility by air and other transport modes.

---

## ☁️ Local AI vs Cloud AI

| Feature | Local AI (Ollama) | Cloud AI (e.g., ChatGPT) |
|--------|-------------------|--------------------------|
| Privacy | ✅ 100% on your machine | ❌ Data sent to servers |
| Cost | ✅ Free after setup | ❌ Subscription/API costs |
| Internet required | ❌ After initial download | ✅ Always |
| Performance | Depends on hardware | High (cloud servers) |
| Customisation | ✅ Full control | ❌ Limited |

---

## 🧠 Understanding RAG

**RAG = Retrieval-Augmented Generation**

Local AI models are trained on general knowledge — they don't have access to your personal files, documents, or real-time data. RAG is the technique used to give AI models access to custom/private knowledge bases by retrieving relevant information before generating a response.

> 🔍 This explains why the local AI couldn't answer personal questions — it only knows what it was trained on.

---

## 🎭 Creating a Custom AI Persona

You can create a custom Modelfile to define your AI's personality and behavior.

**Example: Coding Tutor Persona**

```bash
# Create a Modelfile
cat <<EOF > Modelfile
FROM qwen2.5:0.5b

SYSTEM """
You are an expert coding tutor. You explain programming concepts clearly and patiently,
always providing examples in multiple languages when helpful. You encourage learners
and break down complex ideas into simple steps.
"""
EOF

# Build the custom model
ollama create coding-tutor -f Modelfile

# Run your custom persona
ollama run coding-tutor
```

---

## 💡 Key Concepts Learned

- **What Ollama is** — a tool to run LLMs locally without cloud infrastructure
- **Model parameters** — what `0.5b` and `1b` mean and how they affect performance
- **Local vs cloud AI** — trade-offs between privacy, cost, and performance
- **RAG fundamentals** — why local models lack personal/contextual knowledge
- **Custom personas** — how system prompts shape AI behaviour

---

## ⏱️ Time to Complete

Approximately **1.5 hours**, with the most time-consuming step being the initial model download (varies by internet speed).

---

## 🌱 What's Next?

Here are some ideas to extend this project:

- [ ] Try a larger model like `llama3.2` or `mistral`
- [ ] Build a simple chat UI using Python + Streamlit
- [ ] Implement RAG with your own documents using LangChain
- [ ] Explore the [Ollama REST API](https://github.com/ollama/ollama/blob/main/docs/api.md) to integrate into apps
- [ ] Build websites and projects using [Claude](https://claude.ai)

---

## 📚 Resources

- [Ollama Official Docs](https://github.com/ollama/ollama)
- [Ollama Model Library](https://ollama.com/library)
- [NextWork Project Page](http://learn.nextwork.org/projects/ai-ollama-setup)
- [Understanding RAG — IBM](https://research.ibm.com/blog/retrieval-augmented-generation-RAG)

---

## 🙌 Acknowledgements

This project was completed as part of the [NextWork](http://learn.nextwork.org) learning program. Thanks to the open-source community behind Ollama, Qwen, and Gemma for making local AI accessible to everyone.

---

<p align="center">Made with ❤️ by <strong>Pavitra Sunkari</strong></p>
