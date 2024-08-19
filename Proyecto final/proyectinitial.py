import random as rd
import os as stop

RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

invasor = []
defensor = []
armamento = ["misiles", "torpedo", "granadas", "sentinel", "chiwi"]
vehiculos = ["tanque", "cazador", "submarino", "destructor", "buque", "fragata"]
resta_armamento = ["cazador", "destructor", "fragata", "sentinel"]
vehiculos_lista_invasor = len(vehiculos)
vehiculos_modi_invasor = vehiculos_lista_invasor
vehiculos_lista_defensor = len(vehiculos)
vehiculos_modi_defensor = vehiculos_lista_defensor
azar_invasor = 0
azar_defensor = 0


class UsuarioInvasor:
    def __init__(self, pnombre):
        self.nombre = pnombre
    def __str__(self):
        return f"{YELLOW}invasor: {RESET}{MAGENTA}{self.nombre}{RESET}"

class UsuarioDefensor:
    def __init__(self, pnombre):
        self.nombre = pnombre
    def __str__(self):
        return f"{YELLOW}defensor: {RESET}{MAGENTA}{self.nombre}{RESET}"


def abandonar_menu_principal():
    while True:
        opcion = input(f"{MAGENTA}{BOLD}digite 'x' para volver al menu principal: {RESET}").lower()
        if opcion == "x":
            break
        else:
            print(f"{RED}{BOLD}Error:{RESET}{YELLOW} digite 'x' si desea salir!{RESET}")
def reglas():
    print(f"\n{BOLD}{MAGENTA}reglas e indicaciones{RESET}")
    print(f"{BLUE}1.{RESET}{GREEN}No puede seleccionar un area ya antes atacado.")
    print(f"{BLUE}2.{RESET}{GREEN}Un turno por usuario.")
    print(f"{BLUE}3.{RESET}{GREEN}Solo existen 3 maneras de ganar: {RESET}")
    print(f"{RED}a. {RESET}{GREEN}Que un bando se retire.{RESET}")
    print(f"{RED}b. {RESET}{GREEN}Que uno de los bandos tenga más del 80% más vehículos o naves con armas, que el bando contrario.{RESET}")
    print(f"{RED}c. {RESET}{GREEN}Que uno de los bandos cuente con mas del 70% de municiones que el bando contrario lo que implica que no podrá defenderse.{RESET}")
    print(f"{BLUE}4.{RESET}{GREEN}El juego consta de un mecanismo que lo hara funcionar de manera aleatoria, es cuestion de suerte e inteligencia, muy buena suerte!{RESET}")
    stop.system("pause")


def invasor_aleatorio():
    global filas_invasor, columnas_invasor
    filas_invasor = 7
    columnas_invasor = 7
    for i in range(filas_invasor):
        invasor.append([0]*columnas_invasor)
    coordenadas = [(fil, colum) for fil in range(filas_invasor) for colum in range(columnas_invasor)]
    coordenadas_aleatorias = rd.sample(coordenadas, 7)

    for vehiculo, (fil, colum) in zip(vehiculos, coordenadas_aleatorias):
        invasor[fil][colum] = vehiculo

def defensor_aleatorio():
    # en esta funcion creamos el tablero(matriz) del defensor, donde asignamos x cantidad de filas y columnas para la matriz
    global filas_defensor, columnas_defensor
    filas_defensor = 7
    columnas_defensor = 7
    for i in range(filas_defensor):
        #a este for le indicamos que el iterador va a recorrer las x filas
        defensor.append([0]*columnas_defensor)
        #al defensor.append le estamos indicando que va agregar a la lista defensor que antes creamos el valor numerico 0 a las x columnas indicadas antes
        #por lo tanto se esta creando un tablero con x filas y columnas llenas de 0
    coordenadas = [(fil, colum) for fil in range(filas_defensor) for colum in range(columnas_defensor)]
    #en la variable cordenadas estamos creando un recorrido con 2 iteradores en este caso fil, colum en las filas y columnas del tablero(matriz)
    coordenadas_aleatorias = rd.sample(coordenadas, 7)
    #en esta variable cordenadas_aleatorias estamos seleccionando espacios del tablero(matriz) con un limite, o sea que se escogieron al azar x espacios de este tablero(matriz)

    #con este for vamos a asignar vehículos a las coordenadas aleatorias creadas anteriormente
    for vehiculo, (fil, colum) in zip(vehiculos, coordenadas_aleatorias):
        defensor[fil][colum] = vehiculo

