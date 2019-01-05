import urllib
from bs4 import BeautifulSoup
import urlparse
import mechanize


# introducir URL en la source del Cyberscan.py para proceder el scanneo.
# Codec CyberSecRoot
# Title: Programing CyberSecRoot
#------ Cyberpunks-------#
#1 Exploit               #
#2 GNU Make              #
#3 PHP                   #
#4 Objective-C           #
#5 Bash                  #
#6 PureBasic             #
#7 Cygwin                #
#8 VMWare                #
##########################
#Ser Una Rata De La Red...
#FB:https://www.facebook.com/Cyberpunks.Hackers.2015



print " Cyberscan Web Security Scanner Modules By: CyberSecRoot"

print " #------ Cyberpunks-------# "
print " #1 Exploit               # "
print " #2 GNU Make              # "
print " #3 PHP                   # "
print " #4 Objective-C           # "
print " #5 Bash                  # "
print " #6 PureBasic             # "
print " #7 Cygwin                # "
print " #8 VMWare                # "
print " ########################## "

print " Escaneando el contenido del servidor web"
print "........................................."


url = raw_input("Ingresa URL: ")
br = mechanize.Browser()

# Puedes crear una lista para proceder hacer un multiscanneo
urls = [url]
visited = [url]


# acuedate que la lista de host debe ser dinamica
#   interceptando el trafico de web dinamico
#   Create source CyberSecRoot
while len(urls)>0:
    try:
        br.open(urls[0])
        urls.pop(0)
        for link in br.links():
            newurl =  urlparse.urljoin(link.base_url,link.url)
            #print newurl
            if newurl not in visited and url in newurl:
                visited.append(newurl)
                urls.append(newurl)
                print newurl
    except:
        print "error"
        urls.pop(0)

print visited
