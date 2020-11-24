from virustotal_python import Virustotal
from pprint import pprint
import hashlib
import discord
import time


async def vcheck(message):
    
    vtotal = Virustotal("e4fe0679f47c487ccf166f1e2602901da454ad98b8d5ea27b41b20a876093ae8")

    mess = message.clean_content

    mess = mess.split(".check ")[1]

    website = mess

    if mess.startswith('http'):    

        #Message in Byte Code umwandel fürs Hashen
        mess = str.encode(mess)

        #Neuer Has sha256 erstellen
        hash = hashlib.new('sha256')

        #Haswert von Varible mess erstellen
        hash.update(mess)

        #hash.hexdigest() aktueller Hash code

        #resp = vtotal.file_scan(".\\VirusTotal.py")

        #resp = vtotal.file_report([hash.hexdigest()])

        hashWert = hash.hexdigest()

        resp = vtotal.url_report([hashWert])

        if resp['json_resp']["response_code"] == 1:
            print("Webseite kann abgerufen werden")
            if resp['json_resp']["positives"] == 0:
                await message.channel.send("Webseite sicher")
            else:
                await message.channel.send("Webseite nicht sicher")

        elif resp['json_resp']["response_code"] == 0:
            print("Webseite wurde noch nicht gescannt")
            resp2 = vtotal.url_scan(website)
            await message.channel.send("Webseite wurde noch nicht gescannt. Beginne Scanning bitte warte")
            status = 0
            status2 = 0
            while status == 0:
                if status2 == 0:
                    resp2 = vtotal.url_report([hashWert])
                    status2 = 1
                else:
                    resp2 = vtotal.url_scan(website)
                    if resp2['json_resp']["response_code"] == 0:
                        time.sleep(5)
                    elif resp2['json_resp']["response_code"] == -2:
                        time.sleep(5)
                    elif resp2['json_resp']["response_code"] == 1:
                        await message.channel.send("Webseite sicher")
                        status = 1
            


        elif resp['json_resp']["response_code"] == -2:
            print("Webseite wird noch gescannt, bitte warten Sie")
            await message.channel.send("Webseite wird noch gescannt, bitte warten Sie")


            

        #response_code:   0 = Wenn gesucht und nichts gefunden wurde   -2 = Gesendete Item wird noch gescannt     1 = Item ist da und kann erhalten werden

    