from flask import Flask 
app = flask (__name__)

@app.route("/")
def hello():
    return "hello world"

if __name__ == "__main__":
app.run("host=127.0.0.1", port=8080, debug=True)