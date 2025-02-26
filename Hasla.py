import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    x = bcrypt.hashpw(password.encode(), salt).decode()  # Hashowanie i dekodowanie
    return x

def zapisywanie(x, filename="hasla.txt"):
    with open(filename, "wt") as plik_zapis:
        plik_zapis.write(x + "\n")

def otwieranie(filename="hasla.txt"):
    with open(filename, "r") as plik_odczyt:
        return plik_odczyt.readline().strip()

def sprawdzanie(x):
    do_sprawdzenia = input("Podaj swoje hasło: ")
    zapisane_haslo = otwieranie()
    if bcrypt.checkpw(do_sprawdzenia.encode(), zapisane_haslo.encode()):
        print("Hasło zgodne! \n")
    else:
        print("Hasło niezgodne!")

class Konto:
    def __init__(self,login, haslo):
        self.login = login
        self.haslo = haslo

def tworzenie_konta():
    global x
    login = input("Login: ")
    haslo = input("Haslo: ")
    haslo2 = input("podaj haslo ponownie: ")
    if haslo == haslo2:
        uzytkownik = Konto(login, haslo)
        print(uzytkownik.login, uzytkownik.haslo)
        x = uzytkownik.haslo
    else:
        print("haslo nieprawidłowe, spróbuj jeszcze raz")
        tworzenie_konta()

def menu():
    global x
    while True:
        print("\n1: Zmiana Hasla")
        print("2: Hashowanie hasla")
        print("3: Zapisywanie do pliku")
        print("4: Sprawdzanie Hasla ")
        print("5: Wyjście \n")
        wybor2 = int(input("Podaj co chcesz zrobic "))
        match wybor2:
            case 1:
                x = input("Podaj hasło do zapisania: ")
                zapisywanie(x)
            case 2:
                x = hash_password(x)
                print('Haslo zahashowane')
                print("Twoje zahashowane hasło to:", x)
            case 3:
                zapisywanie(x)
                print('Haslo zapisane \n')
            case 4:
                sprawdzanie(x)
                print('SPRAWDZENIE HASLA ...')
            case 5:
                exit()

print("=============== Witaj w menedżerze hasel ===============")
print('1. Aby stworzyc konto ')
print('2. Aby sie zalogować ')
print('3. Aby sie wyjść ')

while True:
    wybor1 = input(('Wybierz co chcesz zrobić : '))
    if wybor1 == '1':
        tworzenie_konta()
        menu()
    elif wybor1 == '2':
        print("Tuaj bedzie logowanie")
        menu()
    elif wybor1 == '3':
        break
    else:
        print("NIPRAWIDLOWY WYBOR ! \nSPRÓBUJ JESZCZE RAZ")
