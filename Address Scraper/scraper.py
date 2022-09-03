from audioop import add
from time import sleep, strftime
import requests,re
from datetime import date, datetime

# Extremely simple scraper that fetches addresses from a repo in Balancer-Labs


addresses= [line.rstrip() for line in open('./address.txt')]
csvAddress = [line.rstrip() for line in open('./address.csv')]
def scrap():
    github= requests.get("https://raw.githubusercontent.com/balancer-labs/balancer-sdk/844e40143aa4a60b6b65d8f89beba033e0052fde/balancer-js/src/modules/data/token-prices/initial-list.json")   
    textGithub = github.text
    counter =0
    csvCounter=0
    
    regexFetch=re.findall(r'"address": "(.*?)"',textGithub)
    regexFetch = list(set(regexFetch))
    

    for x in regexFetch:
        dateTime=datetime.now()
        currentTime=dateTime.strftime("%d-%m-%Y  (%H:%M:%S)")
        if x in addresses:
            counter= counter+1
        else:
            addresses.append(x)
            with open("./address.txt",'a') as file:
                file.write(x + "\n")
        if x in csvAddress:
            csvCounter=csvCounter+1
        else:
            with open("./address.csv",'a') as csvFile:
                csvFile.write(x + "     Time: " +currentTime +"\n")

  #  print(regexFetch)
  #  print("TOTAL COUNT: {}".format(counter))
  #  print(len(regexFetch))


def main():
    while(True):
        scrap()
        print('ITERATING')
       # print(addresses)
       # print(len(addresses))
        sleep(10)


if __name__ == "__main__":
    main()