import json

medicos = []

def carregar_medicos():
    global medicos
    try:
        with open('medicos.json', 'r', encoding='utf-8') as f:
            medicos = json.load(f)
    except FileNotFoundError:
        medicos = []

def salvar_medicos():
    with open('medicos.json', 'w', encoding='utf-8') as f:
        json.dump(medicos, f, ensure_ascii=False, indent=2)

# Carregar dados ao importar o módulo
carregar_medicos()

def adicionar_medico(codigo, nome, endereco, telefone, codigo_cidade, codigo_especialidade):

    for medico in medicos:
        if medico["codigo"] == codigo:
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
    salvar_medicos()  # Salvar após adicionar
    return True

def buscar_medico_por_codigo(codigo):
    for medico in medicos:
        if medico["codigo"] == codigo:
            return medico
    return None


def listar_medicos():

    return medicos


def atualizar_medico(codigo, nome, endereco, telefone, codigo_cidade, codigo_especialidade):
    for medico in medicos:
        if medico["codigo"] == codigo:
            medico["nome"] = nome
            medico["endereco"] = endereco
            medico["telefone"] = telefone
            medico["codigo_cidade"] = codigo_cidade
            medico["codigo_especialidade"] = codigo_especialidade
            salvar_medicos()  # Salvar após atualizar
            return True

    return False


def remover_medico(codigo):
    for i, medico in enumerate(medicos):
        if medico["codigo"] ==  codigo:
            del medicos[i]
            salvar_medicos()  # Salvar após remover
            return True
    return False



def buscar_medico_por_campo(campo, valor):
    resultado = []
    for medico in medicos:
        if medico.get(campo) == valor:
            resultado.append(medico)
    return medico