from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home')
def home_page():
    return render_template("home_page.html")

@app.route('/nutrition')
def nutrition_page():
    return render_template("nutrition_page.html")


@app.route('/training')
def training_page():
    return render_template("training_page.html")


@app.route('/questions')
def questions_page():
    return render_template("questions_page.html")


if __name__ == '__main__':
    app.run()
