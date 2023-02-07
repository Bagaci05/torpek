torpek = ["hapci","vidor","szundi"]
magassagok = [101,105,102]

run = 0

while run == 0:
    option = int(input("Válasszon egy számot:\n1. Törpék listázása\n2. Legalacsonyabb törpe\n3. Legmagasabb törpe\n4. Törpe hozzáadása\n5. Kilépés\n: "))
    if option == 1:
        index = 0
        while index < len(torpek):
            print(torpek[index])
            index += 1
    #2. Legalacsonyabb törpe
    if option == 2:
        index = 0
        min = magassagok[0]
        while index < len(magassagok):
            if magassagok[index] < min:
                min = magassagok[index]
            index += 1
        print("A legalacsonyabb törpe: ", min)

    #3. Legmagasabb törpe
    if option == 3:
        index = 0
        max = magassagok[0]
        while index < len(magassagok):
            if magassagok[index] > max:
                max = magassagok[index]
            index += 1
        print("A legmagasabb törpe: ", max)
    
    if option == 4:
        torp = input("Add meg a törpének a nevét: ")
        magassag = int(input("Add meg a törpének a magasságát: "))
        torpek.append(torp)
        magassagok.append(magassag)
    
    if option == 5:
        run = 1

