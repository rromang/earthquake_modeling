# python version 3.8.12
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, MetaData, inspect, Table

from flask import Flask, jsonify, render_template
from flask import url_for
import json


# #################################################
# # Flask Setup
# #################################################
app = Flask(__name__, static_url_path='/static/')

# #################################################
# # Flask Routes
# #################################################

@app.route("/")
def welcome():
    # """List all available api routes."""
    return render_template('index.html')

@app.route("/sweetviz")
def viz1():
    # """List all available api routes."""
    return render_template('SWEETVIZ_REPORT.html')

@app.route("/initial_EDA")
def viz2():
    # """List all available api routes."""
    return render_template('initial_data.html')

@app.route("/ML")
def viz3():
    # """List all available api routes."""
    return render_template('ML_data.html')

@app.route("/histograms")
def viz4():
    # """List all available api routes."""
    return render_template('histogram.html')


if __name__ == '__main__':
    app.run(debug=True)