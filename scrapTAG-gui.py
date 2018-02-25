import sys
import urllib.request
from bs4 import BeautifulSoup

# import the library
from appJar import gui



def main():
    # my code here

    # create a GUI variable called app
    app = gui("scrapTAG", "480x320")

    #app.setFont(16)
    # add & configure widgets - widgets get a name, to help referencing them later
    app.addLabel("title", "scrapTAG")
    app.setLabelBg("title", "orange")

    app.addLabelEntry("Insert URL")
    app.setFocus("Insert URL")


    def press(button):
        if button == "Cancel":
            app.stop()
        else:
            url = app.getEntry("Insert URL")
            file = open("ptags.txt","w+")
            soup = BeautifulSoup(urllib.request.urlopen(url), "html.parser")
            scrap = soup.findAll('a',{'class':'pull-left btn btn-search-pill'})
            for tag in scrap:
                tags = (tag.get_text(strip=True))
                print (tags)
                file.write(tags + '\n')
            file.close()

    # link the buttons to the function called press
    app.addButtons(["Cancel", "Submit"], press)

    # start the GUI
    app.go()

if __name__ == "__main__":
        main()

#url = sys.argv[1]
