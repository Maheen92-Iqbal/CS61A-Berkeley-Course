import hog
import dice
from ucb import main

import Tkinter as tk
from Tkinter import *
import argparse



playerselect = '#5FFB17'
select_bg = '#F75D59'
bg1='#E55451'
bg2 = '#CCFB5D'

fg='#ffffff'
font=('Arial', 12)

button_theme = {
    'font': font,
    'activebackground': select_bg,
    'bg': bg1,
    'fg': fg,
}

frame_theme = {
    'bg': bg2,
}

label_theme = {
    'font': font,
    'bg': bg2,
    'fg': fg,
}  

entry_theme = {
    'fg': fg,
    'bg': bg2,
    'font': font,
    'insertbackground': fg,
}  

class BetterWidget(object):
    """A BetterWidget returns itself on pack and config for call chaining."""
    def pack(self, **kwargs):
        super(BetterWidget,self).pack(**kwargs)
        return self

    def config(self, **kwargs):
        super(BetterWidget,self).config(**kwargs)
        return self
     
class TextWidget(BetterWidget):
    
    def __init__(self, **arguments):
        
        #for label and entry widget we need to first extract the stringvar() which is the text variable after that we set that
        #as the textvariable = self.textvar
        self.textvar = arguments.get('textvariable', tk.StringVar())
        self.config(textvariable = self.textvar)
        
        #this is for when we need to set the text through Label(parent,text= '')
        
        if 'text' in arguments:
            
            self.textvar.set(arguments['text'])
     
    #so we can use this method anywhere without referencing it with its class       
    @property
    def text(self):
        
        return self.textvar.get()
    
    #if we need to set any value of the text than we use the setter attribute    
    @text.setter
    def text(self,value):
        
        return self.textvar.set(str(value))
        
class Label(TextWidget, tk.Label):
    """A Label is a text label."""
    def __init__(self, *args, **kwargs):
        kwargs.update(label_theme)
        tk.Label.__init__(self, *args, **kwargs)
        TextWidget.__init__(self,**kwargs)

class Button(BetterWidget, tk.Button):
   
    #__init__ returns the newly created object
    #self provides a reference to this instance
    
    def __init__(self, *args, **kwargs):
        kwargs.update(button_theme)
        
        #it inherits the tk.Button super class and we can use its methods in this way 
        tk.Button.__init__(self, *args, **kwargs)

class Entry(TextWidget, tk.Entry):
    """An Entry widget accepts text entry."""
    def __init__(self, *args, **kwargs):
        kwargs.update(entry_theme)
        tk.Entry.__init__(self, *args, **kwargs)
        TextWidget.__init__(self,**kwargs)

class Frame(BetterWidget, tk.Frame):
    """A Frame contains other widgets."""
    def __init__(self, *args, **kwargs):
        kwargs.update(frame_theme)
        tk.Frame.__init__(self, *args, **kwargs)
  
def name(who):
    
    return 'Player {0}'.format(who)
    
    
class HogGameException(BaseException):
    """HogGUI-specific Exception. Used to exit a game prematurely."""
    pass
        
