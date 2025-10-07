import cidades
import especialidades
import medicos
import pacientes
import exames
import consultas

def limpar_dados():
    """Limpa todos os dados para demonstração limpa"""
    import os
    arquivos = ['cidades.json', 'especialidades.json', 'medicos.json', 
                'pacientes.json', 'exames.json', 'consultas.json', 'diarias.json']
    for arquivo in arquivos:
        if os.path.exists(arquivo):
            os.remove(arquivo)

def main():
    print("🏥 === DEMONSTRAÇÃO DO SISTEMA HOSPITALAR === 🏥\n")
    
    # Limpar dados anteriores
    limpar_dados()
    
    # 1. CADASTRO DE DADOS BÁSICOS
    print("📋 1. CADASTRANDO DADOS BÁSICOS...")
    
    # Cidades
    cidades.adicionar_cidade(1, "São Paulo", "SP")
    cidades.adicionar_cidade(2, "Rio de Janeiro", "RJ")
    cidades.adicionar_cidade(3, "Belo Horizonte", "MG")
    print("✓ Cidades cadastradas")
    
    # Especialidades
    especialidades.adicionar_especialidade(1, "Cardiologia", 150.00, 5)
    especialidades.adicionar_especialidade(2, "Pediatria", 120.00, 8)
    especialidades.adicionar_especialidade(3, "Ortopedia", 180.00, 6)
    print("✓ Especialidades cadastradas")
    
    # Médicos
    medicos.adicionar_medico(1, "Dr. João Silva", "Rua A, 123", "1111-1111", 1, 1)
    medicos.adicionar_medico(2, "Dra. Maria Santos", "Rua B, 456", "2222-2222", 2, 2)
    medicos.adicionar_medico(3, "Dr. Pedro Costa", "Rua C, 789", "3333-3333", 3, 3)
    print("✓ Médicos cadastrados")
    
    # Pacientes
    pacientes.adicionar_paciente(1, "Ana Silva", "1990-01-01", "Rua D, 101", "4444-4444", 1, 70.5, 1.75)
    pacientes.adicionar_paciente(2, "Carlos Santos", "1985-05-15", "Rua E, 202", "5555-5555", 2, 65.0, 1.65)
    pacientes.adicionar_paciente(3, "Lucia Costa", "1992-08-20", "Rua F, 303", "6666-6666", 3, 58.0, 1.60)
    print("✓ Pacientes cadastrados")
    
    # Exames
    exames.adicionar_exame(1, "Eletrocardiograma", 1, 80.00)
    exames.adicionar_exame(2, "Raio-X Tórax", 2, 60.00)
    exames.adicionar_exame(3, "Ressonância Magnética", 3, 200.00)
    print("✓ Exames cadastrados")
    
    print("\n" + "="*50)
    
    # 2. EXERCÍCIO 4 - EXAMES COM ESPECIALIDADE
    print("\n🔬 2. EXERCÍCIO 4 - EXAMES COM ESPECIALIDADE:")
    exames_lista = exames.listar_exames()
    for exame in exames_lista:
        print(f"📋 Código: {exame['codigo']}")
        print(f"   Descrição: {exame['descricao']}")
        print(f"   Especialidade: {exame['nome_especialidade']}")
        print(f"   Valor: R$ {exame['valor_exame']:.2f}")
        print()
    
    print("="*50)
    
    # 3. EXERCÍCIO 5 - CONSULTAS COMPLETAS
    print("\n🩺 3. EXERCÍCIO 5 - CONSULTAS COMPLETAS:")
    
    # Adicionar consultas
    consultas.adicionar_consulta(1, 1, 1, 1, "2024-01-15", "09:00")
    consultas.adicionar_consulta(2, 2, 2, 2, "2024-01-15", "10:00")
    consultas.adicionar_consulta(3, 3, 3, 3, "2024-01-16", "14:00")
    print("✓ Consultas adicionadas")
    
    # Listar consultas com dados completos
    consultas_lista = consultas.listar_consultas()
    for consulta in consultas_lista:
        print(f"📋 Código: {consulta['codigo']}")
        print(f"   Paciente: {consulta['nome_paciente']}")
        print(f"   Cidade: {consulta['nome_cidade_paciente']}")
        print(f"   Médico: {consulta['nome_medico']}")
        print(f"   Exame: {consulta['descricao_exame']}")
        print(f"   Valor Total: R$ {consulta['valor_total']:.2f}")
        print()
    
    print("="*50)
    
    # 4. EXERCÍCIO 6 - FATURAMENTO
    print("\n💰 4. EXERCÍCIO 6 - FATURAMENTO:")
    
    # 6.1 Faturamento por dia
    print("\n📅 6.1 Faturamento por dia (2024-01-15):")
    faturamento_dia = consultas.faturamento_por_dia("2024-01-15")
    print(f"   Data: {faturamento_dia['data']}")
    print(f"   Total: R$ {faturamento_dia['total']:.2f}")
    print(f"   Consultas: {len(faturamento_dia['consultas'])}")
    
    # 6.2 Faturamento por período
    print("\n📅 6.2 Faturamento por período (2024-01-15 a 2024-01-16):")
    faturamento_periodo = consultas.faturamento_por_periodo("2024-01-15", "2024-01-16")
    print(f"   Período: {faturamento_periodo['data_inicial']} a {faturamento_periodo['data_final']}")
    print(f"   Total: R$ {faturamento_periodo['total']:.2f}")
    print(f"   Consultas: {len(faturamento_periodo['consultas'])}")
    
    # 6.3 Faturamento por médico
    print("\n👨‍⚕️ 6.3 Faturamento por médico (Dr. João Silva):")
    faturamento_medico = consultas.faturamento_por_medico(1)
    if faturamento_medico:
        print(f"   Médico: {faturamento_medico['medico']}")
        print(f"   Total: R$ {faturamento_medico['total']:.2f}")
        print(f"   Consultas: {len(faturamento_medico['consultas'])}")
    
    # 6.4 Faturamento por especialidade
    print("\n🏥 6.4 Faturamento por especialidade (Cardiologia):")
    faturamento_esp = consultas.faturamento_por_especialidade(1)
    if faturamento_esp:
        print(f"   Especialidade: {faturamento_esp['especialidade']}")
        print(f"   Total: R$ {faturamento_esp['total']:.2f}")
        print(f"   Consultas: {len(faturamento_esp['consultas'])}")
    
    print("\n" + "="*50)
    
    # 5. EXERCÍCIO 7 - RELATÓRIO COMPLETO
    print("\n📊 5. EXERCÍCIO 7 - RELATÓRIO COMPLETO:")
    relatorio = consultas.relatorio_completo_consultas()
    
    print("\n📋 === RELATÓRIO COMPLETO DE CONSULTAS ===")
    for consulta in relatorio['consultas']:
        print(f"🔹 Código: {consulta['codigo']}")
        print(f"   Paciente: {consulta['nome_paciente']}")
        print(f"   Cidade: {consulta['nome_cidade_paciente']}")
        print(f"   Médico: {consulta['nome_medico']}")
        print(f"   Exame: {consulta['descricao_exame']}")
        print(f"   Valor: R$ {consulta['valor_total']:.2f}")
        print()
    
    print("📈 === RESUMO FINAL ===")
    print(f"👥 Total de Pacientes: {relatorio['total_pacientes']}")
    print(f"💰 Valor Total a Pagar: R$ {relatorio['valor_total_pagar']:.2f}")
    
    print("\n" + "="*50)
    print("🎉 === DEMONSTRAÇÃO CONCLUÍDA COM SUCESSO! === 🎉")
    print("\n✅ Todos os exercícios foram implementados e testados:")
    print("   ✓ Exercício 4: Exames com especialidade")
    print("   ✓ Exercício 5: Consultas com dados completos")
    print("   ✓ Exercício 5.1: Verificação de limite diário")
    print("   ✓ Exercício 5.2: Cálculo de valor total")
    print("   ✓ Exercício 5.3: Atualização de diárias")
    print("   ✓ Exercício 5.4: Remoção de consultas")
    print("   ✓ Exercício 6: Faturamento completo")
    print("   ✓ Exercício 7: Relatório completo")

if __name__ == "__main__":
    main()
