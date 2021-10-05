# def leer_sucursales(ini_sucursales):
#     cant_sucursales = 0
#     while ini_sucursales < 1:
#         ini_sucursales = int(input())
#     cant_sucursales = ini_sucursales
#     return cant_sucursales

# def existencias(cant_existencias, lista_sucursales):
#     cant_existencias = 0
#     lista_sucursales = []

#     for i in range(0, len(lista_sucursales)):
#             print(f"Estamos en la posicion: {lista_sucursales[i]}")
#             aux = int(input())
#             if cant_existencias < 1:
#                 while cant_existencias < 1:
#                     aux = int(input())
#             else:
#                 cant_existencias.append(aux)
#     return cant_existencias
def crearMatriz(a, b, c ,d):
    matriz = []
    for i in range(a):
        fila = []
        for j in range(b):
            fila.append(a)
            fila.append(b)
            fila.append(c)
            fila.append(d)
        matriz.append(a)
    return matriz

def recorrer_su(cant_sucursales):
    ini_sucursales = 0
    cant_sucursales = 0
    while ini_sucursales < 1:
        ini_sucursales = int(input())
    cant_sucursales = ini_sucursales
    lista_sucursales = []
    cont = 0
    for i in range(0, cant_sucursales):
        cont +=1
        lista_sucursales.append(cont)
    return lista_sucursales
    
def enlistar_pacientes(cant_pacientes):
    lista_pacientes = []
    cont = 0
    for i in range(0, cant_pacientes):
        cont +=1
        lista_pacientes.append(cont)
    return lista_pacientes

def leer_medicamentos(cantm, lista_sucursales):
    lista_sucursales = []
    for i in range(0, len(lista_sucursales)):
        lista_sucursales.append(input())
    return lista_sucursales

