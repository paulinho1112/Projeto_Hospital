import json
from arvore_simples import ArvoreBinaria

consultas = []
indice = ArvoreBinaria()

def carregar_consultas():
    global consultas, indice
    try:
        with open('consultas.json', 'r', encoding='utf-8') as f:
            consultas = json.load(f)
            # Reconstruir índice
            for consulta in consultas:
                indice.inserir_dados(consulta["codigo"], consulta)
    except FileNotFoundError:
        consultas = []

def salvar_consultas():
    with open('consultas.json', 'w', encoding='utf-8') as f:
        json.dump(consultas, f, ensure_ascii=False, indent=2)

# Carregar dados ao importar o módulo
carregar_consultas()

def adicionar_consulta(codigo, codigo_paciente, codigo_medico, codigo_exame, data_consulta, hora_consulta):
    # Verificar se código já existe usando índice
    if indice.buscar_codigo(codigo) is not None:
        print("código de consulta já existe!")
        return False
    
    # Verificar limite diário (exercício 5.1)
    if not verificar_limite_diario(codigo_medico, data_consulta):
        print("Limite diário de consultas atingido para esta especialidade!")
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
    indice.inserir_dados(codigo, nova_consulta)  # Adicionar ao índice
    
    # Atualizar diárias (exercício 5.3)
    atualizar_diarias_consulta(codigo_medico, data_consulta, 1)
    
    salvar_consultas()  # Salvar após adicionar
    return True
   

def buscar_consulta_por_codigo(codigo):
    """Busca usando índice (mais rápido)"""
    return indice.buscar_codigo(codigo)



def listar_consultas():
    """Lista usando índice (em ordem de código) com dados completos"""
    try:
        consultas_ordenadas = indice.listar_todos_dados_cres()
        
        for consulta in consultas_ordenadas:
            try:
                # Dados do paciente
                dados_paciente = buscar_dados_paciente(consulta['codigo_paciente'])
                consulta['nome_paciente'] = dados_paciente['nome_paciente']
                consulta['nome_cidade_paciente'] = dados_paciente['nome_cidade']
                
                # Dados do médico
                dados_medico = buscar_dados_medico(consulta['codigo_medico'])
                consulta['nome_medico'] = dados_medico['nome_medico']
                
                # Dados do exame
                dados_exame = buscar_dados_exame(consulta['codigo_exame'])
                consulta['descricao_exame'] = dados_exame['descricao_exame']
                consulta['valor_exame'] = dados_exame['valor_exame']
                
                # Dados da especialidade (via médico)
                dados_especialidade = buscar_dados_especialidade(dados_medico['codigo_especialidade'])
                consulta['valor_consulta'] = dados_especialidade['valor_consulta']
                
                # Valor total
                consulta['valor_total'] = consulta['valor_consulta'] + consulta['valor_exame']
                
            except Exception as e:
                # Se houver erro em uma consulta específica, usar valores padrão
                print(f"Erro ao processar consulta {consulta.get('codigo', 'N/A')}: {e}")
                consulta['nome_paciente'] = 'Erro ao carregar'
                consulta['nome_cidade_paciente'] = 'N/A'
                consulta['nome_medico'] = 'Erro ao carregar'
                consulta['descricao_exame'] = 'Erro ao carregar'
                consulta['valor_exame'] = 0
                consulta['valor_consulta'] = 0
                consulta['valor_total'] = 0
        
        return consultas_ordenadas
        
    except Exception as e:
        print(f"Erro geral ao listar consultas: {e}")
        return []


def atualizar_consulta(codigo, codigo_paciente, codigo_medico, codigo_exame, data_consulta, hora_consulta):
    # Buscar usando índice
    consulta = indice.buscar_codigo(codigo)
    if consulta is not None:
        consulta["codigo_paciente"] = codigo_paciente
        consulta["codigo_medico"] = codigo_medico
        consulta["codigo_exame"] = codigo_exame
        consulta["data_consulta"] = data_consulta
        consulta["hora_consulta"] = hora_consulta
        # Atualizar no índice também
        indice.inserir_dados(codigo, consulta)
        salvar_consultas()  # Salvar após atualizar
        return True
    return False



def remover_consulta(codigo):
    # Buscar consulta antes de remover
    consulta = indice.buscar_codigo(codigo)
    if consulta is None:
        return False
    
    # Remover da lista
    for i, c in enumerate(consultas):
        if c["codigo"] == codigo:
            del consultas[i]
            indice.remover_no(codigo)  # Remover do índice
            
            # Subtrair 1 das diárias (exercício 5.4)
            atualizar_diarias_consulta(consulta["codigo_medico"], consulta["data_consulta"], -1)
            
            salvar_consultas()  # Salvar após remover
            return True
    return False



