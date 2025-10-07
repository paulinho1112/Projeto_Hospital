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
                indice.inserir_dados(medico["codigo"], medico)
    except FileNotFoundError:
        medicos = []

def salvar_medicos():
    with open('medicos.json', 'w', encoding='utf-8') as f:
        json.dump(medicos, f, ensure_ascii=False, indent=2)

# Carregar dados ao importar o módulo
carregar_medicos()

def adicionar_medico(codigo, nome, endereco, telefone, codigo_cidade, codigo_especialidade):
    # Verificar se código já existe usando índice
    if indice.buscar_codigo(codigo) is not None:
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
    indice.inserir_dados(codigo, novo_medico)  # Adicionar ao índice
    salvar_medicos()  # Salvar após adicionar
    return True

def buscar_medico_por_codigo(codigo):
 
    return indice.buscar_codigo(codigo)


def listar_medicos():
    medicos_ordenados = indice.listar_todos_dados_cres()
    for medico in medicos_ordenados:
        # cidade
        dados_cidade = buscar_dados_cidade(medico["codigo_cidade"])
        medico["nome_cidade"] = dados_cidade["nome_cidade"]
        medico["estado"] = dados_cidade["estado"]

        # especialidade
        dados_esp = buscar_dados_especialidade(medico["codigo_especialidade"])
        medico["descricao_especialidade"] = dados_esp["descricao_especialidade"]
        medico["valor_consulta"] = dados_esp["valor_consulta"]
        medico["limite_diario"] = dados_esp["limite_diario"]

    return medicos_ordenados


def atualizar_medico(codigo, nome, endereco, telefone, codigo_cidade, codigo_especialidade):
    # Buscar usando índice
    medico = indice.buscar_codigo(codigo)
    if medico is not None:
        medico["nome"] = nome
        medico["endereco"] = endereco
        medico["telefone"] = telefone
        medico["codigo_cidade"] = codigo_cidade
        medico["codigo_especialidade"] = codigo_especialidade
        # Atualizar no índice também
        indice.inserir_dados(codigo, medico)
        salvar_medicos()  # Salvar após atualizar
        return True
    return False


def remover_medico(codigo):
    # Remover da lista
    for i, medico in enumerate(medicos):
        if medico["codigo"] == codigo:
            del medicos[i]
            indice.remover_no(codigo)  # Remover do índice
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
   
    return indice.listar_todos_dados_cres()

def buscar_medico_por_posicao(posicao):
  
    return indice.buscar_por_posicao_lista(posicao)

def contar_medicos():
   
    return indice.contar_registro()

def listar_codigos_medicos():
    
    return indice.listar_codigos_cres()

def buscar_dados_cidade(codigo_cidade):
    import cidades

    cidade = cidades.buscar_cidade_por_codigo(codigo_cidade)
    if cidade:
        return{
            'nome_cidade' : cidade['descricao'],
            'estado': cidade['estado']
        }
    else:
        return {
            'nome_cidade': 'Cidade não encontrada',
            'estado': 'N/A'
        }


def buscar_dados_especialidade(codigo):
    import especialidades
    esp = especialidades.buscar_especialidade_por_codigo(codigo)
    if esp:
        return {
            'descricao_especialidade': esp['descricao'],
            'valor_consulta': esp['valor_consulta'],
            'limite_diario': esp['limite_diario'],
        }
    return {
        'descricao_especialidade': 0,
        'valor_consulta': 0,
        'limite_diario': 0,
    }