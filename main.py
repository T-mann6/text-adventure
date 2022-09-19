kniv = 1
liv = 100
navn = input("Hva heter du? -> ")


print("velkommen " + navn)
print("Du går i skogen og ser en bjørn")
print("Hva gjør du", navn, "?")
valg1 = input("A: ignorer bjørnen, B: slåss -> ")

if valg1 == "A":
    print("Du ignorerer bjørnen og går videre")
    print("Etter 15 minutter treffer du på et vann")
    print("Hva gjør du", navn, "?")
    valg2 = input("A: svømm gjennom, B: gå rundt -> ")
    
    if valg2 == "A":
        liv -= 50
        print(" Du svømte gjennom vannet og kom til den andre siden.")
        if liv < 60:
            print("Helikopter kommer og henter deg. Du blir fraktet til sykehuset")
            print("Noen dager etter får du dra hjem, det er fint vær og du lurer på om du skal på tur igjen")

    elif valg2 == "B":
        print("Du gikk rundt vannet, men kom alltid tilbake til samme plass")
        print("Hva gjør du nå", navn, "?")
        valg3 = input("A: Svømm gjennom, B: Bli i skogen -> ")

        if valg3 == "A":
            liv -= 50
            print("Du svømte gjennom og mistet pusten delvis gjennom, kom til den andre siden.")
            if liv < 60:
                print("Helikopter kommer og henter deg. Du blir fraktet til sykehuset")

        elif valg3 == "B":
            print("Du blir i skogen.")
            liv -= 100
            if liv <1:
                print("Du døde i skogen")
                exit()
        else:
            print("fant ikke ut hva du valgte")
    else:
        print("fant ikke ut hva du valgte")

elif valg1 == "B":
    kniv -= 1
    print("Du går i kamp mot bjørnen og dreper den, men kniven blir ødelagt i kampen, du går videre.")
    print("Etter 15 minutter treffer du på et vann")
    print("Hva gjør du", navn + "?")
    valg2 = input("A: svømm gjennom, B: gå rundt -> ")
    
    if valg2 == "A":
        liv -= 50
        print(" Du svømte gjennom vannet og kom til den andre siden.")
        if liv < 60:
            print("Helikopter kommer og henter deg. Du blir fraktet til sykehuset")
            print("Noen dager etter får du dra hjem, det er fint vær og du lurer på om du skal på tur igjen")

    elif valg2 == "B":
        print("Du gikk rundt vannet, men kom alltid tilbake til samme plass")
        print("Hva gjør du nå", navn, "?")
        valg3 = input("A: Svømm gjennom, B: Bli i skogen -> ")

        if valg3 == "A":
            liv -= 50
            print("Du svømte gjennom og mistet pusten delvis gjennom, kom til den andre siden.")
            if liv < 60:
                print("Helikopter kommer og henter deg. Du blir fraktet til sykehuset")

        elif valg3 == "B":
            print("Du blir i skogen.")
            liv -= 100
            if liv <1:
                print("Du døde i skogen")
                exit()
        else:
            print("fant ikke ut hva du valgte")
    else:
        print("fant ikke ut hva du valgte")
else:
    print("fant ikke ut hva du valgte")