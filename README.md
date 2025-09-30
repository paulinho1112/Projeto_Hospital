# Sistema Hospitalar com Árvore Binária

## Funcionalidades Implementadas

### ✅ Operações Básicas
- **Inclusão** de novos registros nas tabelas
- **Consulta** de registros das tabelas  
- **Exclusão** de registros das tabelas
- **Leitura exaustiva** das tabelas

### 🌳 Estrutura de Dados
- **Árvore Binária** implementada para indexação
- Busca, inclusão e exclusão com complexidade O(log n)
- Listagem ordenada por código

### 📊 Módulos Disponíveis
- `medicos.py` - Gestão de médicos
- `pacientes.py` - Gestão de pacientes
- `consultas.py` - Gestão de consultas
- `exames.py` - Gestão de exames
- `especialidades.py` - Gestão de especialidades
- `diarias.py` - Gestão de diárias
- `cidades.py` - Gestão de cidades

### 🚀 Como Usar
```python
import medicos

# Adicionar médico
medicos.adicionar_medico(1, "Dr. João", "Rua A, 123", "1111-1111", 1, 1)

# Buscar médico
medico = medicos.buscar_medico_por_codigo(1)

# Listar todos os médicos (em ordem)
todos = medicos.listar_medicos()
```

---
*Implementado com árvore binária para performance otimizada*
