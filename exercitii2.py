import turtle

#Exerictiul 1
print("--- Aplicația mea ---")
nume = input("Cum te cheamă? ")
print(f"Salut, {nume}! Bine ai venit.")

#Exerictiul 2
scor_str = input("Introdu un scor de la 1 la 10: ")
scor = int(scor_str)
print(f"Dacă dublăm scorul, obținem {scor * 2}.")
if scor % 2 == 0:
    print("Ai introdus un număr par.")
else:
    print("Ai introdus un număr impar.")

#Exerictiul 3
scor = int(input("Introdu un scor de la 1 la 5: "))
if scor > 5:
    print("Bravo!")
elif scor == 4 or scor == 3:
    print("Aproape!")
else:
    print("Mai încearcă!")

#Nivelul 2
#Exercitiul 1
x = input("Mai încerci? (da/nu)")
while x.lower()=="da":
    x = input("Mai încerci? (da/nu)")
    if x.lower()=="nu":
        break

#Exercitiul 2 

import turtle

#Exerictiul 1
print("--- Aplicația mea ---")
nume = input("Cum te cheamă? ")
print(f"Salut, {nume}! Bine ai venit.")

#Exerictiul 2
scor_str = input("Introdu un scor de la 1 la 10: ")
scor = int(scor_str)
print(f"Dacă dublăm scorul, obținem {scor * 2}.")
if scor % 2 == 0:
    print("Ai introdus un număr par.")
else:
    print("Ai introdus un număr impar.")

#Exerictiul 3
scor = int(input("Introdu un scor de la 1 la 5: "))
if scor > 5:
    print("Bravo!")
elif scor == 4 or scor == 3:
    print("Aproape!")
else:
    print("Mai încearcă!")

#Nivelul 2
#Exercitiul 1
x = input("Mai încerci? (da/nu)")
while x.lower()=="da":
    x = input("Mai încerci? (da/nu)")
    if x.lower()=="nu":
        break

#Exercitiul 2 
ecran = turtle.Screen()                                                                                                                                                                                        
t = turtle.Turtle()                                                                                                                                                                                            
t.shape("turtle")                                                                                                                                                                                              
t.color("blue")                                                                                                                                                                                                
while True:
    x = input("Vrei sa se opreasca? (da/nu): ")
    if x.lower() == "da":
        break                                                                                                                                                                                                    
    turtle.clear()                                                                                                                                                                                             
    for i in range(4):                                                                                                                                                                                         
        turtle.forward(100)                                                                                                                                                                                    
        turtle.left(10)                                                                                                                                                                                        
        break                                                                                                                                                                                                  
        turtle.left(20)                                                                                                                                                                                                                                                                                                                                                                                        
turtle.bye()

#Exercitiul 3
rezultate = []
print("Introdu rezultatele sau numele pe rând.")
print("Când ai terminat, scrie cuvântul 'stop'.")
print("-" * 30)
while True:
    intrare = input("Introdu o valoare: ")
    if intrare.lower() == 'stop':
        break
    rezultate.append(intrare)
numar_elemente = len(rezultate)
print("\n" + "=" * 30)
print(f"Ai salvat {numar_elemente} elemente în listă:")
for element in rezultate:
    print(f"{element}")

#Nivelul 3
#Exercitiul 1
def saluta(nume):
    return f"Salut, {nume}! Bine ai venit."

def calculeaza(a, b):
    return a + b

nume_utilizator = input("Cum te cheamă? ")
mesaj = saluta(nume_utilizator)
print(mesaj)

primul_numar = int(input("Introdu primul număr: "))
al_doilea_numar = int(input("Introdu al doilea număr: "))
rezultat = calculeaza(primul_numar, al_doilea_numar)
print(f"Suma lor este {rezultat}")
#Exercitiul 2
def porneste_jocul():
    print("Jocul a pornit!")
def afiseaza_scor():
    print("Scorul tău este 100.")
def afiseaza_setari():
    print("Setările au fost deschise.")
while True:
    print("1. Joacă")
    print("2. Vezi scorul")
    print("3. Setări")
    print("0. Ieșire")
    alegere = input("Alege o opțiune: ")
    if alegere == "1":
        porneste_jocul()
    elif alegere == "2":
        afiseaza_scor()
    elif alegere == "3":
        afiseaza_setari()
    elif alegere == "0":
        print("La revedere!")
        break
    else:
        print("Opțiune invalidă!")
#Exercitiul 3
numere_salvate = []
while True:
    intrare = input("Introdu un număr (sau 'stop' pentru ieșire): ")
    if intrare == "stop":
        break
    if intrare.isdigit():
        numar = int(intrare)
        if numar not in numere_salvate:
            numere_salvate.append(numar)
            print(f"Numărul {numar} a fost adăugat cu succes.")
        else:
            print("Acest număr există deja. Nu a fost adăugat.")
    else:
        print("Ceea ce ai introdus nu este un număr. Încearcă din nou.")
print("Lista finală este:")
print(numere_salvate)
