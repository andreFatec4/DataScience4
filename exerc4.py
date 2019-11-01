import random
import math

def dot (v, w):
    return sum(v_i * w_i for v_i, w_i in zip (v, w))

def test_dot ():
    v = [1, 2, 7, 8]
    w = [4, 1, 2, 3]
    z = dot (v, w)
    print ('v: ' + str(v))
    print ('w: ' + str(w))
    print('vetor->[v*w] = ', [a*b for a, b in zip(v,w)])
    print ('soma da multiplicações: ' + str(z))

def variance (v):
    mean = sum(v) / len(v)
    #print ("média: ", mean)
    return [v_i - mean for v_i in v]

def test_variance():
    v = [1, 2, 3]
    print (f"variância de cada elemento do vetor: {variance(v)}")

# 1 Escreva uma função que calcula a covariância entre idade e número de amigos.
def covariance (x, y):
    n = len (x)
    return dot(variance(x), variance(y)) / (n - 1)

def test_covariance():
#teste 1
    idade = [30, 22, 41]
    n_amigos = [102, 189, 94]
    print ("Teste 1")
    print ("idade:", idade)
    print ("número de amigos: ", n_amigos)
    print ("variancia idade:", variance(idade))
    print ("variancia número de amigos: ", variance(n_amigos))
    print(f'covariance: {covariance(idade, n_amigos)}')


# 2 Escreva uma função que calcula a correlação entre idade e número de amigos.
def sum_of_squares (v):
    return dot (v, v)

def correlation (x, y):
    desvio_padrao_x = math.sqrt(sum_of_squares(variance(x)) / (len(x) - 1))
    desvio_padrao_y = math.sqrt(sum_of_squares(variance(y)) / (len(y) - 1))
    if desvio_padrao_x > 0 and desvio_padrao_y > 0:
        return print(f'Correlação: {covariance(x, y) / desvio_padrao_y / desvio_padrao_x}')
    else:
        return 0

def test_correlation():
    listas = [
        ([31, 26, 54],[102, 189, 94]),
        ([18, 28, 51],[108, 82, 29]),
        ([31, 26, 54],[42, 76, 14])
    ]
    for i, elemento in enumerate(listas, start=1):
        print(f'Teste: {i}')
        correlation(elemento[0], elemento[1])

# 3 Escreva uma função que devolve uma tupla de duas listas. A primeira lista contém quantidades 
# de amigos que cada usuário da rede tem. A segunda, quantidades de minutos passados em média
# na rede por cada usuário. Cada lista tem tamanho n, sendo n um valor recebido como parâmetro.
# Os dados devem ser gerados aleatoriamente. Faça três versões.

def gera_tupla(a1, a2, m1, m2, n):
    n_amigos = [random.randint(a1, a2) for i in range(n)]
    minutos = [random.randint(m1, m2) for i in range(n)]
    tupla = (n_amigos, minutos)
    #print(tupla)
    return tupla

# 3.1 Gere dados aleatoriamente garantindo correlação próxima de 1.
def tupla_positiva(t):
    l1 = sorted(t[0])
    l2 = sorted(t[1])
    return (l1, l2)

# 3.2 Gere dados aleatoriamente garantindo correlação próxima de -1.
def tupla_negativa(t):
    l1 = sorted(t[0])
    l2 = sorted(t[1], reverse=True)
    return (l1, l2)

# 3.3 Gere dados aleatoriamente garantindo correlação próxima de 0.

# 4 Escreva uma função de teste que mostra que os dados gerados no Exercício 3 estão 
# de acordo com o solicitado.
def test_correlacao():
    n = int(input("Número de elementos das Listas: "))
    t = gera_tupla(10, 25, 2, 50, n)
    print (f'A Tupla ficou assim: {t}')
    print("Correlação próxima de Zero: ")
    correlation (t[0], t[1])
    print (f"=" * 120)
    t = tupla_positiva(t)
    print (f'Ordenando positivamente a Tupla temos: {t}')
    print("Correlação próxima de Um: ")
    correlation (t[0], t[1])
    print (f"=" * 120)
    t = tupla_negativa(t)
    print (f'Deixando as listas com ordenação inversa temos: {t}')
    print("Correlação próxima de Menos Um: ")
    correlation (t[0], t[1])


def main():
    #gera_tupla(10, 25, 2, 50, 10)   
    #test_dot ()
    #test_variance()
    #test_covariance()
    #test_correlation()
    test_correlacao()
main()