def generador_estadisticas():
    global intentos, termina, vidas_invasor, vidas_modi_invasor, porcentaje_vidas_invasor, vidas_defensor, vidas_modi_defensor, porcentaje_vidas_defensor
    global aleatorio_armamento_invasor1, aleatorio_balas_invasor1, balas_modi_invasor1, porcentaje_balas_invasor1
    global aleatorio_armamento_invasor2, aleatorio_balas_invasor2, balas_modi_invasor2, porcentaje_balas_invasor2
    global aleatorio_armamento_defensor1, aleatorio_balas_defensor1, balas_modi_defensor1, porcentaje_balas_defensor1
    global aleatorio_armamento_defensor2, aleatorio_balas_defensor2, balas_modi_defensor2, porcentaje_balas_defensor2, cierre, logica_vidas_invasor, logica_vidas_defensor
    global fallos_invasor, aciertos_tanques_invasor, aciertos_submarinos_invasor, aciertos_cazador_invasor, aciertos_total_invasor, aciertos_buque_invasor, aciertos_fragata_invasor, aciertos_destructor_invasor
    global fallos_defensor, aciertos_tanques_defensor, aciertos_submarinos_defensor, aciertos_cazador_defensor, aciertos_total_defensor, aciertos_buque_defensor, aciertos_fragata_defensor, aciertos_destructor_defensor
    fallos_invasor = 0
    aciertos_tanques_invasor = 0
    aciertos_submarinos_invasor = 0
    aciertos_cazador_invasor = 0
    aciertos_total_invasor = 0
    aciertos_buque_invasor = 0
    aciertos_fragata_invasor = 0
    aciertos_destructor_invasor = 0
    aciertos_total_invasor = 0


    fallos_defensor = 0
    aciertos_tanques_defensor = 0
    aciertos_submarinos_defensor = 0
    aciertos_cazador_defensor = 0
    aciertos_buque_defensor = 0
    aciertos_fragata_defensor = 0
    aciertos_destructor_defensor = 0
    aciertos_total_defensor = 0

    cierre = False
    termina = 0

    aleatorio_armamento_invasor1 = rd.choice(resta_armamento)
    aleatorio_balas_invasor1 = rd.randint(40, 49)
    balas_modi_invasor1 = aleatorio_balas_invasor1
    porcentaje_balas_invasor1 = (balas_modi_invasor1 / aleatorio_balas_invasor1) * 100

    #aleatorio_armamento_invasor2 = rd.choice(resta_armamento)
    #aleatorio_balas_invasor2 = rd.randint(1, 5)
    #balas_modi_invasor2 = aleatorio_balas_invasor2
    #porcentaje_balas_invasor2 = (balas_modi_invasor2 / aleatorio_balas_invasor2) * 100

    aleatorio_armamento_defensor1 = rd.choice(resta_armamento)
    aleatorio_balas_defensor1 = rd.randint(40, 49)
    balas_modi_defensor1 = aleatorio_balas_defensor1
    porcentaje_balas_defensor1 = (balas_modi_defensor1 / aleatorio_balas_defensor1) * 100

    #aleatorio_armamento_defensor2 = rd.choice(resta_armamento)
    #aleatorio_balas_defensor2 = rd.randint(1, 5)
    #balas_modi_defensor2 = aleatorio_balas_defensor2
    #porcentaje_balas_defensor2 = (balas_modi_defensor2 / aleatorio_balas_defensor2) * 100


def mostrar_estadisticas_invasor1():
    global nuevoporcentaje_vidas_defensor, vehiculos_modi_defensor, Nuevoporcentaje_balas_invasor1, balas_modi_invasor1, aleatorio_balas_invasor1
    nuevoporcentaje_vidas_defensor = (vehiculos_modi_defensor / vehiculos_lista_defensor) * 100
    nuevoporcentaje_balas_invasor1 = (balas_modi_invasor1 / aleatorio_balas_invasor1) * 100
    print(f"{YELLOW}al defensor le quedan {vehiculos_modi_defensor} vehiculos, o sea un {nuevoporcentaje_vidas_defensor:.2f}% de vehiculos{RESET}")
    print(f"{YELLOW}al invasor le quedan {balas_modi_invasor1} balas en el armamento, o sea un {nuevoporcentaje_balas_invasor1:.2f}% de balas{RESET}")




def mostrar_estadisticas_defensor1():
    global nuevoporcentaje_vidas_invasor, vehiculos_modi_invasor, nuevoporcentaje_balas_defensor1, balas_modi_defensor1, aleatorio_balas_defensor1
    nuevoporcentaje_vidas_invasor = (vehiculos_modi_invasor / vehiculos_lista_invasor) * 100
    nuevoporcentaje_balas_defensor1 = (balas_modi_defensor1 / aleatorio_balas_defensor1) * 100
    print(f"{BOLD}{RED}Mensaje: {RESET}{YELLOW}al invasor le quedan {vehiculos_modi_invasor} vehiculos, o sea un {nuevoporcentaje_vidas_invasor:.2f}% de vehiculos{RESET}")
    print(f"{BOLD}{RED}Mensaje: {RESET}{YELLOW}al defensor le quedan {balas_modi_defensor1} balas en el armamento, o sea un {nuevoporcentaje_balas_defensor1:.2f}% de balas{RESET}")

