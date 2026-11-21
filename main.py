game_active = False
keuze_laag_1 = "0"
while game_active == False:
    print("-----------------------------------------------------")
    print("Welkom bij .... spel")
    print("Dit spel werkt als volgt ...")
    print("-----------------------------------------------------")
    print("Wilt u beginnen?")
    start_game = input("[y/n]: ")
    start_game = start_game.lower()
    if start_game == "y" or start_game == "yes":
        game_active = True
    else:
        print("-----------------------------------------------------")
        print("Wilt u beginnen?")
        start_game = input("[y/n]: ")

while game_active == True:
    print("-----------------------------------------------------")
    print("Je staat in de start kamer, er zijn vier verschillende deuren.")
    print("[Deur 1],     [Deur 3]")
    print("[Deur 2],     [Deur 4]")
    print("-----------------------------------------------------")
    print("Welke deur kies je?")
    while keuze_laag_1 == "0":
        keuze_laag_1 = input("[1, 2, 3 of 4]: ")
        if keuze_laag_1 == "1":
            print("1")
        elif keuze_laag_1 == "2":
            print("2")
        elif keuze_laag_1 == "3":
            print("3")
        elif keuze_laag_1 == "4":
            print("4")
        else:
            print("-----------------------------------------------------")
            print("Ongeldig, kies een van de vier deuren.")
            keuze_laag_1 = input("[1, 2, 3 of 4]: ")