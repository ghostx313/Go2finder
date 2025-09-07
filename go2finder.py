import os
import requests
import phonenumbers
from phonenumbers import geocoder, carrier
from phonenumbers import timezone
from fake_useragent import UserAgent
import whois
import time
import json

class Colours:
    GR = "\033[32m"
    RD = "\033[31m"
    YE = "\033[33m"
    BU = "033[34m"
    MG = "033[35m"

    #bright colours

    BG = "\033[92m"
    BR = "\033[91m"
    BB = "\033[94m"

    #RESET    

    RES = "\033[0m"

    #EFF

    BD = "\033[1m"

def banner():
    print(f"""{Colours.BR} 
    
    
    
    
    

                           .%@@@@@@@@@@@@@@@*                          
                           @@@@@@@@@@@@@@@@@@@@@@@@                    
                        .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*               
                      @@@@@@@@@%%%%%%%%%%%%%%%@@@@@@@@@@@@@            
                    @@@@@@@-=:.:-=*#%%%%%%%%%%%%%%%+@@@@@@@@@@         
                 %@@@@@@=:.       .:*######%%%%%%%%%%=++@@@@@@ @@      
               @@@@@@@=-:           .+#########%%%%%%%===+#@@@@:  @+   
             @@@@@@@==-:.            -*###########%%%%%=-===+@@@@    + 
           @@@@@@@==--:..            -+******==-=###%%%%=--===%@@@     
         *@@@@@@%=--::.#=           .+******+=++=*####%%%.:---==@@@    
        @@@@@@@=--::.. %#=.       .:=****+++*+++**+*###%%%.::--== @@   
       @@@@@@@=--:..  *%%#*+-:..:-++**++*******+**=+**##%%%..::-== %@- 
     +@@@@@@@=-::..   %%%%##***-****++***####*****+=***##%% ..::--   @+
    %@@@@@@@=-::..    %%%##****=+**+***##@@@@##**+*-+***#%%:  ..:--    
   @@@@@@@@=-::..     %%%#***+*=+**+**##@@@@@###***-=***##%%  ...:-    
  #@@@@@@@@--:..      %%%#***+*=+**+**##@@@@@@##**+-=****##%   ..::    
 :@@   @@@@-::..      .%%#***+*-+=*****##@@@@##**+=-=****##%    ..:    
 @     +@@@-:..        %##***+**=+**++**##@@##***+-=+****###    ..:    
        @@@::..        #%#******-==**++*********+*==+****##%     .     
         @@@...         %##******==+***+*+====+**=++*****##:     .     
          *@+..          ##*******-=+***++===+++++==*+-:::#            
            @..          +##*******--=+++*++*+++=--**+-::-*            
             @.           *##*****+++----=====---==****###             
              +.           :##******+==::::::::=====**###              
                .            ###****==============++*###               
                              -###**++=========+++**###                
                                =###**++++++++++**#**                  
                                   #*##********##*+                    
    
    
                                                       {Colours.RES}""")
def clear():
    os.system("cls" if os.name == "nt" else "clear")


def meanu():
    clear()
    banner()
    print(f"{Colours.BG} OPTION {Colours.RES}")
    print(f"""{Colours.BR}
            [1] DOMAIN OSINT
            [2] IPADDRESS LOOKUP
            [3] PHONENUMER LOOKUP 
            [0] exit from program 


    
    {Colours.RES}""")