def retiro_invasor():
    global cierre
    while True:
        decision = input(f"{CYAN}{BOLD}-Desea retirarse? s/n: {RESET}").lower()
        if decision == "s":
            print(f"{RED}{BOLD}Mensaje: {RESET}{YELLOW}se ha retirado el invasor, ha ganado el defensor{RESET}")
            cierre = True
            estadisticas_finales()
            break
        elif decision == "n":
            break
        elif decision != "n":
            print(f"{RED}{BOLD}Error:{RESET}{YELLOW} digite una opcion valida! ('s' o 'n'){RESET}")


def retiro_defensor():
    global cierre
    while True:
        decision = input(f"{CYAN}{BOLD}-Desea retirarse? s/n: {RESET}").lower()
        if decision == "s":
            print(f"{RED}{BOLD}Mensaje: {RESET}{YELLOW}se ha retirado el defensor, ha ganado el invasor{RESET}")
            cierre = True
            estadisticas_finales()
            break
        elif decision == "n":
            break
        elif decision != "n":
            print(f"{RED}{BOLD}Error:{RESET}{YELLOW} digite una opcion valida! ('s' o 'n'){RESET}")



def informacion_de_vehivulos_invasor():
    if azar_invasor == "cazador":
        print(f"{RED}{BOLD}Mensaje:{RESET}{YELLOW} el cazador gasta un total de 7 municiones por ronda!{RESET}")
    elif azar_invasor == "destructor":
        print(f"{RED}{BOLD}Mensaje:{RESET}{YELLOW} el destrucor gasta un total de 2 municiones por ronda!{RESET}")
    elif azar_invasor == "fragata":
        print(f"{RED}{BOLD}Mensaje:{RESET}{YELLOW} el fragata gasta un total de 4 municiones por ronda!{RESET}")
    elif azar_invasor == "sentinel":
        print(f"{RED}{BOLD}Mensaje:{RESET}{YELLOW} el sentinel gasta la enorme cantidad de 9 municiones por ronda!{RESET}")

def informacion_de_vehivulos_defensor():
    if azar_defensor == "cazador":
        print(f"{RED}{BOLD}Mensaje:{RESET}{YELLOW} el cazador gasta un total de 7 municiones por ronda!{RESET}")
    elif azar_defensor == "destructor":
        print(f"{RED}{BOLD}Mensaje:{RESET}{YELLOW} el destrucor gasta un total de 2 municiones por ronda!{RESET}")
    elif azar_defensor == "fragata":
        print(f"{RED}{BOLD}Mensaje:{RESET}{YELLOW} el fragata gasta un total de 4 municiones por ronda!{RESET}")
    elif azar_defensor == "sentinel":
        print(f"{RED}{BOLD}Mensaje:{RESET}{YELLOW} el sentinel gasta la enorme cantidad de 9 municiones por ronda!{RESET}")

def resta_al_fallar_invasor():
    global fallos_invasor, balas_modi_invasor1, resta_invasor1
    if azar_invasor == "cazador":
        resta_invasor1 = balas_modi_invasor1 - 7
        balas_modi_invasor1 = resta_invasor1
    elif azar_invasor == "destructor":
        resta_invasor1 = balas_modi_invasor1 - 2
        balas_modi_invasor1 = resta_invasor1
    elif azar_invasor == "fragata":
        resta_invasor1 = balas_modi_invasor1 - 4
        balas_modi_invasor1 = resta_invasor1
    elif azar_invasor == "sentinel":
        resta_invasor1 = balas_modi_invasor1 - 9
        balas_modi_invasor1 = resta_invasor1
    defensor[fila][columna] = "x"

def resta_al_fallar_defensor():
    global resta_vida_invasor, vidas_modi_invasor, resta_defensor1, balas_modi_defensor1, fila, columna, azar
    if azar_defensor == "cazador":
        resta_defensor1 = balas_modi_defensor1 - 7
        balas_modi_defensor1 = resta_defensor1
    elif azar_defensor == "destructor":
        resta_defensor1 = balas_modi_defensor1 - 2
        balas_modi_defensor1 = resta_defensor1
    elif azar_defensor == "fragata":
        resta_defensor1 = balas_modi_defensor1 - 4
        balas_modi_defensor1 = resta_defensor1
    elif azar_defensor == "sentinel":
        resta_defensor1 = balas_modi_defensor1 - 9
        balas_modi_defensor1 = resta_defensor1
    invasor[fila][columna] = "x"

