from flask import Flask, request, render_template_string
from transformers import pipeline

app = Flask(__name__)

# Initialize the summarizer
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def extractive_summarize(text, max_length=150, min_length=40):
    # Split the input text into chunks of 1024 tokens each
    max_chunk = 1024
    chunks = [text[i:i+max_chunk] for i in range(0, len(text), max_chunk)]
    summary = ""
    for chunk in chunks:
        summarized_chunk = summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)
        summary += summarized_chunk[0]['summary_text'] + " "
    return summary.strip()

TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <title>Article Summarizer</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f9f9f9;
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }
    .container {
      background-color: #fff;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      padding: 30px;
      border-radius: 8px;
      max-width: 800px;
      width: 100%;
    }
    h1 {
      font-size: 2em;
      margin-bottom: 20px;
      color: #333;
    }
    form {
      display: flex;
      flex-direction: column;
    }
    textarea {
      resize: none;
      padding: 10px;
      font-size: 1em;
      border: 1px solid #ddd;
      border-radius: 4px;
      margin-bottom: 20px;
    }
    button {
      background-color: #4CAF50;
      color: white;
      border: none;
      padding: 15px 20px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 1em;
      margin: 4px 2px;
      cursor: pointer;
      border-radius: 4px;
    }
    button:hover {
      background-color: #45a049;
    }
    h2 {
      font-size: 1.5em;
      color: #333;
      margin-top: 20px;
    }
    p {
      font-size: 1em;
      color: #555;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Article Summarizer</h1>
    <form method="post">
      <textarea name="article" rows="10" cols="100" placeholder="Paste your article here..."></textarea>
      <button type="submit">Summarize</button>
    </form>
    {% if summary %}
    <h2>Summary</h2>
    <p>{{ summary }}</p>
    {% endif %}
  </div>
</body>
</html>

'''

@app.route('/', methods=['GET', 'POST'])
def home():
    summary = ''
    if request.method == 'POST':
        article = request.form['article']
        summary = extractive_summarize(article)
    return render_template_string(TEMPLATE, summary=summary)

if __name__ == '__main__':
    app.run(debug=True)



