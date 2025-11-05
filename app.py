from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

baloes = []
num_equipes = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global num_equipes
    if request.method == 'POST':
        num_equipes = int(request.form['num_equipes'])
        return redirect(url_for('painel'))
    return render_template('index.html')

@app.route('/painel')
def painel():
    return render_template('painel.html', num_equipes=num_equipes, baloes=baloes)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    equipe = request.form['equipe']
    letra = request.form['letra']

    # Mapeamento simples de letras para cores
    cores = {
        'A': 'Vermelho',
        'B': 'Azul',
        'C': 'Verde',
        'D': 'Amarelo',
        'E': 'Roxo',
        'F': 'Laranja'
    }

    cor = cores.get(letra.upper(), 'Branco')

    baloes.append({
        'equipe': equipe,
        'letra': letra.upper(),
        'cor': cor,
        'entregue': False
    })
    socketio.emit('atualizar', baloes)
    return redirect(url_for('painel'))

@app.route('/entregar/<int:index>', methods=['POST'])
def entregar(index):
    if 0 <= index < len(baloes):
        baloes[index]['entregue'] = True
        socketio.emit('atualizar', baloes)
    return ('', 204)

@app.route('/delivery')
def delivery():
    return render_template('delivery.html', baloes=baloes)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
