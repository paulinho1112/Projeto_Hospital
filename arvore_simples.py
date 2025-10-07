class NoArvore:
    def __init__(self, codigo, dados):
        self.codigo = codigo
        self.dados = dados
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
        self._contador = 0
    
    def inserir_dados(self, codigo, dados):
        if self.raiz is None:
            self.raiz = NoArvore(codigo, dados)
            self._contador = 1
            return True
        else:
            return self._inserir_recursivo(self.raiz, codigo, dados)
    
    def _inserir_recursivo(self, no, codigo, dados):
        if codigo == no.codigo:
            # Atualiza dados se código já existe
            no.dados = dados
            return True
        elif codigo < no.codigo:
            if no.esquerda is None:
                no.esquerda = NoArvore(codigo, dados)
                self._contador += 1
                return True
            else:
                return self._inserir_recursivo(no.esquerda, codigo, dados)
        else:
            if no.direita is None:
                no.direita = NoArvore(codigo, dados)
                self._contador += 1
                return True
            else:
                return self._inserir_recursivo(no.direita, codigo, dados)
    
    def buscar_codigo(self, codigo):
        return self._buscar_recursivo(self.raiz, codigo)
    
    def _buscar_recursivo(self, no, codigo):
        if no is None:
            return None
        elif codigo == no.codigo:
            return no.dados
        elif codigo < no.codigo:
            return self._buscar_recursivo(no.esquerda, codigo)
        else:
            return self._buscar_recursivo(no.direita, codigo)
    
    def remover_no(self, codigo):
        if self.raiz is None:
            return False
        
        # Caso especial: remover raiz
        if self.raiz.codigo == codigo:
            self.raiz = self._remover_no(self.raiz)
            self._contador -= 1
            return True
        
        # Buscar o nó pai
        pai = self._buscar_pai(self.raiz, codigo)
        if pai is None:
            return False
        
        # Determinar se é filho esquerdo ou direito
        if pai.esquerda and pai.esquerda.codigo == codigo:
            pai.esquerda = self._remover_no(pai.esquerda)
        else:
            pai.direita = self._remover_no(pai.direita)
        
        self._contador -= 1
        return True
    
    def _buscar_pai(self, no, codigo):
        if no is None:
            return None

        if (no.esquerda and no.esquerda.codigo == codigo) or \
           (no.direita and no.direita.codigo == codigo):
            return no
        
        if codigo < no.codigo:
            return self._buscar_pai(no.esquerda, codigo)
        else:
            return self._buscar_pai(no.direita, codigo)
    
    def _remover_no(self, no):
        if no.esquerda is None:
            return no.direita
        elif no.direita is None:
            return no.esquerda
        else:
            # Nó tem dois filhos - encontrar sucessor
            sucessor = self._encontrar_menor_codigo(no.direita)
            no.codigo = sucessor.codigo
            no.dados = sucessor.dados
            no.direita = self._remover_menor_codigo(no.direita)
            return no
    
    def _encontrar_menor_codigo(self, no):
        while no.esquerda is not None:
            no = no.esquerda
        return no
    
    def _remover_menor_codigo(self, no):
        if no.esquerda is None:
            return no.direita
        no.esquerda = self._remover_menor_codigo(no.esquerda)
        return no
    
    def listar_todos_dados_cres(self):
        resultado = []
        self._inorder_traversal(self.raiz, resultado)
        return resultado
    
    def _inorder_traversal(self, no, resultado):
        """Percorre a árvore em ordem (esquerda, raiz, direita)"""
        if no is not None:
            self._inorder_traversal(no.esquerda, resultado)
            resultado.append(no.dados)
            self._inorder_traversal(no.direita, resultado)
    
    def listar_codigos_cres(self):
        codigos = []
        self._inorder_codigos(self.raiz, codigos)
        return codigos
    
    def _inorder_codigos(self, no, codigos):
        if no is not None:
            self._inorder_codigos(no.esquerda, codigos)
            codigos.append(no.codigo)
            self._inorder_codigos(no.direita, codigos)
    
    def buscar_por_posicao_lista(self, posicao):
        codigos = self.listar_codigos_cres()
        if 0 <= posicao < len(codigos):
            return self.buscar_codigo(codigos[posicao])
        return None
    
    def contar_registro(self):
        return self._contador
    
    def altura_arvore(self): 
        return self._calcular_altura_no(self.raiz)
    
    def _calcular_altura_no(self, no):
        if no is None:
            return 0
        return 1 + max(self._calcular_altura_no(no.esquerda), 
                      self._calcular_altura_no(no.direita))

# Manter compatibilidade com código existente
IndiceSimples = ArvoreBinaria
