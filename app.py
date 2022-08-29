from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from housing.logger import logging
from housing.exception import HousingException
import sys

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return "Hello, Working on my first End to End Project"


if __name__ == '__main__':
    app.run()
