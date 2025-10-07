from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import json
import os
from datetime import datetime

# Importar módulos do sistema
import cidades
import especialidades
import medicos
import pacientes
import exames
import consultas
import diarias

app = Flask(__name__)
app.secret_key = 'sistema_hospitalar_2024'

# Função para limpar dados (opcional)
def limpar_dados():
    """Limpa todos os dados para demonstração limpa"""
    arquivos = ['cidades.json', 'especialidades.json', 'medicos.json', 
                'pacientes.json', 'exames.json', 'consultas.json', 'diarias.json']
    for arquivo in arquivos:
        if os.path.exists(arquivo):
            os.remove(arquivo)

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# ===== ROTAS PARA CIDADES =====
@app.route('/cidades')
def listar_cidades():
    cidades_lista = cidades.listar_cidades()
    return render_template('cidades.html', cidades=cidades_lista)

@app.route('/cidades/adicionar', methods=['GET', 'POST'])
def adicionar_cidade():
    if request.method == 'POST':
        codigo = int(request.form['codigo'])
        descricao = request.form['descricao']
        estado = request.form['estado']
        
        if cidades.adicionar_cidade(codigo, descricao, estado):
            flash('Cidade adicionada com sucesso!', 'success')
        else:
            flash('Erro ao adicionar cidade. Código já existe!', 'error')
        return redirect(url_for('listar_cidades'))
    
    return render_template('adicionar_cidade.html')

# ===== ROTAS PARA ESPECIALIDADES =====
@app.route('/especialidades')
def listar_especialidades():
    especialidades_lista = especialidades.listar_especialidades()
    return render_template('especialidades.html', especialidades=especialidades_lista)

@app.route('/especialidades/adicionar', methods=['GET', 'POST'])
def adicionar_especialidade():
    if request.method == 'POST':
        codigo = int(request.form['codigo'])
        descricao = request.form['descricao']
        valor_consulta = float(request.form['valor_consulta'])
        limite_diario = int(request.form['limite_diario'])
        
        if especialidades.adicionar_especialidade(codigo, descricao, valor_consulta, limite_diario):
            flash('Especialidade adicionada com sucesso!', 'success')
        else:
            flash('Erro ao adicionar especialidade. Código já existe!', 'error')
        return redirect(url_for('listar_especialidades'))
    
    return render_template('adicionar_especialidade.html')

# ===== ROTAS PARA MÉDICOS =====
@app.route('/medicos')
def listar_medicos():
    medicos_lista = medicos.listar_medicos()
    return render_template('medicos.html', medicos=medicos_lista)

@app.route('/medicos/adicionar', methods=['GET', 'POST'])
def adicionar_medico():
    if request.method == 'POST':
        codigo = int(request.form['codigo'])
        nome = request.form['nome']
        endereco = request.form['endereco']
        telefone = request.form['telefone']
        codigo_cidade = int(request.form['codigo_cidade'])
        codigo_especialidade = int(request.form['codigo_especialidade'])
        
        if medicos.adicionar_medico(codigo, nome, endereco, telefone, codigo_cidade, codigo_especialidade):
            flash('Médico adicionado com sucesso!', 'success')
        else:
            flash('Erro ao adicionar médico. Código já existe!', 'error')
        return redirect(url_for('listar_medicos'))
    
    cidades_lista = cidades.listar_cidades()
    especialidades_lista = especialidades.listar_especialidades()
    return render_template('adicionar_medico.html', cidades=cidades_lista, especialidades=especialidades_lista)

# ===== ROTAS PARA PACIENTES =====
@app.route('/pacientes')
def listar_pacientes():
    pacientes_lista = pacientes.listar_pacientes()
    return render_template('pacientes.html', pacientes=pacientes_lista)

@app.route('/pacientes/adicionar', methods=['GET', 'POST'])
def adicionar_paciente():
    if request.method == 'POST':
        codigo = int(request.form['codigo'])
        nome = request.form['nome']
        data_nascimento = request.form['data_nascimento']
        endereco = request.form['endereco']
        telefone = request.form['telefone']
        codigo_cidade = int(request.form['codigo_cidade'])
        peso = float(request.form['peso'])
        altura = float(request.form['altura'])
        
        if pacientes.adicionar_paciente(codigo, nome, data_nascimento, endereco, telefone, codigo_cidade, peso, altura):
            flash('Paciente adicionado com sucesso!', 'success')
        else:
            flash('Erro ao adicionar paciente. Código já existe!', 'error')
        return redirect(url_for('listar_pacientes'))
    
    cidades_lista = cidades.listar_cidades()
    return render_template('adicionar_paciente.html', cidades=cidades_lista)

# ===== ROTAS PARA EXAMES =====
@app.route('/exames')
def listar_exames():
    exames_lista = exames.listar_exames()
    return render_template('exames.html', exames=exames_lista)

@app.route('/exames/adicionar', methods=['GET', 'POST'])
def adicionar_exame():
    if request.method == 'POST':
        codigo = int(request.form['codigo'])
        descricao = request.form['descricao']
        codigo_especialidade = int(request.form['codigo_especialidade'])
        valor_exame = float(request.form['valor_exame'])
        
        if exames.adicionar_exame(codigo, descricao, codigo_especialidade, valor_exame):
            flash('Exame adicionado com sucesso!', 'success')
        else:
            flash('Erro ao adicionar exame. Código já existe!', 'error')
        return redirect(url_for('listar_exames'))
    
    especialidades_lista = especialidades.listar_especialidades()
    return render_template('adicionar_exame.html', especialidades=especialidades_lista)

