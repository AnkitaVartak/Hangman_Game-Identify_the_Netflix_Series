import random
from tkinter import *

# (Lower & upper limit)
MAX = 10
MIN = 1



class Application(Frame):
    """The GUI application (Guess My Number)."""

    __slots__ = "number", "tries", "question", "ans", "qlabel", "list_done"

    def __init__(self, master):
        """Initialize Frame."""
        Frame.__init__(self, master)

        master.minsize(width=200, height=100)

        self.list_done = []

        self.qlabel = Label(self)

        self.grid()

        self.reset()

    def set_game(self):
        qno = self.number

        self.list_done.append(qno)

        if self.number == 1:
            self.question = "A terminally ill Chemistry teacher teams with a former student to manufacture crystal meth to secure his family's future."
            self.ans = "Breaking Bad"

        elif self.number == 2:
            self.question = "A privileged New Yorker ends up in a women's prison when a past crime catches up with her in this Emmy-winning series."
            self.ans = "Orange is the New Black"

        elif self.number == 3:
            self.question = "When a young boy vanishes, a small town uncovers a mystery involving secret experiments, terrifying supernatural forces and one strange little girl."
            self.ans = "Stranger Things"

        elif self.number == 4:
            self.question = "Set in 1960s New York City, this award-winning series takes a peek inside an ad agency during an era when the cutthroat business had a glamorous lure."
            self.ans = "Mad Men"

        elif self.number == 5:
            self.question = "In this updated take on Sir Arthur Conan Doyle's beloved mystery tales, the eccentric sleuth prowls the streets of modern London in search of clues."
            self.ans ="Sherlock"

        elif self.number == 6:
            self.question = "Rich, unreasonably attractive private school students do horrible, scandalous things to each other. Repeatedly."
            self.ans ="Gossip Girl"


        elif self.number == 7:
            self.question = "After a teenage girl's perplexing suicide, a classmate receives a series of tapes that unravel the mystery of her tragic choice."
            self.ans ="13 Reasons Why"


        elif self.number == 8:
            self.question = "Love, laughter and the best friends you could ask for. Just like real life. But with really nice apartments."
            self.ans ="F.R.I.E.N.D.S"


        elif self.number == 9:
            self.question = "Mild-mannered man works for the police department as a blood-splatter analyst but moonlights as a murderer who only targets other killers."
            self.ans ="Dexter"


        elif self.number == 10:
            self.question = "The true story of Columbia's infamously violent and powerful drug cartels fuels this gritty gangster drama series."
            self.ans ="Narcos"


        elif self.number == 11:
            self.question = "The boss is an idiot, the workers are clueless, elaborate pranks and feuds abound. Just another day at the office."
            self.ans ="The Office"


        elif self.number == 12:
            self.question = "A ruthless politician will stop at nothing to conquer Washington, D. C., in this Emmy and Golden Globe-winning political drama."
            self.ans ="House of Cards"


        elif self.number == 13:
            self.question = "While navigating the troubled waters of sex, romance, school, and family, a teen and his gang become entangled in a dark mystery."
            self.ans ="Riverdale"


        elif self.number == 14:
            self.question = "A notorious gang in 1919 Birmingham, England, is led by the fierce Tommy Shelby, a crime boss set on moving up in the world no matter the cost."
            self.ans ="Peaky Blinders"

            
        elif self.number == 15:
            self.question = "A super-powered woman who had a brief superhero career until an incident where the villainous Kilgrave caused her to kill someone. After that incident, she became a private investigator."
            self.ans ="Jessica Jones"

            
        elif self.number == 16:
            self.question = "The sleek world of tomorrow offers opportunities beyond our wildest dreams. At a price of our worse nightmares."
            self.ans ="Black Mirror"

            
        elif self.number == 17:
            self.question = "The story focuses on a seasoned and cynical Bombay police officer, summoned by an anonymous tip one morning, a voice which promises him an opportunity to capture a powerful criminal overlord of the G-Company. As the stakes mount, it becomes clear that the game the two players thought they were engaged in is in fact part of a much larger scenario, one that expands beyond their city."
            self.ans ="Sacred Games"

            
        elif self.number == 18:
            self.question = "One of Manhattan's top corporate lawyers sets out to recruit a new hotshot associate and hires the only guy that impresses him, a brilliant but unmotivated college dropout. Though he isn't actually a lawyer, this legal prodigy has the book smarts of a Harvard law grad and the street smarts of a hustler. However, in order to serve justice and save their jobs, both these unconventional thinkers must continue the charade."
            self.ans ="Suits"

            
        elif self.number == 19:
            self.question = "Eight thieves take hostages and lock themselves in the Royal Mint of Spain as a criminal mastermind manipulates the police to carry out his plan."
            self.ans ="Money Heist"
            
        else:
            self.question = "Family. Power. A young woman rises to rule an empire amid the challenges of the modern age."
            self.ans ="The Crown"


    def create_widgets(self):
        """Program all the widgets to be used."""
        if self.qlabel is not None:
            self.qlabel.grid_forget()

        #self.qlabel = Label(self, text = self.question)

        #self.qlabel.grid(row=0, column=0, columnspan=2, sticky=W)

        Label(self, text = self.question).grid(row=0, column=0, columnspan=2, sticky=W)

        Label(self,
              text="Try to guess the answer"
              ).grid(row=1, column=0, columnspan=2, sticky=W)

        Label(self,
              text="Rounds done : 0"
              ).grid(row=0, column=2, columnspan=1, sticky=W)

        Label(self,
              text="Guess"
              ).grid(row=2, column=0, sticky=W)


        # Entry widget to allow guessing
        self.guess_ent = Entry(self)
        self.guess_ent.grid(row=2, column=1, sticky=W)

        # Submit button to obtain guess
        Button(self,
               text="Enter",
               command=self.get_guess
               ).grid(row=2, column=2, columnspan=4, sticky=W)
        Button(self,
               text="Reset",
               command=self.reset
               ).grid(row=1, column=2, columnspan=1, sticky=W)

        self.results_txt = Text(self, width=40, height=5, wrap=WORD)
        self.results_txt.grid(row=3, column=0, columnspan=3)

    def get_guess(self):
        """Obtain the player's guess and verify it."""
        try:
            guess = str(self.guess_ent.get())
        except(ValueError):
            self.display_message("Invalid entry. Try again.")
        else:
            self.tries += 1
            if self.tries == 10:
                self.display_message("You win!!")
                self.guess_ent.grid_forget()
                #Label(self, text="     You won!!                    ").grid(row=3, column=0, columnspan=3)
                #print("You won!!")
                #exit(0)
            Label(self,
                  text="Rounds done : " + str(self.tries)
                  ).grid(row=0, column=2, columnspan=1, sticky=W)
            self.check_guess(guess)

    def next_question(self):

        self.number = random.randrange(MIN, MAX + 1)
        while self.number in self.list_done:
            self.number = random.randrange(MIN, MAX + 1)

        self.set_game()

        #Label(self, text="                                       ").grid(row=0, column=0, columnspan=2, sticky=W)

        self.qlabel.grid_forget()

        self.qlabel = Label(self, text=self.question)

        #Label(self, text=self.question).grid(row=0, column=0, columnspan=2, sticky=W)

        self.qlabel.grid(row=0, column=0, columnspan=2, sticky=W)


        #self.qlabel.text = self.question

    def check_guess(self, guess):
        """
        Verify if the player's guess is correct.
        Keyword argument:
        guess - the int value to be verified
        """

        if guess == self.ans:
            self.next_question()
            self.display_message("Correct Answer")
            return

        else:
            self.display_message("Wrong Answer. Game Over!")
            self.guess_ent.grid_forget()
            #Label(self, text = "     Wrong Answer. Game Over!     ").grid(row=3, column=0, columnspan=3)
            #print("Wrong Answer. Game Over!")
            #exit(0)
            return

        '''if guess < MIN or guess > MAX:
            self.display_message("Invalid Input, Guess Out Side Of Range.")
            self.tries -= 1  # This try doesn't count
            return

        # If guess equals the number, end current game.
        if guess == self.number:
            self.resetgame()
            return

        # Otherwise, see if guess is higher or lower than the chosen number.
        if guess < self.number:
            self.display_message("Guess Higher...")
            return
        elif guess > self.number:
            self.display_message("Guess Lower...")
            return
        '''



    def display_message(self, message):
        """
        Display a message on the text box.
        Keyword argument:
        message -- the message to be displayed

        """
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, message)

    def reset(self):
        """Prepare for a new game."""
        # Word to be guessed by player.
        self.number = random.randrange(MIN, MAX + 1)
        while self.number in self.list_done:
            self.number = random.randrange(MIN, MAX + 1)

        self.tries = 0

        self.set_game()

        self.create_widgets()
        '''self.number = random.randrange(MIN, MAX + 1)
        self.display_message("Game Reset. Please enter another number to play again.")
        self.tries = 0
        Label(self,
              text="Number Of Tries: " + str(self.tries)
              ).grid(row=0, column=2, columnspan=1, sticky=W)'''
    def resetgame(self):
        self.display_message("Congrats! You guessed correctly. The number was " + \
                             str(self.number) + ". And it only took you " + \
                             str(self.tries) + " tries!" + " Click The Reset Button To Play Again" )


def main():
    """Kickstart Guess My Number."""
    root = Tk()
    root.title("Guess The Word")
    app = Application(root)
    root.mainloop()



# start Guess The Number
main()
