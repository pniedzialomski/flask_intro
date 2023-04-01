from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello, world! hahaha ale jaja jak berety"

if __name__ == "__main__":
    app.run(debug=True)

