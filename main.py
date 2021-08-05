from tkinter import *
import datetime
import random

import time
# done
# dac przycisk wyjdz podczas gry



slowa = ["serious","occur","media","ready","sign","thought","list","individual","simple","quality","pressure","accept","answer","hard","resource","identify","left","meeting","determine","prepare","disease","whatever","success","argue","cup","particularly","amount","ability","staff","recognize","indicate","character","growth","loss","degree","wonder","attack","herself","region","television","box","TV","training","pretty","trade","deal","election","everybody","physical","lay","general","feeling","standard","bill","message","fail","outside","arrive","analysis","benefit","name","sex","forward","lawyer","present","section","environmental","glass","answer","skill","sister","PM","professor","operation","financial","crime","stage","ok","compare","authority","miss","design","sort","one","act","ten","knowledge","gun","station","blue","state","strategy","little","clearly","discuss","indeed","force","truth","song","example","democratic","check","environment","leg","dark","public","various","rather","laugh","guess","executive","set","study","prove","hang","entire","rock","design","enough","forget","since","claim","note","remove","manager","help","close","sound","enjoy","network","legal","religious","cold","form","final","main","science","green","memory","card","above","seat","cell","establish","nice","trial","expert","that","spring","firm","Democrat","radio","visit","management","care","avoid","imagine","tonight","huge","ball","no","close","finish","yourself","talk","theory","impact","respond","statement","maintain","charge","popular","traditional","onto","reveal","direction","weapon","employee","cultural","contain","peace","head","control","base","pain","apply","play","measure","wide","shake","fly","interview","manage","chair","fish","particular","camera","structure","politics","perform","bit","weight","suddenly","discover","candidate","top","production","treat","trip","evening","affect","inside","conference","unit","best","style","adult","worry"]


class App():
    def __init__(self):
        self.root = Tk()
        self.root.title('Type speed game')
        self.root.geometry("550x400")
        self.root.configure(background='white')

        self.logo = Label(self.root, text='60 seconds type speed game', bg='white', fg='black', font=("Helvetica", 20))
        self.logo.place(x=140,y=130)

        self.startbutton = Button(self.root, text='Start', command=self.startapp, bg='white', fg='black', highlightbackground='white')
        self.startbutton.place(x=240, y=200)

        self.zlelabel = Button(self.root, text='Bad', fg='red', bg='white', highlightbackground='white')

        self.dobrzelabel = Button(self.root, text='Good', fg='green', bg='white', highlightbackground='white')

        self.root.mainloop()

    def startapp(self):

        # zamykamy z poprzedniej gry
        self.zlelabel.place(x=6000,y=6000)
        self.dobrzelabel.place(x=6000,y=6000)
        try:
            self.koniec.destroy()
            self.statystykalabel1.destroy()
            self.statystykalabel2.destroy()
            self.statystykalabel3.destroy()
            self.zagrajjeszczeraz.destroy()
        except:
            pass


        self.word = slowa[random.randint(0,int(len(slowa)))]

        self.slowo = Button(self.root, text=self.word, width=15, bg='white', fg='black', highlightbackground='white')
        self.entryy = Entry(self.root, width=20, bg='white', fg='black', highlightbackground='white', insertbackground='black')
        self.entryy.bind("<Return>", self.wyslijslowo)

        self.slowo.place(x=185, y=100)
        self.entryy.place(x=173, y=200)
        self.entryy.focus()

        self.czas1 = datetime.datetime.now() 



        self.clock = Label(self.root, text='00:00', bg='white', fg='black')
        self.seconds = 0
        self.clock.place(x=254,y=10)
        self.updateclock()



        self.ileslow = 0

        self.iledobrze = 0
        self.ilezle = 0


        self.logo.place(x=10000,y=10000)
        self.startbutton.place(x=10000, y=10000)

    def updateclock(self):
        self.seconds+=1
        if self.seconds<10:
            text = '00:0'+str(self.seconds)
        elif self.seconds>59:
            minut = self.seconds//60
            text=str(minut)+":"+str(abs((60*minut) - self.seconds))

        else:
            text='00:'+str(self.seconds)



        self.clock.configure(text=text)

        self.after_id = self.root.after(1000, self.updateclock)


    def wyslijslowo(self, _Event=None):
        self.czas2 = datetime.datetime.now()
        x = str(self.czas2-self.czas1)
        print(x)
        if x[3]=="0" and x[2]=="0" and x[0]=="0":
            slowko = self.entryy.get()
            
            # sprawdzic czy poprawne jest wpisane slowo
            #print(slowko)
            #print(self.word)
            if slowko==self.word:
            # jesli tak:
                print('good')
                self.dobrzelabel.place(x=240,y=250)
                self.zlelabel.place(x=6000,y=0)

                self.ileslow+=1
                self.iledobrze+=1

                self.word = slowa[random.randint(0,int(len(slowa)))]
                self.slowo.configure(text=self.word)
                self.entryy.delete(0, END)

            else:
                print('bad')
                self.ilezle+=1
                self.zlelabel.place(x=245,y=250)
                self.dobrzelabel.place(x=6000,y=0)
        else:
            # koniec, pokaz statystyki

            self.root.after_cancel(self.after_id)
            self.clock.destroy()



            self.slowo.destroy()
            self.entryy.destroy()

            self.zlelabel.place(x=6000,y=6000)
            self.dobrzelabel.place(x=6000,y=6000)

            print('END')
            text2 = (str(self.ileslow) + " words per minute")
            text1 = (str(self.ileslow) + " WPM")
            text3 = "Good words: " + str(self.iledobrze) + ", bad: " + str(self.ilezle)

            self.koniec = Label(self.root, text='The end', font=('SF Pro Display', 25), bg='white', fg='black')
            self.koniec.place(x=180,y=50)

            self.statystykalabel1 = Label(self.root, text=text1, font=('SF Pro Display', 20), bg='white', fg='black')
            self.statystykalabel1.place(x=150, y=150)

            self.statystykalabel2 = Label(self.root, text=text2, font=('SF Pro Display', 20), bg='white', fg='black')
            self.statystykalabel2.place(x=150, y=150)

            self.statystykalabel3 = Label(self.root, text=text3, font=('SF Pro Display', 20), bg='white', fg='black')
            self.statystykalabel3.place(x=150, y=220)


            self.zagrajjeszczeraz = Button(self.root, text='Play again', command=self.startapp, bg='white', fg='black', highlightbackground='white')
            self.zagrajjeszczeraz.place(x=190, y=270)


App()