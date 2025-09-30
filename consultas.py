import json
from arvore_simples import ArvoreBinaria

consultas = []
indice = ArvoreBinaria()

def carregar_consultas():
    global consultas, indice
    try:
        with open('consultas.json', 'r', encoding='utf-8') as f:
            consultas = json.load(f)
            # Reconstruir índice
            for consulta in consultas:
                indice.inserir(consulta["codigo"], consulta)
    except FileNotFoundError:
        consultas = []

def salvar_consultas():
    with open('consultas.json', 'w', encoding='utf-8') as f:
        json.dump(consultas, f, ensure_ascii=False, indent=2)

# Carregar dados ao importar o módulo
carregar_consultas()

def adicionar_consulta(codigo, codigo_paciente, codigo_medico, codigo_exame, data_consulta, hora_consulta):
    # Verificar se código já existe usando índice
    if indice.buscar(codigo) is not None:
        print("código de consulta já existe!")
        return False
    
    nova_consulta = {
        "codigo": codigo,
        "codigo_paciente": codigo_paciente,
        "codigo_medico": codigo_medico,
        "codigo_exame": codigo_exame,
        "data_consulta": data_consulta,
        "hora_consulta": hora_consulta
    }

    consultas.append(nova_consulta)
    indice.inserir(codigo, nova_consulta)  # Adicionar ao índice
    salvar_consultas()  # Salvar após adicionar
    return True
   

def buscar_consulta_por_codigo(codigo):
    """Busca usando índice (mais rápido)"""
    return indice.buscar(codigo)



def listar_consultas():
    """Lista usando índice (em ordem de código)"""
    return indice.listar_todos()


def atualizar_consulta(codigo, codigo_paciente, codigo_medico, codigo_exame, data_consulta, hora_consulta):
    # Buscar usando índice
    consulta = indice.buscar(codigo)
    if consulta is not None:
        consulta["codigo_paciente"] = codigo_paciente
        consulta["codigo_medico"] = codigo_medico
        consulta["codigo_exame"] = codigo_exame
        consulta["data_consulta"] = data_consulta
        consulta["hora_consulta"] = hora_consulta
        # Atualizar no índice também
        indice.inserir(codigo, consulta)
        salvar_consultas()  # Salvar após atualizar
        return True
    return False



def remover_consulta(codigo):
    # Remover da lista
    for i, consulta in enumerate(consultas):
        if consulta["codigo"] == codigo:
            del consultas[i]
            indice.remover(codigo)  # Remover do índice
            salvar_consultas()  # Salvar após remover
            return True
    return False



def buscar_consulta_por_campo(campo, valor):
    resultado = []
    for consulta in consultas:
        if consulta.get(campo) == valor:
            resultado.append(consulta)
    return resultado

# Funções extras usando o índice
def listar_consultas_ordenadas():
    """Lista consultas em ordem de código (usando índice)"""
    return indice.listar_todos()

def buscar_consulta_por_posicao(posicao):
    """Busca consulta por posição na lista ordenada"""
    return indice.buscar_por_posicao(posicao)

def contar_consultas():
    """Conta quantas consultas existem"""
    return indice.contar()

def listar_codigos_consultas():
    """Lista apenas os códigos das consultas em ordem"""
    return indice.listar_codigos()