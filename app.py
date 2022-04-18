import os
from flask import Flask, render_template, json, request, jsonify

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('submit_json.html')

@app.route('/index2')
def index2():
    return render_template('no_submit.html')

@app.route('/api/submit_json', methods=['POST'])
def submit_json():
    json = request.get_json()
    primeiro_nome = json['primeiro']
    print(primeiro_nome)
    ultimo_nome = json['ultimo']
    print(ultimo_nome)
    return jsonify(primeiro_nome=primeiro_nome, ultimo_nome=ultimo_nome)

@app.route('/api/no_submit', methods=['POST'])
def no_submit():
    primeiro_nome = request.form['primeiro_nome']
    ultimo_nome = request.form['ultimo_nome']
    print(primeiro_nome)
    print(ultimo_nome)
    return jsonify(primeiro_nome=primeiro_nome)









if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)