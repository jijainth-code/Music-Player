self.img = Image.open(self.data[self.I]['img'])
        self.photo = self.img.resize((400,400), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.photo)