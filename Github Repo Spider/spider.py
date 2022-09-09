import requests,re

links=[]
pages=[]
githubRepo="https://github.com/orgs/Unipilot/repositories"
base="https://github.com"

def main():
    repository=requests.get(githubRepo)
    firstRegex=re.findall('data-hovercard-type="repository" data-hovercard-url="(.*?)data-view-component="',repository.text)
    
    for elements in firstRegex:
        links.append(re.search('href="(.+)"',elements).group(1))
    for elements in links:
        print(elements)

    for ix,x in enumerate(links):
        print(base+x)
        recursiveCalls=requests.get(base+x)
        recursion=True
        #print(recursiveCalls.text)
        # with open("./test.txt","a") as file:
        #     file.write("{}".format(recursiveCalls.text))
        regexR=re.findall('<a class="js-navigation-open Link--primary(.*?)</a>',recursiveCalls.text)
        print(len(regexR))
           

if __name__=="__main__":
    main()