def resta_estadisticas_invasor1():
    #["cazador", "destructor", "fragata", "sentinel"]
    global resta_vida_defensor, vehiculos_modi_defensor, resta_invasor1, balas_modi_invasor1, fila, columna, aleatorio_armamento_invasor1
    resta_invasor1 = balas_modi_invasor1 - 1
    balas_modi_invasor1 = resta_invasor1
    resta_vida_defensor = vehiculos_modi_defensor - 1
    vehiculos_modi_defensor = resta_vida_defensor
    defensor[fila][columna] = "x"

def resta_estadisticas_invasor2():
    global resta_vida_defensor, vidas_modi_defensor, resta_invasor2, balas_modi_invasor2, fila, columna
    if aleatorio_armamento_invasor2 == "cazador":
        resta_invasor2 = balas_modi_invasor2 - 7
        balas_modi_invasor2 = resta_invasor2
    elif aleatorio_armamento_invasor2 == "destructor":
        resta_invasor2 = balas_modi_invasor2 - 2
        balas_modi_invasor2 = resta_invasor2
    elif aleatorio_armamento_invasor2 == "fragata":
        resta_invasor2 = balas_modi_invasor2 - 4
        balas_modi_invasor2 = resta_invasor2
    elif aleatorio_armamento_invasor2 == "sentinel":
        resta_invasor2 = balas_modi_invasor2 - 9
        balas_modi_invasor2 = resta_invasor2

    resta_vida_defensor = vidas_modi_defensor - 1
    vidas_modi_defensor = resta_vida_defensor
    defensor[fila][columna] = "x"

def resta_estadisticas_defensor1():
    global resta_vida_invasor, vehiculos_modi_defensor, resta_defensor1, balas_modi_defensor1, fila, columna
    resta_defensor1 = balas_modi_defensor1 - 1
    balas_modi_defensor1 = resta_defensor1
    resta_vida_invasor = vehiculos_modi_defensor - 1
    vehiculos_modi_defensor = resta_vida_invasor
    invasor[fila][columna] = "x"

def resta_estadisticas_defensor2():
    global resta_vida_invasor, vidas_modi_invasor, resta_defensor2, balas_modi_defensor2, fila, columna
    if aleatorio_armamento_defensor1 == "cazador":
        resta_defensor2 = balas_modi_defensor2 - 9
        balas_modi_defensor2 = resta_defensor2
    elif aleatorio_armamento_defensor1 == "destructor":
        resta_defensor2 = balas_modi_defensor2 - 2
        balas_modi_defensor2 = resta_defensor2
    elif aleatorio_armamento_defensor1 == "fragata":
        resta_defensor2 = balas_modi_defensor2 - 4
        balas_modi_defensor2 = resta_defensor2
    elif aleatorio_armamento_defensor1 == "sentinel":
        resta_defensor2 = balas_modi_defensor2 - 9
        balas_modi_defensor2 = resta_defensor2

    resta_vida_invasor = vidas_modi_invasor - 1
    vidas_modi_invasor = resta_vida_invasor
    invasor[fila][columna] = "x"


