def arithmetic_arranger(data, show=False):

    uno = []
    dos = []
    tres = []
    a = b = c = d = ""
    max_len = 0

    for calc in data:
        splitted = calc.split()
        uno.append(splitted[0])
        dos.append(splitted[1])
        tres.append(splitted[2])

    if len(uno) > 5: #Mas de 5 problemas
        return ("Error: Too many problems.")
        quit()

    i = 0
    while i<len(uno):

        try: #No contiene solo digitos
            int(uno[i])
            int(tres[i])
        except:
            return ("Error: Numbers must only contain digits.")
            quit()

        if dos[i] == "/" or dos[i] == "*": #Division o multiplicacion
            return ("Error: Operator must be '+' or '-'.")
            quit()

        if len(uno[i]) > 4 or len(tres[i]) > 4: #Mas de 4 digitos
            return ("Error: Numbers cannot be more than four digits.")
            quit()

        if len(str(uno[i])) < len(str(tres[i])):
            espacios = 1
            length = len(str(tres[i])) + 2
        else:
            espacios = len(str(uno[i])) - len(str(tres[i])) + 1
            length = len(str(uno[i])) + 2

        a_new = str(uno[i])
        a_new = a_new.rjust(length," ")
        a = a + a_new
        b_new = dos[i] + " "*espacios + str(tres[i])
        b_new = b_new.rjust(length," ")
        b = b + b_new
        c = c + "-"*length

        if dos[i] == "+":
            resultado = str(int(uno[i]) + int(tres[i]))
        elif dos[i] == "-":
            resultado = str(int(uno[i]) - int(tres[i]))
        resultado = resultado.rjust(length," ")
        d = d + resultado

        if i < len(uno)-1:
            a = a + " "*4
            b = b + " "*4
            c = c + " "*4
            d = d + " "*4

        i += 1

    if show == True:
        return a + "\n" + b + "\n" + c + "\n" + d
    else:
        return a + "\n" + b + "\n" + c
