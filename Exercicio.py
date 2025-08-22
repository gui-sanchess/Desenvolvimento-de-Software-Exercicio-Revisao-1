class Prato:
    
    def __init__(self, nome, tipo, preco, ingredientes):
        self.nome = nome          
        self.tipo = tipo          
        self._preco = preco       
        self.ingredientes = ingredientes

    def print(self):
        print("--- Pratos ---")
        print("Nome:", self.nome)
        print("Tipo:", self.tipo)
        print("Ingredientes:", self.ingredientes)
        print("Preço:", self._preco)
        print()

if __name__ == "__main__":
    prato1 = Prato("Feijoada", "Brasileiro", 45.90, "Feijão preto, carne de porco, arroz, couve")
    prato2 = Prato("Sushi", "Japonês", 65.50, "Arroz, peixe cru, alga")

    prato1.print()
    prato2.print()
