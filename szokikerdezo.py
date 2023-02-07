angolszavak = ["dog", "cat", "mouse", "horse", "cow", "pig", "sheep", "chicken", "duck", "goat"]
magyar = ["kutya", "macska", "egér", "ló", "tehén", "malac", "bárány", "csirke", "kacsa", "kecske"]

run = 0
while run == 0:
    option = int(input("1. Szókikérdezés\n2. Új szó felvitele\n3. Kilépés\n:"))
    #Az 1. pontban kérdezzen rá 5 szó angol megfelelőjére, majd írja ki az elért eredményt százalékosan. A 2. pontban bővítse a szótárt a felhasználó által bevítt új kifejezéssel.
    if option == 1:
        index = 0
        correct = 0
        while index < 5:
            answer = input(angolszavak[index] + ": ")
            if answer == magyar[index]:
                correct += 1
            index += 1
        print("Ön ", correct, " helyes választ adott meg, ez ", correct / 5 * 100, "%")
    if option == 2:
        angol = input("Add meg az új szót angolul: ")
        magyar.append(input("Add meg a magyar megfelelőjét: "))
        angolszavak.append(angol)