def estadisticas_finales():
    global fallos_invasor, aciertos_tanques_invasor, aciertos_submarinos_invasor, aciertos_helicopteros_invasor, aciertos_total_invasor, nombre_invasor, nombre_defensor
    global fallos_defensor, aciertos_tanques_defensor, aciertos_submarinos_defensor, aciertos_helicopteros_defensor, aciertos_total_defensor
    print(f"{CYAN}{BOLD}=====ESTADISTICAS====={RESET}")
    print(f"{YELLOW}{BOLD}-fallos invasor:{RESET}")
    print(f"{MAGENTA}{BOLD}total: {RESET}{fallos_invasor}")
    print(f"{YELLOW}{BOLD}-aciertos invasor:{RESET}")
    aciertos_total_invasor = suma_aciertos_invasor()
    print(f"{MAGENTA}{BOLD}total: {RESET}{aciertos_total_invasor}")
    print(f"{YELLOW}{BOLD}-Derribos invasor:{RESET}")
    print(f"{MAGENTA}{BOLD}tanques:{RESET} {aciertos_tanques_invasor}{RED}|{RESET}{MAGENTA}{BOLD}cazadores: {RESET}{aciertos_cazador_invasor}{RED}|{RESET}{MAGENTA}{BOLD}submarinos: {RESET}{aciertos_submarinos_invasor}")
    print(f"{MAGENTA}{BOLD}buques:{RESET} {aciertos_buque_invasor}{RED}|{RESET}{MAGENTA}{BOLD}destructores: {RESET}{aciertos_destructor_invasor}{RED}|{RESET}{MAGENTA}{BOLD}fragatas: {RESET}{aciertos_fragata_invasor}")

    print(f"\n{YELLOW}{BOLD}-fallos defensor:{RESET}")
    print(f"{MAGENTA}{BOLD}total: {RESET}{fallos_defensor}")
    print(f"{YELLOW}{BOLD}-aciertos defensor:{RESET}")
    aciertos_total_defensor = suma_aciertos_defensor()
    print(f"{MAGENTA}{BOLD}total: {RESET}{aciertos_total_defensor}")
    print(f"{YELLOW}{BOLD}-Derribos defensor:{RESET}")
    print(f"{MAGENTA}{BOLD}tanques:{RESET} {aciertos_tanques_defensor}{RED}|{RESET}{MAGENTA}{BOLD}cazadores: {RESET}{aciertos_cazador_defensor}{RED}|{RESET}{MAGENTA}{BOLD}submarinos: {RESET}{aciertos_submarinos_defensor}")
    print(f"{MAGENTA}{BOLD}buques:{RESET} {aciertos_buque_defensor}{RED}|{RESET}{MAGENTA}{BOLD}destructores: {RESET}{aciertos_destructor_defensor}{RED}|{RESET}{MAGENTA}{BOLD}fragatas: {RESET}{aciertos_fragata_defensor}")
    abandonar_menu_principal()



def suma_aciertos_invasor():
    return aciertos_tanques_invasor + aciertos_cazador_invasor + aciertos_submarinos_invasor + aciertos_fragata_invasor + aciertos_destructor_invasor + aciertos_buque_invasor
def suma_aciertos_defensor():
    return aciertos_tanques_defensor + aciertos_cazador_defensor + aciertos_submarinos_defensor + aciertos_fragata_defensor + aciertos_destructor_defensor + aciertos_buque_defensor

def nombre_de_jugadores():
    global nombre_invasor, nombre_defensor
    while True:
        consulta_nombre = input(f"{GREEN}{BOLD}desea el jugador 1 y 2 añadir algun NameID? s/n: {RESET}").lower()
        if consulta_nombre == "s":
            nombre_invasor = input(f"{CYAN}digite su nombre o apodo (invasor/jugador 1): ").capitalize()
            nombre_defensor = input(f"digite su nombre o apodo (defensor/jugador 2): {RESET}").capitalize()
            invasor = UsuarioInvasor(nombre_invasor)
            defensor = UsuarioDefensor(nombre_defensor)
            print(invasor)
            print(defensor)
            print(f"{BLUE}Buena suerte {nombre_invasor} y {nombre_defensor}!{RESET}")
            break
        elif consulta_nombre == "n":
            nombre_invasor = "Jugador 1"
            nombre_defensor = "jugador 2"
            break
        elif consulta_nombre != "n":
            print(f"{RED}{BOLD}Error:{RESET}{YELLOW} digite una opcion valida! ('s' o 'n'){RESET}")

def vehiculo_aleatorio_invasor():
    global azar_invasor
    azar_invasor = rd.choice(resta_armamento)
    print(f"{RED}(1){RESET}{YELLOW}vehiculo:{RESET} {azar_invasor} | {YELLOW}municion:{RESET} {balas_modi_invasor1}")

def vehiculo_aleatorio_defensor():
    global azar_defensor
    azar_defensor = rd.choice(resta_armamento)
    print(f"{RED}(1){RESET}{YELLOW}vehiculo:{RESET} {azar_defensor} | {YELLOW}municion:{RESET} {balas_modi_defensor1}")





