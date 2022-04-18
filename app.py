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
    primeiro_nome = json['primeiro'].upper()
    print(primeiro_nome)
    email_form = json['email']
    print(email_form)
    return jsonify(primeiro_nome=primeiro_nome, email_form=email_form)

@app.route('/api/no_submit', methods=['POST'])
def no_submit():
    primeiro_nome = request.form['primeiro_nome']
    email_form = request.form['email_form']
    print(primeiro_nome)
    print(email_form)
    return jsonify(primeiro_nome=primeiro_nome, email_form=email_form)









if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)