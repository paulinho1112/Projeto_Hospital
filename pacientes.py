import json

pacientes = []

def carregar_pacientes():
    global pacientes
    try:
        with open('pacientes.json', 'r', encoding='utf-8') as f:
            pacientes = json.load(f)
    except FileNotFoundError:
        pacientes = []

def salvar_pacientes():
    with open('pacientes.json', 'w', encoding='utf-8') as f:
        json.dump(pacientes, f, ensure_ascii=False, indent=2)

# Carregar dados ao importar o módulo
carregar_pacientes()

def adicionar_paciente(codigo, nome, data_nascimento, endereco, telefone, codigo_cidade, peso, altura):

    for paciente in pacientes:
        if paciente["codigo"] == codigo:
            print("código de paciente já existe!")
            return False
    
    novo_paciente = {
        "codigo": codigo,
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco,
        "telefone": telefone,
        "codigo_cidade": codigo_cidade,
        "peso": peso,
        "altura": altura
    }

    pacientes.append(novo_paciente)
    salvar_pacientes()  # Salvar após adicionar
    return True

def buscar_paciente_por_codigo(codigo):
    for paciente in pacientes:
        if paciente["codigo"] == codigo:
            return paciente
    return None


def listar_pacientes():

    return pacientes


def atualizar_paciente(codigo, nome, data_nascimento, endereco, telefone, codigo_cidade, peso, altura):
    for paciente in pacientes:
        if paciente["codigo"] == codigo:
            paciente["nome"] = nome
            paciente["data_nascimento"] = data_nascimento
            paciente["endereco"] = endereco
            paciente["telefone"] = telefone
            paciente["codigo_cidade"] = codigo_cidade
            paciente["peso"] = peso
            paciente["altura"] = altura
            salvar_pacientes()  # Salvar após atualizar
            return True

    return False



def remover_paciente(codigo):
    for i, paciente in enumerate(pacientes):
        if paciente["codigo"] == codigo:
            del pacientes[i]
            salvar_pacientes()  # Salvar após remover
            return True
    return False


def buscar_pacientes_por_campo(campo, valor):
    resultado = []
    for paciente in pacientes:
        if paciente.get(campo) == valor:
            resultado.append(paciente)
    return resultado