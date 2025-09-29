from cidades import cidades, salvar_cidades
from pacientes import pacientes, salvar_pacientes
from exclusoes import excluir_por_codigo, excluir_por_campo

# Excluir cidade código 1
excluir_por_codigo(cidades, 1, salvar_cidades)

# Excluir todas as cidades de SP
excluir_por_campo(cidades, "estado", "SP", salvar_cidades)

# Excluir paciente código 5
excluir_por_codigo(pacientes, 5, salvar_pacientes)

# Excluir pacientes de uma cidade
excluir_por_campo(pacientes, "codigo_cidade", 1, salvar_pacientes)

# Remove cidade código 1 e salva
cidades[:] = [c for c in cidades if c["codigo"] != 1]; salvar_cidades()

# Remove todas de SP e salva
cidades[:] = [c for c in cidades if c["estado"] != "SP"]; salvar_cidades()

def excluir_simples():
    print("1. Cidades")
    print("2. Pacientes") 
    print("3. Médicosss")
    
    opcao = input("Escolha a tabela: ")
    codigo = int(input("Código para excluir: "))
    
    if opcao == "1":
        from cidades import cidades, salvar_cidades
        cidades[:] = [c for c in cidades if c["codigo"] != codigo]
        salvar_cidades()
        print("Cidade excluída!")
    
    elif opcao == "2":
        from pacientes import pacientes, salvar_pacientes
        pacientes[:] = [p for p in pacientes if p["codigo"] != codigo]
        salvar_pacientes()
        print("Paciente excluído!")

# Usar
excluir_simples()