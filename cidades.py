import json
from arvore_simples import IndiceSimples

cidades = []
indice = IndiceSimples()

def carregar_cidades():
    global cidades, indice
    try:
        with open('cidades.json', 'r', encoding='utf-8') as f:
            cidades = json.load(f)
            # Reconstruir índice
            for cidade in cidades:
                indice.inserir_dados(cidade["codigo"], cidade)
    except FileNotFoundError:
        cidades = []

def salvar_cidades():
    with open('cidades.json', 'w', encoding='utf-8') as f:
        json.dump(cidades, f, ensure_ascii=False, indent=2)

# Carregar dados ao importar o módulo
carregar_cidades()

def adicionar_cidade(codigo, descricao, estado):

    for cidade in cidades:
        if cidade["codigo"] == codigo:
            print("código de cidade já existe!")
            return False
    
    nova_cidade = {
        "codigo": codigo,
        "descricao": descricao,
        "estado": estado
    }

    cidades.append(nova_cidade)
    indice.inserir_dados(codigo, nova_cidade)  # Adicionar ao índice
    salvar_cidades()  # Salvar após adicionar
    return True


def buscar_cidade_por_codigo(codigo):
    return indice.buscar_codigo(codigo)
           

def listar_cidades():
    return indice.listar_todos_dados_cres()


def buscar_cidades_por_estado(estado):
    resultado = []
    for cidade in cidades:
        if cidade["estado"] == estado:
            resultado.append(cidade)  # coloca a cidade encontrada dentro da lista resultado
    return resultado

def atualizar_cidade(codigo, nova_descricao, novo_estado):
    for cidade in cidades:
        if cidade["codigo"] == codigo:
            cidade["descricao"] = nova_descricao
            cidade["estado"] = novo_estado
            # manter índice sincronizado
            indice.inserir_dados(codigo, cidade)
            salvar_cidades()  # Salvar após atualizar
            return True

    return False

     

def remover_cidade(codigo):
    for i, cidade in enumerate(cidades):
        if cidade["codigo"] == codigo:
            del cidades[i]
            indice.remover_no(codigo)  # Remover do índice
            salvar_cidades()  # Salvar após remover
            return True
    return False


def buscar_cidade_por_campo(campo, valor):
    resultado = []
    for cidade in cidades:
        if cidade.get(campo) == valor:
            resultado.append(cidade)
    return resultado

# Funções extras usando o índice
def listar_cidades_ordenadas():
    return indice.listar_todos_dados_cres()

def buscar_cidade_por_posicao(posicao):
    return indice.buscar_por_posicao_lista(posicao)

def contar_cidades():
    return indice.contar_registro()

def listar_codigos_cidades():
    return indice.listar_codigos_cres()
