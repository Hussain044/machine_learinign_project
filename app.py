from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Working on my first End to End Project"


if __name__ == '__main__':
    app.run(debug=True, port=5000)