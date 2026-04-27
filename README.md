# LangChain Learning Projects

A collection of hands-on projects demonstrating various capabilities of the **LangChain** framework with OpenAI integration. This repository serves as a practical learning resource for building LLM-powered applications.

## 📋 Overview

This repository contains educational code examples showcasing:

- AI Agents with tool integration
- Retrieval-Augmented Generation (RAG)
- Vector embeddings and similarity search
- Chat history management
- Audio transcription with Whisper
- Prompt engineering templates
- Multi-model integration (GPT-4o, Gemma, Mistral)

## 🛠️ Tech Stack

| Component       | Library/Version                      |
| --------------- | ------------------------------------ |
| Framework       | LangChain 1.0.7                      |
| LLM Integration | OpenAI 2.8.0, LangChain OpenAI 1.0.3 |
| Vector Database | ChromaDB 1.3.4                       |
| Web UI          | Streamlit 1.51.0                     |
| Language        | Python 3.13+                         |

## 📁 Project Structure

```
langchain/
├── agents/              # AI agent implementations (ReAct, search tools)
├── assignments/         # Practical applications (blog generator, email generator)
├── audio_whisper/       # Audio transcription demos
├── basics/              # Basic LangChain & OpenAI demos
├── chains/              # Chain implementations (LCEL, sequential chains)
├── chathistory/         # Chat history & prompt template demos
├── embeddings/          # Vector embeddings & similarity search
├── imageprocessing/     # Image processing demos
├── prompttemplates/     # Prompt template examples
├── rag/                 # RAG systems for documents & PDFs
└── requirements.txt     # Project dependencies
```

## 🚀 Setup

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd langchain
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## 📂 Module Descriptions

### `/basics`

Foundation demos for LangChain and OpenAI integration.

- `openai_demo.py` - Basic GPT-4o interaction
- `gemma_demo.py` - Google Gemma model integration
- `streamlit_demo.py` - Simple Streamlit UI

### `/agents`

AI agents with autonomous decision-making capabilities.

- `agent_demo.py` - ReAct-style agent with Wikipedia & DuckDuckGo tools
- `landmark_helper.py` - Landmark information agent

### `/rag`

Retrieval-Augmented Generation systems for document Q&A.

- `rag_demo.py` - Text document Q&A with ChromaDB
- `pdf_rag_demo.py` - PDF document Q&A system

### `/chains`

Chain implementations for complex workflows.

- `lcel_demo.py` - LangChain Expression Language
- `sequential_chain_demo.py` - Multi-step sequential chains
- `multiple_llms_demo.py` - Working with multiple LLMs

### `/embeddings`

Vector embeddings and semantic similarity search.

- `embeddings_demo.py` - Text embedding generation
- `similarity_finder.py` - Semantic similarity search
- `job_search_helper.py` - Job matching using embeddings

### `/chathistory`

Chat applications with persistent conversation history.

- `streamlit_chathistory_demo.py` - Streamlit chat app with history
- `chathistory_demo.py` - Basic chat history management

### `/audio_whisper`

Audio processing and transcription.

- `whisper_demo.py` - Basic Whisper integration
- `streamlit_audio_demo.py` - Audio transcription web app

### `/prompttemplates`

Reusable prompt template systems.

- `prompttemplate_demo.py` - Basic template patterns
- `travelguide_demo.py` - Travel guide template example

### `/assignments`

Practical AI applications.

- `blogpost_generator.py` - Automated blog post creation
- `interview_helper.py` - Interview preparation assistant
- `marketing_email_generator.py` - Marketing email copywriter
- `mistral_demo.py` - Mistral model integration

## 🏃 Running Examples

Most scripts can be run directly with Python:

```bash
python basics/openai_demo.py
python rag/rag_demo.py
```

For Streamlit-based demos:

```bash
streamlit run basics/streamlit_demo.py
streamlit run chathistory/streamlit_chathistory_demo.py
```

## 📚 Learning Outcomes

This repository covers:

- LangChain framework fundamentals
- Building RAG systems from scratch
- Creating autonomous AI agents
- Vector database operations with ChromaDB
- Audio transcription with Whisper
- Streamlit UI development
- Prompt engineering best practices

## 📝 Requirements

See `requirements.txt` for complete dependency list. Key dependencies:

- `langchain` >= 1.0.7
- `langchain-openai` >= 1.0.3
- `langchain-community` >= 0.4.1
- `chromadb` >= 1.3.4
- `openai` >= 2.8.0
- `streamlit` >= 1.51.0

## 🔑 API Keys Required

- **OpenAI API Key** (required for most demos)

## 📄 License

This project is for educational purposes.

---

**Note:** This is a learning repository. Feel free to explore, modify, and use the code examples for your own projects.
