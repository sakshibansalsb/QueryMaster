# QueryMaster (Queryable Document Index Using Gemini Language Model)

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Applications](#applications)

## Project Overview

This project creates a queryable index of documents using the Gemini language model. It leverages vector embeddings to allow users to query a collection of documents for specific information. The project uses various Python libraries such as `llama_index`, `huggingface`, and `dotenv` to efficiently manage the document loading, embedding, and querying processes.

## Key Features

- Create and manage a vector-based index of documents.
- Efficiently query the indexed documents using natural language questions.
- Easily integrate with the Gemini language model for advanced query handling.

## Setup Instructions

To set up and run the project locally, follow these instructions:

### Prerequisites

- Python 3.7 or later
- Pip (Python package installer)

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/queryable-document-index.git
    cd queryable-document-index
    ```

2. **Create and Activate a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. **Install Dependencies**

    ```bash
    pip install docx2txt llama_index huggingface python-dotenv
    ```

4. **Set Up Environment Variables**

    Create a `.env` file in the root directory with the following content:

    ```env
    GEMINI_API_KEY=your_actual_gemini_api_key_here
    ```

5. **Create Project Structure**

    - **Create a `data` Directory**: 
      In the VS Code file explorer, right-click in the workspace area and select New Folder. Name the folder `data`. This folder will hold the files you want to perform Q&A on.

    - **Add Files to the `data` Folder**: 
      Place the text files or documents you want to query into the `data` folder.

    - **Create `app.py`**: 
      In the root of your project (where the `venv` and `data` folders are located), right-click and select New File. Name the file `app.py`.

    - **Write the Code**: 
      Open `app.py` and add the provided code.

6. **Run the Application**

    ```bash
    python app.py
    ```

## Usage

- **Start the Application**: Run the `app.py` file to start the application.
- **Query the Index**: Enter your query when prompted to receive responses based on the indexed documents.

## Applications

- **Document Search**: Quickly find relevant information from a large corpus of documents.
- **Q&A Systems**: Build responsive Q&A systems that interact with users and provide precise answers from a specified dataset.
- **Content Summarization**: Summarize the contents of documents based on specific queries.

## Additional Notes

- Make sure your documents in the `data` folder are in a compatible format.
- Adjust model names and API configurations as needed based on your requirements.
