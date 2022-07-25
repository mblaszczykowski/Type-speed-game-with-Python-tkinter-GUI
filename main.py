from tkinter import *
import datetime
import random
import time

words = ["serious","occur","media","ready","sign","thought","list","individual","simple","quality","pressure","accept","answer","hard","resource","identify","left","meeting","determine","prepare","disease","whatever","success","argue","cup","particularly","amount","ability","staff","recognize","indicate","character","growth","loss","degree","wonder","attack","herself","region","television","box","TV","training","pretty","trade","deal","election","everybody","physical","lay","general","feeling","standard","bill","message","fail","outside","arrive","analysis","benefit","name","sex","forward","lawyer","present","section","environmental","glass","answer","skill","sister","PM","professor","operation","financial","crime","stage","ok","compare","authority","miss","design","sort","one","act","ten","knowledge","gun","station","blue","state","strategy","little","clearly","discuss","indeed","force","truth","song","example","democratic","check","environment","leg","dark","public","various","rather","laugh","guess","executive","set","study","prove","hang","entire","rock","design","enough","forget","since","claim","note","remove","manager","help","close","sound","enjoy","network","legal","religious","cold","form","final","main","science","green","memory","card","above","seat","cell","establish","nice","trial","expert","that","spring","firm","Democrat","radio","visit","management","care","avoid","imagine","tonight","huge","ball","no","close","finish","yourself","talk","theory","impact","respond","statement","maintain","charge","popular","traditional","onto","reveal","direction","weapon","employee","cultural","contain","peace","head","control","base","pain","apply","play","measure","wide","shake","fly","interview","manage","chair","fish","particular","camera","structure","politics","perform","bit","weight","suddenly","discover","candidate","top","production","treat","trip","evening","affect","inside","conference","unit","best","style","adult","worry"]

class App():
    def __init__(self):
        self.root = Tk()
        self.root.title('Type speed game')
        self.root.geometry("550x400")
        self.root.configure(background='white')

        self.logo = Label(self.root, text='60 seconds type speed game', bg='white', fg='black', font=("Helvetica", 20))
        self.logo.place(x=140,y=130)

        self.startButton = Button(self.root, text='Start', command=self.startapp, bg='white', fg='black', highlightbackground='white')
        self.startButton.place(x=240, y=200)

        self.badLabel = Button(self.root, text='Bad', fg='red', bg='white', highlightbackground='white')

        self.goodLabel = Button(self.root, text='Good', fg='green', bg='white', highlightbackground='white')

        self.root.mainloop()

    def startapp(self):
        # Cleaning from the previous game
        self.badLabel.place(x=6000,y=6000)
        self.goodLabel.place(x=6000,y=6000)
        try:
            self.theEnd.destroy()
            self.statsLabel1.destroy()
            self.statsLabel2.destroy()
            self.statsLabel3.destroy()
            self.playAgain.destroy()
        except:
            pass

        self.word = words[random.randint(0,int(len(words)))]

        self.wordLabel = Button(self.root, text=self.word, width=15, bg='white', fg='black', highlightbackground='white')
        self.entryy = Entry(self.root, width=20, bg='white', fg='black', highlightbackground='white', insertbackground='black')
        self.entryy.bind("<Return>", self.sendWordLabel)

        self.wordLabel.place(x=185, y=100)
        self.entryy.place(x=173, y=200)
        self.entryy.focus()

        self.time1 = datetime.datetime.now() 

        self.clock = Label(self.root, text='00:00', bg='white', fg='black')
        self.seconds = 0
        self.clock.place(x=254,y=10)
        self.updateClock()

        self.howManyWords = 0
        self.howManyWordsCorrect = 0
        self.howManyWordsBad = 0

        self.logo.place(x=10000,y=10000)
        self.startButton.place(x=10000, y=10000)

    def updateClock(self):
        self.seconds+=1
        if self.seconds<10:
            text = '00:0'+str(self.seconds)
        elif self.seconds>59:
            minut = self.seconds//60
            text=str(minut)+":"+str(abs((60*minut) - self.seconds))

        else:
            text='00:'+str(self.seconds)

        self.clock.configure(text=text)

        self.after_id = self.root.after(1000, self.updateClock)


    def sendWordLabel(self, _Event=None):
        self.czas2 = datetime.datetime.now()
        x = str(self.czas2-self.time1)
        print(x)
        if x[3]=="0" and x[2]=="0" and x[0]=="0":
            wordFromEntry = self.entryy.get()
            
            if wordFromEntry==self.word:
                self.goodLabel.place(x=240,y=250)
                self.badLabel.place(x=6000,y=0)

                self.howManyWords+=1
                self.howManyWordsCorrect+=1

                self.word = words[random.randint(0,int(len(words)))]
                self.wordLabel.configure(text=self.word)
                self.entryy.delete(0, END)

            else:
                print('bad')
                self.howManyWordsBad+=1
                self.badLabel.place(x=245,y=250)
                self.goodLabel.place(x=6000,y=0)
        else:
            # The end, show statistics
            self.root.after_cancel(self.after_id)
            self.clock.destroy()

            self.wordLabel.destroy()
            self.entryy.destroy()

            self.badLabel.place(x=6000,y=6000)
            self.goodLabel.place(x=6000,y=6000)

            text1 = (str(self.howManyWords) + " WPM")
            text2 = (str(self.howManyWords) + " words per minute")
            text3 = "Good words: " + str(self.howManyWordsCorrect) + ", bad: " + str(self.howManyWordsBad)

            self.theEnd = Label(self.root, text='The end', font=('SF Pro Display', 25), bg='white', fg='black')
            self.theEnd.place(x=180,y=50)

            self.statsLabel1 = Label(self.root, text=text1, font=('SF Pro Display', 20), bg='white', fg='black')
            self.statsLabel1.place(x=150, y=150)

            self.statsLabel2 = Label(self.root, text=text2, font=('SF Pro Display', 20), bg='white', fg='black')
            self.statsLabel2.place(x=150, y=150)

            self.statsLabel3 = Label(self.root, text=text3, font=('SF Pro Display', 20), bg='white', fg='black')
            self.statsLabel3.place(x=150, y=220)


            self.playAgain = Button(self.root, text='Play again', command=self.startapp, bg='white', fg='black', highlightbackground='white')
            self.playAgain.place(x=190, y=270)


App()