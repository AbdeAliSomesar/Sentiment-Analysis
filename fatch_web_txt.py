import bs4
import urllib3
from bs4 import BeautifulSoup
import Final
class rank:
    name='w'
    rate=0.0
no=0
r1=[]
def somefunc(link):
    http=urllib3.PoolManager()
    req=http.request('GET',link)
    soup=BeautifulSoup(req.data,'html.parser')
    #print("Step 1\n")
    f=open('Review.txt','a')
    global no
    global r1
    #print('number =')
    #print(no)
    r1.append(rank())
    for e in soup.find_all('h1'):
        h1=e.get('class')
        if h1 is not None and 'heading_title' in h1:
            f.writelines("******************************************")
            f.writelines(e.text)
            r1[no].name=e.text
            f.writelines("******************************************")
            f.writelines("\n\n")
    e1=soup.find_all("div",{"class":"entry"})
    sum=0
    for e in e1[1:10]:
        #if e.text is not None in e:
        h=e.text
        try:
            f.writelines(e.text)
            num=Final.rate(e.text)
            f.writelines('\n\n')
            print(e.text)
            if num > 3:
                f.writelines("Excellent Review: ")
                print("Excellent Review: ")
            elif num > 1:
                f.writelines("Good Review: ")
                print("Good Review: ")
            elif num < 0:
                f.writelines("Bad Review: ")
                print("Bad Review:")
            else:
                f.writelines("Average Review: ")
                print("Average Review: ")
            f.writelines(str(num))
            print(num)
            sum=sum+num
            f.writelines('\n\n\n')
        except:
            print('some Error')

    #print(sum)
    #print(no)
    r1[no].rate=sum
    f.close()
    no=no+1
        #if num>1:
            #f.writelines("Good Review: \n")
        #elif num<0:
            #f.writelines("Bad Review: \n")
        #else:
            #f.writelines("Average Review: \n")             
                
        #f.writelines(str(num+'\n'))
        
        
http=urllib3.PoolManager()
myurl='https://www.tripadvisor.in/Restaurants-g304555-Jaipur_Jaipur_District_Rajasthan.html'
req=http.request('GET',myurl)
f=open('Review.txt','w')
f.writelines('*')
f.close()
soup=BeautifulSoup(req.data,'html.parser')
count=1;
for e in soup.find_all('a'):
    href=e.get('class')
    if href is not None and 'poiTitle' in href:
        count=count+1
        if count >10:
            break
        link=e.get('href')
        somefunc(str('https://www.tripadvisor.in/'+link))
f1=open('Review.txt','a')
print('\n\n****************************************Rating************************************')
f1.writelines
f1.writelines("**********************************Rating*******************************")
for e in r1:
    print("\n")
    f1.writelines("\n\n")
    f1.writelines(e.name)
    f1.writelines(":- ")
    f1.writelines(str(round(e.rate/7)))
    print(e.name)
    print(round(e.rate/7))