def verificador_diferencia():
    global cierre
    diferencia_absoluta = abs(balas_modi_invasor1 - balas_modi_defensor1)
    porcentaje_diferencia = (diferencia_absoluta / max(balas_modi_invasor1, balas_modi_defensor1)) * 100
    if balas_modi_invasor1 > balas_modi_defensor1:
        if porcentaje_diferencia > 70:
            print(f"{BOLD}{RED}Mensaje: {RESET}{YELLOW}Ganó el invasor ya que la diferencia de municion es mayor al 70% ({BLUE}{porcentaje_diferencia:.2f}%{RESET}{YELLOW}) en comparacion con la municion del defensor.{RESET}")
            cierre = True
            estadisticas_finales()
        elif porcentaje_diferencia == 70:
            print(f"{BOLD}{RED}Mensaje: {RESET}{YELLOW}Ganó el invasor ya que la diferencia de municion es igual al 70% ({BLUE}{porcentaje_diferencia:.2f}%{RESET}{YELLOW}) en comparacion con la municion del defensor.{RESET}")
            cierre = True
            estadisticas_finales()
        else:
            print(f"{BOLD}{RED}Mensaje: {RESET}{YELLOW}la diferencia de municion es del ({BLUE}{porcentaje_diferencia:.2f}%{RESET}{YELLOW}), a favor del invasor.{RESET}")
            cierre = False
    elif balas_modi_defensor1 > balas_modi_invasor1:
        if porcentaje_diferencia > 70:
            print(f"{BOLD}{RED}Mensaje: {RESET}{YELLOW}Ganó el defensor ya que la diferencia de municion es mayor al 70% ({BLUE}{porcentaje_diferencia:.2f}%{RESET}{YELLOW}) en comparacion con la municion del invasor.{RESET}")
            cierre = True
            estadisticas_finales()
        elif porcentaje_diferencia == 70:
            print(f"{BOLD}{RED}Mensaje: {RESET}{YELLOW}Ganó el defensor ya que la diferencia de municion es igual al 70% ({BLUE}{porcentaje_diferencia:.2f}%{RESET}{YELLOW}) en comparacion con la municion del invasor.{RESET}")
            cierre = True
            estadisticas_finales()
        else:
            print(f"{BOLD}{RED}Mensaje: {RESET}{YELLOW}la diferencia de municion es del ({BLUE}{porcentaje_diferencia:.2f}%{RESET}{YELLOW}), a favor del defensor.{RESET}")
            cierre = False
    elif balas_modi_defensor1 == balas_modi_invasor1:
        print(f"{BOLD}{RED}Mensaje: {RESET}{YELLOW}hay un ({BLUE}{porcentaje_diferencia:.2f}%{RESET}{YELLOW}) de diferencia, vamos, desempata!{RESET}")
    else:
        print("Por qué?")

def agrupar_funciones_invasor():
    global aciertos_tanques_invasor
    resta_estadisticas_invasor1()
    mostrar_estadisticas_invasor1()
    verificador_diferencia()

def agrupar_funciones_defensor():
    resta_estadisticas_defensor1()
    mostrar_estadisticas_defensor1()
    verificador_diferencia()


