from tkinter import *
#print("1. the imported file is", tkinter.__file__)

from PIL import ImageTk,Image
import PIL.Image
import requests
from bs4 import BeautifulSoup
import urllib.request
import re
#from _tkinter import *
#print("2. the imported file is", _tkinter.__file__)


def displayText():
    """ Display the Entry text value. """

    global entryWidget

    url = str(entryWidget.get().strip())
    # # #url = "D:\MY PROJECTS\Hoverzoom Extension for facebook locked profile pics\myhtml.html"
    r = requests.get(url)
    # # soup = BeautifulSoup("myhtml.html","html.parser")
    soup = BeautifulSoup(r.content.decode('utf-8'),"html.parser")
    # # #print (soup.prettify().encode("utf-8"))
    # # print("-----------------------")
    # # print("-----------------------")
    # # #print(s)
    # # print("-----------------------")

    item = re.findall("profile_id=+\S+&amp;next",str(soup.encode("utf-8")))
    print("1 -----------------------")    
    print(item)
    s1 = str(item)
    if(s1.endswith("[]")):
        item = re.findall("\"entity_id\":\"+\S+\"}\]\,\[\]\]\,\[\"U",str(soup.encode("utf-8")))
        print("2-----------------------")
        print(item)
        s1 = str(item)
        s1 = s1[+15:]
        s1 = s1[:-13]
        # print(item)
        # # print("3-----------------------")
        # # print(s1)
        # print("-4----------------------")
    else:
        s1 = s1[:-11]
        s1 = s1[+13:]

    print(s1)



    # #if(item in s):
    # #print("YES")
    # #print(s.split('&')[0]) 



    # #print(s.split("profile_id=",1)[0].encode("utf-8"))

    # #print(prof_id)
    # #links  = soup.find_all("")


    prof_id = s1
    url2 = "http://graph.facebook.com/"+str(prof_id)+"/picture?width=800"


    urllib.request.urlretrieve(url2, "local-filename.jpg")

    #"profile_id" in soup
    #print(profile_id)
    #for link in links:
    #if "http" in link.get("href"):
    #    print("<a href = '%s'>%s</a>" %(link.get("href"),link.text))

    #print (soup.prettify().encode("utf-8"))
    #print(links)
    #print (soup.encode("utf-8"))

      # url = https://www.facebook.com/simplyabhinav

    
    window = Tk()
    window.title("Output")
    window.geometry("960x960")
    window.configure(background='grey')

    path = "local-filename.jpg"

    #Creates a tkinter-compatible photo image, which can be used everywhere tkinter expects an image object.
    img1 = ImageTk.PhotoImage(PIL.Image.open(path))

    #The Label widget is a standard tkinter widget used to display a text or image on the screen.
    panel = Tk.Label(window, image = img1)

    #The Pack geometry manager packs widgets in rows or columns.
    panel.pack(side = "bottom", fill = "both", expand = "yes")

    #Start the GUI
    window.mainloop()

    os.remove("local-filename.jpg")
 

if __name__ == "__main__":

    root = Tk()
    
    root.title("tkinter Entry Widget")
    root["padx"] = 40
    root["pady"] = 20       

    # Create a text frame to hold the text Label and the Entry widget
    textFrame = Frame(root)
    
    #Create a Label in textFrame
    entryLabel = Label(textFrame)
    entryLabel["text"] = "Enter the URL:"
    entryLabel.pack(side=LEFT)

    # Create an Entry Widget in textFrame
    entryWidget = Entry(textFrame)
    entryWidget["width"] = 50
    entryWidget.pack(side=LEFT)

    textFrame.pack()

    button = Button(root, text="Submit", command=displayText)
    button.pack() 
    
    root.mainloop()



