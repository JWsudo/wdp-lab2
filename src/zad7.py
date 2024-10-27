haslo = 'pk47!jy0893'
hasSpecialChar = False

for char in haslo:
    if(ord(char) == 33):
        hasSpecialChar = True
if(len(haslo) >= 11 and hasSpecialChar):
    print("Haslo poprawne")
else:
    print("Haslo niepoprawne")
    