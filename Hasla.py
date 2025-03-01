import bcrypt
import json

dane_konta = {}


def hash_password(password):
    salt = bcrypt.gensalt()
    x = bcrypt.hashpw(password.encode(), salt).decode()  # Hashowanie i dekodowanie
    dane_konta["Haslo"] = x
    return x


def zapisywanie():
    with open('dane.json', 'r') as file:  # otwieranie pliku
        users = json.load(file)
        users = [user for user in users if user.get("Login") != dane_konta["Login"]]
        users.append(dane_konta)  # dodawnie nowego uzytkownika do pliku
    with open('dane.json', 'w') as file:
        json.dump(users, file)
    print(users)


def otwieranie():
    with open("dane.json", "r", encoding="utf-8") as file:
        return json.load(file)  # Zwracaj listę użytkowników


def sprawdzanie_hasla():
    otwieranie()  # Wczytaj aktualne dane
    do_sprawdzenia = input("Podaj swoje hasło: ")
    zapisane_haslo = dane_konta["Haslo"]
    print("==== SPRAWDZANIE HASLA.... ====")
    if bcrypt.checkpw(do_sprawdzenia.encode(), zapisane_haslo.encode()):
        print("Hasło zgodne! \n")
        return True
    else:
        print("Hasło niezgodne!")
        return False


class Konto:
    def __init__(self, login, haslo):
        self.login = login
        self.haslo = haslo


def tworzenie_konta():
    otwieranie()
    login = input("Login: ")
    haslo = input("Haslo: ")
    haslo2 = input("podaj haslo ponownie: ")
    if haslo == haslo2:
        dane_konta["Login"] = login
        dane_konta["Haslo"] = haslo
        uzytkownik = Konto(login, haslo)
        print(uzytkownik.login, uzytkownik.haslo)
        hash_password(uzytkownik.haslo)
        zapisywanie()
    else:
        print("haslo nieprawidłowe, spróbuj jeszcze raz")
        tworzenie_konta()


def menu():
    global x
    while True:
        print("\n1: Zmiana Hasla")
        print("2: Zmiana Loginu")
        print("3: Sprawdzanie Hasla ")
        print("4: USUNIĘCIE KONTA ")
        print("5: Wyjście \n")
        wybor2 = int(input("Podaj co chcesz zrobic "))
        match wybor2:
            case 1:

                if sprawdzanie_hasla():
                    nowe_haslo = input("Podaj nowe hasło: ")
                    dane_konta["Haslo"] = nowe_haslo  # Zaktualizuj hasło w słowniku
                    hash_password(dane_konta["Haslo"])
                    zapisywanie()
                    print("Hasło zmienione!")
                else:
                    print("Podałeś niepoprawne hasło")

            case 2:
                print("Tutaj bedzie zmiana loginu")

            case 3:
                sprawdzanie_hasla()
                print('Haslo zapisane \n')

            case 4:
                print(' ========================== USUWANIE KONTA ==========================  \n')

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

# Dodanie aby mozna bylo dodać dużo użytkowników
# Dodanie funkcji logowania
# Sprawdzenie czy taki uzytkownik o takim logniei istnieje jezeli tak to wymus zrobienie innego loginu
# Dodainie dodatkowego sposobu uwierzytelniania