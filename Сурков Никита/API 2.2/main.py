from flask import Flask, render_template, request, jsonify, app
from flask_mysqldb import MySQL
from App.ALLS import *
from App.ADDR import *
from App.P3 import *
from App.Connect import *


@app.route("/AllSportsmens", methods=['GET'])
def GETAllSport():
    return AllSportsmens()


@app.route("/AddRole", methods=['POST'])
def AR():
    return Add()


@app.route("/P3", methods=['GET'])
def GETP3():
    return P3()


if __name__ == "__main__":
    app.run("localhost", 5000)
