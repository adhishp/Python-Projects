import urllib

def profanitychecking():
    #content = open("C:\\Users\\adhis\\OneDrive\\Documents\\UDACITY\\Intro to Python\\Python Projects\\cursefile.txt")
    #words = content.read()
    print("Please Enter a Statement, whatever comes to your mind:")
    words = raw_input()
    #content.close()
    compare(words)
    print("Do you want to play this game again?")
    bina = raw_input()
    if bina == 'yes':
          profanitychecking()


def compare(words):
    webpage = urllib.urlopen("http://www.wdylike.appspot.com/?q="+words)
    content = webpage.read()
    if 'true' in content:
        print("Improve your language kid! This is not what you say!")
    else:
        print("You seem to be like a good kid, Keep your language clean like this!")
    webpage.close()

profanitychecking()
