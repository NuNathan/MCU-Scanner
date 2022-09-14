from urllib.request import urlopen
import re

def ScanMovieName(url, Title):
    TitleSplit = Title.split()
    response = urlopen(url)
    decoded = response.read().decode("utf-8")
    textSplit = re.split(r'[<>\"\' ]',decoded)

    for i in range(len(textSplit)):
        #print(textSplit[i])
        if textSplit[i] == TitleSplit[0]:
            for u in range(len(TitleSplit)):
                if(textSplit[i+u] == TitleSplit[u]):
                    continue
                else:
                    break
            if u ==len(TitleSplit)-1:
                print("YES") 
                response.close()
                x = 0
                while(True):
                    if textSplit[i-x] == "href=":
                        break
                    x+=1
                return(f"https://www.imdb.com{textSplit[i-x+1]}")
    response.close()
    return(False)