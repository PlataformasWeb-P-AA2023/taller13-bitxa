from flask import Flask, render_template
import requests
import json
from config import usuario, clave

app = Flask(__name__, template_folder='templates')

django_api_base_url = "http://127.0.0.1:8000/api/"


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/departamentos")
def departamentos():
    """
    """
    r = requests.get(django_api_base_url + "departamentos/",
                     auth=(usuario, clave))
    departamentos = json.loads(r.content)['results']
    numero_departamentos = json.loads(r.content)['count']
    return render_template("departamentos.html", departamentos=departamentos,
                           numero_departamentos=numero_departamentos)


@app.route("/edificios")
def edificios():
    """
    """
    r = requests.get(django_api_base_url + "edificios/",
                     auth=(usuario, clave))
    edificios = json.loads(r.content)['results']
    numero_edificios = json.loads(r.content)['count']
    return render_template("edificios.html", edificios=edificios,
                           numero_edificios=numero_edificios)


@app.route("/propietarios")
def propietarios():
    """
    """
    r = requests.get(django_api_base_url + "propietarios/",
                     auth=(usuario, clave))
    edificios = json.loads(r.content)['results']
    numero_edificios = json.loads(r.content)['count']
    return render_template("propietarios.html", propietarios=edificios,
                           numero_propietarios=numero_edificios)
