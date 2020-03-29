import requests,os
import json

def banner():
    os.system("clear")
    print("""
        Author = IMAM BARMAWI
        Code   = PYTHON 3
        Date   = 29 MARET 2020
        API    = https://kawalcorona.com
    """)
    
def corona():
    banner()
    negara = input("masukkan negara : ")
    url = requests.get('https://api.kawalcorona.com/'+negara).text
    cok = json.loads(url)
    print("="*30)
    print("NEGARA    = ", cok[0]['name'])
    print("POSITIF   = ", cok[0]['positif'])
    print("SEMBUH    = ", cok[0]['sembuh'])
    print("MENINGGAL = ", cok[0]['meninggal'])
    print("="*30)
    
corona()