def ejecutar_juego():
    global intentos, termina, vidas_invasor, vidas_modi_invasor, porcentaje_vidas_invasor, vidas_defensor, vidas_modi_defensor, porcentaje_vidas_defensor
    global aleatorio_armamento_invasor1, aleatorio_balas_invasor1, balas_modi_invasor1, porcentaje_balas_invasor1
    global aleatorio_armamento_invasor2, aleatorio_balas_invasor2, balas_modi_invasor2, porcentaje_balas_invasor2
    global aleatorio_armamento_defensor1, aleatorio_balas_defensor1, balas_modi_defensor1, porcentaje_balas_defensor1
    global aleatorio_armamento_defensor2, aleatorio_balas_defensor2, balas_modi_defensor2, porcentaje_balas_defensor2
    global fila, columna, cierre, filas_invasor, columnas_invasor, filas_defensor, columnas_defensor, nombre_invasor, nombre_defensor
    global fallos_invasor, aciertos_tanques_invasor, aciertos_submarinos_invasor, aciertos_cazador_invasor, aciertos_total_invasor, aciertos_buque_invasor, aciertos_fragata_invasor, aciertos_destructor_invasor
    global fallos_defensor, aciertos_tanques_defensor, aciertos_submarinos_defensor, aciertos_cazador_defensor, aciertos_total_defensor, aciertos_buque_defensor, aciertos_fragata_defensor, aciertos_destructor_defensor
    print(f"{BOLD}{YELLOW}=====BIENVENIDOS A BATTLE SHIP-GUERRA DE MUNDOS====={RESET}")

    while not cierre:
        print(f"{BOLD}{MAGENTA}----turno de {nombre_invasor}(invasor)----{RESET}")
        retiro_invasor()
        if not cierre:
            vehiculo_aleatorio_invasor()
            informacion_de_vehivulos_invasor()
        while not cierre:
            try:
                print(f"{MAGENTA}donde desea atacar?: {RESET}")
                fila = int(input(f"{GREEN}indica la fila que desea atacar (0 a {filas_invasor - 1}): {RESET}"))
                columna = int(input(f"{GREEN}indique la columna que desea atacar (0 a {filas_invasor - 1}): {RESET}"))
                if 0 <= fila < filas_invasor and 0 <= columna < columnas_invasor:
                    if balas_modi_invasor1 == termina:
                        print(f"{RED}{BOLD}ya no te quedan balas, utiliza otro armamento que contenga municion{RESET}")
                    elif defensor[fila][columna] == "x":
                        print(f"{RED}{BOLD}ya no puedes utilizar esa posicion {RESET}")
                    #["tanque", "cazador", "submarino", "destructor", "buque", "fragata"]
                    elif (defensor[fila][columna]==0):
                        print(f"{RED}{BOLD}Mensaje: {RESET}{YELLOW}fallaste!{RESET}")
                        fallos_invasor += 1
                        resta_al_fallar_invasor()
                        mostrar_estadisticas_invasor1()
                        verificador_diferencia()
                        break

                    elif defensor[fila][columna] == "tanque":
                        print(f"{RED}{BOLD}Mensaje: {RESET}{MAGENTA}le has dado a un tanque! y se te ha restado 1 municion por el acierto!{RESET}")
                        aciertos_tanques_invasor += 1
                        agrupar_funciones_invasor()
                        break

                    elif defensor[fila][columna] == "cazador":
                        print(f"{RED}{BOLD}Mensaje: {RESET}{MAGENTA}le has dado a un cazador! y se te ha restado 1 municion por el acierto!{RESET}")
                        aciertos_cazador_invasor += 1
                        agrupar_funciones_invasor()
                        break

                    elif defensor[fila][columna] == "submarino":
                        print(f"{RED}{BOLD}Mensaje: {RESET}{MAGENTA}le has dado a un submarino! y se te ha restado 1 municion por el acierto!{RESET}")
                        aciertos_submarinos_invasor += 1
                        agrupar_funciones_invasor()
                        break

                    elif defensor[fila][columna] == "destructor":
                        print(f"{RED}{BOLD}Mensaje: {RESET}{MAGENTA}le has dado a un destructor! y se te ha restado 1 municion por el acierto!{RESET}")
                        aciertos_destructor_invasor += 1
                        agrupar_funciones_invasor()
                        break

                    elif defensor[fila][columna] == "buque":
                        print(f"{RED}{BOLD}Mensaje: {RESET}{MAGENTA}le has dado a un buque! y se te ha restado 1 municion por el acierto!{RESET}")
                        aciertos_buque_invasor += 1
                        agrupar_funciones_invasor()
                        break

                    elif defensor[fila][columna] == "fragata":
                        print(f"{RED}{BOLD}Mensaje: {RESET}{MAGENTA}le has dado a un fragata! y se te ha restado 1 municion por el acierto!{RESET}")
                        aciertos_fragata_invasor += 1
                        agrupar_funciones_invasor()
                        break
                else:
                    print(f"{RED}{BOLD}Error:{RESET}{YELLOW} el valor de las filas y columnas debe estar entre 0 y {filas_invasor - 1}!")
                    print(f"intentemos de nuevo! :) {RESET}")

            except ValueError:
                print(f"{RED}{BOLD}Error:{RESET}{YELLOW} no puede estar vacio o con valores alfabeticos!")
                print(f"intentemos de nuevo! :){RESET}")


        while not cierre:
            print(f"{MAGENTA}{BOLD}----turno de {nombre_defensor}(defensor)----{RESET}")
            retiro_defensor()
            if not cierre:
                vehiculo_aleatorio_defensor()
                informacion_de_vehivulos_defensor()
            while not cierre:
                try:
                    print(f"{MAGENTA}donde desea atacar?: {RESET}")
                    fila = int(input(f"{GREEN}indica la fila que desea atacar (0 a {filas_invasor - 1}): {RESET}"))
                    columna = int(input(f"{GREEN}indique la columna que desea atacar (0 a {filas_invasor - 1}): {RESET}"))
                    if 0 <= fila < filas_defensor and 0 <= columna < columnas_defensor:
                        if balas_modi_defensor1 == termina:
                            print(f"{RED}No te quedan balas, utiliza otro armamento que contenga municion{RESET}")

                        elif invasor[fila][columna] == "x":
                            print(f"{RED}{BOLD}ya no puedes utilizar esa posicion {RESET}")
                        # ["tanque", "cazador", "submarino", "destructor", "buque", "fragata"]
                        elif (invasor[fila][columna] == 0):
                            print(f"{RED}{BOLD}Mensaje: {RESET}{YELLOW}fallaste!{RESET}")
                            fallos_defensor += 1
                            resta_al_fallar_defensor()
                            mostrar_estadisticas_defensor1()
                            verificador_diferencia()
                            break

                        elif invasor[fila][columna] == "tanque":
                            print(f"{RED}{BOLD}Mensaje: {RESET}{MAGENTA}le has dado a un tanque! y se te ha restado 1 municion por el acierto!{RESET}")
                            aciertos_tanques_defensor += 1
                            agrupar_funciones_defensor()
                            break

                        elif invasor[fila][columna] == "cazador":
                            print(f"{RED}{BOLD}Mensaje: {RESET}{MAGENTA}le has dado a un cazador! y se te ha restado 1 municion por el acierto!{RESET}")
                            aciertos_cazador_defensor += 1
                            agrupar_funciones_defensor()
                            break

                        elif invasor[fila][columna] == "submarino":
                            print(f"{RED}{BOLD}Mensaje: {RESET}{MAGENTA}le has dado a un submarino! y se te ha restado 1 municion por el acierto!{RESET}")
                            aciertos_submarinos_defensor += 1
                            agrupar_funciones_defensor()
                            break

                        elif invasor[fila][columna] == "destructor":
                            print(f"{RED}{BOLD}Mensaje: {RESET}{MAGENTA}le has dado a un destructor! y se te ha restado 1 municion por el acierto!{RESET}")
                            aciertos_destructor_defensor += 1
                            agrupar_funciones_defensor()
                            break

                        elif invasor[fila][columna] == "buque":
                            print(f"{RED}{BOLD}Mensaje: {RESET}{MAGENTA}le has dado a un buque de guerra! y se te ha restado 1 municion por el acierto!{RESET}")
                            aciertos_buque_defensor += 1
                            agrupar_funciones_defensor()
                            break

                        elif invasor[fila][columna] == "fragata":
                            print(f"{RED}{BOLD}Mensaje: {RESET}{MAGENTA}le has dado a un fragata! y se te ha restado 1 municion por el acierto!{RESET}")
                            aciertos_fragata_defensor += 1
                            agrupar_funciones_defensor()
                            break
                    else:
                        print(f"{RED}{BOLD}Error:{RESET}{YELLOW} el valor de las filas y columnas debe estar entre 0 y {filas_invasor - 1}!")
                        print(f"intentemos de nuevo! :) {RESET}")
                except ValueError:
                    print(f"{RED}{BOLD}Error:{RESET}{YELLOW} no puede estar vacio o con valores alfabeticos!")
                    print(f"intentemos de nuevo! :){RESET}")
            break









