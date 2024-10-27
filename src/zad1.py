punkty = int(input("Podaj liczbe zdobytych punktów: "))
if punkty > 80:
    print("Zaliczony w terminie 0")
elif punkty >= 50 :
    print("Możesz poprawić egzamin.")
else:
    print("Musisz poprawić egzamin")