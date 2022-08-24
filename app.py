from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from housing.logger import logging
from housing.exception import HousingException
import sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        housing = HousingException(e, sys)
        logging.info(housing.error_message)   
        logging.info("We are testing the logger")
    return "Hello, Working on my first End to End Project"


if __name__ == '__main__':
    app.run(debug=True)