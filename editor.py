from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import colorchooser
from tkinter import messagebox
from  wikipedia import summary


class text_editor:
    file_name = 'no_name'

    def open_me(self):
        f = filedialog.askopenfile(filetypes=(('Text Files', '.txt'), ('All Files', '*.*')))
        if f != None:
            self.text_area.delete(1.0, END)

            for line in f:
                self.text_area.insert(END, line)

    def Save_as(self):
        result = self.text_area.get(1.0, END)
        file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if file!= None:
            file.write(result)
            file.close()
            self.file_name = file.name

    def Save_(self):
        if self.file_name == 'no_name':
            self.Save_as()
        else:
            f = open(self.file_name, mode='w+')
            f.write(self.text_area.get(1.0, END))
            f.close()

    def new_(self):
        self.file_name = 'no_name'
        self.text_area.delete(1.0, END)

    def copy(self):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())

    def cut(self):
        self.copy()
        self.text_area.delete('sel.first', 'sel.last')

    def paste(self):
        self.text_area.insert(INSERT, self.text_area.clipboard_get())
    def size(self):
        a = simpledialog.askinteger("Font Size","Enter font Size")
        if a!= None:
            self.text_area.config(font=("arial",a))

    def bg(self):
        clr = colorchooser.askcolor()
        self.text_area.config(bg=clr[1])

    def fg(self):
        clr = colorchooser.askcolor()
        self.text_area.config(fg=clr[1])


    def show_me(self):
        abt = "The notepad software is a basic text editor.\nDeveloped by Pavan BN.\n "
        messagebox.showinfo("About",abt)

    def search_me(self):
        self.val = self.entry.get()
        try:
            print('before summary')
            self.answer = summary(self.val)
            self.text.delete(1.0, END)
            self.text.insert(INSERT, self.answer)
        except:
            self.text.insert(INSERT, "Can't Find")

    def wiki(self):
        self.sun_window = Toplevel()

        self.entry = Entry(self.sun_window, width=30, bd=2)
        self.entry.pack()
        self.bt = Button(self.sun_window, text="Search", command=self.search_me).pack()
        self.f1 = Frame(self.sun_window, bd=2).pack(side=BOTTOM)
        self.scroll = Scrollbar(self.f1)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.text = Text(self.sun_window, width=100, height=150, wrap=WORD, yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.text.yview)
        self.text.pack(side=LEFT)

    def __init__(self, master):
        self.master = master
        self.text_area = Text(self.master, undo=True,font=('arial',15))
        self.text_area.pack(fill=BOTH, expand=1)
        self.main_menu = Menu(master)
        master.config(menu=self.main_menu)



        # create file menu

        self.file_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label='File', menu=self.file_menu)
        self.file_menu.add_command(label='New', command=self.new_)
        self.file_menu.add_command(label='Open', command=self.open_me)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Save', command=self.Save_)
        self.file_menu.add_command(label='Save As', command=self.Save_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit (Alt-F4)', command=master.quit)

        # create edit

        self.edit_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label='Edit', menu=self.edit_menu)
        self.edit_menu.add_command(label='Undo', command=self.text_area.edit_undo)
        self.edit_menu.add_command(label='Redo', command=self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label='Copy', command=self.copy)
        self.edit_menu.add_command(label='Cut', command=self.cut)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label='Paste', command=self.paste)


        #create view

        self.view_menu = Menu(self.main_menu,tearoff =False)
        self.main_menu.add_cascade(label="View",menu=self.view_menu)
        self.view_menu.add_command(label = "Font Size",command=self.size)
        self.view_menu.add_separator()
        self.view_menu.add_command(label="Background Color", command=self.bg)
        self.view_menu.add_separator()
        self.view_menu.add_command(label="Font Color", command=self.fg)

        #create about
        self.about_menu = Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label = "About",menu=self.about_menu)
        self.about_menu.add_command(label="Developer Details",command=self.show_me)

        #create search
        self.search = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Wikipedia", menu=self.search)
        self.search.add_command(label="Wikipedia Search", command=self.wiki)




root = Tk()
root.title("NotePad                                                                                           By Pavan BN♦♦♦♣  ")
obj = text_editor(root)
root.geometry("800x600")
root.mainloop()
