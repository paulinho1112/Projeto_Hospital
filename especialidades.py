import json
from arvore_simples import ArvoreBinaria

especialidades = []
indice = ArvoreBinaria()

def carregar_especialidades():
    global especialidades, indice
    try:
        with open('especialidades.json', 'r', encoding='utf-8') as f:
            especialidades = json.load(f)
            # Reconstruir índice
            for especialidade in especialidades:
                indice.inserir_dados(especialidade["codigo"], especialidade)
    except FileNotFoundError:
        especialidades = []

def salvar_especialidades():
    with open('especialidades.json', 'w', encoding='utf-8') as f:
        json.dump(especialidades, f, ensure_ascii=False, indent=2)

# Carregar dados ao importar o módulo
carregar_especialidades()

def adicionar_especialidade(codigo, descricao, valor_consulta, limite_diario):
    # Verificar se código já existe usando índice
    if indice.buscar_codigo(codigo) is not None:
        print("código de especialidade já existe!")
        return False
    
    nova_especialidade = {
        "codigo": codigo,
        "descricao": descricao,
        "valor_consulta": valor_consulta,
        "limite_diario": limite_diario 
    }
    especialidades.append(nova_especialidade)
    indice.inserir_dados(codigo, nova_especialidade)  # Adicionar ao índice
    salvar_especialidades()  # Salvar após adicionar
    return True

def buscar_especialidade_por_codigo(codigo):
    return indice.buscar_codigo(codigo)

  

def listar_especialidades():
    """Lista usando índice (em ordem de código)"""
    return indice.listar_todos_dados_cres()


def atualizar_especialidade(codigo, descricao, valor_consulta):
    # Buscar usando índice
    especialidade = indice.buscar_codigo(codigo)
    if especialidade is not None:
        especialidade["descricao"] = descricao
        especialidade["valor_consulta"] = valor_consulta
        # Atualizar no índice também
        indice.inserir_dados(codigo, especialidade)
        salvar_especialidades()  # Salvar após atualizar
        return True
    return False


def remover_especialidade(codigo):
    # Remover da lista
    for i, especialidade in enumerate(especialidades):
        if especialidade["codigo"] == codigo:
            del especialidades[i]
            indice.remover_no(codigo)  # Remover do índice
            salvar_especialidades()  # Salvar após remover
            return True
    return False



def buscar_especialidade_por_campo(campo, valor):
    resultado = []
    for especialidade in especialidades:
        if especialidade.get(campo) == valor:
            resultado.append(especialidade)
    return resultado

# Funções extras usando o índice
def listar_especialidades_ordenadas():
    """Lista especialidades em ordem de código (usando índice)"""
    return indice.listar_todos_dados_cres()

def buscar_especialidade_por_posicao(posicao):
    """Busca especialidade por posição na lista ordenada"""
    return indice.buscar_por_posicao_lista(posicao)

def contar_especialidades():
    """Conta quantas especialidades existem"""
    return indice.contar_registro()

def listar_codigos_especialidades():
    """Lista apenas os códigos das especialidades em ordem"""
    return indice.listar_codigos_cres()





    