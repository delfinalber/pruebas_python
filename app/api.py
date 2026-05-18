import http.client

from flask import Flask

from app import util
from app.calc import Calculator

CALCULATOR = Calculator()
api_application = Flask(__name__)
HEADERS = {"Content-Type": "text/plain", "Access-Control-Allow-Origin": "*"}


def _execute_binary_operation(op_1, op_2, operation):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return (f"{operation(num_1, num_2)}", http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


def _execute_unary_operation(op_1, operation):
    try:
        num_1 = util.convert_to_number(op_1)
        return (f"{operation(num_1)}", http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


@api_application.route("/")
def hello():
    return "Hello from The Calculator!\n"


@api_application.route("/calc/add/<op_1>/<op_2>", methods=["GET"])
def add(op_1, op_2):
    return _execute_binary_operation(op_1, op_2, CALCULATOR.add)


@api_application.route("/calc/substract/<op_1>/<op_2>", methods=["GET"])
def substract(op_1, op_2):
    return _execute_binary_operation(op_1, op_2, CALCULATOR.substract)


@api_application.route("/calc/multiply/<op_1>/<op_2>", methods=["GET"])
def multiply(op_1, op_2):
    return _execute_binary_operation(op_1, op_2, CALCULATOR.multiply)


@api_application.route("/calc/divide/<op_1>/<op_2>", methods=["GET"])
def divide(op_1, op_2):
    return _execute_binary_operation(op_1, op_2, CALCULATOR.divide)


@api_application.route("/calc/power/<op_1>/<op_2>", methods=["GET"])
def power(op_1, op_2):
    return _execute_binary_operation(op_1, op_2, CALCULATOR.power)


@api_application.route("/calc/sqrt/<op_1>", methods=["GET"])
def sqrt(op_1):
    return _execute_unary_operation(op_1, CALCULATOR.sqrt)


@api_application.route("/calc/log10/<op_1>", methods=["GET"])
def log10(op_1):
    return _execute_unary_operation(op_1, CALCULATOR.log10)
