import requests,re
from time import sleep
from datetime import datetime

from asyncore import file_dispatcher
from audioop import add


addresses= [line.rstrip() for line in open('./address.txt')]
etherscanAPI ="GCQP7EA7N2F7GAIQ2JW5HVYDTZ9ZSE5VRS"
addressToTrack=""
endpoint="https://api.etherscan.io/api?module=account&action=balance&address={}&tag=latest&apikey={}"



def tracker():
    counter=0
    for index,addr in enumerate(addresses):
        print(addr)
        historyReq= requests.get(endpoint.format(addr,etherscanAPI))
        history= historyReq.text
        counter+=1
        with open("transactions.txt","a") as file:
            file.write("ADDRESS # {}: {}\n".format(index+1,addr))
            file .write("\tTransactions: {} \n\n".format(history))
        if counter==5:
            sleep(2)
            counter=0
    pass

def main():
    tracker()
    pass


if __name__ == "__main__":
    main()