def Menu_principal():
    global consulta
    consulta = 0
    while True:
        try:
            print(f"\n{BOLD}{BLUE}-----Menu Principal-----{RESET}")
            print(f"\n{BOLD}{YELLOW}1.{RESET}leer las reglas")
            print(f"{BOLD}{YELLOW}2.{RESET}empezar juego")
            print(f"{BOLD}{YELLOW}3.{RESET}records de jugadores")
            print(f"{BOLD}{YELLOW}4.{RESET}creditos")
            print(f"{BOLD}{YELLOW}5.{RESET}Mostrar tableros")
            print(f"{BOLD}{YELLOW}6.{RESET}salir")
            opcion = int(input(f"\n{BOLD}{GREEN}seleccione una opcion: {RESET}"))
            if opcion == 1:
                reglas()
            elif opcion == 2:
                consulta = 1
                invasor_aleatorio()
                defensor_aleatorio()
                generador_estadisticas()
                nombre_de_jugadores()
                ejecutar_juego()
            elif opcion == 3:
                if consulta == 1:
                    estadisticas_finales()
                elif consulta == 0:
                    print(f"{RED}{BOLD}Aviso:{RESET}{YELLOW} no hay estadisticas para mostrar!{RESET}")
                    print(f"{RED}{BOLD}Mensaje:{RESET}{YELLOW} porfavor juegue para que se generen estadisticas conforme vaya jugando, gracias y buena suerte!{RESET}")
                    abandonar_menu_principal()
            elif opcion == 4:
                print(f"{RED}{BOLD}Mensaje: {RESET}{CYAN}{BOLD}algoritmo creado por Donald Miranda con muchisima dedicacion, gracias por jugar a Guerra de Mundos!{RESET}")
                stop.system("pause")
            elif opcion == 5:
                if consulta == 1:
                    mostrar_invasor()
                    mostrar_defensor()
                    stop.system("pause")
                elif consulta == 0:
                    print(f"{RED}{BOLD}Mensaje:{RESET}{YELLOW} No puedes ver los tableros antes de jugar, tramposo!{RESET}")
                    abandonar_menu_principal()
            elif opcion == 6:
                break

        except ValueError:
            print(f"{RED}no puede dejar el espacio vacio o ingresar caracteres alfabeticos!{RESET}")

def mostrar_invasor():
    print("invasor")
    for fila in invasor:
        print(fila)

def mostrar_defensor():
    print("defensor")
    for fila in defensor:
        print(fila)

if __name__ == "__main__":
    Menu_principal()


