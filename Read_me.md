# Smart Chatbot with Web Search

A lightweight, beginner-friendly conversational chatbot using **LangChain** and **DuckDuckGo Search API**, integrated with real-time web search results to answer factual queries. This project demonstrates the power of modern Python libraries and APIs to build intelligent chatbots without relying on expensive services.

## Features

- **Conversational Chatbot**: Uses LangChain for managing the chatbot's memory and conversation flow.
- **Real-Time Web Search**: Fetches real-time search results using DuckDuckGo API to answer factual queries.
- **Lightweight**: No paid APIs required for core functionality, making it cost-effective.
- **Easy Setup**: Simple, plug-and-play functionality for users with clear setup instructions.
- **Modular Design**: The project is designed to be beginner-friendly, allowing for easy modifications and extensions.

## Technologies Used

- **Python**: The primary programming language used for the development of the chatbot.
- **LangChain**: A framework that facilitates building conversational models with memory.
- **DuckDuckGo Search API**: Fetches real-time web search results to assist in answering factual queries.
- **Transformers**: Hugging Face’s Transformers library is used for NLP tasks and accessing pre-trained language models.
- **Torch**: Used for deep learning tasks, particularly for language model operations.
- **Requests**: For making HTTP requests to external services like the DuckDuckGo API.

## Installation

To get this project up and running on your local machine, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/smart-chatbot-with-websearch.git
2. **Navigate into the project folder**:

   ```bash
   cd smart-chatbot-with-websearch
3. **setup a virtual environment**:

   ```bash
   python -m venv env
4. **activate the virtual environment**
   
   **windows**
   
   ```bash
   .\env\Scripts\activate
   
  **mac/linux**
  
  ```bash
    source env/bin/activate
  ```

5. **install the dependencies manually**

   ```bash
   pip install langchain requests torch transformers duckduckgo-search
    ```
6. run the chatbot
   
  ```bash
  python chatbot.py
  ```
   
## Acknowledgements

- **LangChain**: A powerful framework for creating conversational AI systems that simplifies working with language models and memory management. [LangChain GitHub](https://github.com/hwchase17/langchain)
  
- **DuckDuckGo API**: Used to fetch real-time search results for answering queries, enabling the chatbot to provide more relevant and up-to-date information. [DuckDuckGo API](https://duckduckgo.com/api)

- **Hugging Face Transformers**: A library that provides pre-trained models for natural language processing (NLP) tasks, which are essential for generating chatbot responses. [Hugging Face GitHub](https://github.com/huggingface/transformers)

- **Requests**: A simple HTTP library for making requests to external APIs, including the DuckDuckGo API for web search integration. [Requests GitHub](https://github.com/psf/requests)

- **PyTorch**: A deep learning framework that supports the efficient training and deployment of NLP models like the ones used in this project. [PyTorch GitHub](https://github.com/pytorch/pytorch)