class HogGame(Frame):
    
    KILL = -9
    
    def __init__(self,parent):
        
        #This reference to the next instance after HogGame which would be Frame
        super(HogGame,self).__init__(parent)
        self.pack()
        self.parent = parent
        self.who = 0
        self.initScores()
        self.initRolls()
        
        self.init_status()
        self.init_dice_images()
        hog.six_sided = dice.make_fair_dice(6)
        hog.four_sided = dice.make_fair_dice(4)
        self.play()
               
    def initScores(self):
        
        #we are making a frame with self as the parent window and then we are making that window visible too by packing it
        self.scoreFrame = Frame(self).pack()
        
        self.p_frames = [None, None]
        self.p_labels = [None, None]
        self.s_labels = [None, None]
        for i in range(0, 2):
            self.p_frames[i] = Frame(self.scoreFrame, padx=50).pack(side=LEFT)
            self.p_labels[i] = Label(self.p_frames[i],text=name(i) + ':').pack()
            self.s_labels[i] = Label(self.p_frames[i]).pack()
        
     
    def initRolls(self):
        
        self.RollFrame = Frame(self,pady=20).pack()
        self.RollLabel = Label(self.RollFrame).pack()
        self.RollEntry = Entry(self.RollFrame,justify=CENTER)
        self.RollEntry.bind('<Return>',lambda event: self.RollButton.invoke())
        self.RollEntry.pack()
        self.IntVariable = IntVar()
        self.RollButton = Button(self.RollFrame,text='Roll',command=self.roll,padx=10).pack(pady=10)
        
    def init_status(self):
        
        self.status_label = Label(self).pack()
        
      
    def init_dice_images(self):
        
        self.imageFrame1 = Frame(self).pack()
        self.imageFrame2 = Frame(self).pack()
        
        self.images = { 0: PhotoImage(file='D:\python\CS61A\hog\images\die1.gif'),
        1: PhotoImage(file='D:\python\CS61A\hog\images\die2.gif'),
        2: PhotoImage(file='D:\python\CS61A\hog\images\die3.gif'),
        3: PhotoImage(file='D:\python\CS61A\hog\images\die4.gif'),
        4: PhotoImage(file='D:\python\CS61A\hog\images\die5.gif'),
        5: PhotoImage(file='D:\python\CS61A\hog\images\die6.gif'),}

        self.firstHalf_frames = {}
        self.firstHalf_labels = {}
       
        for i in range(0, 3):
            
            self.firstHalf_frames[i] = Frame(self.imageFrame1).pack(side=LEFT)
            self.firstHalf_labels[i] = Label(self.firstHalf_frames[i],image=self.images[i]).pack()
            
        self.secondHalf_frames = {}
        self.secondHalf_labels = {}
       
        for i in range(3, 6):
            
            self.secondHalf_frames[i] = Frame(self.imageFrame2).pack(side=LEFT)
            self.secondHalf_labels[i] = Label(self.secondHalf_frames[i],image=self.images[i]).pack()
            
        self.extralabel = Label(self).pack()
        
    def roll(self):
        
        #we set the text or the roll number that we enter into the entry field in that specific int variable
        result = self.RollEntry.text
        self.IntVariable.set(int(result))
        
    def switch(self,who=None):
        
        self.p_frames[self.who].config(bg=bg2)
        self.p_labels[self.who].config(bg=bg2)
        self.s_labels[self.who].config(bg=bg2)
        
        self.who = 1 - self.who
        if self.who is None:
            self.who = 0
            
        self.p_frames[self.who].config(bg=playerselect)
        self.p_labels[self.who].config(bg=playerselect)
        self.s_labels[self.who].config(bg=playerselect)
        
    
    def strategy(self,score,opponent_score):
        
        if self.who == 0:
            
            s0 = score
            s1 = opponent_score
            
        else:
            
            s0 = opponent_score
            s1 = score
            
        self.s_labels[0].text = s0
        self.s_labels[1].text = s1
        
        self.RollLabel.text = name(self.who) + ' will roll'
        self.status = self.status_label.text
        
        if hog.select_dice(score,opponent_score) == hog.four_sided:
            
            self.status += ' Hog Wild' 
        
        #we remove the Hog Wild before moving further and printing the rolls that the player has played    
        self.status_label.text = self.status
            
        #to stop the mainloop we use the wait_variable            
        self.wait_variable(self.IntVariable)
        
        result = self.IntVariable.get()
        self.RollEntry.text = ''
        
        self.status_label.text = '{} chose to role {}'.format(name(self.who),result)
        
        self.switch()
        
        return result
        
    def play(self):
        
        self.switch(1)
        
        self.s_labels[0].text = '0'
        self.s_labels[1].text = '0'
        self.status_label.text = ''
        
        try:
             score, opponent_score = hog.play(self.strategy,
                                             self.strategy)
        except HogGameException:
            pass
            
        else:
            
            #this is used when we just break from the loop after having the score uptill or more than 100
            #as after breaking from the loop the strategy method is not applicable so in order to print the final score
            #we need to set the labels like this.
            
            self.s_labels[0].text = score
            self.s_labels[1].text = opponent_score
            
            if score > opponent_score:
                
                winner = 0
            else:
                winner = 1
                
            self.status_label.text = 'Game Over! {} Wins'.format(name(winner))

    def destroy(self):
        """Overrides the destroy method to end the current game."""
        self.IntVariable.set(HogGame.KILL)
        super(HogGame,self).destroy()

root = Tk()
root.configure(background='#F75D59')
root.title('The Game of Hog')
root.minsize(520, 400)
root.geometry("600x500")
HogGame(root)


#This loop waits for an input and if it gets one than it sends the message so we need to program the internal widgets that how
#they can respond to that message.
root.mainloop()