def domain_osint():
    clear()
    print(f"""{Colours.BD}{Colours.RD}
            
              

.....................................................................................................
.....................................................................................................
.....................................................................................................
.....................................................................................................
.....................................................................................................
.....................................................................................................
.......................................+%#################*+*=.......................................
..................................*############*###++++*##-*+###+*+..................................
..............................-##############+##++++++=+++=######+#***:..............................
............................###*########*#####*++#*##======***#**#*#+=#++:...........................
.........................#%**#############**#++#====#**+===*=*#*****#*=+-++*.........................
.......................#%%#%=+##+######=++=+#=#*=-*===****==+*=********:***=+*.......................
.....................*%#######+++###*++*++*+===***++=****************:#****##+#*.....................
....................######**+++++++++++++====****===**=**********#.+*********=+*#....................
..................%#*##****+++++++++++++===+*****=====---=****+.****=*********==#++..................
.................%#*##*####*+++++++++++====#*****===-------.**********.**********+++.................
................###########+++++++++++++=======*=------+++---++++++****+*********==++................
...............%##+%#######++++++++++++=========-------.++=+==+++++++****-*******:=+++...............
..............##%%%###+===*+++++++++++=========-------:-.=========+++++***.****:**#=+++..............
.............%##%%######*++++++++++++=========------=====.==========++++***:+.*****==+++.............
............=%*%%#######+++++++++++++========-----:-======:==========++++=.*:******===++-............
............%#%%%######*+++++++++++++========----+=======-:----=======.-++***.******==+++............
...........=#########***++++++++++++++=======---++=====----.---==:.-===+++****.*****==+++-...........
...........%%%#######***++++++++++++++=======--+++=====----=..:--=====++++*****-*****=++++...........
...........*%#%%%####****++++++++++++++=======**++===-..----:=--======+++************+++++...........
..........-*#*+%%####****++++++++++++++=====*=..:=+=======-=-.=======++++*******:****#=+++:..........
..........*#%%%%#%#+=++**++++++++++++++====#*****+++=========--=====++++*********+**#-#+++=..........
..........*%%%%%%%####****++++++++#####-##=+*******++++=======.===++++***********-=-####**+..........
..........+%%%###%####*#***+++++#######**##**********+++++++=+=-=++++**********-:#*#######=..........
..........:%%%###########**++++#########=#**#************++++++.+**********+:+*#**-#######:..........
...........%%%###%########**+++#########=####==+*====**********++******=:+*******#-#######...........
...........*#####%####*###***++*####++##=########***************.*-:=************#*#######...........
...........-%#########+#####**++*+++++###=#########*********=::*=************############=...........
............###%#%%###+%##########+++++++=##########*=::+++*****#:*********##############............
............:###=+#%##%################++**+---+++++++=========++==+###*#############+##-............
.............##%%###%%#+##******########*+=#*##++++++++++++++=======+*############++####.............
..............#%%###%%%#%#################=####++++++++++++++++++++++++++++++++++#=####..............
...............%########+%#################+###*++++++++++++++++++++++++++++++########...............
................%########%%%###############=###++++++++++++++++++++++++++++++*###=###................
.................%%%%####*#%%###############=#+++++++++++++++++++++++++++++++######%.................
..................*#####%%+%%%%#############*#*+++++++++++++++++++++++++++++######+..................
....................#*%%%%#+%%%%%############=#****+++++++++++++++++++++***#####*....................
.....................+%##%##+++++++++++*#####%+###***********++***********###*#+.....................
.......................#%%%#%#%######%%#############%#*****************##+%###.......................
.........................+%%%%#+#%%%%%%##%%####+%#######%*************%##%%+.........................
............................%###%#%#%%######%%%%+%########**********#%#%%............................
...............................#%%%##%########%#%*#%%#*+*%#*******%###...............................
..................................-%%*#######%%%%####%%#%%#******#-..................................
.......................................-##%#%###%#%%*%#%%%##*-.......................................
.....................................................................................................
.....................................................................................................
.....................................................................................................
.....................................................................................................
.....................................................................................................
.....................................................................................................  
    
    
    
    {Colours.RES}""")
    print(f"{Colours.BR} WELCOME USER TO DOAMIN OSINT {Colours.RES}")
    print(f"{Colours.BR} 1. get a whole domain info {Colours.RES}")
    print(f"{Colours.BR} 2. default searches {Colours.RES}")
    print(f"{Colours.BR} 3. exit to menu {Colours.RES}") 

    OPT = input(f"{Colours.BG} ENTER YOUR CHOICE: {Colours.RES}")
    if OPT == "1":
        time.sleep(2)
        print(f"{Colours.BD}{Colours.RD} GETTING FULL DOMAIN INFO....{Colours.RES}")
        FULL = input(f"{Colours.BR}enter your target domain name: {Colours.RES}")
        print(f"{Colours.GR} PLEASE HOLD......{Colours.RES}")
        try:
            website = whois.whois(FULL)
            website.json
            if website:
                print(f"{Colours.BG}DOMAIN_NAME:{Colours.RES}", website.domain_name)
                print(f"{Colours.BG}REGISTAR: {Colours.RES}", website.registrar)
                print(f"{Colours.BG}CREATION_DATE:{Colours.RES}", website.creation_date)
                print(f"{Colours.BG}EXPIRATION_DATE:{Colours.RES}", website.expiration_date)
                print(f"{Colours.BG}DOMAIN_INFO:{Colours.RES}", website.domain_info)
                print(f"{Colours.BG}WHOSIS_SERVER:{Colours.RES}", website.whois_server)
                print(f"{Colours.BG}UPDATED_DATE:{Colours.RES}", website.update_date)
                print(f"{Colours.BG}NAME_SERVE:{Colours.RES}", website.name_server)
                print(f"{Colours.BG}IP_ADDRESS:{Colours.RES}", website.name_server)
                print(f"{Colours.BG}EMAILS:{Colours.RES}", website.emails)
                print(f"{Colours.BG}PHONE:{Colours.RES}", website.phone)
            else:
                print(f"{Colours.BD}{Colours.RD}INVAILD INTO{Colours.RES}")
                print("going to main menu......")
                meanu()
        except Exception as e:
            print(f"{Colours.RD}ERROR,CONNECT TO THE INTERNET{e}{Colours.RES}")
            time.sleep(2)
            print(f"{Colours.RD} EXITING {Colours.RES}")
            clear()
            meanu()
        
    elif OPT == "2":
        time.sleep(2)
        print(f"{Colours.RD}setting up defalt,please hold......")
        time.sleep(2)
        cmd = input(f"{Colours.YE}PLEASE INTO YOUR TARGET DOMAIN: {Colours.RES}")
        try:
            WEBSITES = whois.whois(cmd)
            if WEBSITES:
                time.sleep(2)
                print(f"{Colours.BG}NAME:{Colours.RES}", WEBSITES.name)
                print(f"{Colours.BG}STATUS:{Colours.RES}", WEBSITES.status)
                print(f"{Colours.BG}CITY:{Colours.RES}", WEBSITES.city)
                print(f"{Colours.BG}ZIPCODE:{Colours.RES}", WEBSITES.zipcode)
                print(f"{Colours.BG}STATE:{Colours.RES}", WEBSITES.state)
                print(f"{Colours.BG}ORG:{Colours.RES}", WEBSITES.org)
                print(f"{Colours.BG}COUNTRY:{Colours.RES}", WEBSITES.country)
                print(f"{Colours.BG}ADDRESS:{Colours.RES}", WEBSITES.address)
            else:
                print(f"{Colours.BD}{Colours.RD}INVAILD INTO{Colours.RES}")
                print("going to main menu........")
                time.sleep(0.5)
                main()
        except Exception as e:
            print(f"{Colours.RD}ERROR,CONNECT TO THE INTERNET{e}{Colours.RES}")
            clear()
            meanu()

    elif OPT == "3":
        print(f"{Colours.BD}{Colours.RD}exiting......{Colours.RES}")
        time.sleep(0.5)
        main()
