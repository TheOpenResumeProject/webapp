from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/editor')
def editor():
    return render_template('editor.html')


@app.route('/script')
def script():
    return render_template('script.js')


if __name__ == '__main__':
    app.run(debug=True)
