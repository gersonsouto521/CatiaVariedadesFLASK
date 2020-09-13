from flask import Flask
from flask import request, render_template
import pandas as pd
from io import StringIO
import os


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/relatorio', methods=['POST'])
def relatorio():
    lista = request.form['relatorio']
    tuca = StringIO(str(lista))
    df = pd.read_csv(tuca, sep="	")
    tamanho = len(df)
    return render_template('relatorio.html',df=df,tamanho=tamanho)

@app.route('/etiquetas', methods=['POST'])
def etiquetas():
    info_etiquetas = request.form['etiquetas']
    tuca = StringIO(str(info_etiquetas))
    df = pd.read_csv(tuca, sep="	")
    tamanho = len(df)
    return render_template('etiquetas.html',df=df,tamanho=tamanho)
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    #app.run()