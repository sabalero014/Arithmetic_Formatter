def arithmetic_arranger(problems,display):
    #solo se ejecuta si display is True
    if display is not True:
        #print('saliendo')
        exit()
    #Variables a usar
    todos = [] #todos los listados
    resultados= []
    primero=[]
    segundo = []
    operador = []
    #check1 :5 problemas
    if len(problems) > 5:
        #máximo de 5 problemas
        print("Error: Too many problems.")
        exit()

    for k in problems:
        #separar por espacio y agrego a una lista con valores
        oper = k.split(' ')
        primero.append(oper[0])
        segundo.append(oper[2])
        operador.append(oper[1])

    """print(f'Primeros: {primero}')
    print(f'segundos: {segundo}')
    print(f'Operadores {operador}')"""
    def entero (listado):
        #check3: enteros
        for k in listado:
            try:
                int(k)
            except:
                print('Error: Numbers must only contain digits.')
                exit()
            #check4: hasta 4 digitos
            if len(k)>4:
                print('Error: Numbers cannot be more than four digits.')
                exit()
    entero(primero)
    entero(segundo)
    def conjunto (listado):
        return todos.append(listado)
    #obtengo todos los primeros términos de cada operación
    conjunto(primero)
    conjunto(operador)
    conjunto(segundo)
    #print(todos)
    toditos = list(zip(primero,operador, segundo))
    #print(toditos)
    for i in operador:
        #check2: operadores + o -
        if i == "+": pass
        elif i == "-": pass
        else:
            print("Error: Operator must be '+' or '-'.")
            exit()
    for i in toditos:
        #check2: operadores + o -
        if i[1] == '+':
            suma=int(i[0])+int(i[2])
            resultados.append(suma)
            #print(f'Sumando: {suma}')
        elif i[1] == '-':
            resta=int(i[0])-int(i[2])
            resultados.append(resta)
            #print(f'Restando: {resta}')
        else:
            #print("Error: Operator must be '+' or '-'.")
            exit()
    #print(resultados)
    toditos = list(zip(primero,operador, segundo,resultados))
    conjunto(resultados)
    """print('¿Cuál es mejor?')
    print(f'Toditos: muestra cada operación con su resultado \n{toditos}')
    print(f"Todos: muestra cada operador por separado. \n{todos}") #--- > esta es mejor"""
    ren1="" #primer numero
    reng2=""#simbolo mas segundo numero
    divisor=""#lineas horizontales
    reng3=""#resultados
    for i in toditos:
        print(i)
        #debo volver a iterar en cada elemento para sacar el máximo
        #print(max(len(i)))

#    return arranged_problems

arithmetic_arranger(["32 + 698", "3801 + 2", "45 + 43", "123 + 49"],True)
