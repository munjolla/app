from flask import Flask

app = Flask(__name__)

@app.route('/')
def inedx():
    return "<h1>NEŠTO KAO RADIM</h1>"

@app.route('/about')
def about():
    return "<h1>ČUPAM I SADIM</h1>"

if __name__ == "__main__":
    app.run(debug=True)
