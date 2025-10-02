import json
from arvore_simples import ArvoreBinaria

pacientes = []
indice = ArvoreBinaria()

def carregar_pacientes():
    global pacientes, indice
    try:
        with open('pacientes.json', 'r', encoding='utf-8') as f:
            pacientes = json.load(f)
            # Reconstruir índice
            for paciente in pacientes:
                indice.inserir(paciente["codigo"], paciente)
    except FileNotFoundError:
        pacientes = []

def salvar_pacientes():
    with open('pacientes.json', 'w', encoding='utf-8') as f:
        json.dump(pacientes, f, ensure_ascii=False, indent=2)

# Carregar dados ao importar o módulo
carregar_pacientes()

def adicionar_paciente(codigo, nome, data_nascimento, endereco, telefone, codigo_cidade, peso, altura):
    # Verificar se código já existe usando índice
    if indice.buscar(codigo) is not None:
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
    indice.inserir(codigo, novo_paciente)  # Adicionar ao índice
    salvar_pacientes()  # Salvar após adicionar
    return True

def buscar_paciente_por_codigo(codigo):
    return indice.buscar(codigo)


def listar_pacientes():
    pacientes_ordenados = indice.listar_todos()

    for paciente in pacientes_ordenados:
        dados_cidade = buscar_dados_cidade(paciente['codigo_cidade'])
        paciente['nome_cidade'] = dados_cidade['nome_cidade']
        paciente['estado'] = dados_cidade['estado']
        
    return pacientes_ordenados


def atualizar_paciente(codigo, nome, data_nascimento, endereco, telefone, codigo_cidade, peso, altura):
    # Buscar usando índice
    paciente = indice.buscar(codigo)
    if paciente is not None:
        paciente["nome"] = nome
        paciente["data_nascimento"] = data_nascimento
        paciente["endereco"] = endereco
        paciente["telefone"] = telefone
        paciente["codigo_cidade"] = codigo_cidade
        paciente["peso"] = peso
        paciente["altura"] = altura
        # Atualizar no índice também
        indice.inserir(codigo, paciente)
        salvar_pacientes()  # Salvar após atualizar
        return True
    return False



def remover_paciente(codigo):
    # Remover da lista
    for i, paciente in enumerate(pacientes):
        if paciente["codigo"] == codigo:
            del pacientes[i]
            indice.remover(codigo)  # Remover do índice
            salvar_pacientes()  # Salvar após remover
            return True
    return False


def buscar_pacientes_por_campo(campo, valor):
    resultado = []
    for paciente in pacientes:
        if paciente.get(campo) == valor:
            resultado.append(paciente)
    return resultado

# Funções extras usando o índice
def listar_pacientes_ordenados():
    return indice.listar_todos()

def buscar_paciente_por_posicao(posicao):
    return indice.buscar_por_posicao(posicao)

def contar_pacientes():

    return indice.contar()

def listar_codigos_pacientes():  
    return indice.listar_codigos()

def buscar_dados_cidade(codigo_cidade):
    import cidades

    cidade = cidades.buscar_cidade_por_codigo(codigo_cidade)
    if cidade:
        return {
            'nome_cidade': cidade['descricao'],
            'estado': cidade['estado']
        }
    else:
        return {
            'nome_cidade': 'Cidade não encontrada',
            'estado': 'N/A'
        }


def calcular_imc(peso, altura):
    imc = peso / (altura)**2
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc >= 18.5 and imc < 25:
        return "Peso normal"
    elif imc >= 25 and imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

