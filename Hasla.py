import bcrypt
import json

dane_konta ={}

def hash_password(password):
    salt = bcrypt.gensalt()
    x = bcrypt.hashpw(password.encode(), salt).decode()  # Hashowanie i dekodowanie
    dane_konta["Haslo"] = x
    return x

def zapisywanie():
    with open('dane.json', 'r') as file: #otwieranie pliku
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

def sprawdzanie_loginu():
    login_do_sprawdzenia = input("Podaj swój login: ")
    with open('dane.json', 'r') as file:
        users = json.load(file)
        for user in users:
            if user.get("Login") != login_do_sprawdzenia:
                continue
            else:
                print("Login prawidłowy")
                print(user)
                users.remove(user)
                with open('dane.json', 'w') as file:
                    json.dump(users, file, indent=4)
                return True

def usuwanie_danych_z_pliku():
    usuwanie_danych_z_pliku = input("Podaj swój login: ")
    with open('dane.json', 'r') as file:
        users = json.load(file)
        for user in users:
            if user.get("Login") != usuwanie_danych_z_pliku:
                continue
            else:
                print("Login prawidłowy")
                do_sprawdzenia = input("Podaj Haslo do swojego konta")
                print(user)
                zapisane_haslo = user.get("Haslo")
                if bcrypt.checkpw(do_sprawdzenia.encode(), zapisane_haslo.encode()):
                    users.remove(user)
                    with open('dane.json', 'w') as file:
                        json.dump(users, file, indent=4)
                    return True
                else:
                    return False

class Konto:
    def __init__(self,login, haslo):
        self.login = login
        self.haslo = haslo

def tworzenie_konta():
    login = input("Login: ")
    with open('dane.json', 'r') as file:
        users = json.load(file)
        if any(user.get("Login") == login for user in users):
            print("Konto z takim Loginem już istnieje \nSPRÓBUJ UŻYĆ INNEGO LOGINU \n")
            return tworzenie_konta()

        else:
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

def logowanie():
    login = input("Login: ")
    with open('dane.json', 'r') as file:
        users = json.load(file)
        user = next((u for u in users if u.get("Login") == login), None)

        if not user:
            print("Login nie istnieje!")
            return  # Jeśli login nie został znaleziony, kończymy funkcję

        do_sprawdzenia = input("Hasło: ")
        zapisane_haslo = user.get("Haslo")

        if bcrypt.checkpw(do_sprawdzenia.encode(), zapisane_haslo.encode()):
            dane_konta["Login"] = login
            dane_konta["Haslo"] = zapisane_haslo
            zapisywanie()
            print("Poprawne dane ")
            print("ZALOGOWANO ")
        else:
            print("Niepoprawne hasło!")
            exit()  # Kończymy program po złym haśle


def menu():
    global x
    while True:
        print("\n1: Zmiana Hasla")
        print("2: Sprawdzanie Hasla")
        print("3: Zmiana Loginu ")
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
                sprawdzanie_hasla()
                print('Haslo zapisane \n')

            case 3:
                print("Tutaj bedzie zmiana loginu")
                if sprawdzanie_loginu():
                    nowy_login_do_zmiany = input("Podaj nowe login: ")
                    dane_konta["Login"] = nowy_login_do_zmiany
                    zapisywanie()
                else:
                    print("Login nieprawidlowy")

            case 4:
                print('========================== USUWANIE KONTA ==========================\n')
                if usuwanie_danych_z_pliku():
                    print("Konto zostało poprawnie usunięte")
                    exit()
                else:
                    print("\n Podałeś nieprawidlowe dane ! ")
                    menu()
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
        logowanie()
        menu()
    elif wybor1 == '3':
        break
    else:
        print("NIPRAWIDLOWY WYBOR ! \nSPRÓBUJ JESZCZE RAZ")

#Dodainie dodatkowego sposobu uwierzytelniania
#Zastąpienie powtarzająego sie kodu funkcjami.