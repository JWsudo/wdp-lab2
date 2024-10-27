with open("../resources/notowania_gieldowe.txt", "r") as file:
    for line in file:
        print(line)

file = open("../resources/notowania_gieldowe.txt", "a")
file.write("\nALR, 123")
file.close()
with open("../resources/notowania_gieldowe.txt", "r") as file:
    for line in file:
        print(line)