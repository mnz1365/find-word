import tkinter
import tkinter.messagebox
import tkinter.scrolledtext

# count word found
findCount = 0
countLetters = 0
letterStart = 0
letterEnd = 0
count = 0
countLines = 1
linePositionStart = None
linePositionEnd = None

root = tkinter.Tk()
root.geometry("670x430")
root.title("search")
root.resizable(False, False)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)   
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
   
   
firstLabel = tkinter.Label(root, text="enter your text")
firstLabel.grid(row=0, column=0)

# text
T = tkinter.scrolledtext.ScrolledText(root, height=15, width=55)
T.grid(row=0, column=1)

# word or target that search through text to find similar words
textEntry = tkinter.Entry(root)
textEntry.grid(row=1, column=1)
T.focus_set()

# when you press enter then active the button or active the function that sreach for words!
def activeButton(event):
    # resultButton.invoke()
    # changing background color for second to green
   
    if textEntry.get() != "":        
        resultButton.configure(bg="gray")
        resultButton.after(100, lambda: resultButton.configure(bg="lightgray"))
        mySearch()

def mySearch():
    oneData = ""
    global findCount, count, countLetters, letterStart, letterEnd, linePositionStart, linePositionEnd, countLines, T
    letterStart = 0
    letterEnd = 0
    countLines = 1
    count = 0
    count_letters_in_lines = -1
    linePositionStart = None
    linePositionEnd = None
    T.tag_delete("start")
    myData = T.get("1.0", tkinter.END)
    myData = myData.lower()
    myTarget = textEntry.get()
    myTarget = myTarget.lower() 
    myTargetList = list(myTarget)

    # check if text area is empty or not and 
   
    if len(myData) == 1:
        tkinter.messagebox.showwarning("warning", "please fill the text area")
    
    if len(myData) > 1 and myTarget == "":
        tkinter.messagebox.showwarning("warning", "please enter the word!")
        textEntry.focus_set()
        
    
    findCount = 0
    mydataLetters = list(myData)
    myData = myData.split()


    
    for letter in mydataLetters:
        if letter == "\n":
            countLines = countLines + 1
            letterStart = 0
            letterEnd = 0
            count_letters_in_lines = -1
        count = count + 1
        
        if letter != myTargetList[countLetters]:
            countLetters = 0
            letterStart = 0
            letterEnd = 0
        if letter == myTargetList[countLetters]:
            if countLetters == 0:
                letterStart = count_letters_in_lines
            countLetters = countLetters + 1
           
        count_letters_in_lines = count_letters_in_lines + 1
        
        if countLetters == len(myTargetList):
            findCount = findCount + 1
            letterEnd = letterStart + countLetters
            countLetters = 0
            if countLines == 1:
                linePositionStart =  str(countLines)+"."+str(letterStart+1)
                linePositionEnd = str(countLines)+"."+str(letterEnd+1)
            else:
                linePositionStart =  str(countLines)+"."+str(letterStart)
                linePositionEnd = str(countLines)+"."+str(letterEnd)
            T.tag_add("start", linePositionStart, linePositionEnd)
            T.tag_config("start", background="yellow", foreground="black")
            
            
            

    
    
    # update the result label in each search
    resultLabel["text"] = '{0} words found'.format(findCount)
                           

        


resultButton = tkinter.Button(root, text="search", command=mySearch)
resultButton.grid(row=1, column=2)

resultLabel = tkinter.Label( root, text="")

resultLabel.grid(row=2, column=2)

# acitve enter
root.bind('<Return>', activeButton)

root.mainloop()