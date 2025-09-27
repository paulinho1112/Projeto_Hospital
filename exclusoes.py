def excluir_por_codigo(tabela, codigo, salvar_func):
    original_len = len(tabela)
    tabela[:] = [item for item in tabela if item["codigo"] != codigo]

    if len(tabela) < original_len:
        salvar_func()
        return True
    return False

def excluir_por_campo(tabela, campo, valor, salvar_func):
    """Exclui registros por qualquer campo"""
    original_len = len(tabela)
    tabela[:] = [item for item in tabela if item.get(campo) != valor]
    
    if len(tabela) < original_len:
        salvar_func()  # Salva automaticamente
        return True
    return False