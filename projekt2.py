from tkinter import messagebox
from tkinter import *


def dodaj():
    imie = enN.get()
    tel = enT.get()
    if not imie or not tel:
        messagebox.showinfo("Komunikat", "Pola nie moga byc puste!!!")
        return
    kontakty.insert(END,imie+": "+tel)

def usun():
    index = kontakty.curselection()[0]
    kontakty.delete(index)
    messagebox.showinfo(title="Komunikat",
                        message="Kontakt został usunięty.")
    
def wyjdz():
    #root.quit()
    if messagebox.askyesno("Title","chcesz wyjsc?"):
        root.quit()
    return
    
root = Tk()
Label(root, text="Książka telefoniczna").pack()#side="left")

x1 = Frame(root)
x1.pack()

labN = Label(x1, text="Nazwisko:")
labN.grid(row=0, column=0)

enN = Entry(x1)
enN.grid(row=0, column=1)

labT = Label(x1, text="Numer:")
labT.grid(row=1, column=0)

enT = Entry(x1)
enT.grid(row=1, column=1)



y1 = Frame(root)
y1.pack()

kontakty=Listbox(y1)
kontakty.pack()



kontakty.insert(END,"Nowak: 22333555", 
            "Kowalski: 444555666", 
            "Abakan: 777555444", 
            "Badowski: 333211333",
            "Dobrzanski: 888666555", 
            "Gutowski: 333111567", 
            "Janczak: 542765345", 
            "Fikus: 753876234")



z1 = Frame(root)
z1.pack()

but1 = Button(z1, text='Wyjdź', command=wyjdz)
but1.grid(row=3, column=0, sticky=W, pady=4)


but2 = Button(z1, text="Dodaj", command=dodaj)
but2.grid(row=0, column=0)

but3 = Button(z1, text='Usuń', command=usun)
but3.grid(row=0, column=1, sticky=W, pady=4)





root.mainloop()


