
# flaskq | FastAPI

from flask import Flask, request, render_template, jsonify

# criando a aplicação em Flask

app = Flask(__name__)

# rota de exemplo

@app.route('/helloworld', methods=['GET'])
def helloworld():
    return jsonify({
        "msg": "ola mundo!"
    })

@app.route('/')
def home():
    return render_template('index.html')

# iniciar o servidor

if __name__ == "__main__":
    app.run(debug=True)
