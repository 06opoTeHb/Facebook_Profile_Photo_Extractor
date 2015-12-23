import requests
from bs4 import BeautifulSoup
import urllib.request
import re
#from pprint import pprint
#import re

url = "https://www.facebook.com/simplyabhinav"
#url = "D:\MY PROJECTS\Hoverzoom Extension for facebook locked profile pics\myhtml.html"
r = requests.get(url)
#soup = BeautifulSoup("myhtml.html","html.parser")
soup = BeautifulSoup(r.content,"html.parser")
#print (soup.prettify().encode("utf-8"))
print("-----------------------")


s = str(soup.encode("utf-8"))


print("-----------------------")
#print(s)
print("-----------------------")


item= re.findall("profile_id=+\S+&amp;next",s)
print(str(item))
print("-----------------------")

s1 = str(item)
print(s1)
print("-----------------------")


#if(s1.endswith('&amp;next')):
s1 = s1[:-11]
s1 = s1[+13:]

print(s1)



#if(item in s):
	#print("YES")
	#print(s.split('&')[0]) 
 


#print(s.split("profile_id=",1)[0].encode("utf-8"))

#print(prof_id)
#links  = soup.find_all("")


prof_id = s1
url2 = "http://graph.facebook.com/"+str(prof_id)+"/picture?width=800"


urllib.request.urlretrieve(url2, "local-filename.jpg")

#"profile_id" in soup
	#print(profile_id)
#for link in links:
	#if "http" in link.get("href"):
	#	print("<a href = '%s'>%s</a>" %(link.get("href"),link.text))

#print (soup.prettify().encode("utf-8"))
#print(links)
#print (soup.encode("utf-8"))



