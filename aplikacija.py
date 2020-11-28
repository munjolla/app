from flask import Flask

app = Flask(__name__)

@app.route('/')
def inedx():
    return "evo i mene"

if __name__ == "__main__":
    app.run(debug=True)
