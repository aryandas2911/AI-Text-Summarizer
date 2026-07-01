# AI Text Summarizer

A simple web app that summarizes text and documents using pretrained Hugging Face transformer models, wrapped in a [Streamlit](https://streamlit.io/) UI.

## Features

- **Text input** — paste any text and summarize it.
- **File input** — upload a `.txt` or `.md` file (UTF-8 or Latin-1 encoded).
- **Multiple models** — choose between `distilbart-cnn-12-6` (fast), `bart-large-cnn` (higher quality), and `t5-small` (lightweight).
- **Adjustable output** — control minimum/maximum summary length (in tokens) and toggle sampling for more creative summaries.
- **Input cleaning** — whitespace is normalized and long inputs are truncated to keep the model within its limits.

## Requirements

- Python 3.9+
- Dependencies (see [requirements.txt](requirements.txt)):
  - `streamlit`
  - `transformers>=4.40,<5`
  - `torch`
  - `sentencepiece`

> **Note:** `transformers` is pinned to `<5` on purpose. In transformers v5 the `"summarization"` pipeline task was removed, which breaks this app.

## Setup

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
streamlit run app.py
```

This opens the app in your browser (default: http://localhost:8501).

1. Choose an **Input Type** (Text or File).
2. Pick a **Model**.
3. Set the **minimum** and **maximum** summary length (in tokens).
4. Optionally enable **sampling** for more varied summaries.
5. Provide your text or upload a file, then click **Summarize**.

The original text appears on the right, with the generated summary below it.

> The first run with a given model downloads its weights from the Hugging Face Hub (a few hundred MB for the BART models), so the initial summarization may take a while.

## How it works

| Component | Purpose |
|-----------|---------|
| `clean_and_truncate()` | Normalizes whitespace and caps input at ~20,000 characters. |
| `Summarizer` | Loads a Hugging Face `summarization` pipeline once, then exposes a `summarize()` method. |
| `main()` | Builds the Streamlit UI and wires user input to the summarizer. |

## Models

| Model | Notes |
|-------|-------|
| `sshleifer/distilbart-cnn-12-6` | Default. Distilled BART — fast, good quality. |
| `facebook/bart-large-cnn` | Larger, higher quality, slower. |
| `t5-small` | Small and lightweight. |

All summarization models used here have a **~1024-token input limit**; longer inputs are truncated.

## License

For educational and personal use.