def main():
    lista_sucursales = []
    lista_sucursales = recorrer_su(lista_sucursales)
    #print(lista_sucursales)
    lista_pacientes = []
    cant_pacientes = int(input())
    lista_pacientes = enlistar_pacientes(cant_pacientes)
    #print(lista_pacientes)
    cant_existencias = 0
    lista_existencias =[]
    cont = 0
    cont_aux = []
    
    #print(f"La lista tiene una longitud de: {len(lista_sucursales)} sucursales")
    for i in range(0, len(lista_sucursales)):
        #print(f"Estamos en la sucursal: {lista_sucursales[i]}")
        if cant_existencias < 1:
            aux = int(input())
        else: 
            aux = int(input())
        lista_existencias.append(aux)
        cont_aux.append(0)
        lista_existencias1 = lista_existencias
        cont += aux
    cant_existencias = cont
    #print(f"Cantidad de existencias: {cant_existencias}")
    #print(f"Esta es la lista de existencias: {lista_existencias}")
    lista_existenciastot = lista_existencias
    cont = 1
    #existencias_totales = [] #Activar solo si las existencias totales varian
    
    cont2 = 0
    while cant_pacientes>0:
        #print(f"Paciente #{cont}")
        #print(f"dijite numero de sucursal, de 1 hasta {len(lista_sucursales)}", end=" ")
        sucursal = int(input())
        for j in range(0, len(lista_sucursales)):
            if lista_sucursales[j] == sucursal:

                lista_main_sucursales = []
                lista_main_existencias = []
                lista_main_pacientes = []
                lista_main_existenciastot = []
                lista_main_medentregados = []
                # print("Esta sucursal existe")
                # print(f"Cantidad de existencias en esta sucursal: {lista_existencias[j]}")
                #Leer presiones
                # print("Presion sistolica:", end=" ")
                ps = int(input())
                # print("Presion diastolica:", end=" ")
                pd = int(input())
                psa = ps
                pda = pd
                #Condicionales entregando medicamentos
                #existencias_totales = lista_existencias[j]
                if(ps>0 and ps<89 and pd>0 and pd<53):
                    categoria = "Hipotension"
                    alerta = "Alerta Amarilla"
                    
                    medaux = lista_existencias[j] - 9
                    if medaux <0:
                        break
                    else:
                        lista_existencias[j] = lista_existencias[j] - 9
                        cont_aux[j] = cont_aux[j] + 9
                elif(ps>=89 and ps<101):
                    if(pd>= 53 and pd<71):
                        categoria = "Ideal"
                        alerta = "Alerta Verde"
                        cont_aux[j] +=0
                        medaux = lista_existencias[j] - 0
                        if medaux <0:
                            break
                        else:
                            lista_existencias[j] = lista_existencias[j] - 0
                    else: 
                        categoria ="No se puede determinar la categoria"
                        alerta ="Alerta Gris"
                        #print(categoria, alerta)
                elif(ps>=101 and ps<139):
                    if(pd>= 71 and pd<88):
                        categoria = "Comun"
                        alerta ="Alerta Verde"
                        cont_aux[j] +=0
                        medaux = lista_existencias[j] - 0
                        if medaux <0:
                            break
                        else:
                            lista_existencias[j] = lista_existencias[j] - 0
                    else:
                        categoria ="No se puede determinar la categoria"
                        alerta ="Alerta Gris"
                        #print(categoria, alerta)
                elif(ps>=139 and ps<156):
                    if(pd>= 88 and pd<105):
                        categoria ="Comun-Alta"
                        alerta ="Alerta Amarilla"
                        cont_aux[j] +=2
                        medaux = lista_existencias[j] - 2
                        if medaux <0:
                            break
                        else:
                            lista_existencias[j] = lista_existencias[j] - 2
                    else:
                        categoria ="No se puede determinar la categoria"
                        alerta ="Alerta Gris"
                        #print(categoria, alerta)
                elif(psa>=156 and psa<172):
                    if(pda>= 105 and pda<124):
                        categoria ="HTAG1"
                        alerta ="Alerta Naranja"
                        cont_aux[j] +=7
                        medaux = lista_existencias[j] - 7
                        if medaux < 0:
                            break
                        else:
                            lista_existencias[j] = lista_existencias[j] - 7
                    else:
                        categoria ="No se puede determinar la categoria"
                        alerta ="Alerta Gris"
                        #print(categoria, alerta)
                elif(ps>=172 and ps<223):
                    if(pd>= 124 and pd>0 and pd<143):
                        categoria ="HTAG2"
                        alerta ="Alerta Naranja"
                        cont_aux[j] +=13
                        medaux = lista_existencias[j] - 13
                        if medaux <0:
                            break
                        else:
                            lista_existencias[j] = lista_existencias[j] - 13
                    elif(ps>141):
                        if(pd>0 and pd<103):
                            categoria ="HTASA"
                            alerta ="Alerta Roja"
                            #print(categoria, alerta)
                            cont_aux[j] += 16
                            medaux = lista_existencias[j] - 16
                            if medaux <0:
                                break
                            else:
                                lista_existencias[j] -= 16
                            #print(f"Atendidos {cont_cl}")
                            #print(f"Medicamentos 1: {med1}", f"Medicamentos 2: {med2}")
                        else:
                            categoria ="5 -No se puede determinar la categoria"
                            alerta ="Alerta Gris"
                            #print(categoria, alerta)
                elif(ps>=223):
                    if(pd>= 143):
                        categoria ="HTAG3"
                        alerta ="Alerta Roja"
                        cont_aux[j] +=25
                        medaux = lista_existencias[j] - 25
                        if medaux <0:
                            break
                        else:
                            lista_existencias[j] = lista_existencias[j] - 25
                    elif(ps>141):
                        if(pd>0 and pd<103):
                            categoria ="HTASA"
                            alerta ="Alerta Roja"
                            cont_aux[j] +=16
                            medaux = lista_existencias[j] - 16 
                            if medaux <0:
                                break
                            else:
                                lista_existencias[j] = lista_existencias[j] - 16
                        else:
                            categoria ="No se puede determinar la categoria"
                            alerta ="Alerta Gris"
                            # print(categoria, alerta)
                elif(ps>=142):
                    if(pd>0 and pd<103):
                        categoria ="HTASA"
                        alerta ="Alerta Roja"
                        cont_aux[j] +=16
                        medaux = lista_existencias[j] - 16 
                        if medaux <0:
                            break
                        else:
                            lista_existencias[j] = lista_existencias[j] - 16
                    else:
                        categoria ="No se puede determinar la categoria"
                        alerta ="Alerta Gris"
                        #print(categoria, alerta)
                elif(pd<1 or psa<1):
                    categoria ="No se puede determinar la categoria"
                    alerta ="Alerta Gris"
                    #print(categoria, alerta)
                else:
                    categoria ="No se puede determinar la categoria"
                    alerta ="Alerta Gris"
                    #print(categoria, alerta)
                #print(f"Cantidades faltantes: {lista_existencias[j]}")
                
                # lista_main_sucursales.append(lista_sucursales)
                # lista_main_existencias.append(existencias_totales)
                # lista_main_pacientes.append(lista_pacientes)
                #lista_main_existenciastot.append(lista_existencias)
                #lista_main_medentregados.append(cont_aux)
                
            elif lista_sucursales[j] < sucursal:
                continue
            else:
                continue
        
        cont +=1
        cant_pacientes -=1
    
    #Ordenamiento
    aux = 0
    aux2 = 0
    aux3 = 0
    # print(lista_sucursales)
    # print(lista_existencias)
    # print(cont_aux)
    lista_sucursales_aux = lista_sucursales
    lista_existencias_aux = lista_existencias
    cont_aux_2 = cont_aux
    # print(lista_sucursales_aux)
    # print(lista_existencias_aux)
    # print(cont_aux_2)
    
    for i in range(1, len(lista_existencias)):
        for j in range(0, len(lista_existencias)-i): 
            if len(lista_existencias)== i:
                # print("Esta porquería se va a romper")
                break
            else:
                # print(f"indice i: ",lista_existencias[j])
                # print("indice i+1: ", lista_existencias[j+1])
                aux2 = lista_existencias[j]
                aux3 = lista_existencias[j+1]
                if aux2 > aux3:
                    #Ordenamiento existencias
                    aux = lista_existencias[j]
                    lista_existencias[j] = lista_existencias[j+1]
                    lista_existencias[j+1] = aux
                    #lista_existencias.sort()
                    #Ordenamiento sucursales
                    aux = lista_sucursales[j]
                    lista_sucursales[j] = lista_sucursales[j+1]
                    lista_sucursales[j+1] = aux

                    aux = cont_aux[j]
                    cont_aux[j] = cont_aux[j+1]
                    cont_aux[j+1] = aux
                else:
                    continue
    # print("\n")            
    # print(lista_sucursales)
    # print(lista_existencias)
    # print(cont_aux)
    a=lista_sucursales.pop()
    b=lista_existencias.pop()
    print(f"{lista_sucursales[0]} {lista_existencias[0]}")
    print(f"{a} {b}")
    lista_sucursales.append(a)
    lista_existencias.append(b)

    #for i in range(len(lista_existencias)):
    i = 0
    for i in range(1, len(lista_sucursales_aux)):
        for j in range(0, len(lista_sucursales_aux)-i): 
            if len(lista_sucursales_aux)== i:
                # print("Esta porquería se va a romper")
                break
            else:
                # print(f"indice i: ",lista_existencias[j])
                # print("indice i+1: ", lista_existencias[j+1])
                aux2 = lista_sucursales_aux[j]
                aux3 = lista_sucursales_aux[j+1]
                if aux2 > aux3:
                    #Ordenamiento existencias
                    aux = lista_sucursales_aux[j]
                    lista_sucursales_aux[j] = lista_sucursales_aux[j+1]
                    lista_sucursales_aux[j+1] = aux
                    #lista_existencias.sort()
                    #Ordenamiento sucursales
                    aux = lista_existencias_aux[j]
                    lista_existencias_aux[j] = lista_existencias_aux[j+1]
                    lista_existencias_aux[j+1] = aux

                    aux = cont_aux_2[j]
                    cont_aux_2[j] = cont_aux_2[j+1]
                    cont_aux_2[j+1] = aux
                else:
                    continue
    # print(lista_sucursales_aux)
    for i in range(0, len(lista_sucursales_aux)):
        # print(f"Sucursal #{lista_sucursales_aux[i]}")
        if cont_aux_2[i] == 0:
            porcentaje = 0
            print(lista_sucursales_aux[i], f"{porcentaje:.2f}%")
        else:
            existencias_totales = cont_aux_2[i] + lista_existencias_aux[i]
            porcentaje = (cont_aux_2[i]*100)/existencias_totales
            print(lista_sucursales_aux[i], f"{porcentaje:.2f}%")
main()
