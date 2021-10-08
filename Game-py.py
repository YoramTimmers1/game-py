#begin
print("+-------------------------------------------------------------------------------------------------+")
print("Hey gaat alles goed?")
print("Je bent zojuist flauwgevallen en word wakker en herrinert je dat je opweg bent naar de eindbaas")
print("Je groep helpt je omhoog maar je bent vergeten welke class je bent")
print("Dus je vraagt aan je groep welke class je bent")

# JE CLASS KEUZE

KiesjeClass = input("Kies je Class |Warrior| : ")

# CLASS WARRIOR

if KiesjeClass == "warrior":
    print("Je hebt de Warrior class gekozen")
    print("Je groep vertelt dat je de Warrior class bent en je staat op en het team zegt dat ze weer verder gaan lopen naar de eindbaas ")
    GaJeMee = input("""Je vertrouwd het niet helemaal en je maakt een besluit (Je kunt kiezen tusseneen paar antwoorden) |gamee renweg of blijfstaan| : """)



# KEUZE 1 Ga je mee
    if GaJeMee =="blijfstaan":
        print("je blijft staan en je word achtergelaten door je team je hebt geen eten bij dus je sterft van de honger")
        print("U DIED")
    elif GaJeMee == "renweg":
        print("je rent weg en besluit in een grot te overnachten je valt in slaap en word wakker en je ziet dan dat je word op gegeten door wolven en sterft")
        print("u died")
    else:
        print("je besluit om mee te gaan met de groep en herrinert je dat ze echt je teamates zijn en jullie gaan op weg naar de eindbaas")
        print("jullie gaan naar de eindbaas maar jullie komen hoge level wolven tegen")
        WolvenVechten = input("Wat ga je doen (je hebt keuze uit |Rennen Vechten en Opofferen| : ")    



        #keuze wolvengevecht

        if WolvenVechten == "rennen":
            print("Je rent voor de wolven alleen je bent niet sneller jullie worden in gehaald en de wolven eten jullie op")
            print("u died")

        elif WolvenVechten == "vechten":
            print("Je bent in gevecht gegaan met de wolven en je hebt het gevecht gewonnen")
            print("je loopt verder naar het kasteel van de eindbaas")

            print("je bent bij de eindbaas zijn kasteel gekomen en je loopt naar binnen en start het gevecht")
            eindbaaskeuze = input("je vecht met de eindbaas je hele ateam raakt gewond wat doe je |Vecht, heal of (vraag) je team om hulp| : ")
            if eindbaaskeuze == "vecht":
                print("je besluit om door te vechten maar je bent te zwak en word dood geslagen door de eindbaas")
                print("u died")
                
            elif eindbaaskeuze == "heal":
                    print("je gaat jezelf healen en je team gaat dood omdat je alleen je zelf healed en daarna ga jij dood")
                    print("u died")
                
            elif eindbaaskeuze == "vraag":
                    print("je vraagt om hulp je support healed het hele team en jullie kunnen weer vechten en je verslaat de eindbaas")
                    print("U WON!!!")


        else:
            print("Je overlegt met je team wie je gaat opofferen en jij word gekozen en sterft")
            print("u died")