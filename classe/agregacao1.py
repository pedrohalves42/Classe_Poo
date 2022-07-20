from agregacao import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta', 50)
p2 = Produto('Iphone 13', 6000)
p3 = Produto('relogio', 530)

carrinho.inser_produto(p1)
carrinho.inser_produto(p2)
carrinho.inser_produto(p3)
carrinho.inser_produto(p1)
carrinho.inser_produto(p2)
carrinho.lista_produto()
print(carrinho.soma_total())