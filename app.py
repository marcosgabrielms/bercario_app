from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector
from mysql.connector import Error
import os # Modulo OS
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

app = Flask(__name__)

# Configuração do Banco de Dados 
db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME'),
    'port': os.getenv('DB_PORT'),
    'ssl_disabled': False,
    'ssl_verify_cert': False
}

def get_db_connection():
    """Função auxiliar para criar uma conexão com o banco de dados."""
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

# --- ROTA PRINCIPAL E DE SUCESSO ---

@app.route('/')
def index():
    """Serve a página principal que contém toda a lógica do frontend."""
    return render_template('index.html')

@app.route('/sucesso')
def sucesso():
    """Mostra a página de sucesso após um cadastro."""
    return render_template('sucesso.html')

# --- ENDPOINTS DE API (para o JavaScript) ---

@app.route('/api/medicos')
def api_get_medicos():
    """Retorna uma lista de todos os médicos em formato JSON."""
    conn = get_db_connection()
    if not conn: return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id_medico, nome FROM medicos ORDER BY nome")
        medicos = cursor.fetchall()
        return jsonify(medicos)
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

@app.route('/api/responsaveis')
def api_get_responsaveis():
    """Retorna uma lista de todos os responsáveis em formato JSON."""
    conn = get_db_connection()
    if not conn: return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id_responsavel, nome FROM responsaveis ORDER BY nome")
        responsaveis = cursor.fetchall()
        return jsonify(responsaveis)
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# --- ROTAS PARA SUBMISSÃO DOS FORMULÁRIOS ---

@app.route('/adicionar_medico', methods=['POST'])
def adicionar_medico():
    form_data = request.form
    conn = get_db_connection()
    if not conn: return "<h1>Erro de conexão.</h1>", 500
    
    try:
        cursor = conn.cursor()
        query = "INSERT INTO medicos (nome, especialidade, crm) VALUES (%s, %s, %s)"
        cursor.execute(query, (form_data['nome'], form_data['especialidade'], form_data['crm']))
        conn.commit()
    except Error as e:
        return f"<h1>Ocorreu um erro: {e}</h1>"
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
    return redirect(url_for('sucesso'))

@app.route('/adicionar_responsavel', methods=['POST'])
def adicionar_responsavel():
    form_data = request.form
    conn = get_db_connection()
    if not conn: return "<h1>Erro de conexão.</h1>", 500
    
    try:
        cursor = conn.cursor()
        query = "INSERT INTO responsaveis (nome, parentesco, cpf, telefone) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (form_data['nome'], form_data['parentesco'], form_data['cpf'], form_data['telefone']))
        conn.commit()
    except Error as e:
        return f"<h1>Ocorreu um erro: {e}</h1>"
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
    return redirect(url_for('sucesso'))

@app.route('/adicionar_bebe', methods=['POST'])
def adicionar_bebe():
    form_data = request.form
    conn = get_db_connection()
    if not conn: return "<h1>Erro de conexão.</h1>", 500
    
    try:
        cursor = conn.cursor()
        query = "INSERT INTO bebes (nome, data_nascimento, sexo, id_medico, id_responsavel) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (form_data['nome'], form_data['data_nascimento'], form_data['sexo'], form_data['id_medico'], form_data['id_responsavel']))
        conn.commit()
    except Error as e:
        return f"<h1>Ocorreu um erro: {e}</h1>"
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
    return redirect(url_for('sucesso'))

if __name__ == '__main__':
    app.run(debug=True)
