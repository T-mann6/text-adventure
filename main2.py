kniv = 1
liv = 100

def newgame():
    print("game over")
    global liv, kniv
    kniv = 1
    liv = 100
    print("vil du starte på nytt")
    valg = input("Ja:, Nei:")
    if valg == "Ja":
        startplace()

    else:
        exit()

def startplace():
    print("Du går i skogen og ser en bjørn")
    print("Hva gjør du?")
    
    asking = True
    while asking == True:
        valg1 = input("A: ignorer bjørnen, B: slåss -> ")

        if valg1 == "A":
            asking = False
            vann1a()

        elif valg1 == "B":
            asking = False
            vann1b()

        else:
            print("fant ikke ut hva du svarte")

def vann1a():                                                                                                     
    print("Du ignorerer bjørnen og går videre")
    print("Etter 15 minutter treffer du på et vann")
    print("Hva gjør du? ")
    
    asking = True
    while asking == True:
        valg2 = input("A: svømm gjennom, B: gå rundt -> ")
        if valg2 == "A":
            asking = False
            sykehus1a()

        elif valg2 == "B":
            asking = False
            vann2a()

        else:
            print("fant ikke ut hva du svarte")

def sykehus1a():
    global liv
    liv -= 50
    print(" Du svømte gjennom vannet og kom til den andre siden.")
    if liv < 60:
        print("Helikopter kommer og henter deg. Du blir fraktet til sykehuset")
        print("Noen dager etter får du dra hjem, det er fint vær og du lurer på om du skal på tur igjen")
        newgame()

def vann2a():
    print("Du gikk rundt vannet, men kom alltid tilbake til samme plass")
    print("Hva gjør du nå?")
    
    asking = True
    while asking == True:
        valg3 = input("A: Svømm gjennom, B: Bli i skogen -> ")
        if valg3 == "A":
            asking = False
            sykehus2a()

        elif valg3 == "B":
            asking = False
            vann3a()

        else:
            print("fant ikke ut hva du svarte")

def sykehus2a():
    global liv
    liv -= 50
    print("Du svømte gjennom og mistet pusten delvis gjennom, kom til den andre siden.")
    if liv < 60:
        print("Helikopter kommer og henter deg. Du blir fraktet til sykehuset")
        print("Noen dager etter får du dra hjem, det er fint vær og du lurer på om du skal på tur igjen")
        newgame()

def vann3a():
    global liv
    print("Du blir i skogen.")
    liv -= 100
    if liv <1:
        print("Du døde i skogen")
        newgame()

def vann1b():
    global kniv
    kniv -= 1
    print("Du går i kamp mot bjørnen og dreper den, men kniven blir ødelagt i kampen, du går videre.")
    print("Etter 15 minutter treffer du på et vann")
    print("Hva gjør du?")
    
    asking = True
    while asking == True:
        valg2 = input("A: svømm gjennom, B: gå rundt -> ")
        if valg2 == "A":
            asking = False
            sykehus1b()

        elif valg2 == "B":
            asking = False
            vann2b()

        else:
            print("fant ikke ut hva du svarte")


def sykehus1b():
    global liv
    liv -= 50
    print(" Du svømte gjennom vannet og kom til den andre siden.")
    if liv < 60:
        print("Helikopter kommer og henter deg. Du blir fraktet til sykehuset")
        print("Noen dager etter får du dra hjem, det er fint vær og du lurer på om du skal på tur igjen")
        newgame()

def vann2b():
    print("Du gikk rundt vannet, men kom alltid tilbake til samme plass")
    print("Hva gjør du nå?")
    
    asking = True
    while asking == True:
        valg3 = input("A: Svømm gjennom, B: Bli i skogen -> ")
        if valg3 == "A":
            asking = False
            sykehus2b()

        elif valg3 == "B":
            asking = False
            vann3b()

        else:
            print("fant ikke ut hva du svarte")

def sykehus2b():
    global liv
    liv -= 50
    print("Du svømte gjennom og mistet pusten delvis gjennom, kom til den andre siden.")
    if liv < 60:
        print("Helikopter kommer og henter deg. Du blir fraktet til sykehuset")
        print("Noen dager etter får du dra hjem, det er fint vær og du lurer på om du skal på tur igjen")
        newgame()

def vann3b():
    global liv
    print("Du blir i skogen.")
    liv -= 100
    if liv <1:
        print("Du døde i skogen")
        newgame()




startplace()