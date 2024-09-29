# PDF Chatbot with LLM

A Streamlit application that allows users to upload a PDF document and ask questions based on its content. The app extracts text from the uploaded PDF and leverages OpenAI's GPT models to provide insightful answers to user queries.

## Features

- **PDF Upload**: Easily upload any PDF document through the web interface.
- **Text Extraction**: Extracts text from the uploaded PDF using `PyMuPDF`.
- **Summarization**: Automatically summarizes lengthy PDFs to fit within token limits.
- **Interactive Q&A**: Ask questions related to the PDF content and receive answers powered by OpenAI's GPT models.
- **User-Friendly Interface**: Clean and intuitive UI built with Streamlit.

## Demo

![App Screenshot](assets/screenshot.png)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Limitations](#limitations)
- [Security and Privacy](#security-and-privacy)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.7 or higher
- An OpenAI API key. You can obtain one by [signing up for an OpenAI account](https://platform.openai.com/signup/).

### Clone the Repository

```bash
git clone https://github.com/yourusername/pdf-chatbot-llm.git
cd pdf-chatbot-llm
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

- On Windows:

  ```bash
  venv\Scripts\activate
  ```

- On macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Set Up OpenAI API Key

Set your OpenAI API key as an environment variable:

- On Windows:

  ```bash
  set OPENAI_API_KEY=your-api-key-here
  ```

- On macOS/Linux:

  ```bash
  export OPENAI_API_KEY=your-api-key-here
  ```

Alternatively, you can create a `.env` file in the project root:

```bash
OPENAI_API_KEY=your-api-key-here
```

### Run the App

```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`.

## Configuration

You can adjust the app's behavior by modifying the following parameters in `app.py`:

- **Model Selection**: Change the `model` parameter in the `query_llm` function to switch between OpenAI models (e.g., `"gpt-3.5-turbo"` or `"gpt-4"`).
- **Token Limits**: Adjust the `max_tokens` parameter to control the response length.
- **Summarization Threshold**: Modify the character length threshold that triggers summarization.

## Limitations

- **Token Limits**: OpenAI's models have maximum context lengths (e.g., ~4096 tokens for `gpt-3.5-turbo` and ~8192 tokens for `gpt-4`). Extremely large PDFs may exceed these limits even after summarization.
- **Response Time**: Processing and generating responses for large documents may take longer.
- **Costs**: Usage of OpenAI's API is not free. Ensure you monitor your API usage to avoid unexpected charges.

## Security and Privacy

- **API Key Security**: Never share your OpenAI API key or hardcode it in public repositories.
- **User Data**: Uploaded PDFs and queries are sent to OpenAI's servers for processing. Avoid uploading sensitive or confidential documents.
- **Data Handling**: The app does not store any user data. All processing is done in memory.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

### Steps to Contribute

1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Commit your changes:

   ```bash
   git commit -m "Add your message here"
   ```

4. Push to the branch:

   ```bash
   git push origin feature/your-feature-name
   ```

5. Open a pull request on GitHub.

## License

This project is licensed under the [MIT License](LICENSE).

---

**Disclaimer**: This project is for educational purposes. The developer is not responsible for any misuse of the application.

# Additional Information

## Dependencies

- **[Streamlit](https://streamlit.io/)**
- **[PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)** (imported as `fitz`)
- **[OpenAI](https://github.com/openai/openai-python)**
- **[tiktoken](https://github.com/openai/tiktoken)** (optional, for token counting)

Install them via:

```bash
pip install streamlit pymupdf openai tiktoken
```

## Contact

For any questions or suggestions, please open an issue or contact me at [your-email@example.com](mailto:your-email@example.com).

# Code Overview

Here's a brief overview of how the application works:

- **Text Extraction**: The `extract_text_from_pdf` function reads the uploaded PDF file and extracts text from each page.
- **Summarization**: If the extracted text exceeds a certain length, the `summarize_text` function summarizes it to fit within the token limits of the OpenAI model.
- **Query Handling**: When a user submits a question, the app combines the extracted (or summarized) text with the user's query to form a prompt.
- **LLM Response**: The `query_llm` function sends the prompt to the OpenAI API and returns the assistant's response.

# Future Enhancements

- **Embeddings and Vector Stores**: Implement embeddings to handle larger documents and improve response relevance.
- **Chunking Strategy**: Split large texts into manageable chunks and retrieve relevant sections based on the query.
- **UI Improvements**: Enhance the user interface with better styling and responsiveness.
- **Error Handling**: Add more robust error handling and user feedback mechanisms.

---

Thank you for using the PDF Chatbot with LLM! If you find this project useful, please give it a star on GitHub.
