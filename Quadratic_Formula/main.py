

if __name__ == '__main__':

    total = 0
    menu = {}
    comanda = []
    platosInexistentes = []
    billetes = {"quinientos": 0, "doscientos": 0, "cien": 0, "cincuenta": 0, "veinte": 0, "diez": 0, "cinco": 0}
    monedas = {"dos": 0, "un": 0, "cincuenta céntimos": 0, "veinte céntimos": 0, "diez céntimos": 0,
                   "cinco céntimos": 0, "dos céntimos": 0, "un céntimo": 0}
    continuar = True

    platosMenu = int(input("¿Cuántos platos quieres en el menú? "))

    for x in range(platosMenu):
        plato = input("Nombre del plato: ")
        precio = float(input("Precio del plato: "))
        menu[plato] = precio

    while continuar:

        for key in menu:
            print(key, "---", menu[key])

        pedido = input("Que quieres para comer? ")
        comanda.append(pedido)
        continuarComprando = True

        while continuarComprando:
            seguir = input("Quieres segir comprando? Si/No ")
            if seguir == "No":
                continuar = False
                continuarComprando = False
            elif seguir == "Si":
                continuarComprando = False
            else:
                print("Has de escribir Si o No.")

    for comida in comanda:
        if comida in menu:
            total += menu[comida]
        else:
            platosInexistentes.append(comida)
            print("El plato", comida, "no existe.")

    for platoInexistente in platosInexistentes:
        comanda.remove(platoInexistente)
    print("Precio final: ", total)
    while total != 0:
        if total >= 500:
            billetes["quinientos"] += 1
            total -= 500
        elif total >= 200:
            billetes["doscientos"] += 1
            total -= 200
        elif total >= 100:
            billetes["cien"] += 1
            total -= 100
        elif total >= 50:
            billetes["cincuenta"] += 1
            total -= 50
        elif total >= 20:
            billetes["veinte"] += 1
            total -= 20
        elif total >= 10:
            billetes["diez"] += 1
            total -= 10
        elif total >= 5:
            billetes["cinco"] += 1
            total -= 5
        elif total >= 2:
            monedas["dos"] += 1
            total -= 2
        elif total >= 1:
            monedas["un"] += 1
            total -= 1
        elif total >= 0.5:
            monedas["cincuenta céntimos"] += 1
            total -= 0.5
        elif total >= 0.2:
            monedas["veinte céntimos"] += 1
            total -= 0.2
        elif total >= 0.1:
            monedas["diez céntimos"] += 1
            total -= 0.1
        elif total >= 0.05:
            monedas["cinco céntimos"] += 1
            total -= 0.05
        elif total >= 0.02:
            monedas["dos céntimos"] += 1
            total -= 0.02
        elif total >= 0.01:
            monedas["un céntimo"] += 1
            total -= 0.01
        else:
            total = 0

    textoFinal = "Has de pagar con "
    for billete in billetes:
        if billetes[billete] > 0:
            textoFinal += format(billetes[billete])+" de "+format(billete)+" "

    for moneda in monedas:
        if monedas[moneda] > 0:
            textoFinal += format(monedas[moneda])+" de "+format(moneda)+" "
    print(textoFinal)