def ipaddess_lookup():
    clear()
    print(f"""{Colours.RD}
    
    
    
    
    
    
     ________  ________    _______  ________ ___  ________   ________  _______   ________         
|\   ____\|\   __  \  /  ___  \|\  _____\\  \|\   ___  \|\   ___ \|\  ___ \ |\   __  \        
\ \  \___|\ \  \|\  \/__/|_/  /\ \  \__/\ \  \ \  \\ \  \ \  \_|\ \ \   __/|\ \  \|\  \       
 \ \  \  __\ \  \\\  \__|//  / /\ \   __\\ \  \ \  \\ \  \ \  \ \\ \ \  \_|/_\ \   _  _\      
  \ \  \|\  \ \  \\\  \  /  /_/__\ \  \_| \ \  \ \  \\ \  \ \  \_\\ \ \  \_|\ \ \  \\  \|     
   \ \_______\ \_______\|\________\ \__\   \ \__\ \__\\ \__\ \_______\ \_______\ \__\\ _\     
    \|_______|\|_______| \|_______|\|__|    \|__|\|__| \|__|\|_______|\|_______|\|__|\|__|    
                                                                                              
                                                                                              
                                                                                              

                                                                                        {Colours.RES}""")
    
    

    print(f"{Colours.BD}{Colours.YE} PLEASE ENTER YOUR TARGET IP ADDRESS / NOTE: [0] TO EXIT {Colours.RES}")
    ip_address = input(">>>> ")

    if ip_address.strip() == "0":
        print("Exiting...")
        return

    url = f"http://ipwho.is/{ip_address}"

    try:
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()

        if not data.get("success", False):
            print(f"{Colours.RD}Invalid IP or API returned failure.{Colours.RES}")
            time.sleep(3)
            return

        clear()
        print("IP Address Info:\n")
        print(f"{Colours.BG}Success:{Colours.RES}", data["success"])
        print(f"{Colours.BG}Continent:{Colours.RES}", data["continent"])
        print(f"{Colours.BG}Region Code:{Colours.RES}", data["region_code"])
        print(f"{Colours.BG}Type:{Colours.RES}", data["type"])
        print(f"{Colours.BG}Country:{Colours.RES}", data["country"])
        print(f"{Colours.BG}Region:{Colours.RES}", data["region"])
        print(f"{Colours.BG}City:{Colours.RES}", data["city"])
        print(f"{Colours.BG}Latitude:{Colours.RES}", data["latitude"])
        print(f"{Colours.BG}Longitude:{Colours.RES}", data["longitude"])
        print(f"{Colours.BG}Postal:{Colours.RES}", data["postal"])
        print(f"{Colours.BG}Calling Code:{Colours.RES}", data["calling_code"])
        print(f"{Colours.BG}Capital Code:{Colours.RES}", data.get("capital_code", "N/A"))
        print(f"{Colours.BG}Capital:{Colours.RES}", data.get("capital", "N/A"))
        print(f"{Colours.BG}Borders:{Colours.RES}", data.get("borders", "N/A"))
        print(f"{Colours.BG}Continent Code:{Colours.RES}", data["continent_code"])
        print(f"{Colours.BG}Is EU:{Colours.RES}", data["is_eu"])

        lat = data["latitude"]
        lon = data["longitude"]
        print(f"{Colours.BD}Map:{Colours.RES} https://www.google.com/maps/@{lat},{lon},8z")

        # Nested dictionaries
        flag_emoji = data.get("flag", {}).get("emoji", "🏳️")
        print(f"{Colours.BG}Country Flag:{Colours.RES}", flag_emoji)

        connection = data.get("connection", {})
        print(f"{Colours.BG}ASN:{Colours.RES}", connection.get("asn", "N/A"))
        print(f"{Colours.BG}ORG:{Colours.RES}", connection.get("org", "N/A"))
        print(f"{Colours.BG}ISP:{Colours.RES}", connection.get("isp", "N/A"))
        print(f"{Colours.BG}Domain:{Colours.RES}", connection.get("domain", "N/A"))

        timezone = data.get("timezone", {})
        print(f"{Colours.BG}Time Zone ID:{Colours.RES}", timezone.get("id", "N/A"))
        print(f"{Colours.BG}Abbr:{Colours.RES}", timezone.get("abbr", "N/A"))
        print(f"{Colours.BG}DST:{Colours.RES}", timezone.get("is_dst", "N/A"))
        print(f"{Colours.BG}Offset:{Colours.RES}", timezone.get("offset", "N/A"))
        print(f"{Colours.BG}UTC:{Colours.RES}", timezone.get("utc", "N/A"))
        print(f"{Colours.BG}Current Time:{Colours.RES}", timezone.get("current_time", "N/A"))

        input(f"{Colours.YE}Press ENTER to return to menu...{Colours.RES}")
        menu()

    except Exception as e:
        print(f"{Colours.RD}An error occurred: {e}{Colours.RES}")
        time.sleep(5)
        meanu()
