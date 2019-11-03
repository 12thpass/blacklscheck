import socket
from colorama import Fore, Back, Style 
# below line for get multiple ip input 
xip = [str(newx) for newx in input("Enter multiple value: ").split()] 
print("Number of list is: ", xip)
# you can add more blacklis here 
bl = ["b.barracudacentral.org",
    "dnsbl.sorbs.net",
    "dnsbl-1.uceprotect.net",
    "dnsbl-2.uceprotect.net",
    "dnsbl-3.uceprotect.net",
    "pbl.spamhaus.org",
    "sbl.spamhaus.org",
    "xbl.spamhaus.org",
    "zen.spamhaus.org"]
# below for loop get our ip and run for all blacklist for more contact deepakmeena900@gmail.com
for ip in xip :
    print ( Fore.YELLOW + ip + " checking")
    for xbl in bl:
        querybad = '.'.join(reversed(str(ip).split("."))) + "." + xbl
        try: 
            addr1 = socket.gethostbyname(querybad)
            print( Fore.RED + str(ip) + " listed in " + str(xbl))
        except :
            #print( Fore.GREEN + str(ip) + " NO listed in " + str(xbl))
            pass
