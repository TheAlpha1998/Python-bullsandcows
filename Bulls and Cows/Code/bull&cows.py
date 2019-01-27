#-------------------------------------------------------------------------------
#Author- Om Rastogi
#Dated - 29-July-2015
#My 11th class project
#Project- BULLS AND COWS
#-------------------------------------------------------------------------------

class game:
    def __init__(self):
        self.array=[]
        self.x=[]
        self.bexit=None
        self.start=None
        self.subm=None
        self.head2=None
        self.g=None
        self.root=None
        self.e=0
        self.p=0
        self.py=0
        self.head2=None
        self.flag=0
        self.comm=None
        self.score=0
        self.scoreboard=None
        self.scoreboard1=None

    def mainwindow(self):
        print"hello, welcome to bulls and cows"
        import Tkinter
        self.root = Tkinter.Tk()
        self.root.title("bulls and cows")
        self.root.config(bg="#8FD2F9")
        self.root.geometry("600x400")
        w = Tkinter.Canvas(self.root, width=596, height=396, bg="#8FD2F9")
        w.place(x=0,y=0)
        w.create_line(260, 0, 260, 400, fill="#FFFFFF", width=2)
        w.create_line(0, 350, 600, 350, fill="#003B59", width=40)
        w.create_line(0, 322, 600, 322, fill="#FFFFFF", width=2)
        w.create_line(260, 48, 600, 48, fill="#FFFFFF", width=2)
        w.create_line(260, 80, 600, 80, fill="#FFFFFF", width=2)
        w.create_line(455, 80, 455, 320, fill="#FFFFFF", width=2)
        w.create_line(378, 80, 378, 320, fill="#FFFFFF", width=2)

        self.bexit=Tkinter.Button(self.root,text="EXIT",font=('Arial', 28),fg="#00DB7B",bg="#003B59",command=self.exitme)
        self.bexit.place(x=10,y=200)
        self.bexit.config(width=10, height=1)

        self.start=Tkinter.Button(self.root,text="RESET",font=('Arial', 28),fg="#00DB7B",bg="#003B59",command=self.give)#start
        self.start.config(width=10, height=1)
        self.start.place(x=10,y=100)

        self.comm = Tkinter.Label(self.root, text="ONLY EIGHT INPUTS ARE ALLOWED", font=('Arial', 20))
        self.comm.place(x=50,y=330)
        self.comm.config(fg="#8FD2F9",bg="#003B59")

        self.subm=Tkinter.Button(self.root,text="SUBMIT",font=('Bold', 11,),fg="#0068E4",bg="#CDE8FF",command=self.sub)#initialized in method give(

        self.g = Tkinter.Entry(self.root,font=('Arial', 10),)#entry

        self.scoreboard= Tkinter.Label(self.root, text="SCORE:", font=('Arial', 20),bg="#8FD2F9")

        #self.scoreboard1= Tkinter.Label(self.root, text=self.score, font=('Arial', 20),bg="#8FD2F9")

        self.head2 = Tkinter.Label(self.root, text="NUMBER    COWS     BULLS", font=('Arial', 15),bg="#8FD2F9")

        heading = Tkinter.Label(self.root, text="Bulls & Cows", font=('Arial', 30),fg="#8FD2F9", bg="#003B59")
        heading.place(x=10,y=10)

        self.give()

        self.root.mainloop()

    def give(self):
        if self.flag!=0:
            self.flag=0
            self.exitme()
            self.mainwindow()
        self.array=[]
        self.flag=1
        self.py=0
        import Tkinter
        import random
        for i in range (0,4):
            x = random.randint(0,9)
            while self.array.__contains__(x):
                x = random.randint(0,9)
            self.array.append(x)

        self.head2.place(x=280,y=50)
        self.subm.place(x=330,y=10)
        self.g.place(x=410,y=20)
        self.g.focus_set()#subm
        print self.array


    def exitme(self):
        self.root.destroy()


    def input(self):
        self.x=[]
        s1=""
        self.g.focus_set()
        s1=self.g.get()
        if len(s1)!=4:
            return 0

        f=int(self.g.get())

        for i in range (0,4):
            d=f%10
            self.x.append(d)
            f=f/10
        self.x[0],self.x[1],self.x[2],self.x[3]=self.x[-1],self.x[-2],self.x[-3],self.x[-4]
        print self.x
        return 1

    def exist(self):
            self.e=0
            for i in range (0,4):
                for j in range (0,4):
                    if self.x[i]==self.array[j]:
                        self.e+=1
                        if i>0:
                            if self.x[i]==self.x[i-1] and self.x[i]==self.array[j] and self.e>0:
                                self.e-=1
            return self.e

    def position(self):
            self.p=0
            for i in range (0,4):
                if self.x[i]==self.array[i]:
                    self.p+=1
            return self.p

    def decision(self):
        self.py+=30
        import Tkinter
        self.e=self.exist()
        self.p=self.position()
        if self.p==4:
             self.score=1100-(self.py*100)/30
             self.scoreboard1= Tkinter.Label(self.root, text=self.score, font=('Arial', 20),bg="#8FD2F9")
             self.scoreboard1.place(x=120,y=280)
             self.scoreboard.place(x=10,y=280)
             win = Tkinter.Label(self.root, text="       CONGRATULATION YOU WON!!                     ", font=('Arial', 20),fg="#8FD2F9",bg="#003B59")
             win.place(x=50,y=330)
             self.subm.config(state='disabled')

        elif self.py==(30*8):
            self.score=0
            self.scoreboard1= Tkinter.Label(self.root, text=self.score, font=('Arial', 20),bg="#8FD2F9")
            self.scoreboard1.place(x=120,y=280)

            self.scoreboard.place(x=10,y=280)
            lose = Tkinter.Label(self.root, text="  YOU LOST!! THE NUMBER IS: ", font=('Arial', 20),fg="#8FD2F9",bg="#003B59")
            lose.place(x=35,y=330)
            num3 =Tkinter.Label(self.root, text=self.array, font=('Arial', 20),fg="#8FD2F9",bg="#003B59")
            num3.place(x=440,y=330)
            self.subm.config(state='disabled')
        self.g.delete(0, 'end')

    def exception1(self):
        import Tkinter
        import tkMessageBox
        tkMessageBox.showinfo("Error","Enter any four digit number only. Eg-8397")

