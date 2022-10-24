from os import link
import requests,re

links=[]
pages=[]
visited=[]
report=[]

githubRepo="https://github.com/orgs/Unipilot/repositories"
base="https://github.com"
ignoreForks='<span class="text-small lh-condensed-ultra no-wrap mt-1" data-repository-hovercards-enabled>       forked from'

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
        
        recursion=True
        #print(recursiveCalls.text)
        # with open("./test.txt","a") as file:
        #     file.write("{}".format(recursiveCalls.text))
        regexR=re.findall('<a class="js-navigation-open Link--primary(.*?)</a>',recursiveCalls.text)

        findFork=re.findall('forked from',recursiveCalls.text)
        print(findFork)
        if len(findFork) >0:
            links.pop(0)
            continue

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