#######################################################################
#   Aaren Patel, Evan Knaak, Armaan Khatri
#   We pledge our honor that we have abided by the Stevens Honor System
#   11/16/22
#   CS 115 - Group Project
#######################################################################

listPeople = {}
def start():
    """Holds the main program that will call other programs when needed based on user input - Aaren"""
    
    #Opens and reads file - Creates new file if one doesn't exist
    musicrecplus = open("musicrecplus.txt", "a")
    musicrecplus.close
    musicrecplus = open("musicrecplus.txt", "r")
    text = musicrecplus.readlines()
    musicrecplus.close
    
    #Creates dictionary from file
    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j] == ":":
                listPeople[text[i][:j]] = text[i][j+1:len(text[i])-1].split(",")
    
    #Gets users name
    name = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private): ")
    print(listPeople)
    #Runs Program
    if name in listPeople:
        program(name)
    else:
        listPeople[name] = inputArtists()
        program(name)

    #Ends Program
    strTxt = ""
    for i in listPeople:
        strTxt += i + ":" + addArtists(listPeople[i]) + "\n"
    musicrecplus = open("musicrecplus.txt", "w")
    musicrecplus.write(strTxt)
    musicrecplus.close

def program(name):
    """Asks user for what they want to do within the recommender - Aaren"""
    run = True
    while run == True:
        userInput = input("e - Enter preferences\nd - Delete preferences\ns - Show preferences\nr - Get recommendations\np - Show most popular artists\nh - How popular is the most popular\nm - Which user has the most likes\nq - Save and quit\n")
        if userInput == "e":
            listPeople[name] = inputArtists(listPeople[name])
        elif userInput == "d":
            listPeople[name] = deletePreferences(listPeople[name])
        elif userInput == "s":
            print(showPreferences(listPeople[name]))
        elif userInput == "r":
            print(getRecs(name))
        elif userInput == "p":
            popArtists()
        elif userInput == "h":
            popPopArtists()
        elif userInput == "m":
            mostLikes()
        elif userInput == "q":
            run = False

def inputArtists(listArtists = []):
    """Creates a list of artists that the user inputs - Aaren"""
    run = True
    while run:
        artist = input("Enter an artist that you like (Enter to finish): ")
        if artist == "":
            run = False
        else:
            listArtists += [artist.title()]
    return listArtists
        
def addArtists(listArtists):
    """Formats artists to be put back into the txt file - Aaren"""
    strArtists = ""
    for i in listArtists:
        strArtists += i + ","
    return strArtists[:-1]

def showPreferences(artists):
    """Lists the preferences of the user - Aaren"""
    strArt = ""
    if artists == []:
        return "No artists listed"
    for i in artists:
        strArt += i + ", "
    return strArt[:-2]

def deletePreferences(artists):
    """Deletes an artist that the user chooses - Armaan"""
    print(showPreferences(artists))
    delete = input("Enter name of artist from above exactly: \n")
    newList = []
    for i in artists:
        if i == delete:
            None
        else:
            newList += [i]
    return newList

def getRecs(name):
    """Gives reccomendations based on your liked artists - Armaan"""
    similar = []
    for i in listPeople:
        if i[-1] == "$" or i == name:
            None
        else:
            count = 0
            for j in listPeople[i]:
                if j in listPeople[name]:
                    count += 1;
            if count != len(j):
                similar += [[count, i]]
    if similar == []:
        return "No recommendations found"
    maxVal = [0, ""]
    for i in similar:
        if i[0] > maxVal[0]:
            maxVal = i
    if maxVal == [0, ""]:
        return "No recommendations found"
    for i in listPeople[maxVal[1]]:
        if i in listPeople[name]:
            None
        else:
            print(i)

def popArtists():
    '''determines the artists who have the most non-private likes and prints the top 3 - Evan'''
    artists=[]
    for i in listPeople:
        if i[-1]=='$':
            None
        else:
            artists+=listPeople[i]
    if artists==[]:
        print('Sorry, no artists found')
    else:
        mentions={}
        for i in artists:
            if i not in mentions:
                mentions[i]=1
            else:
                mentions[i]=mentions[i]+1
        order=[]
        for i in mentions:
            order+=[[mentions[i],i]]
        if len(order)<=3:
            for i in range(len(order)):
                print(order[i][1])
        else:
            x=0
            while x<3:
                print(max(order)[1])
                max(order)[0]=0
                x+=1
 
def popPopArtists():
    '''determines the artists with the most non-private likes and prints that value - Evan'''
    artists=[]
    for i in listPeople:
        if i[-1]=='$':
            None
        else:
            artists+=listPeople[i]
    if artists==[]:
        print('Sorry, no artists found')
    else:
        mentions={}
        for i in artists:
            if i not in mentions:
                mentions[i]=1
            else:
                mentions[i]=mentions[i]+1
        order=[]
        for i in mentions:
            order+=[mentions[i]]
        print(max(order))
 
def mostLikes():
    '''determines the non-private user who has the most liked artists and prints that user's name - Evan'''
    test=[]
    for i in listPeople:
        if i[-1]=='$':
            None
        else:
            test+=listPeople[i]
    if test==[]:
        print('Sorry, no user found')
    else:
        users={}
        for i in listPeople:
            if i[-1]=='$':
                None
            else:
                users[i]=len(listPeople[i])
        likes=[]
        for i in users:
            likes+=[[users[i],i]]
        print(max(likes)[1])
 
start()
