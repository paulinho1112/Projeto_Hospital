import bisect

class IndiceSimples:
    def __init__(self):
        self.codigos = []
        self.dados = {}
    
    def inserir(self, codigo, dados):
        """Insere dados mantendo ordem"""
        if codigo not in self.dados:
            bisect.insort(self.codigos, codigo)
        self.dados[codigo] = dados
    
    def buscar(self, codigo):
        """Busca por código"""
        return self.dados.get(codigo)
    
    def remover(self, codigo):
        """Remove por código"""
        if codigo in self.dados:
            del self.dados[codigo]
            self.codigos.remove(codigo)
            return True
        return False
    
    def listar_todos(self):
        """Lista todos em ordem de código"""
        return [self.dados[codigo] for codigo in self.codigos]
    
    def listar_codigos(self):
        """Lista apenas os códigos em ordem"""
        return self.codigos.copy()
    
    def buscar_por_posicao(self, posicao):
        """Busca por posição na lista ordenada"""
        if 0 <= posicao < len(self.codigos):
            codigo = self.codigos[posicao]
            return self.dados[codigo]
        return None
    
    def contar(self):
        """Conta quantos registros existem"""
        return len(self.codigos)
