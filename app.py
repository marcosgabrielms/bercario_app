from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error

# Inicialização da aplicação Flask
app = Flask(__name__)

# Configuração do Banco de Dados do Railway (os seus dados estão corretos)
db_config = {
    'host': 'yamanote.proxy.rlwy.net',
    'user': 'root',
    'password': 'fgjGNsVYaPxaIxnUWkIMJOEZlNlHRZSc',
    'database': 'railway',
    'port': '53499',
    'ssl_disabled': False,
    'ssl_verify_cert': False
}


@app.route('/')
def index():
    return render_template('formulario_medico.html')


@app.route('/adicionar_medico', methods=['POST'])
def adicionar_medico(): # Também ajustei o nome da função para o singular.
    nome = request.form['nome']
    especialidade = request.form['especialidade']
    crm = request.form['crm']

    
    conn = None
    cursor = None

    try:
        # Tenta a conexão com o Banco de Dados
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        query = "INSERT INTO medicos (nome, especialidade, crm) VALUES (%s, %s, %s)"
        cursor.execute(query, (nome, especialidade, crm))
        conn.commit()
    
    except Error as e:
        return f"<h1> Ocorreu um erro: {e}</h1>"
    
    finally:
        
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()
            
    return redirect(url_for('sucesso')) 

@app.route('/sucesso')
def sucesso():
    return render_template('sucesso.html')

# Roda a aplicação
if __name__ == '__main__':
    app.run(debug=True)
