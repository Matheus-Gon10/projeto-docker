from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify(mensagem="Olá, Docker!")


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/soma")
def soma():
    try:
        a = float(request.args["a"])
        b = float(request.args["b"])
    except (KeyError, ValueError):
        return jsonify(erro="Informe os parâmetros numéricos 'a' e 'b'"), 400
    return jsonify(resultado=a + b)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
