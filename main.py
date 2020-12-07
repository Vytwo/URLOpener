import webbrowser as wb
import os 

os.system("cls")

urlnames = []
urllst = []

def readurls():
    f = open("urls.txt", "r")
    lines = f.readlines()
    f.close()
    for line in lines:
        try:
            line = line.strip()
            line = line.split()
            urlnames.append(line[0])
            urllst.append(line[1])

        except:
            pass



def display():
    x = 0
    for item in urlnames:
        print("[" + str(x+1) + "]"+ item)
        x +=1

def helpuser():
    os.system("cls")
    print("Commands: ")
    print("")
    print("For opening a URL just type a number in brackets")
    print("")
    print("exit  | close the program    ")
    print("add   | add a URL            ")
    print("rem   | remove a URL         ")
    print("help  | commands             ")
    print("")
    print("Report bugs on https://github.com/Vytwo/URLOpener ")
    print("")

def addurl():
    new_name = input("Enter name of the website: ")
    new_url = input("Enter the url of the website: ")

    new_name.strip()
    new_url.strip()

    f = open("urls.txt", "a")
    f.write("\n" + new_name + " " + new_url)
    f.close()

    os.system("cls")

def removeurl():
    removeindex = input("Which one do you want to remove: ")
    removeindex = int(removeindex) - 1

    f = open("urls.txt", "r")
    lines = f.readlines()
    f.close()

    del lines[removeindex]

    f = open("urls.txt", "w+")
    for line in lines:
        f.write(line)
    
    f.close()
    os.system("cls")
        
while True:
    readurls()
    display()

    userinput = input("/<UO#V1>/ ").lower()
    userinput.strip()

    os.system("cls")

    if userinput == "help":
        helpuser()

    if userinput == "exit":
        break
    
    if userinput == "add":
        addurl()

    if userinput == "rem":
        removeurl()

    if userinput.isdigit():

        userinput = int(userinput)

        if userinput <= len(urllst) and userinput > 0:     
            wb.open_new_tab(urllst[userinput - 1])
            print("Opening url ...")
            break
        else:
            print("Unvalid number")

    urlnames.clear()
    urllst.clear()
