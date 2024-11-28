from flask import Flask, jsonify, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'




@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
