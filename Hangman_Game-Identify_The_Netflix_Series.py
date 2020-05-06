import random
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

class Hangman(Frame):

    def __init__(self,master):
        self.next_question()

    list_done = []
    def random_number_generator(self):
        #Randomly generating a whole number from 1 to 20 with a condition that it is not previously present in list_done [].
        #The condition helps in avoiding repetitions of quesitons so that player gets to see all 20 questions in his 20 chances.
        self.question_number = random.randrange(1,21,1)
        while self.question_number in self.list_done:
            self.question_number = random.randrange(1,21,1)

    def question_selector(self):
        #Selecting a question-answer pair based on the question number generated in def random_number_generator().
        #Also keeping a record of al previously selected question numbers (in list_done []) to avoid repetitions of questions.
        self.list_done.append(self.question_number)
        if self.question_number == 1:
            self.question = "A terminally ill Chemistry teacher teams with a former student to manufacture crystal meth to secure his family's future."
            self.answer = "Breaking Bad"
        elif self.question_number == 2:
            self.question = "A privileged New Yorker ends up in a women's prison when a past crime catches up with her in this Emmy-winning series."
            self.answer = "Orange is the New Black"
        elif self.question_number == 3:
            self.question = "When a young boy vanishes, a small town uncovers a mystery involving secret experiments, terrifying supernatural forces and one strange little girl."
            self.answer = "Stranger Things"
        elif self.question_number == 4:
            self.question = "Set in 1960s New York City, this award-winning series takes a peek inside an ad agency during an era when the cutthroat business had a glamorous lure."
            self.answer = "Mad Men"
        elif self.question_number == 5:
            self.question = "In this updated take on Sir Arthur Conan Doyle's beloved mystery tales, the eccentric sleuth prowls the streets of modern London in search of clues."
            self.answer = "Sherlock"
        elif self.question_number == 6:
            self.question = "Rich, unreasonably attractive private school students do horrible, scandalous things to each other. Repeatedly."
            self.answer = "Gossip Girl"
        elif self.question_number == 7:
            self.question = "After a teenage girl's perplexing suicide, a classmate receives a series of tapes that unravel the mystery of her tragic choice."
            self.answer = "13 Reasons Why"
        elif self.question_number == 8:
            self.question = "Love, laughter and the best friends you could ask for. Just like real life. But with really nice apartments."
            self.answer = "FRIENDS"
        elif self.question_number == 9:
            self.question = "Mild-mannered man works for the police department as a blood-splatter analyst but moonlights as a murderer who only targets other killers."
            self.answer = "Dexter"
        elif self.question_number == 10:
            self.question = "The true story of Columbia's infamously violent and powerful drug cartels fuels this gritty gangster drama series."
            self.answer = "Narcos"
        elif self.question_number == 11:
            self.question = "The boss is an idiot, the workers are clueless, elaborate pranks and feuds abound. Just another day at the office."
            self.answer = "The Office"
        elif self.question_number == 12:
            self.question = "A ruthless politician will stop at nothing to conquer Washington, D. C., in this Emmy and Golden Globe-winning political drama."
            self.answer = "House of Cards"
        elif self.question_number == 13:
            self.question = "While navigating the troubled waters of sex, romance, school, and family, a teen and his gang become entangled in a dark mystery."
            self.answer = "Riverdale"
        elif self.question_number == 14:
            self.question = "A notorious gang in 1919 Birmingham, England, is led by the fierce Tommy Shelby, a crime boss set on moving up in the world no matter the cost."
            self.answer = "Peaky Blinders"
        elif self.question_number == 15:
            self.question = "A super-powered woman who had a brief superhero career until an incident where the villainous Kilgrave caused her to kill someone. After that incident, she became a private investigator."
            self.answer = "Jessica Jones"
        elif self.question_number == 16:
            self.question = "The sleek world of tomorrow offers opportunities beyond our wildest dreams. At a price of our worse nightmares."
            self.answer = "Black Mirror"
        elif self.question_number == 17:
            self.question = "The story focuses on a seasoned and cynical Bombay police officer, summoned by an anonymous tip one morning, a voice which promises him an opportunity to capture a powerful criminal overlord of the G-Company. As the stakes mount, it becomes clear that the game the two players thought they were engaged in is in fact part of a much larger scenario, one that expands beyond their city."
            self.answer = "Sacred Games"
        elif self.question_number == 18:
            self.question = "One of Manhattan's top corporate lawyers sets out to recruit a new hotshot associate and hires the only guy that impresses him, a brilliant but unmotivated college dropout. Though he isn't actually a lawyer, this legal prodigy has the book smarts of a Harvard law grad and the street smarts of a hustler. However, in order to serve justice and save their jobs, both these unconventional thinkers must continue the charade."
            self.answer = "Suits"
        elif self.question_number == 19:
            self.question = "Eight thieves take hostages and lock themselves in the Royal Mint of Spain as a criminal mastermind manipulates the police to carry out his plan."
            self.answer = "Money Heist"
        else:
            self.question = "Family. Power. A young woman rises to rule an empire amid the challenges of the modern age."
            self.answer = "The Crown"

    def clicked(self,alphabet):
        ###image_paths = ['Step1.jpg','Step2.jpg','Step3.jpg','Step4.jpg','Step5.jpg']
        ###photo = Image.open(image_paths[self.count_negative])
        ###banner = Button(window,image=photo.resize(4)).grid(column=0,row=12,columnspan=12)
        #img = Image.open(image_paths[self.count_negative])
        #img = ImageTk.PhotoImage(img.resize((200,200)))
        #Hangman_Drawing = Button(root,image=img).grid(column=0,row=12,columnspan=5)
        answer = self.answer
        previous_position = 0
        if alphabet in self.answer.upper():
            while alphabet in answer.upper():
                position = answer.upper().find(alphabet)
                self.blanks[position + previous_position]["text"] = alphabet
                answer = answer[position + 1:]
                previous_position = previous_position + position + 1
                self.count_positive += 1
            if self.count_positive == (len(self.answer) - self.whitespace_count):
                messagebox.showinfo("Bravo!","You're right!")
                self.reset_blanks()
                self.next_question()
                if len(self.list_done) == 21:
                    messagebox.showinfo("Congratulations!", "You've completed the game!")
                    window.destroy()

        elif alphabet not in self.answer.upper():
            self.count_negative += 1
            Counter = Button(window, text=str(5 - self.count_negative) + " Chances Left.").grid(row=12, column=7,columnspan=6)
            if self.count_negative == 5:
                messagebox.showinfo("Sorry!","Game Over!")
                window.destroy()
                exit()

    def next_question(self):
        #Invoking methods to randomly select one question out of the question-bank consisting of 20 questions
        self.random_number_generator()
        self.question_selector()

        #Placing elements (Netflix image, title text, and question text) on the GUI window
        photo = PhotoImage(file="Netflix.png")
        self.banner = Button(window,text="hi",image=photo.subsample(3,5)).grid(column=0,row=0,columnspan=12)
        self.title = Label(window,text="HANGMAN GAME - GUESS THE NETFLIX SERIES",bg="Black",font=("Georgia",20),fg="red").grid(row=1,column=0,columnspan=12)
        self.question = Label(window,text=self.question,bg="Black",fg="White",wraplength=600)
        self.question.grid(row=2,column=0,columnspan=12)
        self.rounds = Label(window,text="Question # "+str(len(self.list_done))).grid(column=7,row=11,columnspan=6)

        #Placing one blank box on the window, per character in the Netflix series' name
        position = 0
        column_no = 0
        row_no = 0
        self.blanks = [Button]*100
        while position<len(self.answer):
            row_no = int(position/7)
            column_no = position - (7 * row_no)
            self.blanks[position] = Button(window,text=" ",bg="white",fg="Black",width=3,height=1)
            self.blanks[position].grid(column=column_no,row=3+row_no)
            position += 1

        #Placing alphanumeric keypad on the window to help the player enter characters for guessing the Netflix series' name
        self.count_positive = 0
        self.count_negative = 0
        self.whitespace_count = 0
        for character in self.answer:
            if character.isspace():
                self.whitespace_count += 1
        A = Button(window,text="A",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("A")).grid(column=7,row=3)
        B = Button(window,text="B",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("B")).grid(column=8,row=3)
        C = Button(window,text="C",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("C")).grid(column=9,row=3)
        D = Button(window,text="D",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("D")).grid(column=10,row=3)
        E = Button(window,text="E",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("E")).grid(column=11,row=3)
        F = Button(window,text="F",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("F")).grid(column=7,row=4)
        G = Button(window,text="G",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("G")).grid(column=8,row=4)
        H = Button(window,text="H",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("H")).grid(column=9,row=4)
        I = Button(window,text="I",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("I")).grid(column=10,row=4)
        J = Button(window,text="J",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("J")).grid(column=11,row=4)
        K = Button(window,text="K",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("K")).grid(column=7,row=5)
        L = Button(window,text="L",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("L")).grid(column=8,row=5)
        M = Button(window,text="M",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("M")).grid(column=9,row=5)
        N = Button(window,text="N",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("N")).grid(column=10,row=5)
        O = Button(window,text="O",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("O")).grid(column=11,row=5)
        P = Button(window,text="P",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("P")).grid(column=7,row=6)
        Q = Button(window,text="Q",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("Q")).grid(column=8,row=6)
        R = Button(window,text="R",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("R")).grid(column=9,row=6)
        S = Button(window,text="S",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("S")).grid(column=10,row=6)
        T = Button(window,text="T",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("T")).grid(column=11,row=6)
        U = Button(window,text="U",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("U")).grid(column=7,row=7)
        V = Button(window,text="V",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("V")).grid(column=8,row=7)
        W = Button(window,text="W",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("W")).grid(column=9,row=7)
        X = Button(window,text="X",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("X")).grid(column=10,row=7)
        Y = Button(window,text="Y",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("Y")).grid(column=11,row=7)
        Z = Button(window,text="Z",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("Z")).grid(column=7,row=8)
        a1 = Button(window,text="1",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("1")).grid(column=8,row=8)
        a2 = Button(window,text="2",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("2")).grid(column=9,row=8)
        a3 = Button(window,text="3",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("3")).grid(column=10,row=8)
        a4 = Button(window,text="4",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("4")).grid(column=11,row=8)
        a5 = Button(window,text="5",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("5")).grid(column=7,row=9)
        a6 = Button(window,text="6",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("6")).grid(column=8,row=9)
        a7 = Button(window,text="7",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("7")).grid(column=9,row=9)
        a8 = Button(window,text="8",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("8")).grid(column=10,row=9)
        a9 = Button(window,text="9",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("9")).grid(column=11,row=9)
        a0 = Button(window,text="0",bg="skyBlue",fg="Black",activebackground="Green",width=3,height=1,command=lambda:self.clicked("0")).grid(column=9,row=10)

    def reset_blanks(self):
        for position in range (0,len(self.answer)):
            self.blanks[position].grid_forget()
            self.question.grid_forget()

window = Tk()
window.geometry("645x550")
window.config(background="black")
window.title("Hangman Game - Guess the Netflix Series")
app = Hangman(window)
window.mainloop()
