"""
Sistema simples de cadastro e consulta de dados
Pensado para cadastro de leads/clientes/produtos
"""
from flask import Flask, render_template, request, redirect, url_for, flash
from database import init_db, cadastrar_registro, listar_registros, buscar_registros
import re

app = Flask(__name__)
app.secret_key = 'cadastro_consulta_secret_key_2024'

# Inicializa o banco de dados ao iniciar a aplicação
init_db()

def validar_email(email):
    """Valida formato básico de email"""
    if not email:
        return False  # Email é obrigatório
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

@app.route('/')
def index():
    """Página inicial com listagem de registros"""
    registros = listar_registros()
    return render_template('index.html', registros=registros)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    """Página de cadastro de registros"""
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        email = request.form.get('email', '').strip()
        telefone = request.form.get('telefone', '').strip()
        empresa = request.form.get('empresa', '').strip() or None
        observacoes = request.form.get('observacoes', '').strip() or None
        
        # Validação básica
        erros = []
        
        if not nome:
            erros.append('Nome é obrigatório')
        elif len(nome) < 2:
            erros.append('Nome deve ter pelo menos 2 caracteres')
        
        if not email:
            erros.append('Email é obrigatório')
        elif not validar_email(email):
            erros.append('Email inválido')
        
        if not telefone:
            erros.append('Telefone é obrigatório')
        elif len(telefone) < 8:
            erros.append('Telefone deve ter pelo menos 8 caracteres')
        
        if erros:
            for erro in erros:
                flash(erro, 'error')
            return render_template('cadastro.html', 
                                 nome=nome, email=email, telefone=telefone, 
                                 empresa=empresa, observacoes=observacoes)
        
        # Cadastra o registro
        resultado = cadastrar_registro(nome, email, telefone, empresa, observacoes)
        
        if resultado['sucesso']:
            flash('Registro cadastrado com sucesso!', 'success')
            return redirect(url_for('index'))
        else:
            flash(resultado.get('erro', 'Erro ao cadastrar registro'), 'error')
    
    return render_template('cadastro.html')

@app.route('/busca', methods=['GET', 'POST'])
def busca():
    """Página de busca de registros"""
    registros = []
    termo_busca = ''
    
    if request.method == 'POST':
        termo_busca = request.form.get('termo', '').strip()
        
        if termo_busca:
            registros = buscar_registros(termo_busca)
            if not registros:
                flash('Nenhum registro encontrado', 'info')
        else:
            flash('Digite um termo para buscar', 'error')
    
    return render_template('busca.html', registros=registros, termo_busca=termo_busca)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
