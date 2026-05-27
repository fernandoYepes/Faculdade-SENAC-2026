from arvore import Arvore

a = Arvore() 

a.inserir(a.raiz, 48)
a.inserir(a.raiz, 97)
a.inserir(a.raiz, 51)
a.inserir(a.raiz, 63)
a.inserir(a.raiz, 22)
a.inserir(a.raiz, 44)
a.inserir(a.raiz, 21)
a.inserir(a.raiz, 14)
a.inserir(a.raiz, 5)

print("\n ---Em Ordem ---")
a.imprimirEmOrdem(a.raiz)
print("\n ---Pré Ordem---")
a.imprimirPreOrdem(a.raiz)
print("\n ---Pós Ordem ---")
a.imprimirPosOrdem(a.raiz)
print("\n ---Reverso ---")
a.imprimirReverso(a.raiz)
print("\n ---Em Nivel ---")
a.imprimirEmNivel(a.raiz)

