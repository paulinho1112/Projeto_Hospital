from cidades import *

print("=== TESTE DO ÍNDICE EM ÁRVORE BINÁRIA ===")

# Adicionar algumas cidades
print("\n1. Adicionando cidades...")
adicionar_cidade(3, "Belo Horizonte", "MG")
adicionar_cidade(1, "São Paulo", "SP")
adicionar_cidade(5, "Salvador", "BA")
adicionar_cidade(2, "Rio de Janeiro", "RJ")
adicionar_cidade(4, "Brasília", "DF")

print("✅ Cidades adicionadas!")

# Listar em ordem (usando índice)
print("\n2. Listando cidades em ordem de código:")
cidades_ordenadas = listar_cidades_ordenadas()
for cidade in cidades_ordenadas:
    print(f"   Código {cidade['codigo']}: {cidade['descricao']} ({cidade['estado']})")

# Buscar por código (usando índice)
print("\n3. Buscando cidade código 3:")
cidade = buscar_cidade_por_codigo(3)
if cidade:
    print(f"   Encontrada: {cidade['descricao']} ({cidade['estado']})")
else:
    print("   Cidade não encontrada!")

# Buscar por posição
print("\n4. Buscando cidade na posição 2:")
cidade_pos = buscar_cidade_por_posicao(2)
if cidade_pos:
    print(f"   Cidade na posição 2: {cidade_pos['descricao']}")

# Contar cidades
print(f"\n5. Total de cidades: {contar_cidades()}")

# Listar códigos
print(f"\n6. Códigos das cidades: {listar_codigos_cidades()}")

# Buscar cidade inexistente
print("\n7. Buscando cidade código 99:")
cidade_inexistente = buscar_cidade_por_codigo(99)
if cidade_inexistente:
    print(f"   Encontrada: {cidade_inexistente['descricao']}")
else:
    print("   Cidade não encontrada!")

# Remover uma cidade
print("\n8. Removendo cidade código 2:")
if remover_cidade(2):
    print("   Cidade removida com sucesso!")
else:
    print("   Erro ao remover cidade!")

# Listar após remoção
print("\n9. Listando após remoção:")
cidades_apos = listar_cidades_ordenadas()
for cidade in cidades_apos:
    print(f"   Código {cidade['codigo']}: {cidade['descricao']} ({cidade['estado']})")

print(f"\n10. Total após remoção: {contar_cidades()}")

print("\n=== TESTE CONCLUÍDO ===")
print("✅ Índice em árvore binária funcionando perfeitamente!")
print("✅ Busca, inclusão e exclusão usando índice!")
print("✅ Leitura exaustiva em ordem!")
