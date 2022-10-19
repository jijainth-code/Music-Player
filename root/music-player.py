
from email.mime import image
import tkinter as tk
from audioplayer import AudioPlayer
from pygame import mixer
from PIL import ImageTk, Image
import json

mixer.init()

class MainApplication(tk.Frame):

    


    


    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

       
        #constants
        self.state = 0
        
        with open('data.json') as f:
            self.data = json.load(f)
            self.data = self.data['song']
        
        self.LEN = len(self.data)
        self.I = 1
        


        #functions

        def play():
            mixer.music.load(self.data[self.I]['path'])
            
            if self.state == 0:
                self.state = 1
                print("playing")
                self.play.configure(text="pause")
                mixer.music.play()
            else :
                self.state = 0
                print("paused")
                self.play.configure(text="play")
                mixer.music.stop()

        def next():
            play()
            if self.I+1 > self.LEN-1:
                self.I = 0
            else :
                self.I +=1
            
            self.desc_text.configure(text=self.data[self.I]['name'])


        def back():
            play()
            if self.I-1 < 0:
                self.I = self.LEN - 1
            else :
                self.I -=1
            
            
            self.desc_text.configure(text=self.data[self.I]['name'])


        self.parent = parent

        #TITLE

        self.TITLE = tk.Label(self , text="MUSIC PLAYER" ,background="orange")
        self.TITLE.grid(row=0,column=0, columnspan=2,  sticky="nwse")


        #IMAGE

        self.img = Image.open(self.data[0]['img'])
        self.photo = self.img.resize((400,400), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.photo)

        self.IMAGE_FRAME = tk.Frame(self )
        self.IMAGE_FRAME.grid(row=1 , column=0 , columnspan=2 , rowspan=18 , sticky="nwse")

        

        self.IMAGE_LABEL = tk.Label(self.IMAGE_FRAME , background="black" , image=self.photo)
        self.IMAGE_LABEL.grid(row=0 , column=0 ,columnspan=10 )

        #DESCRIPTION

       

        self.DESC = tk.Frame(self , background="gray")
        self.DESC.grid(row=18 , column=0 , columnspan=2 , rowspan=2, sticky="nwse")

        self.desc_text = tk.Label(self.DESC , text="Jijainth")
        self.desc_text.grid(column=0 , row=0)
        self.desc_text.pack(anchor='center')




        #BUTTON FRAME AND BUTTON
        
        self.BUTTON_FRAME = tk.Frame(self , background="blue")
        self.BUTTON_FRAME.grid(row=19 , column=0 , columnspan=2 , rowspan=1, sticky="nwse")



        self.back =tk.Button(self.BUTTON_FRAME , text='<' , command=back)
        self.back.pack(  side="left" )
        self.back.config(height=2 , width=15)


        self.next =tk.Button(self.BUTTON_FRAME , text='>' , command=next)
        self.next.pack( side="right")
        self.next.config(height=2 , width=15)

        self.btn_text = "play"
        self.play = tk.Button(self.BUTTON_FRAME , text=self.btn_text , command=play)
        self.play.pack(  )
        self.play.config(height=2 , width=20)





        for row in range(20):
            self.grid_rowconfigure(row, weight=1)
        for col in range(2):
            self.grid_columnconfigure(col, weight=1)


    

    


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x500")
    MainApplication(root).pack(side="top", fill="both", expand=True)


root.mainloop()