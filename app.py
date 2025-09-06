from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>🔮 Previsor de Idade</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea, #764ba2);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            color: #333;
        }
        .container {
            background: #fff;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
            text-align: center;
            width: 400px;
        }
        h1 {
            margin-bottom: 20px;
            color: #444;
        }
        input {
            width: 80%;
            padding: 10px;
            margin: 15px 0;
            border: 1px solid #ccc;
            border-radius: 8px;
            font-size: 16px;
        }
        button {
            background: #667eea;
            border: none;
            padding: 12px 20px;
            border-radius: 8px;
            color: white;
            font-size: 16px;
            cursor: pointer;
            transition: 0.3s;
        }
        button:hover {
            background: #5a67d8;
        }
        .resultado {
            margin-top: 20px;
            padding: 15px;
            border-radius: 8px;
            background: #f4f8fb;
            color: #222;
            font-size: 18px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔮 Descubra a Idade Média do Seu Nome</h1>
        <form method="post">
            <input type="text" name="nome" placeholder="Digite seu nome" required>
            <br>
            <button type="submit">Prever Idade</button>
        </form>
        {% if idade is not none %}
        <div class="resultado">
            <p>O nome <b>{{ nome }}</b> tem idade média de <b>{{ idade }}</b> anos.</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    idade = None
    nome = None
    if request.method == "POST":
        nome = request.form["nome"]
        url = f"https://api.agify.io/?name={nome}"
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            idade = dados.get("age")
    return render_template_string(HTML, idade=idade, nome=nome)

if __name__ == "__main__":
    app.run(debug=True)
