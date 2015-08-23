from Tkinter import *
import subprocess
import os

main = Tk()


class Menu(object):
    def __init__(self):
        main.title('Leap of Faith')
        main.geometry('800x500+283+50')
        
        
        
        self.start_button = Button(main,text="Start Game!",command=self.start)
        self.about_button = Button(main,text="About the Game!",command=self.about)
        self.settings_button = Button(main,text="Settings",command=self.settings)
        
        
        self.start_button.pack(pady=30,fill='x')
        self.settings_button.pack(pady=30,fill='x')
        self.about_button.pack(pady=30,fill='x')
    def start(self):
        level = Toplevel()
        level.geometry("800x500+283+50")
        level.title("Select Level")
        
        
        level_selection = Spinbox(level,values=("1","2","3","4","5","6","7","8","9","10"))
        level_selection.pack()
        
        def check():
            with open('progress.txt','r') as progress:
                lvl = progress.read()
            
            test = level_selection.get()
            
            if int(lvl) < int(test)-1:
                hah = Toplevel()
                hah.geometry("400x200+533+200")
                hah.title("Oops!")
                    
                wrong = Label(hah,text="It seems you haven't yet completed the previous level!")
                wrong.pack()
            else:
                with open('choice.txt','w') as chosen:
                    chosen.write("%s" % level_selection.get())
                level.destroy()
                os.system('python main.py')
                    
                    
            
                    
        start_button = Button(level,text="Start Level!",command=check)
        start_button.pack()
        
    def about(self):
        about_window = Toplevel()
        about_window.geometry("600x300+383+100")
        about_window.title("About the Game")
        
        self.about_label = Label(about_window,text="""\n\n\n\n\nCreated by Adrian Cisneros,\nfor anyone to enjoy!""")
        self.about_label.pack()
        
        self.close_about = Button(about_window,text="Close",command=about_window.destroy)
        self.close_about.pack(pady=50)
        
        
    def settings(self):
        self.settingsw = Toplevel()
        self.settingsw.geometry("800x500+283+50")
        self.settingsw.title("Settings")
        
        self.controls = Label(self.settingsw,text="""Controls:""")
        self.jump = Label(self.settingsw,text="Climb:")
        self.left = Label(self.settingsw,text="Left:")
        self.right = Label(self.settingsw,text="Right:")
        self.fire = Label(self.settingsw,text="Shoot:")
        self.switch = Label(self.settingsw,text="Switch Firing Mode:")
        
        self.jentry = Entry(self.settingsw)
        self.jentry.insert(END,"Up")
        self.lentry = Entry(self.settingsw)
        self.lentry.insert(END,"Left")
        self.rentry = Entry(self.settingsw)
        self.rentry.insert(END,"Right")
        self.fentry = Entry(self.settingsw)
        self.fentry.insert(END,"Button-1")
        
        self.sentry = Entry(self.settingsw)
        self.sentry.insert(END,"q")
        
        
        
        
        self.controls.grid(row=0,column=0)
        self.jump.grid(row=1,column=1)
        self.left.grid(row=2,column=1)
        self.right.grid(row=3,column=1)
        self.fire.grid(row=4,column=1)
        self.switch.grid(row=5,column=1)
        
        self.jentry.grid(row=1,column=2)
        self.lentry.grid(row=2,column=2)
        self.rentry.grid(row=3,column=2)
        self.fentry.grid(row=4,column=2)
        self.sentry.grid(row=5,column=2)
        
        def save():
            right_key = self.rentry.get()
            left_key = self.lentry.get()
            jump_key = self.jentry.get()
            fire_key = self.fentry.get()
            switch_key = self.sentry.get()
            with open('settings.txt','w') as settings:
                settings.write("%s\n" % right_key)
                settings.write("%s\n" % left_key)
                settings.write("%s\n" % jump_key)
                settings.write("%s\n" % fire_key)
                settings.write("%s\n" % switch_key)
            self.settingsw.destroy()
                
                
                
            
            
        
        self.control_ok_button = Button(self.settingsw,text="Save",command=save)
        self.cancel_button = Button(self.settingsw,text="Cancel",command=self.settingsw.destroy)
        self.cancel_button.grid(row=6,column=1)
        self.control_ok_button.grid(row=6,column=2)
        
    
        
        
        
        



menu = Menu()
        
main.mainloop()
        
        