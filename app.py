from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index(): 
    return "Hello World 2"

@app.route('/pastel')
def pastel(): 
    return "Meu Pastel é mais Barato"

@app.route('/pastel/detalhes')
def pastel_detalhe(): 
    return "5000" 