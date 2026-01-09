"""
Gerenciamento do banco de dados SQLite
Sistema genérico para cadastro de leads/clientes/produtos
"""
import sqlite3
from datetime import datetime

DATABASE = 'cadastro.db'

def get_db():
    """Cria conexão com o banco de dados"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Inicializa o banco de dados criando a tabela de registros"""
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL,
            empresa TEXT,
            observacoes TEXT,
            data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def cadastrar_registro(nome, email=None, telefone=None, empresa=None, observacoes=None):
    """Cadastra um novo registro"""
    conn = get_db()
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            INSERT INTO registros (nome, email, telefone, empresa, observacoes)
            VALUES (?, ?, ?, ?, ?)
        ''', (nome, email, telefone, empresa, observacoes))
        
        conn.commit()
        registro_id = cursor.lastrowid
        return {'sucesso': True, 'id': registro_id}
    except Exception as e:
        return {'sucesso': False, 'erro': str(e)}
    finally:
        conn.close()

def listar_registros():
    """Lista todos os registros cadastrados"""
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT * FROM registros
        ORDER BY data_cadastro DESC
    ''')
    
    registros = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return registros

def buscar_registros(termo):
    """Busca registros por nome ou email"""
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT * FROM registros
        WHERE nome LIKE ? OR email LIKE ? OR empresa LIKE ?
        ORDER BY nome
    ''', (f'%{termo}%', f'%{termo}%', f'%{termo}%'))
    
    registros = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return registros

def obter_registro_por_id(registro_id):
    """Obtém um registro específico por ID"""
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM registros WHERE id = ?', (registro_id,))
    registro = cursor.fetchone()
    conn.close()
    
    return dict(registro) if registro else None
