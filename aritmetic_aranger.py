def arithmetic_arranger(problems,display):
    #Variables a usar
    todos = [] #todos los listados
    resultados= []
    primero=[]
    segundo = []
    operador = []
    #checkear errores
    if len(problems) > 5:
        #máximo de 5 problemas
        print("Error: Too many problems")
        exit()

    for k in problems:
        #separar por espacio y agrego a una lista con valores
        oper = k.split(' ')
        primero.append(oper[0])
        segundo.append(oper[2])
        operador.append(oper[1])

    print(f'Primeros: {primero}')
    print(f'segundos: {segundo}')
    print(f'Operadores {operador}')
    def entero (listado):
        #check enteros
        for k in listado:
            try:
                int(k)
            except:
                print('Error: Numbers must only contain digits.')
                exit()
            if len(k)>4:
                print('Error: Numbers cannot be more than four digits.')
                exit()
    entero(primero)
    entero(segundo)
    def conjunto (listado):
        return todos.append(listado)
    conjunto(primero)
    conjunto(operador)
    conjunto(segundo)
    

#    return arranged_problems

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True)
