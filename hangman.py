from tkinter import *
from tkinter.messagebox import showinfo

def mask(word,exceptions):
    tempstr = ""
    for x in range(len(word)):
        if word[x] in exceptions:
            tempstr += word[x]
        else:
            tempstr += "?"
    return tempstr
        

class hangman(Frame):
    def __init__(self,word, parent=None):
        # Frame init
        Frame.__init__(self,parent)

        # Entry for screen
        self.entry = Entry(self)
        self.entry.grid(row=0,column=1,columnspan=8)
        Label(self, text = "Word:").grid(row=0,column=0,columnspan=1)

        self.right = Entry(self)
        self.right.grid(row=1,column=1,columnspan=8)
        Label(self, text = "Right:").grid(row=1,column=0,columnspan=1)

        self.wrong = Entry(self)
        self.wrong.grid(row=2,column=1,columnspan=8)
        Label(self, text = "Wrong:").grid(row=2,column=0,columnspan=1)

        labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # layout buttons in grid
        # create 1 function for every Button, function is in the loop
        # local function, defined inside another method/function
        for i in range(len(labels)):
            def cmd(key=labels[i]): 
                self.click(key)
            b = Button(self,command=cmd,text=labels[i],width=3,height=3)
            b.grid(row=i//6+3,column=i%6)

        if self.entry.get() == self.secretword:
            showinfo('Hangman','You Win!')
        else:
            if len(self.wrong.get()) >= 6:
                showinfo('Hangman','You Lose!')
        

    def click(self,key):
        print( 'click', key)
        if key in self.secretword:
            # Delete previous and add new masked
            self.entry.delete(0,END)
            self.entry.insert(END,mask(self.secretword,key+self.right.get()))
            if key not in self.right.get():         
                self.right.insert(END,key)
        else:
            if key not in self.wrong.get():
                self.wrong.insert(END,key)

if __name__ == "__main__":
  root = Tk()
  hangman("APPLE", root).pack()
           
