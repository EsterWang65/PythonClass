from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    return "<h1>hello world</h1>"

if __name__ == "main.py":
    app.run(host = "0.0.0.0",port = 5000)