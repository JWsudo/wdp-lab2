liczba_goli = int(input("Podaj liczbę bramek:"))
bonus_a = 0
wynik = 0
bonus_b = 0

wynik+=liczba_goli * 10

if(liczba_goli > 5):
    bonus_a += 5
    bonus_b += 5
elif(liczba_goli > 10):
    bonus_a += 10

if(liczba_goli > 10):
    bonus_b+=10

print(f"A: wynik {wynik + bonus_a}")
print(f"B: wynik {wynik + bonus_b}")
