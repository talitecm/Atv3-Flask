from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/pizzaria')
def pizzaria():
    return render_template('pizzaria.html')

@app.route('/fazer-pedido', methods=["GET", "POST"])
def fazer_pedido():
    return render_template('fazer-pedido.html')

@app.route('/confirmacao', methods=["POST"])
def confirmacao():
    # Recebe os dados enviados pelo formulário
    massa = request.form.get("massa")
    queijo = request.form.get("queijo")
    recheio = request.form.get("recheio")
    borda = request.form.get("borda")
    
    return render_template("confirmacao.html", 
                           massa=massa, 
                           queijo=queijo, 
                           recheio=recheio, 
                           borda=borda)

@app.route('/calc_imc')
def calc_imc():
    return render_template('calc-imc.html')

@app.route('/imc', methods=["GET", "POST"])
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