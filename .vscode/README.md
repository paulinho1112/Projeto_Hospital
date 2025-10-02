# Sistema Hospitalar - Projeto Simples e Funcional

## ✅ Funcionalidades Implementadas

### Operações Básicas
- **Inclusão** de novos registros nas tabelas
- **Consulta** de registros das tabelas  
- **Exclusão** de registros das tabelas
- **Leitura exaustiva** das tabelas

### Estrutura de Dados
- **Árvore Binária** para indexação eficiente
- Busca, inclusão e exclusão otimizadas
- Listagem ordenada por código
- Armazenamento em arquivos JSON

### Módulos Disponíveis
- `medicos.py` - Gestão de médicos
- `pacientes.py` - Gestão de pacientes
- `consultas.py` - Gestão de consultas
- `exames.py` - Gestão de exames
- `especialidades.py` - Gestão de especialidades
- `diarias.py` - Gestão de diárias
- `cidades.py` - Gestão de cidades

### Como Usar
```python
import medicos

# Adicionar médico
medicos.adicionar_medico(1, "Dr. João", "Rua A, 123", "1111-1111", 1, 1)

# Buscar médico
medico = medicos.buscar_medico_por_codigo(1)

# Listar todos os médicos (em ordem)
todos = medicos.listar_medicos()

# Remover médico
medicos.remover_medico(1)
```

### Características
- ✅ Sistema simples e funcional
- ✅ Árvore binária para performance
- ✅ Armazenamento em JSON
- ✅ Todas as operações CRUD implementadas
- ✅ Código limpo e bem documentado

---
*Projeto desenvolvido com foco na simplicidade e funcionalidade*
