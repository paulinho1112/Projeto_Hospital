import pacientes
import cidades


# Teste do IMC
print("=== TESTE DE CÁLCULO E CLASSIFICAÇÃO DE IMC ===")

# Teste 1: IMC básico
imc = pacientes.calcular_imc(56, 1.90)
print(f"Teste 1 - Peso: 56kg, Altura: 1.90m")
print(f"IMC calculado: {imc:.2f}")
print(f"Classificação: {pacientes.classificar_imc(imc)}")


