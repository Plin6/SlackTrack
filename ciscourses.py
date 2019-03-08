from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pickle


my_url = 'http://catalog.uoregon.edu/arts_sciences/computerandinfoscience/#courseinventory'

#opening up conneciton, grabbing the page

data = []

#for the pickle
file_name = "cis_courses.txt"
fileObject = open(file_name, 'w')

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

#grabs containers
containers = page_soup.findAll("div",{"class":"courseblock"})

#for csv file 
filename = "courses.txt"
f = open(filename, "w")

#headers = "Major" 
#f.write(headers)

l1 = []
ex = []
redo = []
plz = []

for container in containers:
    #print(container)
    #newtext = container.replace("&nbsp", "")
    #print(newtext)
    final = container.p.text
    final = final.strip('\xa0').split(" ")    
    data.append(final)
    #print(data[0])
    ####print(final)
    ex.append(final)
    for line in final:
        #course = line[0]
        #print(course)
        #num = line[1]
        #print("inside for loop")
        l1.extend(line.strip('').split('\xa0'))
        #l1.append(course.strip('').split('\xa0'))
        #l1.append(num.strip('').split('\xa0'))
        #redo.append(ep[1:1])
    #line = str(l1)
    #f.write(line)
    first = final[0]
    #print(first)
    data.append(final)
   
    final.append(first)
 
    #print(final)
    #print(final)
    #print(final)
    #data.append(final)
#f.write(l1)
    #f.write(data[container]) 
    #print(final)
#pickle.dump(l1, fileObject, protocol=2)
#for line in data:
    #l1.extend(line.strip('').split('\xa0'))
#print(l1)

#print(ex)
for toop in ex:
    toop = toop[:1]
    #print(toop) 
    redo.extend(toop)
    #str(toop)
    #toop.strip('\xa0').split(" ")
    ###redo.extend(toop.strip('').split('\xa0'))
    #print(toop)
for thing in redo:
    plz.append(thing.strip('').split('\xa0'))

for item in plz:
    f.write("%s\n" % item)   
print(plz)
#print(ex)
f.close()
fileObject.close()
