def somarAte ( n ):
    if n == 1:
        return 1
    else:
        return n + somarAte( n - 1 )
    
def fatorial( x ):
    if x == 0:
        return 1
    else:
        return x * fatorial( x - 1)
    
print( "Soma de 1 até 5: ", somarAte(5) )
print( "Soma 5 é: ", fatorial(5) )

# 1) Implemente uma função recursiva para cálculo de potencia
# 2) Implemente uma função recursiva para contagem regressiva
# 3) Implemente uma funcao recurisva para inverter uma string


# 1)
def potencia(base, expoente):
    if expoente == 0:
        return 1
        
    elif expoente < 0:
        return 1 / potencia(base, -expoente)
        
    # Multiplica a base pela potência com o expoente reduzido em 1
    else:
        return base * potencia(base, expoente - 1)

# Test
print(f"2 elevado a 3 é: {potencia(2, 3)}") # 8  


# 2)
import time
def contagemRegressiva( x ):
    time.sleep( 1 )
    if x == 0:
        print("Fim")
    else:
        print( x )
        contagemRegressiva( x - 1)

contagemRegressiva(5)