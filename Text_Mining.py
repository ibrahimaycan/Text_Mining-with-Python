import re,shutil,urllib.request
from urllib.request import urlopen

html = urlopen("https://muratcanganiz.com/")
html_doc = html.read()
link ='https://muratcanganiz.com/'
match = re.findall(b'"(.*?\.pdf)"', html_doc)
links = []
titles= []
for i in range(len(match)):  # len(match)
    try:
        links.insert(i,link+match[i].decode('ASCII'))
        titles.insert(i,"pdf"+str(i)+".pdf")
    except:
        pass

for i in range(len(links)): #download part
    try:
        with urllib.request.urlopen(links[i]) as response, open(titles[i], 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
    except:
        pass



