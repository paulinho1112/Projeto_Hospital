import json
from arvore_simples import ArvoreBinaria

diarias = []
indice = ArvoreBinaria()

def carregar_diarias():
    global diarias, indice
    try:
        with open('diarias.json', 'r', encoding='utf-8') as f:
            diarias = json.load(f)
            # Reconstruir índice
            for diaria in diarias:
                indice.inserir_dados(diaria["codigo"], diaria)
    except FileNotFoundError:
        diarias = []

def salvar_diarias():
    with open('diarias.json', 'w', encoding='utf-8') as f:
        json.dump(diarias, f, ensure_ascii=False, indent=2)

# Carregar dados ao importar o módulo
carregar_diarias()

def adicionar_diaria(codigo, codigo_especialidade, quantidade_consultas):
    # Verificar se código já existe usando índice
    if indice.buscar_codigo(codigo) is not None:
        print("Código de dia já existe!")
        return False

    nova_diaria = {
        "codigo": codigo,
        "codigo_especialidade": codigo_especialidade,
        "quantidade_consultas": quantidade_consultas
    }

    diarias.append(nova_diaria)
    indice.inserir_dados(codigo, nova_diaria)  # Adicionar ao índice
    salvar_diarias()  # Salvar após adicionar
    return True


def buscar_diaria_por_codigo(codigo):
    """Busca usando índice (mais rápido)"""
    return indice.buscar_codigo(codigo)

def listar_diarias():
    """Lista usando índice (em ordem de código)"""
    return indice.listar_todos_dados_cres()


def atualizar_diaria(codigo, codigo_especialidade, quantidade_consultas):
    # Buscar usando índice
    diaria = indice.buscar_codigo(codigo)
    if diaria is not None:
        diaria["codigo_especialidade"] = codigo_especialidade
        diaria["quantidade_consultas"] = quantidade_consultas
        # Atualizar no índice também
        indice.inserir_dados(codigo, diaria)
        salvar_diarias()  # Salvar após atualizar
        return True
    return False


def remover_diaria(codigo):
    # Remover da lista
    for i, diaria in enumerate(diarias):
        if diaria["codigo"] == codigo:
            del diarias[i]
            indice.remover_no(codigo)  # Remover do índice
            salvar_diarias()  # Salvar após remover
            return True
    return False



def buscar_diarias_por_campo(campo, valor):
    resultado = []
    for diaria in diarias:
        if diaria.get(campo) == valor:
            resultado.append(diaria)
    return resultado

# Funções extras usando o índice
def listar_diarias_ordenadas():
    """Lista diárias em ordem de código (usando índice)"""
    return indice.listar_todos_dados_cres()

def buscar_diaria_por_posicao(posicao):
    """Busca diária por posição na lista ordenada"""
    return indice.buscar_por_posicao_lista(posicao)

def contar_diarias():
    """Conta quantas diárias existem"""
    return indice.contar_registro()

def listar_codigos_diarias():
    """Lista apenas os códigos das diárias em ordem"""
    return indice.listar_codigos_cres()