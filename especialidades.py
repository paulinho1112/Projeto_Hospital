import json

especialidades = []

def carregar_especialidades():
    global especialidades
    try:
        with open('especialidades.json', 'r', encoding='utf-8') as f:
            especialidades = json.load(f)
    except FileNotFoundError:
        especialidades = []

def salvar_especialidades():
    with open('especialidades.json', 'w', encoding='utf-8') as f:
        json.dump(especialidades, f, ensure_ascii=False, indent=2)

# Carregar dados ao importar o módulo
carregar_especialidades()

def adicionar_especialidade(codigo, descricao, valor_consulta, limite_diario):

    for especialidade in especialidades:
        if especialidade["codigo"] == codigo:
            print("código de especialidade já existe!")
            return False
    
    nova_especialidade = {
        "codigo": codigo,
        "descricao": descricao,
        "valor_consulta": valor_consulta,
        "limite_diario": limite_diario 
    }
    especialidades.append(nova_especialidade)
    salvar_especialidades()  # Salvar após adicionar
    return True

def buscar_especialidade_por_codigo(codigo):
    for especialidade in especialidades:
        if especialidade["codigo"] == codigo:
            return especialidade
    return None

def listar_especialidades():

    return especialidades


def atualizar_especialidade(codigo, descricao, valor_consulta):
    for especialidade in especialidades:
        if especialidade["codigo"] == codigo:
            especialidade["descricao"] = descricao
            especialidade["valor_consulta"] = valor_consulta
            salvar_especialidades()  # Salvar após atualizar
            return True

    return False


def remove_especialidade(codigo):
    for i, especialidade in enumerate(especialidades):
        if especialidade["codigo"] == codigo:
            del especialidades[i]
            salvar_especialidades()  # Salvar após remover
            return True
    return False



def buscar_especialidade_por_campo(campo, valor):
    resultado = []
    for especialidade in especialidades:
        if especialidade.get(campo) == valor:
            resultado.append(especialidade)
    return especialidade