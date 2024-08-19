from flask import Flask, render_template, request, redirect, url_for, session
from calculate import calculate_enthalpy

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessário para usar a sessão

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        temp = int(request.form.get('temperature'))
        memorial = calculate_enthalpy(temp)
        session['memorial'] = memorial  # Armazenar o memorial na sessão
        result = memorial["delta_H_total_Joules"]
    return render_template('index.html', result=result)

@app.route('/memorial')
def memorial():
    memorial = session.get('memorial')  # Recuperar o memorial da sessão
    if memorial is None:
        return redirect(url_for('index'))  # Redirecionar se o memorial não estiver disponível
    return render_template('memorial.html', memorial=memorial)

if __name__ == '__main__':
    app.run(debug=True)
