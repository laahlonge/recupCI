# Lara Franco Chaves Vidal - BCC 4o Período

# Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  fazer  um  programa,  usando  a
# linguagem de programação Python, C++, C, que seja capaz de validar e executar programas escritos na
# linguagem  proposta  a  seguir  emitindo  um  relatório  de  análise  léxica,  a  classificação  como  válida  ou
# invalida para cada declaração da linguagem e o resultado do programa.

# Importando as bibliotecas e fazendo o contador
import string
import math
contador = 0

def validacao_esq(count_esq):
  for m in lista_validacao:
    for n in m:
      esq = "("
      dir = ")"
      if n == esq:
        count_esq = count_esq + 1
  return lista_validacao and count_esq


def validacao_dir(list):
  lista_dir = 0
  for m in lista_validacao:
    for n in m:
      esq = "("
      dir = ")"
      if n == dir:
        lista_dir = lista_dir + 1
  return lista_validacao and lista_dir


def get_file(arquivo):
  return open(arquivo).read()


while contador < 3:
  validar_caracter = string.ascii_lowercase
  lista_calculo = []
  contador = contador + 1
  count_elementos = []
  arquivo = get_file(f"{contador}.txt").split("\n")
  parenteses = False
  lista_contador = []

  for i in arquivo:
    lista_contador.append("1")
    lista_validacao = i.split(" ")
    lista_validacao2 = []
    count_esq = 0
    count_esq = validacao_esq(count_esq)
    lista_dir = 0
    numero = False

    for l in lista_validacao:
      for t in l:
        for o in t:
          if o == '1' or o == '2' or o == '3' or o == '4' or o == '5' or o == '6' or o == '7' or o == '8' or o == '9':
            numero = True

    lista_dir = validacao_dir(lista_dir)

    if lista_dir == count_esq:
      print(" ")
    else:
      print(" ")
      parenteses = True

    for esq in lista_validacao:
      validar_elemento = esq
      for y in ['\n', '\t', '(', ')']:
        validar_elemento = validar_elemento.replace(y, "")
      lista_validacao2.append(validar_elemento)
    lista_validacao = lista_validacao2
    remove_interrogacao = False
    for interrogacao in lista_validacao:
      if interrogacao == '?':
        remove_interrogacao = True

    sencos = False
    if lista_validacao.count('sin') == 1 and lista_validacao.count('op1') == 1:
      sencos = True
      lista_validacao = [esq for esq in lista_validacao if esq != 'sin']
      seno = math.sin(
        math.radians(int(count_elementos[0]) * int(count_elementos[1])))
      print("seno de {} é {}".format(
        int(count_elementos[0]) * int(count_elementos[1]), seno))
    lista_validacao = [esq for esq in lista_validacao if esq != '?']

    buffer_contagem = False
    validado = False

    for q in lista_validacao:
      if q == 'op1' or q == 'op2':
        validado = True
        count_elementos.append(lista_validacao[1])
        count_elementos = [esq for esq in count_elementos if esq != 'op1']
        count_elementos = [esq for esq in count_elementos if esq != 'op2']
        buffer_contagem = True
        if len(count_elementos) == 4:
          count_elementos.pop(0)
          count_elementos.pop(0)

    buffer = 0
    if validado == True:
      for j in lista_validacao:
        if j == '*' or j == '+' or j == '-' or j == '+':
          buffer = j
      if buffer == '*':
        primeiro = float(count_elementos[0])
        segundo = float(count_elementos[1])
        string_validacao = primeiro * segundo

        if lista_validacao.count('op1') == 0:

          print(
            '{} * {} ='.format(float(count_elementos[0]),
                               float(count_elementos[1])),
            ' %.3f' % string_validacao)
        elif buffer == '*':
          lista_calculo.append(string_validacao)

      if buffer == '+':
        primeiro = float(count_elementos[0])
        segundo = float(count_elementos[1])
        string_validacao = primeiro + segundo

        if lista_validacao.count('op1') == 0:
          print(
            '{} + {} ='.format(float(count_elementos[0]),
                               float(count_elementos[1])),
            ' %.3f' % string_validacao)
        elif buffer == '+':
          lista_calculo.append(string_validacao)

      if buffer == '-':
        primeiro = float(count_elementos[0])
        segundo = float(count_elementos[1])
        string_validacao = primeiro - segundo

        if lista_validacao.count('op1') == 0:
          print(
            '{} - {} ='.format(float(count_elementos[0]),
                               float(count_elementos[1])),
            ' %.3f' % string_validacao)
        elif buffer == '-':
          lista_calculo.append(string_validacao)

      if buffer == '/':
        primeiro = float(count_elementos[0])
        segundo = float(count_elementos[1])
        string_validacao = primeiro / segundo
        if lista_validacao.count('op1') == 0:
          print(
            '{} / {} ='.format(float(count_elementos[0]),
                               float(count_elementos[1])),
            ' %.3f' % string_validacao)
        elif buffer == '/':
          lista_calculo.append(string_validacao)
    print("linha: {}".format(len(lista_contador)), "lexemas: ", f" {i} ")

    validdd = True
    if remove_interrogacao == True and sencos == False:
      for interrogacao in lista_validacao:
        if interrogacao == '*' and validdd == False:

          lista_validacao = [esq for esq in lista_validacao if esq != '?']
          lista_validacao = [esq for esq in lista_validacao if esq != '*']
          primeiro_termo = int(lista_validacao[0])

          second = int(lista_calculo[0])

          seno = math.sin(
            math.radians(int(count_elementos[0]) * int(count_elementos[1])))
          resultado = (seno * int(lista_validacao[0]))
          print("resultado é ", ' %.3f' % resultado)

        if interrogacao == '-':
          lista_validacao = [esq for esq in lista_validacao if esq != '?']
          lista_validacao = [esq for esq in lista_validacao if esq != '-']
          primeiro_termo = int(lista_validacao[0])
          second = int(lista_calculo[0])
          seno = math.sin(
            math.radians(int(count_elementos[0]) - int(count_elementos[1])))
          resultado = (seno - int(lista_validacao[0]))
          print("resultado é ", ' %.3f' % resultado)
        if interrogacao == '+':
          lista_validacao = [esq for esq in lista_validacao if esq != '?']
          lista_validacao = [esq for esq in lista_validacao if esq != '+']
          primeiro_termo = int(lista_validacao[0])
          second = int(lista_calculo[0])
          seno = math.sin(
            math.radians(int(count_elementos[0]) + int(count_elementos[1])))
          resultado = (seno + int(lista_validacao[0]))

          print("resultado é ", ' %.3f' % resultado)
        if interrogacao == '/':
          lista_validacao = [esq for esq in lista_validacao if esq != '?']
          lista_validacao = [esq for esq in lista_validacao if esq != '/']
          primeiro_termo = int(lista_validacao[0])
          second = int(lista_calculo[0])
          seno = math.sin(
            math.radians(int(count_elementos[0]) / int(count_elementos[1])))
          resultado = (seno / int(lista_validacao[0]))
          print("resultado é ", ' %.3f' % resultado)

    if buffer_contagem == True:

      lista_validacao = [esq for esq in lista_validacao if esq != 'op1']
      lista_validacao = [esq for esq in lista_validacao if esq != 'op2']
      lista_validacao = [esq for esq in lista_validacao if esq != '']
      buffer = lista_validacao[0]
      if buffer == '*':

        primeiro = float(count_elementos[0])
        segundo = float(count_elementos[1])
        string_validacao = primeiro * segundo

        print(
          '{} * {} ='.format(float(count_elementos[0]),
                             float(count_elementos[1])),
          ' %.3f' % string_validacao)
      if buffer == '+':
        primeiro = float(count_elementos[0])
        segundo = float(count_elementos[1])
        string_validacao = primeiro + segundo
        print(
          '{} + {} ='.format(float(count_elementos[0]),
                             float(count_elementos[1])),
          ' %.3f' % string_validacao)
      if buffer == '-':
        primeiro = float(count_elementos[0])
        segundo = float(count_elementos[1])
        string_validacao = primeiro - segundo
        print(
          '{} - {} ='.format(float(count_elementos[0]),
                             float(count_elementos[1])),
          ' %.3f' % string_validacao)
      if buffer == '/':

        primeiro = float(count_elementos[0])
        segundo = float(count_elementos[1])
        string_validacao = (primeiro / segundo)
        print(
          '{} / {} ='.format(float(count_elementos[0]),
                             float(count_elementos[1])),
          ' %.3f' % string_validacao)

      if buffer == '+':
        primeiro = float(count_elementos[0])
        segundo = float(count_elementos[1])
        string_validacao = primeiro + segundo
        print(
          '{} + {} ='.format(float(count_elementos[0]),
                             float(count_elementos[1])),
          ' %.3f' % string_validacao)
      if buffer == '-':
        primeiro = float(count_elementos[0])
        segundo = float(count_elementos[1])
        string_validacao = primeiro - segundo
        print(
          '{} - {} ='.format(float(count_elementos[0]),
                             float(count_elementos[1])),
          ' %.3f' % string_validacao)
      if buffer == '/':

        primeiro = float(count_elementos[0])
        segundo = float(count_elementos[1])
        string_validacao = (primeiro / segundo)
        print(
          '{} / {} ='.format(float(count_elementos[0]),
                             float(count_elementos[1])),
          ' %.3f' % string_validacao)

    exponenciacao = False
    for exponenciacao in lista_validacao:
      if exponenciacao == 'exp':
        exponenciacao = True
        print(int(lista_validacao[1])**(2))
        lista_validacao = [esq for esq in lista_validacao if esq != 'exp']

    if len(lista_validacao) == 2 and lista_validacao[0] == 'sin':
      angulo = int(lista_validacao[1])
      seno = math.sin(math.radians(angulo))
      print("seno de {} é {}".format(angulo, seno))
      print("linha: {}".format(len(lista_contador)), "sintaxe: correta")

    elif len(lista_validacao) == 2 and lista_validacao[0] == 'cos':
      angulo = int(lista_validacao[1])
      seno = math.cos(math.radians(angulo))
      print("cosseno de {} é {}".format(angulo, seno))
    elif len(lista_validacao) == 3 and lista_validacao[0] == 'exp':
      denominador = int(lista_validacao[1])
      elevador = int(lista_validacao[2])
      print(lista_validacao[1], "elevado lista_validacao", lista_validacao[2],
            "é", denominador**elevador)
    elif len(lista_validacao) == 3 and lista_validacao[0] == 'rot':
      raiz = math.sqrt(int(lista_validacao[1]))
      print("raiz quadrada é", raiz)

    elif len(
        lista_validacao
    ) > 3 and validado == False and numero == True and validdd == False:

      listNovo = []
      for g in lista_validacao:
        elemento = g
        lista_validacao = list(string.ascii_lowercase)
        for p in lista_validacao:
          elemento = elemento.replace(p, "")
        listNovo.append(elemento)

      for esq in listNovo.copy():
        if esq == '':
          listNovo.remove(esq)
      parenteses = False
      contagem = []
      for i in listNovo:
        contagem.append(i)
      if contagem[2] == '+':
        primeiro = float(contagem[0])
        segundo = float(contagem[1])
        print('{} + {} ='.format(float(contagem[0]), float(contagem[1])),
              ' %.3f' % (primeiro + segundo))

      if contagem[2] == '-':
        primeiro = float(contagem[0])
        segundo = float(contagem[1])
        print('{} - {} ='.format(float(contagem[0]), float(contagem[1])),
              ' %.3f' % (primeiro - segundo))
      if contagem[2] == '*':

        primeiro = float(contagem[0])
        segundo = float(contagem[1])

        print('{} * {} ='.format(float(contagem[0]), float(contagem[1])),
              ' %.3f' % (primeiro * segundo))
      if contagem[2] == '/':

        primeiro = float(contagem[0])
        segundo = float(contagem[1])
        print('{} / {} ='.format(float(contagem[0]), float(contagem[1])),
              ' %.3f' % (primeiro / segundo))

    if len(lista_validacao) > 2 and validado == False:

      contagem = []
      for i in lista_validacao:
        contagem.append(i)
      if contagem[2] == '+':
        primeiro = float(contagem[0])
        segundo = float(contagem[1])
        print('{} + {} ='.format(float(contagem[0]), float(contagem[1])),
              ' %.3f' % (primeiro + segundo))

      if contagem[2] == '-':
        primeiro = float(contagem[0])
        segundo = float(contagem[1])
        print('{} - {} ='.format(float(contagem[0]), float(contagem[1])),
              ' %.3f' % (primeiro - segundo))
      if contagem[2] == '*':
        primeiro = float(contagem[0])
        segundo = float(contagem[1])

        print('{} * {} ='.format(float(contagem[0]), float(contagem[1])),
              ' %.3f' % (primeiro * segundo))
      if contagem[2] == '/':

        primeiro = float(contagem[0])
        segundo = float(contagem[1])
        print('{} / {} ='.format(float(contagem[0]), float(contagem[1])),
              ' %.3f' % (primeiro / segundo))
    if parenteses == True:
      print("linha: {}".format(len(lista_contador)), "sintaxe: incorreta")
      parenteses = False
    else:
      if numero == True:
        print("linha: {}".format(len(lista_contador)), "sintaxe: correta")
    if numero == False:
      print("linha: {}".format(len(lista_contador)), "sintaxe: incorreta")
