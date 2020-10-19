def arithmetic_arranger(problems,est = True):
    if est != True: exit()
    # Variables a usar
    todos = []  # todos los listados
    resultados = []
    primero = []
    segundo = []
    operador = []
    longitud = []
    relleno = " "
    check2 = "Error: Operator must be '+' or '-'."
    # check1 :5 problemas
    if len(problems) > 5:
        # máximo de 5 problemas
        arranged_problems = print("Error: Too many problems.")
        return arranged_problems

    for k in problems:
        # separar por espacio y agrego a una lista con valores
        oper = k.split(' ')
        primero.append(oper[0])
        segundo.append(oper[2])
        operador.append(oper[1])
    #agrego a un conjunto
    def conjunto(listado):
        return todos.append(listado)
    # obtengo todos los primeros términos de cada operación
    conjunto(primero)
    conjunto(operador)
    conjunto(segundo)
    # print(todos)
    toditos = list(zip(primero, operador, segundo))
    # print(toditos)
    for i in operador:
        # check2: operadores + o -
        if i == "+":
            pass
        elif i == "-":
            pass
        else:
            arranged_problems = print(check2)
            #print("Error: Operator must be '+' or '-'.")
            return arranged_problems
    # check4: hasta 4 digitos
    def largo (entrada):
        if len(entrada) > 4:
            arranged_problems = print('Error: Numbers cannot be more than four digits.')
            return arranged_problems
    for i in toditos:
        # check4: hasta 4 digitos
        if len(i[0]) > 4:
            arranged_problems = print('Error: Numbers cannot be more than four digits.')
            #print('Error: Numbers cannot be more than four digits.')
            return arranged_problems
        if len(i[2]) > 4:
            arranged_problems = print('Error: Numbers cannot be more than four digits.')
            #print('Error: Numbers cannot be more than four digits.')
            return arranged_problems
        #check enteros a cada valores
        try:
            a = int(i[0])
            b = int(i[2])
        except ValueError:
            arranged_problems = print('Error: Numbers must only contain digits.')
            #exit()
            return arranged_problems
        except:
            arranged_problems = print('otra cosa')
            #exit()
            return arranged_problems
        # check2: operadores + o - y hace la operatoria
        if i[1] == '+':
            suma = a+b
            resultados.append(suma)
            # print(f'Sumando: {suma}')
        elif i[1] == '-':
            resta = a-b
            resultados.append(resta)
            #print(f'Restando: {resta}')
        else:
            arranged_problems = print(check2)
            return arranged_problems
        longitud.append(max(len(i[0]), len(i[2])))
    # print(resultados)
    toditos = list(zip(primero, operador, segundo, resultados, longitud))
    conjunto(resultados)
    conjunto(longitud)

    reng1 = ""  # primer numero
    reng2 = ""  # simbolo mas segundo numero
    divisor = ""  # lineas horizontales
    reng3 = ""  # resultados
    for i in toditos:
        # componentes: (primero,operador, segundo,resultados,longitud)
        reng1 += "  " + i[0].rjust(i[4], relleno) + "    "
        reng2 += i[1] + " " + i[2].rjust(i[4], relleno) + "    "
        divisor += "-" * len("  " + i[0].rjust(i[4], relleno)) + "    "
        reng3 += str(i[3]).rjust(len("-" * len("  " + i[0].rjust(i[4], relleno))), relleno) + "    "

    arranged_problems = print(f'{reng1.rstrip()}\n{reng2.rstrip()}\n{divisor.rstrip()}\n{reng3.rstrip()}')
    return arranged_problems

entrada =["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]
arithmetic_arranger(entrada)
print(len("    3      3801      45      123"))

print("    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----")
print((len("    3      3801      45      123")))