def buscar_consulta_por_campo(campo, valor):
    resultado = []
    for consulta in consultas:
        if consulta.get(campo) == valor:
            resultado.append(consulta)
    return resultado

# Funções extras usando o índice
def listar_consultas_ordenadas():
    """Lista consultas em ordem de código (usando índice)"""
    return indice.listar_todos_dados_cres()

def buscar_consulta_por_posicao(posicao):
    """Busca consulta por posição na lista ordenada"""
    return indice.buscar_por_posicao_lista(posicao)

def contar_consultas():
    """Conta quantas consultas existem"""
    return indice.contar_registro()

def listar_codigos_consultas():
    """Lista apenas os códigos das consultas em ordem"""
    return indice.listar_codigos_cres()

def buscar_dados_paciente(codigo_paciente):
    import pacientes
    
    paciente = pacientes.buscar_paciente_por_codigo(codigo_paciente)
    if paciente:
        dados_cidade = pacientes.buscar_dados_cidade(paciente['codigo_cidade'])
        return {
            'nome_paciente': paciente['nome'],
            'nome_cidade': dados_cidade['nome_cidade']
        }
    else:
        return {
            'nome_paciente': 'Paciente não encontrado',
            'nome_cidade': 'N/A'
        }

def buscar_dados_medico(codigo_medico):
    import medicos
    
    medico = medicos.buscar_medico_por_codigo(codigo_medico)
    if medico:
        return {
            'nome_medico': medico['nome'],
            'codigo_especialidade': medico['codigo_especialidade']
        }
    else:
        return {
            'nome_medico': 'Médico não encontrado',
            'codigo_especialidade': None
        }

def buscar_dados_exame(codigo_exame):
    import exames
    
    exame = exames.buscar_exame_por_codigo(codigo_exame)
    if exame:
        return {
            'descricao_exame': exame['descricao'],
            'valor_exame': exame['valor_exame']
        }
    else:
        return {
            'descricao_exame': 'Exame não encontrado',
            'valor_exame': 0
        }

def buscar_dados_especialidade(codigo_especialidade):
    import especialidades
    
    especialidade = especialidades.buscar_especialidade_por_codigo(codigo_especialidade)
    if especialidade:
        return {
            'valor_consulta': especialidade['valor_consulta']
        }
    else:
        return {
            'valor_consulta': 0
        }

def verificar_limite_diario(codigo_medico, data_consulta):
    """Verifica se ainda há vagas para consultas no dia (exercício 5.1)"""
    import medicos
    import especialidades
    import diarias
    
    # Buscar médico e sua especialidade
    medico = medicos.buscar_medico_por_codigo(codigo_medico)
    if not medico:
        return False
    
    especialidade = especialidades.buscar_especialidade_por_codigo(medico['codigo_especialidade'])
    if not especialidade:
        return False
    
    limite_diario = especialidade['limite_diario']
    
    # Contar consultas do dia para esta especialidade
    consultas_do_dia = 0
    for consulta in consultas:
        if consulta['data_consulta'] == data_consulta:
            # Verificar se o médico da consulta é da mesma especialidade
            med_consulta = medicos.buscar_medico_por_codigo(consulta['codigo_medico'])
            if med_consulta and med_consulta['codigo_especialidade'] == medico['codigo_especialidade']:
                consultas_do_dia += 1
    
    return consultas_do_dia < limite_diario

def atualizar_diarias_consulta(codigo_medico, data_consulta, incremento):
    """Atualiza a quantidade de consultas na tabela Diárias (exercício 5.3 e 5.4)"""
    import medicos
    import diarias
    
    # Buscar médico e sua especialidade
    medico = medicos.buscar_medico_por_codigo(codigo_medico)
    if not medico:
        return
    
    codigo_especialidade = medico['codigo_especialidade']
    
    # Buscar ou criar entrada na tabela diárias
    # Usar data como código (formato: YYYY-MM-DD)
    codigo_diaria = data_consulta
    
    diaria = diarias.buscar_diaria_por_codigo(codigo_diaria)
    if diaria:
        # Atualizar quantidade existente
        nova_quantidade = diaria['quantidade_consultas'] + incremento
        diarias.atualizar_diaria(codigo_diaria, codigo_especialidade, nova_quantidade)
    else:
        # Criar nova entrada
        diarias.adicionar_diaria(codigo_diaria, codigo_especialidade, incremento)