# ===== ROTAS PARA CONSULTAS =====
@app.route('/consultas')
def listar_consultas():
    consultas_lista = consultas.listar_consultas()
    return render_template('consultas.html', consultas=consultas_lista)

@app.route('/consultas/adicionar', methods=['GET', 'POST'])
def adicionar_consulta():
    if request.method == 'POST':
        codigo = int(request.form['codigo'])
        codigo_paciente = int(request.form['codigo_paciente'])
        codigo_medico = int(request.form['codigo_medico'])
        codigo_exame = int(request.form['codigo_exame'])
        data_consulta = request.form['data_consulta']
        hora_consulta = request.form['hora_consulta']
        
        if consultas.adicionar_consulta(codigo, codigo_paciente, codigo_medico, codigo_exame, data_consulta, hora_consulta):
            flash('Consulta adicionada com sucesso!', 'success')
        else:
            flash('Erro ao adicionar consulta. Verifique os dados ou limite diário!', 'error')
        return redirect(url_for('listar_consultas'))
    
    pacientes_lista = pacientes.listar_pacientes()
    medicos_lista = medicos.listar_medicos()
    exames_lista = exames.listar_exames()
    return render_template('adicionar_consulta.html', pacientes=pacientes_lista, medicos=medicos_lista, exames=exames_lista)

# ===== ROTAS PARA RELATÓRIOS =====
@app.route('/relatorios')
def relatorios():
    return render_template('relatorios.html')

@app.route('/relatorios/faturamento-dia', methods=['GET', 'POST'])
def faturamento_dia():
    if request.method == 'POST':
        data = request.form['data']
        faturamento = consultas.faturamento_por_dia(data)
        return render_template('faturamento_dia.html', faturamento=faturamento)
    
    return render_template('faturamento_dia_form.html')

@app.route('/relatorios/faturamento-periodo', methods=['GET', 'POST'])
def faturamento_periodo():
    if request.method == 'POST':
        data_inicial = request.form['data_inicial']
        data_final = request.form['data_final']
        faturamento = consultas.faturamento_por_periodo(data_inicial, data_final)
        return render_template('faturamento_periodo.html', faturamento=faturamento)
    
    return render_template('faturamento_periodo_form.html')

@app.route('/relatorios/faturamento-medico', methods=['GET', 'POST'])
def faturamento_medico():
    if request.method == 'POST':
        codigo_medico = int(request.form['codigo_medico'])
        faturamento = consultas.faturamento_por_medico(codigo_medico)
        return render_template('faturamento_medico.html', faturamento=faturamento)
    
    medicos_lista = medicos.listar_medicos()
    return render_template('faturamento_medico_form.html', medicos=medicos_lista)

@app.route('/relatorios/faturamento-especialidade', methods=['GET', 'POST'])
def faturamento_especialidade():
    if request.method == 'POST':
        codigo_especialidade = int(request.form['codigo_especialidade'])
        faturamento = consultas.faturamento_por_especialidade(codigo_especialidade)
        return render_template('faturamento_especialidade.html', faturamento=faturamento)
    
    especialidades_lista = especialidades.listar_especialidades()
    return render_template('faturamento_especialidade_form.html', especialidades=especialidades_lista)

@app.route('/relatorios/completo')
def relatorio_completo():
    relatorio = consultas.relatorio_completo_consultas()
    return render_template('relatorio_completo.html', relatorio=relatorio)


# ===== ROTAS PARA EXCLUSÃO =====
@app.route('/cidades/<int:codigo>/excluir', methods=['POST'])
def excluir_cidade(codigo):
    if cidades.remover_cidade(codigo):
        flash('Cidade excluída com sucesso!', 'success')
    else:
        flash('Erro ao excluir cidade!', 'error')
    return redirect(url_for('listar_cidades'))

@app.route('/especialidades/<int:codigo>/excluir', methods=['POST'])
def excluir_especialidade(codigo):
    if especialidades.remover_especialidade(codigo):
        flash('Especialidade excluída com sucesso!', 'success')
    else:
        flash('Erro ao excluir especialidade!', 'error')
    return redirect(url_for('listar_especialidades'))

@app.route('/medicos/<int:codigo>/excluir', methods=['POST'])
def excluir_medico(codigo):
    if medicos.remover_medico(codigo):
        flash('Médico excluído com sucesso!', 'success')
    else:
        flash('Erro ao excluir médico!', 'error')
    return redirect(url_for('listar_medicos'))

@app.route('/pacientes/<int:codigo>/excluir', methods=['POST'])
def excluir_paciente(codigo):
    if pacientes.remover_paciente(codigo):
        flash('Paciente excluído com sucesso!', 'success')
    else:
        flash('Erro ao excluir paciente!', 'error')
    return redirect(url_for('listar_pacientes'))

@app.route('/exames/<int:codigo>/excluir', methods=['POST'])
def excluir_exame(codigo):
    if exames.remover_exame(codigo):
        flash('Exame excluído com sucesso!', 'success')
    else:
        flash('Erro ao excluir exame!', 'error')
    return redirect(url_for('listar_exames'))

@app.route('/consultas/<int:codigo>/excluir', methods=['POST'])
def excluir_consulta(codigo):
    if consultas.remover_consulta(codigo):
        flash('Consulta excluída com sucesso!', 'success')
    else:
        flash('Erro ao excluir consulta!', 'error')
    return redirect(url_for('listar_consultas'))

# ===== ROTA PARA LIMPAR DADOS (OPCIONAL) =====
@app.route('/limpar-dados', methods=['POST'])
def limpar_dados_route():
    limpar_dados()
    flash('Dados limpos com sucesso!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