def phonenumber_lookup():
    clear()
    banner()
    print(f"{Colours.RD}======= ENTER A NUMBER WITH COUNTRY CODE ========{Colours.RES}")

    try:
        raw_input = input(">>>> ")
        parsed_number = phonenumbers.parse(raw_input, None)

        holder = carrier.name_for_number(parsed_number, "en")
        location = geocoder.description_for_number(parsed_number, "id")
        is_valid = phonenumbers.is_valid_number(parsed_number)
        is_possible = phonenumbers.is_possible_number(parsed_number)
        time_zone = timezone.time_zones_for_number(parsed_number)

        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, None, with_formatting=True)

        time.sleep(3)
        print(f"{Colours.BB} ===== HOLD, PROCESSING.......... {Colours.RES}")
        time.sleep(2)

        clear()
        banner()
        print(f"{Colours.RD}===== RESULT ======{Colours.RES}")
        print(f"{Colours.YE}PHONE NUMBER: {formatted_number}{Colours.RES}")
        print(f"{Colours.YE}CARRIER: {holder}{Colours.RES}")
        print(f"{Colours.YE}LOCATION: {location}{Colours.RES}")
        print(f"{Colours.YE}VALID: {is_valid}{Colours.RES}")
        print(f"{Colours.YE}POSSIBLE: {is_possible}{Colours.RES}")
        print(f"{Colours.YE}TIME ZONE: {', '.join(time_zone)}{Colours.RES}")
        print(f"{Colours.YE}MOBILE DIAL FORMAT: {formatted_number_for_mobile}{Colours.RES}")
        print(f"{Colours.RD}PRESS ENTER TO EXIT{Colours.RES}")
        input(">> ")
    
    except Exception as e:
        print(f"{Colours.RD}[ERROR] {str(e)}{Colours.RES}")
        input("Press ENTER to exit...")

    
        
        




def main():
    clear()
    meanu()
    while True:
        choice = input(f"{Colours.BG} enter your options: {Colours.RES}")
        if choice == "1":
            domain_osint()
        elif choice == "2":
            ipaddess_lookup()
        elif choice == "3":
            phonenumber_lookup()
       
        elif choice == "0":
            print(f"{Colours.BD}{Colours.YE} EXITING.......")
            time.sleep(2)
            exit()
            break 

        else:
            print(f"{Colours.RD} INVAILD INTO {Colours.RES}")
            exit()
if __name__=="__main__":
    main()
        