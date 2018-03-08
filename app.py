from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('user.html')


@app.route('/hives')
def hives():
    return render_template("hives.html")


@app.route('/info')
def info():
    return render_template("info.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return "You are using POST"
    else:
        return "Your probably using GET"


@app.route('/signup')
def login():
    return render_template("signup.html")


if __name__ == '__main__':
    app.run(debug=True)
