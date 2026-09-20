import random
from flask import Flask, render_template, request

app = Flask(__name__)

jogadorresultado = 0
computadorresultado = 0

escolha_jogador = None
escolha_computador = None
resultado = None

@app.route("/", methods=["GET", "POST"])
def inicio():

    global jogadorresultado, computadorresultado
    global escolha_jogador, escolha_computador, resultado

    if request.method == "POST" and "reiniciar" in request.form:
        jogadorresultado = 0
        computadorresultado = 0
        escolha_jogador = None
        escolha_computador = None
        resultado = None

    if request.method == "POST" and "escolha" in request.form:
        opções = ["pedra", "papel", "tesoura"]

        escolha_jogador = request.form["escolha"]
        escolha_computador = random.choice(opções)

        if escolha_jogador == escolha_computador:
            resultado = "EMPATE! Ninguém ganhou."

        elif ((escolha_jogador == "pedra" and
        escolha_computador == "tesoura") or
            (escolha_jogador == "papel" and
            escolha_computador == "pedra") or
            (escolha_jogador == "tesoura" and
            escolha_computador == "papel")):
                resultado = "VOCÊ VENCEU! PARABÉNS!"
                jogadorresultado += 1

        else:
                resultado = "COMPUTADOR VENCEU! QUE PENA, VOCÊ PERDEU!"
                computadorresultado += 1

    return render_template(
        "index.html",
        escolha_jogador=escolha_jogador,
        escolha_computador=escolha_computador,
        resultado=resultado,
        jogadorresultado=jogadorresultado,
        computadorresultado=computadorresultado
    )

if __name__ == "__main__":
    app.run(debug=True)