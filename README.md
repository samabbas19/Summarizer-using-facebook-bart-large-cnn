README for Article Summarizer Web App
Overview
This web application allows users to input a large article or text and get a summarized version of it. The app is built using Flask and leverages the transformers library from Hugging Face to perform text summarization with a pre-trained BART model.

How It Works
User Input: The user pastes an article into the text area on the web page.
Form Submission: The user submits the form.
Text Processing: The app splits the input text into chunks and summarizes each chunk using the BART model.
Output: The summarized text is displayed on the web page.
Requirements
Python 3.6 or higher
Flask
Transformers (Hugging Face library)
PyTorch (backend for the Transformers library)
# Summarizer-using-facebook-bart-large-cnn
facebook/bart-large-cnn
