import json
from arvore_simples import ArvoreBinaria

medicos = []
indice = ArvoreBinaria()

def carregar_medicos():
    global medicos, indice
    try:
        with open('medicos.json', 'r', encoding='utf-8') as f:
            medicos = json.load(f)
            # Reconstruir índice
            for medico in medicos:
                indice.inserir(medico["codigo"], medico)
    except FileNotFoundError:
        medicos = []

def salvar_medicos():
    with open('medicos.json', 'w', encoding='utf-8') as f:
        json.dump(medicos, f, ensure_ascii=False, indent=2)

# Carregar dados ao importar o módulo
carregar_medicos()

def adicionar_medico(codigo, nome, endereco, telefone, codigo_cidade, codigo_especialidade):
    # Verificar se código já existe usando índice
    if indice.buscar(codigo) is not None:
        print("código do medico já existe!")
        return False
    
    novo_medico = {
        "codigo": codigo,
        "nome": nome,
        "endereco": endereco,
        "telefone": telefone,
        "codigo_cidade": codigo_cidade,
        "codigo_especialidade": codigo_especialidade
    }
    medicos.append(novo_medico)
    indice.inserir(codigo, novo_medico)  # Adicionar ao índice
    salvar_medicos()  # Salvar após adicionar
    return True

def buscar_medico_por_codigo(codigo):
    """Busca usando índice (mais rápido)"""
    return indice.buscar(codigo)


def listar_medicos():
    """Lista usando índice (em ordem de código)"""
    return indice.listar_todos()


def atualizar_medico(codigo, nome, endereco, telefone, codigo_cidade, codigo_especialidade):
    # Buscar usando índice
    medico = indice.buscar(codigo)
    if medico is not None:
        medico["nome"] = nome
        medico["endereco"] = endereco
        medico["telefone"] = telefone
        medico["codigo_cidade"] = codigo_cidade
        medico["codigo_especialidade"] = codigo_especialidade
        # Atualizar no índice também
        indice.inserir(codigo, medico)
        salvar_medicos()  # Salvar após atualizar
        return True
    return False


def remover_medico(codigo):
    # Remover da lista
    for i, medico in enumerate(medicos):
        if medico["codigo"] == codigo:
            del medicos[i]
            indice.remover(codigo)  # Remover do índice
            salvar_medicos()  # Salvar após remover
            return True
    return False



def buscar_medico_por_campo(campo, valor):
    resultado = []
    for medico in medicos:
        if medico.get(campo) == valor:
            resultado.append(medico)
    return resultado

# Funções extras usando o índice
def listar_medicos_ordenados():
    """Lista médicos em ordem de código (usando índice)"""
    return indice.listar_todos()

def buscar_medico_por_posicao(posicao):
    """Busca médico por posição na lista ordenada"""
    return indice.buscar_por_posicao(posicao)

def contar_medicos():
    """Conta quantos médicos existem"""
    return indice.contar()

def listar_codigos_medicos():
    """Lista apenas os códigos dos médicos em ordem"""
    return indice.listar_codigos()