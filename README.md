# 🎬 AI Script & Plot Generator

A lightweight Streamlit web application that uses a fine-tuned text generation model (based on `distilgpt2`) to generate creative movie scripts and plot ideas from user-provided prompts.

## 🚀 Features
* **Interactive Web UI:** Simple, clean interface built using Streamlit.
* **Fine-Tuned Text Generation:** Unpacks custom `distilgpt2` model checkpoints to generate unique narratives.
* **Optimized Resource Loading:** Uses Streamlit caching mechanisms to keep the model persistent in memory.
* **CPU Inference:** Pre-configured to execute text generation tasks locally without demanding a dedicated GPU.

## 🛠️ Prerequisites & Installation

This project manages environments and project dependencies using [uv by Astral](https://github.com).

### 1. Clone the Repository
```bash
git clone https://github.com
cd movie_llm
```

### 2. Configure the Python Version
Ensure your local environment matches the project's requirements (Python 3.13):
```bash
uv python pin 3.13
```

### 3. Install Dependencies
Synchronize your virtual environment and install dependencies like `transformers`, `torch`, and `streamlit`:
```bash
uv sync
```

### 4. Add Your Model Checkpoint
Ensure your local model weights and checkpoints are extracted into the expected directory path:
```text
movie_llm/
└── output/
    └── model/
        └── checkpoint-2740/
            ├── config.json
            └── model.safetensors (or pytorch_model.bin)
```

## 💻 How to Run

Activate your project environment and launch the local Streamlit application server:

```bash
# Activate the uv virtual environment
.venv\Scripts\Activate.ps1

# Start up the Streamlit server
streamlit run app.py
```
*Note: Replace `app.py` with the actual filename containing your script code.*

Once the server builds, open your browser and navigate to the address displayed in your terminal (usually `http://localhost:8501`).

## 📝 Usage Example
1. Type a short starter phrase into the input field (e.g., *"A short film about a pilot who"*).
2. Click **Generate my plot!**
3. View the AI-generated extension displayed on the screen.
