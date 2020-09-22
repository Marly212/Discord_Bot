import discord
import requests

async def BronzeBravery(message):

    try:
        champ = message.content.split(" ")[1]

        champID = getChampID(champ)

        role = message.content.split(" ")[2]

        if role.lower() == "top" :
            role = 0

        elif role.lower() == "jgl" :
            role = 1

        elif role.lower() == "mid" :
            role = 2

        elif role.lower() == "adc" :
            role = 3

        elif role.lower() == "supp" :
            role = 4
        #parameter = {"map":11,"level":10,"language":"en","roles":[0,2,3,4],"champions":[266,103,84,12,32,34,1,523,136,268,432,53,63,201,51,164,69,31,42,122,131,119,36,245,60,28,81,9,114,105,3,41,86,150,79,104,120,74,420,39,427,40,59,24,126,202,222,145,429,43,30,38,55,10,141,85,121,203,240,96,7,64,89,876,127,236,117,99,54,90,57,11,21,62,82,25,267,75,111,518,76,56,20,2,61,516,80,78,555,246,133,497,33,421,58,107,92,68,13,113,235,875,35,98,102,27,14,15,72,37,16,50,517,134,223,163,91,44,17,412,18,48,23,4,29,77,6,110,67,45,161,254,112,8,106,19,498,101,5,157,777,83,350,154,238,115,26,142,143]}

        #Roles: 0 = Top 1 = Mid 2 = JGL 3 = ADC 4 = Supp 

        parameter = {"map":11,"level":30,"language":"en","roles":[role],"champions":[champID]}

        #r = requests.post("https://api.ultimate-bravery.net/bo/api/ultimate-bravery/v1/dataset",data=parameter)

        r = requests.post("https://api.ultimate-bravery.net/bo/api/ultimate-bravery/v1/dataset", json=parameter)

        js = r.json()

        print(r)




    except Exception as e:
            print(e) 



def getChampID(champ):
    if champ.lower() == "atrox":
        return 266

    if champ.lower() == "ahri":
        return 103

    if champ.lower() == "akali":
        return 84

    if champ.lower() == "alistar":
        return 12

    if champ.lower() == "amumu":
        return 32

    if champ.lower() == "anivia":
        return 34

    if champ.lower() == "annie":
        return 1

    if champ.lower() == "aphelios":
        return 523

    if champ.lower() == "ashe":
        return 22

    if champ.lower() == "aurelion sol":
        return 136

    if champ.lower() == "azir":
        return 268

    if champ.lower() == "bard":
        return 432

    if champ.lower() == "blitzcrank":
        return 53

    if champ.lower() == "brand":
        return 63
    

