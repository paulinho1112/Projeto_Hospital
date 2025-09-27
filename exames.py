import json

exames = []

def carregar_exames():
    global exames
    try:
        with open('exames.json', 'r', encoding='utf-8') as f:
            exames = json.load(f)
    except FileNotFoundError:
        exames = []

def salvar_exames():
    with open('exames.json', 'w', encoding='utf-8') as f:
        json.dump(exames, f, ensure_ascii=False, indent=2)

# Carregar dados ao importar o módulo
carregar_exames()

def adicionar_exame(codigo, descricao, codigo_especialidade, valor_exame):

    for exame in exames:
        if exame["codigo"] == codigo:
            print("código de exame já existe!")
            return False
    
    novo_exame = {
        "codigo": codigo,
        "descricao": descricao,
        "codigo_especialidade": codigo_especialidade,
        "valor_exame": valor_exame
    }
    exames.append(novo_exame)
    salvar_exames()  # Salvar após adicionar
    return True

def buscar_exame_por_codigo(codigo):
    for exame in exames:
        if exame["codigo"] == codigo:
            return exame
    return None


def listar_exames():

    return exames


def atualizar_exame(codigo, descricao, codigo_especialidade, valor_exame):
    for exame in exames:
        if exame["codigo"] == codigo:
            exame["descricao"] = descricao
            exame["codigo_especialidade"] = codigo_especialidade
            exame["valor_exame"] = valor_exame
            salvar_exames()  # Salvar após atualizar
            return True

    return False


def remove_exame(codigo):
    for i, exame in enumerate(exames):
        if exame["codigo"] == codigo:
            del exames[i]
            salvar_exames()  # Salvar após remover
            return True
    return False



def buscar_exame_por_campo(campo, valor):
    resultado = []
    for exame in exames:
        if exame.get(campo) == valor:
            resultado.append(exame)
    return exame