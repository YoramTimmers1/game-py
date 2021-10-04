#BEGIN TEXT
print("+-------------------------------------------------------------------------------------------------+")
print("Hey gaat alles goed?")
print("Je bent zojuist flauwgevallen en word wakker en herrinert je dat je opweg bent naar de eindbaas")
print("Je groep helpt je omhoog maar je bent vergeten welke class je bent")
print("Dus je vraagt aan je groep welke class je bent")

# JE CLASS KEUZE

KiesjeClass = input("Kies je Class |Warrior, Mage en Support| :")

# CLASS WARRIOR

if KiesjeClass == "warrior":
    print("Je hebt de Warrior class gekozen")
    print("Je groep vertelt dat je de Warrior class bent en je staat op en team zegt dat ze weer verder gaan lopen naar de eindbass ")
    GaJeMee = input("""Je vertrouwd het niet helemaal en je maakt een besluit (Je kunt kiezen tusseneen paar antwoorden) |gamee renweg of blijfstaan|  """)

# KEUZE 1 Ga je mee

    if GaJeMee == "gamee":
        print("je besluit om mee te gaan met de groep en herrinert je dat ze echt je teamates zijn en jullie gaan op weg naar de eindbaas")
        print("jullie gaan naar de eindbaas maar jullie komen hoge lvl wolven tegen")

    elif GaJeMee == "renweg":
        print("Je besluit om weg te rennen want je vertrouwd het niet helemaal maar je bent erachter gekomen dat het niet de goeien keuze was en gaat dood door high level monsters")
        print("u died")
    else:
        print("je blijft staan en je teamates laten je achter er en komen andere groepen aan die ook naar de einbaas willen gaan en komen tegen en vermoorden je voor loot ")
        print("u died")

#andere classes behanndel later

elif KiesjeClass == "mage":
    print("je hebt de Mage class gekozen")
else:
    ("je hebt de Support class gekozen")


