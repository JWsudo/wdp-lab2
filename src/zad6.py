wejscie = input("Podaj litere:")

znak = ord(wejscie[0])
if (znak >= 65 and znak <= 90):
    print("Duża")
elif(znak >= 97 and znak <=122):
    print("Mała")
else:
    print("To nie jest litera!")