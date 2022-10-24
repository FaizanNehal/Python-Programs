from os import link
import requests,re

links=[]
pages=[]
visited=[]
report=[]

githubRepo="https://github.com/orgs/Unipilot/repositories"
base="https://github.com"
#ignoreForks='<span class="text-small lh-condensed-ultra no-wrap mt-1" data-repository-hovercards-enabled>       forked from'
ignoreForks='forked from'
privateKeysRegex=['\b[5KL][1-9A-HJ-NP-Za-km-z]{50,51}\b','\bxprv[a-km-zA-HJ-NP-Z1-9]{107,108}\b','\b[0-9a-fA-F]{62}[0][0-9a-fA-F]\b']
                    # 1st is for BTC   2nd for xpriv 3rd for MONERO


def branches():
                    ### TODO: implement the spider for each of the branches
    pass


def commits():
                    ### TODO: implement the spider for all the commits and commit history
    pass

def pullRequests():
                    ### TODO: implement the spider for open and closed pull requests
    pass




def main():
    repository=requests.get(githubRepo)
    firstRegex=re.findall('data-hovercard-type="repository" data-hovercard-url="(.*?)data-view-component="',repository.text)
    
    for elements in firstRegex:
        links.append(re.search('href="(.+)"',elements).group(1))
    for elements in links:
        print(elements)

    while len(links)>0:

        x = links[0]
    #for ix,x in enumerate(links):
    
        print(base+x)
        recursiveCalls=requests.get(base+x)
        
        
        #print(recursiveCalls.text)
        # with open("./test.txt","a") as file:
        #     file.write("{}".format(recursiveCalls.text))
        

                ### IT WILL IGNORE THE REPOSITORIES THAT ARE FORKED ### 
        findFork=re.findall(ignoreForks,recursiveCalls.text)
        print(findFork)
        if len(findFork) >0:
            links.pop(0)
            continue

                ### GETTING ALL THE DIRECTORIES AND FILES IN THE CURRENT DIRECTORY ####                
        regexR=re.findall('<a class="js-navigation-open Link--primary(.*?)</a>',recursiveCalls.text)

        print("-----------------------")
        print("-----------------------")

        temp=[]
        for elements in regexR:
            temp.append(re.search('href="(.+)"',elements).group(1))
        for elements in temp:
            if (elements not in visited) and (elements not in links):
                
                
                links.append(elements)
                print("NOT NOT NOT")

        y = links.pop(0)
        visited.append(y)


           

if __name__=="__main__":
    main()