#-------------------------------------------------------------------------------
    def sub(self):
        import Tkinter
        a1=self.input()
        if a1==0:
            self.exception1()
            self.g.delete(0, 'end')
            return None
        self.decision()
        num = Tkinter.Label(self.root, text=self.x, font=('Arial', 15),bg="#8FD2F9")
        num.place(x=290,y=52+self.py)
        num1 = Tkinter.Label(self.root, text=self.e, font=('Arial', 15),bg="#8FD2F9")
        num1.place(x=410,y=52+self.py)
        num2 = Tkinter.Label(self.root, text=self.p, font=('Arial', 15),bg="#8FD2F9")
        num2.place(x=510,y=52+self.py)

#-------------------------------------------------------------------------------
    @classmethod
    def help_(self):
        import Tkinter
        def exitme():
            root.destroy()
        root = Tkinter.Tk()
        root.config(bg="#00E784")

        root.title("bulls and cows")
        root.geometry("600x400")

        help1="Bulls and Cows Game is also known as MasterMind. Computer selects a four digit number, all four digits are different. In current implementation number may not begin with 0. Any number can be guessed in 8 tries or less. Cow column displays total number of digits you guessed right, Bulls shows how many of those that exists were placed at the right spots."
        Tkinter.Message(root, text=help1, font=("Helvetica", 18),bg="#00E784").grid(row=70, column=70, columnspan=3)


        hback=Tkinter.Button(root,text="BACK",bg="#71D5FF",font=('Arial', 20),command=exitme)
        hback.place(x=450,y=20)
        root.mainloop()


def main():
    import Tkinter
    root = Tkinter.Tk()
    mygame = game()
    def exitme():
        root.destroy()
    root.title("bulls and cows")
    root.config(bg="#9FB2BF")
    root.geometry("600x400")
    heading1 = Tkinter.Label(root, text="Bulls & Cows", font=('Arial', 30))
    heading1.place(x=190,y=10)
    heading1.config(bg="#0C1C38",fg="#9FB2BF")
    help1=Tkinter.Button(root,text="HELP",font=('Arial', 30),command=mygame.help_)
    help1.place(x=189,y=200)
    help1.config(width=10, height=1)
    help1.config(bg="#0C1C38",fg="#FFAF00")
    but=Tkinter.Button(root,text="PLAY",font=('Arial', 30),command=mygame.mainwindow)
    but.place(x=189,y=100)
    but.config(width=10, height=1)
    but.config(bg="#0C1C38",fg="#FFAF00")
    mexit=Tkinter.Button(root,text="EXIT",font=('Arial', 30),command=exitme)
    mexit.place(x=189,y=300)
    mexit.config(width=10, height=1)
    mexit.config(bg="#0C1C38",fg="#FFAF00")
    root.mainloop()

main()