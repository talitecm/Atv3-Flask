from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/pizzaria')
def pizzaria():
    return render_template('pizzaria.html')

""" ---------------------------------- """

@app.route('/calc_imc')
def index():
    return render_template('index.html')

@app.route('/imc', methods=["GET"])
def imc():
    nome = request.args.get("nome")
    altura = float(request.args.get("altura"))
    peso = float(request.args.get("peso"))
    imc = round((peso/altura**2),2)

    if (imc < 18.5):
        mensagem = "Você está abaixo do peso!"

    elif(imc < 24.9):
        mensagem = "Você está com o peso normal!"

    elif(imc < 29.9):
        mensagem = "Você está com o sobrepeso!"
    
    else:
        mensagem = "Você está obeso!"

    return render_template("imc.html", mensagem = mensagem)