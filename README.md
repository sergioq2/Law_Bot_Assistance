
# AI Bot Law Assitance 

The JurisBot App is a Python application built using Streamlit, designed to automate the processing of various legal documents, particularly those related to law cases and lawsuits. The app utilizes AI agents trained with Langchain and OpenAI to extract data and insights from large documents. Users can also engage in conversation with an AI agent, acting as a ChatBot, specifically trained for legal matters related to the uploaded documents and the Colombian constitution.


## Project Structure

The project folder is organized as follows:

home.py: The main page of the application where users can upload documents and interact with the AI agent.

front/: A folder containing additional pages and components of the app's front-end
## Acknowledgements

-Document Processing: The app provides the ability to upload PDF and other types of legal documents, automatically extracting and processing the text content for further analysis.

-AI ChatBot: Users can engage in conversations with an AI agent powered by OpenAI's ChatGPT 3.5 model. The AI agent is trained to provide information and insights related to legal matters found in the uploaded documents, focusing on Colombian constitution specifics.

-Image to Text Conversion: The app employs AWS SageMaker's Textract service to convert text embedded within images, making the content accessible for analysis.


## API Reference

Python: The core programming language used for building the application.

Streamlit: A Python library for creating interactive web applications for data science and machine learning.

OpenAI API: The OpenAI API is utilized to integrate the ChatGPT 3.5 model, allowing users to have legal discussions with the AI agent.

AWS SageMaker Textract: Amazon Textract is employed for extracting text from images, enhancing the app's capability to process various types of legal documents.


## Authors

- Sergio Quintero

