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
scor = input("Introdu un scor de la 1 la 5: ")
if scor > 5:
    print("Bravo!")
elif scor == 4 or scor == 5:
    print("Aproape!")
else:
    print("Mai încearcă!")

#Nivelul 2
#Exercitiul 1
while x.lowercase()=="da":
    print("Mai încerci? (da/nu)")
    if x.lowercase()=="nu":
        break

#Exercitiul 2 
ecran = turtle.Screen()                                                                                                                                                                                        
t = turtle.Turtle()                                                                                                                                                                                            
t.shape("turtle")                                                                                                                                                                                              
t.color("blue")                                                                                                                                                                                                
while True:                                                                                                                                                                                                    
    turtle.clear()                                                                                                                                                                                             
    for i in range(4):                                                                                                                                                                                         
        turtle.forward(100)                                                                                                                                                                                    
        turtle.left(10)                                                                                                                                                                                        
        break                                                                                                                                                                                                  
    turtle.left(20)                                                                                                                                                                                                                                                                                                                                                                                        
turtle.bye()

scor = int(input("Introdu un scor: "))
print(f"Ai introdus: {scor}")
    
raspuns = input("Mai încerci? (da/nu) ")
if raspuns.lower() != "da":
    print("La revedere!")
    break
