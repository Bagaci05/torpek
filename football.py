team1 = input("Add meg az első csapat nevét: ")
team2 = input("Add meg a második csapat nevét: ")
team3 = input("Add meg a harmadik csapat nevét: ")
team4 = input("Add meg a negyedik csapat nevét: ")

teams = [team1, team2, team3, team4]
index = 0
while index <= 12:
    print(teams[index % 4], " - ", teams[(index + 1) % 4])
    index += 1