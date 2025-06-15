# toy_claude_code

A toy version of Claude Code using Google's free Gemini API.

## Overview

This repository contains a minimal implementation inspired by Anthropic's Claude Code, but leverages Google's Gemini API. The goal is to provide a lightweight, easy-to-understand codebase demonstrating how to interact with the Gemini API for code analysis, completion, or generation tasks.

## Features

- Connects to Google's Gemini API (free tier)
- Simple, readable Python codebase
- Example scripts for code generation and analysis

## Getting Started

### Prerequisites

- Python 3.8 or later
- A Google Gemini API key (free tier)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Ulz-Sch/toy_claude_code.git
    cd toy_claude_code
    ```

2. (Optional) Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

Set your Gemini API key as an environment variable:

```bash
export GEMINI_API_KEY="your-gemini-api-key"
```

Or create a `.env` file:

```
GEMINI_API_KEY=your-gemini-api-key
```

### Usage

Run the main script to see an example of code completion or analysis:

```bash
python main.py
```

Check the script arguments and adjust according to your use case.

## Contributing

Pull requests, issues, and suggestions are welcome!

## License

This project is released under the MIT License.

---

[Check out my Boot.dev profile](https://www.boot.dev/u/felipe_schulz)
