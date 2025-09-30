import json
from arvore_simples import ArvoreBinaria

exames = []
indice = ArvoreBinaria()

def carregar_exames():
    global exames, indice
    try:
        with open('exames.json', 'r', encoding='utf-8') as f:
            exames = json.load(f)
            # Reconstruir índice
            for exame in exames:
                indice.inserir(exame["codigo"], exame)
    except FileNotFoundError:
        exames = []

def salvar_exames():
    with open('exames.json', 'w', encoding='utf-8') as f:
        json.dump(exames, f, ensure_ascii=False, indent=2)

# Carregar dados ao importar o módulo
carregar_exames()

def adicionar_exame(codigo, descricao, codigo_especialidade, valor_exame):
    # Verificar se código já existe usando índice
    if indice.buscar(codigo) is not None:
        print("código de exame já existe!")
        return False
    
    novo_exame = {
        "codigo": codigo,
        "descricao": descricao,
        "codigo_especialidade": codigo_especialidade,
        "valor_exame": valor_exame
    }
    exames.append(novo_exame)
    indice.inserir(codigo, novo_exame)  # Adicionar ao índice
    salvar_exames()  # Salvar após adicionar
    return True

def buscar_exame_por_codigo(codigo):
    """Busca usando índice (mais rápido)"""
    return indice.buscar(codigo)


def listar_exames():
    """Lista usando índice (em ordem de código)"""
    return indice.listar_todos()


def atualizar_exame(codigo, descricao, codigo_especialidade, valor_exame):
    # Buscar usando índice
    exame = indice.buscar(codigo)
    if exame is not None:
        exame["descricao"] = descricao
        exame["codigo_especialidade"] = codigo_especialidade
        exame["valor_exame"] = valor_exame
        # Atualizar no índice também
        indice.inserir(codigo, exame)
        salvar_exames()  # Salvar após atualizar
        return True
    return False


def remover_exame(codigo):
    # Remover da lista
    for i, exame in enumerate(exames):
        if exame["codigo"] == codigo:
            del exames[i]
            indice.remover(codigo)  # Remover do índice
            salvar_exames()  # Salvar após remover
            return True
    return False



def buscar_exame_por_campo(campo, valor):
    resultado = []
    for exame in exames:
        if exame.get(campo) == valor:
            resultado.append(exame)
    return resultado

# Funções extras usando o índice
def listar_exames_ordenados():
    """Lista exames em ordem de código (usando índice)"""
    return indice.listar_todos()

def buscar_exame_por_posicao(posicao):
    """Busca exame por posição na lista ordenada"""
    return indice.buscar_por_posicao(posicao)

def contar_exames():
    """Conta quantos exames existem"""
    return indice.contar()

def listar_codigos_exames():
    """Lista apenas os códigos dos exames em ordem"""
    return indice.listar_codigos()