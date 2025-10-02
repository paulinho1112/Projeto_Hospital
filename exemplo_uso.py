#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo de uso do Sistema Hospitalar - Simples e Funcional
"""

import medicos
import pacientes
import especialidades
import cidades

def exemplo_basico():
    """Exemplo básico de uso do sistema"""
    print("=== EXEMPLO DE USO - SISTEMA HOSPITALAR ===")
    
    print("\n1. ADICIONANDO DADOS:")
    
    # Adicionar especialidades
    especialidades.adicionar_especialidade(1, "Cardiologia", 150.00, 10)
    especialidades.adicionar_especialidade(2, "Pediatria", 120.00, 15)
    print("   Especialidades adicionadas")
    
    # Adicionar cidades
    cidades.adicionar_cidade(1, "São Paulo", "SP")
    cidades.adicionar_cidade(2, "Rio de Janeiro", "RJ")
    print("   Cidades adicionadas")
    
    # Adicionar médicos
    medicos.adicionar_medico(1, "Dr. João Silva", "Rua A, 123", "1111-1111", 1, 1)
    medicos.adicionar_medico(2, "Dra. Maria Santos", "Rua B, 456", "2222-2222", 2, 2)
    print("   Médicos adicionados")
    
    # Adicionar pacientes
    pacientes.adicionar_paciente(1, "João Silva", "1990-01-01", "Rua X, 789", "3333-3333", 1, 70.5, 1.75)
    pacientes.adicionar_paciente(2, "Maria Costa", "1985-05-15", "Rua Y, 101", "4444-4444", 2, 65.0, 1.65)
    print("   Pacientes adicionados")
    
    print("\n2. CONSULTANDO DADOS:")
    
    # Buscar médico
    medico = medicos.buscar_medico_por_codigo(1)
    if medico:
        print(f"   Médico encontrado: {medico['nome']}")
    
    # Buscar paciente
    paciente = pacientes.buscar_paciente_por_codigo(1)
    if paciente:
        print(f"   Paciente encontrado: {paciente['nome']}")
    
    print("\n3. LISTANDO DADOS:")
    
    # Listar médicos
    todos_medicos = medicos.listar_medicos()
    print(f"   Total de médicos: {len(todos_medicos)}")
    for medico in todos_medicos:
        print(f"     {medico['codigo']}: {medico['nome']}")
    
    # Listar pacientes
    todos_pacientes = pacientes.listar_pacientes()
    print(f"   Total de pacientes: {len(todos_pacientes)}")
    
    print("\n4. ATUALIZANDO DADOS:")
    
    # Atualizar médico
    sucesso = medicos.atualizar_medico(1, "Dr. João Silva Atualizado", "Rua A, 123", "9999-9999", 1, 1)
    print(f"   Atualização do médico: {'OK' if sucesso else 'ERRO'}")
    
    print("\n5. REMOVENDO DADOS:")
    
    # Remover paciente
    sucesso = pacientes.remover_paciente(2)
    print(f"   Remoção do paciente 2: {'OK' if sucesso else 'ERRO'}")
    
    # Verificar se foi removido
    paciente_removido = pacientes.buscar_paciente_por_codigo(2)
    print(f"   Paciente 2 ainda existe: {'SIM' if paciente_removido else 'NÃO'}")
    
    print("\nSUCESSO - Sistema funcionando perfeitamente!")
    print("Dados salvos automaticamente em arquivos JSON")

if __name__ == "__main__":
    exemplo_basico()
