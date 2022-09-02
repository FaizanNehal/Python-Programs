from audioop import add
from time import sleep
import requests,re

# Extremely simple scraper that fetches addresses from a repo in Balancer-Labs


addresses= [line.rstrip() for line in open('./address.txt')]
def scrap():
    github= requests.get("https://raw.githubusercontent.com/balancer-labs/balancer-sdk/844e40143aa4a60b6b65d8f89beba033e0052fde/balancer-js/src/modules/data/token-prices/initial-list.json")   
    textGithub = github.text
    counter =0
    
    regexFetch=re.findall(r'"address": "(.*?)"',textGithub)
    regexFetch = list(set(regexFetch))
    

    for x in regexFetch:
        if x in addresses:
            counter= counter+1
        else:
            addresses.append(x)
            with open("./address.txt",'a') as file:
                file.write(x + "\n")
            

    print(regexFetch)
    print("TOTAL COUNT: {}".format(counter))
    print(len(regexFetch))


def main():
    while(True):
        scrap()
        print('--------------')
      #  print(addresses)
        print(len(addresses))
        sleep(10)

main()