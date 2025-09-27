import json

consultas = []

def carregar_consultas():
    global consultas
    try:
        with open('consultas.json', 'r', encoding='utf-8') as f:
            consultas = json.load(f)
    except FileNotFoundError:
        consultas = []

def salvar_consultas():
    with open('consultas.json', 'w', encoding='utf-8') as f:
        json.dump(consultas, f, ensure_ascii=False, indent=2)

# Carregar dados ao importar o módulo
carregar_consultas()

def adicionar_consulta(codigo, codigo_paciente, codigo_medico, codigo_exame, data_consulta, hora_consulta):

    for consulta in consultas:
        if consulta["codigo"] == codigo:
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
    salvar_consultas()  # Salvar após adicionar
    return True
   

def buscar_consulta_por_codigo(codigo):
    for consulta in consultas:
        if consulta["codigo"] == codigo:
            return consulta
    return None



def listar_consultas():

    return consultas


def atualizar_consulta(codigo, codigo_paciente, codigo_medico, codigo_exame, data_consulta, hora_consulta):
    for consulta in consultas:
        if consulta["codigo"] == codigo:
            consulta["codigo_paciente"] = codigo_paciente
            consulta["codigo_medico"] = codigo_medico
            consulta["codigo_exame"] = codigo_exame
            consulta["data_consulta"] = data_consulta
            consulta["hora_consulta"] = hora_consulta
            salvar_consultas()  # Salvar após atualizar
            return True

    return False



def remover_consulta(codigo):
    for i, consulta in enumerate(consultas):
        if consulta["codigo"] == codigo:
            del consultas[i]
            salvar_consultas()  # Salvar após remover
            return True
    return False



def buscar_consulta_por_campo(campo, valor):
    resultado = []
    for consulta in consultas:
        if consulta.get(campo) == valor:
            resultado.append(consulta)
    return resultado