# ===== FUNÇÕES DE FATURAMENTO (EXERCÍCIO 6) =====

def faturamento_por_dia(data):
    """6.1) Exibir faturamento por dia"""
    total = 0
    consultas_do_dia = []
    
    for consulta in consultas:
        if consulta['data_consulta'] == data:
            # Calcular valor total da consulta
            dados_medico = buscar_dados_medico(consulta['codigo_medico'])
            dados_exame = buscar_dados_exame(consulta['codigo_exame'])
            dados_especialidade = buscar_dados_especialidade(dados_medico['codigo_especialidade'])
            
            valor_total = dados_especialidade['valor_consulta'] + dados_exame['valor_exame']
            total += valor_total
            consultas_do_dia.append({
                'consulta': consulta,
                'valor': valor_total
            })
    
    return {
        'data': data,
        'total': total,
        'consultas': consultas_do_dia
    }

def faturamento_por_periodo(data_inicial, data_final):
    """6.2) Exibir faturamento por período"""
    total = 0
    consultas_periodo = []
    
    for consulta in consultas:
        if data_inicial <= consulta['data_consulta'] <= data_final:
            # Calcular valor total da consulta
            dados_medico = buscar_dados_medico(consulta['codigo_medico'])
            dados_exame = buscar_dados_exame(consulta['codigo_exame'])
            dados_especialidade = buscar_dados_especialidade(dados_medico['codigo_especialidade'])
            
            valor_total = dados_especialidade['valor_consulta'] + dados_exame['valor_exame']
            total += valor_total
            consultas_periodo.append({
                'consulta': consulta,
                'valor': valor_total
            })
    
    return {
        'data_inicial': data_inicial,
        'data_final': data_final,
        'total': total,
        'consultas': consultas_periodo
    }

def faturamento_por_medico(codigo_medico):
    """6.3) Exibir faturamento por médico"""
    import medicos
    
    medico = medicos.buscar_medico_por_codigo(codigo_medico)
    if not medico:
        return None
    
    total = 0
    consultas_medico = []
    
    for consulta in consultas:
        if consulta['codigo_medico'] == codigo_medico:
            # Calcular valor total da consulta
            dados_medico = buscar_dados_medico(consulta['codigo_medico'])
            dados_exame = buscar_dados_exame(consulta['codigo_exame'])
            dados_especialidade = buscar_dados_especialidade(dados_medico['codigo_especialidade'])
            
            valor_total = dados_especialidade['valor_consulta'] + dados_exame['valor_exame']
            total += valor_total
            consultas_medico.append({
                'consulta': consulta,
                'valor': valor_total
            })
    
    return {
        'medico': medico['nome'],
        'total': total,
        'consultas': consultas_medico
    }

def faturamento_por_especialidade(codigo_especialidade):
    """6.4) Exibir faturamento por especialidade"""
    import especialidades
    import medicos
    
    especialidade = especialidades.buscar_especialidade_por_codigo(codigo_especialidade)
    if not especialidade:
        return None
    
    total = 0
    consultas_especialidade = []
    
    for consulta in consultas:
        # Verificar se o médico da consulta é desta especialidade
        medico = medicos.buscar_medico_por_codigo(consulta['codigo_medico'])
        if medico and medico['codigo_especialidade'] == codigo_especialidade:
            # Calcular valor total da consulta
            dados_medico = buscar_dados_medico(consulta['codigo_medico'])
            dados_exame = buscar_dados_exame(consulta['codigo_exame'])
            dados_especialidade = buscar_dados_especialidade(dados_medico['codigo_especialidade'])
            
            valor_total = dados_especialidade['valor_consulta'] + dados_exame['valor_exame']
            total += valor_total
            consultas_especialidade.append({
                'consulta': consulta,
                'valor': valor_total
            })
    
    return {
        'especialidade': especialidade['descricao'],
        'total': total,
        'consultas': consultas_especialidade
    }

# ===== RELATÓRIO COMPLETO (EXERCÍCIO 7) =====

def relatorio_completo_consultas():
    """7) Relatório completo de consultas com totais"""
    consultas_completas = listar_consultas()  # Já vem com todos os dados enriquecidos
    
    total_pacientes = len(set(consulta['codigo_paciente'] for consulta in consultas_completas))
    valor_total_pagar = sum(consulta['valor_total'] for consulta in consultas_completas)
    
    return {
        'consultas': consultas_completas,
        'total_pacientes': total_pacientes,
        'valor_total_pagar': valor_total_pagar
    }