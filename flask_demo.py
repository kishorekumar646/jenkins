from flask import Flask

app = Flask(__name__,)

@app.route('/')
def test():
    
    return "<h1 style='color:red'>Hi hello flask, How are you?</h1>"


if __name__ == "__main__":
    app.run(debug=True)

