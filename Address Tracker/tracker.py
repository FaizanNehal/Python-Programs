import requests,re
from time import sleep
from datetime import datetime

from asyncore import file_dispatcher
from audioop import add


addresses= [line.rstrip() for line in open('./address.txt')]
etherscanAPI ="GCQP7EA7N2F7GAIQ2JW5HVYDTZ9ZSE5VRS"
addressToTrack=""
endpointBalance="https://api.etherscan.io/api?module=account&action=balance&address={}&tag=latest&apikey={}"
endpointInternal="https://api.etherscan.io/api?module=account&action=txlistinternal&address={}&startblock=0&endblock=2702578&page=1&offset=10&sort=asc&apikey={}"
endpoints=[["Balance","https://api.etherscan.io/api?module=account&action=balance&address={}&tag=latest&apikey={}"],
["Internal","https://api.etherscan.io/api?module=account&action=txlistinternal&address={}&startblock=0&endblock=2702578&page=1&offset=10&sort=asc&apikey={}"],
["Normal","https://api.etherscan.io/api?module=account&action=txlist&address={}&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey={}"],
["Block Mined","https://api.etherscan.io/api?module=account&action=getminedblocks&address={}&blocktype=blocks&page=1&offset=10&apikey={}"]] 

placeholders=["Balance is: {}","Internal Transactions by the Address: {}","Normal Transaction by Address: {}","Block Mined by Address: {}"]
                


def tracker():
    counter=0
    Req=""
    for index,addr in enumerate(addresses):
        print(addr) 
        with open("transactions.txt","a") as file:
            file.write("ADDRESS # {}: {}\n".format(index+1,addr))
        for ix,x in enumerate(endpoints):
            for iy,y in enumerate(x):
                if iy ==0:
                    with open("transactions.txt","a") as file:
                        file.write("\t{} Transaction:\n".format(y))
                    print(y)
                elif iy ==1:
                    Req=requests.get(y.format(addr,etherscanAPI))
                    result=Req.json().get("result")
                    with open("transactions.txt","a") as file:
                        file.write("\t\t{}\n".format(placeholders[ix].format(result)))
                else:
                    print("RUNNING")

    
      #  counter+=1
            
      #  file .write("\tTransactions: {} \n\n".format(history))
      #  if counter==5:
      #      sleep(2)
      #      counter=0
    

def main():
    tracker()
    pass


if __name__ == "__main__":
    main()