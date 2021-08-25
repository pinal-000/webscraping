from bs4 import BeautifulSoup
import requests
import csv
import os

url = "https://www.tridhya.com/company/team/"
res = requests.get(url)
soup = BeautifulSoup(res.content,'html5lib')

employeeData = []
data = soup.find('div', attrs = {'class':'entry-content pb-5 pt-5'})  #div with class specified

# get name and designation
for i in data.findAll('div', attrs = {'class':'col-sm-6 col-md-3 profile-card-main'}):
    edata={}
    edata['name'] = i.span.text
    edata['designation'] = i.h2.text
    employeeData.append(edata)

# store employee name and designation in csv file
filename = 'tridhyaEmployee.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['name','designation'])
    w.writeheader()
    for i in employeeData:
        w.writerow(i)
        

# to store profile picture of employee in folder
if not os.path.exists("TridhyaPhoto"):
    os.mkdir("TridhyaPhoto")

for image,i in enumerate(data.findAll('div', attrs = {'class':'profile-img'})):
    try:
        elink = i.img['src']
        r=requests.get(elink).content
        print(elink)
        with open(f"{'TridhyaPhoto'}/image{image+1}.jpg", "wb+") as f:    # {image+1} is name of image
            f.write(r)
    except:
        pass
    
    

