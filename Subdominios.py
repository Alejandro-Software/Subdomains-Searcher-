import argparse
import requests
from os import path
import sys

#With the use of argparse we send a parameter (domain)
parser=argparse.ArgumentParser()
parser.add_argument("-t","--target",help="Indica el dominio victima")
parser=parser.parse_args()

def main():
    if parser.target:
        if path.exists("subdominios.txt"):
            wordlist=open("subdominios.txt","r")   #Openning the file with the subdomaines to make the research
            wordlist=wordlist.read().split("\n")
            
            for subdominios in wordlist:
                url= "https://"+subdominios+"."+parser.target       #Making the url 
                try:
                    requests.get(url)                               #Making the request
                except requests.ConnectionError:
                    pass
                else:
                    print(f"(+) Nuevo subdominio descubierto: {url}")       #Showing the existing url

            for subdominios in wordlist:
                url2="http://"+subdominios+"."+parser.target
                try:
                    requests.get(url2)
                except requests.ConnecionError:
                    pass    
                else:
                    print(f"(+) Nuevo subdominio descubierto: {url2}")
    else:                                                                   #In case there is no target
        print("Debe colocar un target para realizar la ejecucion del programa. ")     


if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()    


