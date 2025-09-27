import json

diarias = []

def carregar_diarias():
    global diarias
    try:
        with open('diarias.json', 'r', encoding='utf-8') as f:
            diarias = json.load(f)
    except FileNotFoundError:
        diarias = []

def salvar_diarias():
    with open('diarias.json', 'w', encoding='utf-8') as f:
        json.dump(diarias, f, ensure_ascii=False, indent=2)

# Carregar dados ao importar o módulo
carregar_diarias()

def adicionar_diaria(codigo, codigo_especialidade, quantidade_consultas):
    
   for diaria in diarias:
       if diaria["codigo"] == codigo:
          print("Código de dia já existe!")
          return False

   nova_diaria = {
        "codigo": codigo,
        "codigo_especialidade": codigo_especialidade,
        "quantidade_consultas": quantidade_consultas
    }

   diarias.append(nova_diaria)
   salvar_diarias()  # Salvar após adicionar
   return True


def buscar_diaria_por_codigo(codigo):
    for diaria in diarias:
        if diaria["codigo"] == codigo:
            return diaria
    return None

def listar_diarias():

    return diarias


def atualizar_diaria(codigo, codigo_especialidade, quantidade_consultas):
    for diaria in diarias:
        if diaria["codigo"] == codigo:
            diaria["codigo_especialidade"] = codigo_especialidade
            diaria["quantidade_consultas"] = quantidade_consultas
            salvar_diarias()  # Salvar após atualizar
            return True

    return False


def remover_diaria(codigo):
    for i, diaria in enumerate(diarias):
        if diaria["codigo"] == codigo:
            del diarias[i]
            salvar_diarias()  # Salvar após remover
            return True
    return False



def buscar_diarias_por_campo(campo, valor):
    resultado = []
    for diaria in diarias:
        if diaria.get(campo) == valor:
            resultado.append(diaria)
    return resultado