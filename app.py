from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    render_template('index.html');
    #return 'hello world!'

@app.route("/users")
def index():
    render_template('index.html');
    #return 'hello world!'

# @app.route("/")
# def index():
#     render_template('index.html');
#     #return 'hello world!'

if __name__ == "__main__":
    app.run(debug=True);    