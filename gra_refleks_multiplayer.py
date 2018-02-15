import time

print("KTO MA LEPSZY REFLEKS")
time.sleep(1)

#POWITANIE
print("Witaj, podaj ilosc graczy:")
ile_graczy=int(input())

#TWORZENIE LISTY PRZECHOWUJACEJ GRACZY
imie = []
Rekord = []
for i in range (ile_graczy):
    print("Podaj imie gracza nr {}".format(i+1))
    imie.append(input())

#PRZEDSTAWIENIE GRACZY
print ("W grze bierze udział {} graczy:".format(ile_graczy))
for i in imie:
    print ("%s" %i)
print ("Kazdy ma 3 proby")

#GRA
for i in imie:
    print ("Kolej gracza %s" %i)
    Twoj_Rekord = 1000
    for i in range (3):
        # GENERACJA OPOZNIENIA
        czas = float(time.time() % 3)
        start = 3.0 + czas

        #GAMEPLAY
        print("Wcisnij enter gdy bedziesz gotowy")
        input()
        print("Szykuj sie...")
        time.sleep(czas)
        print("WAL W ENTER!")
        x=time.time()
        input()
        y=time.time()
        z=y-x
        if z==0.0:
            z=100
            print("Za szybko!")
        print ("Twoj czas to {}".format(z))
        Twoj_Czas=z

        #REKORD DANEGO GRACZA
        if Twoj_Czas < Twoj_Rekord:
            Twoj_Rekord=Twoj_Czas
    print ("Twoj najlepszy czas wyniosl %r" %Twoj_Rekord)
    Rekord.append(float(Twoj_Rekord))
#print(Rekord)
Najlepszy_Gracz = imie[0]
Najlepszy_Czas = Rekord[0]
for i in Rekord:
    if i < Najlepszy_Czas:
        Najlepszy_Czas = i
        j=Rekord.index(i)
        Najlepszy_Gracz = imie[j]
print ("Najlepszy gracz to {} z wynikiem {}".format(Najlepszy_Gracz,Najlepszy_Czas))
