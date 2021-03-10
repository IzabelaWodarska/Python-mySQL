import pymysql as mysql
import tkinter as tk
from tkinter import messagebox
from tkinter import *
import sqlite3

root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title('Księga Meldunkowa Hotel Sudety')
title_label = Label(root, text="Witaj, wprowadź dane Gościa").grid(column=1, padx=10, pady=10)

#podłączenie
mydb = mysql.Connect(host='', unix_socket='', user='', passwd='', db='mysql', database='hotel') 

my_cursor = mydb.cursor() #zmienna

def dodaj():

    sql_command = "INSERT INTO Goscie (Imię, Nazwisko, Adres, Kod, Miasto, Kraj, Paszport, Telefon, Przyjazd, Wyjazd, Nr_Pokoju, Ilosc_Gosci, Ilosc_Nocy, Cena, Platnosc, Uwagi) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (imie_box.get(),nazwisko_box.get(),adres_box.get(),kod_box.get(),miasto_box.get(),kraj_box.get(),paszport_box.get(),tel_box.get(),przyjazd_box.get(),wyjazd_box.get(),pokoj_box.get(),gosci_box.get(),noce_box.get(),cena_box.get(),platnosc_box.get(),uwagi_box.get())
 
    if not imie_box or not nazwisko_box or not adres_box or not kod_box or not miasto_box or not kraj_box or not tel_box or not paszport_box or not przyjazd_box or not wyjazd_box or not pokoj_box or not gosci_box or not noce_box or not cena_box or not platnosc_box:
        messagebox.showinfo("Komunikat","Pola nie mogą być puste!")
        return
           
 #czyść       
    my_cursor.execute(sql_command, values)

    imie_box.delete(0, END)
    nazwisko_box.delete(0, END)
    adres_box.delete(0, END)
    kod_box.delete(0, END)
    miasto_box.delete(0, END)
    kraj_box.delete(0, END)
    paszport_box.delete(0, END)
    tel_box.delete(0, END)
    przyjazd_box.delete(0, END)
    wyjazd_box.delete(0, END)
    pokoj_box.delete(0, END)
    gosci_box.delete(0, END)
    noce_box.delete(0, END)
    cena_box.delete(0, END)
    platnosc_box.delete(0, END)
    uwagi_box.delete(0, END)
    
    mydb.commit()
    
def wyjdz():
    if messagebox.askyesno("Komunikat","Chcesz wyjść?"):
        root.quit()
        return    
        
#formy i boxy
imie_label = Label(root, text="Imię: ").grid(row=1,column=0)
imie_box = Entry(root,width=30)
imie_box.grid(row=1,column=1,padx=20,pady=5)

nazwisko_label = Label(root, text="Nazwisko: ").grid(row=2,column=0) 
nazwisko_box = Entry(root,width=30)
nazwisko_box.grid(row=2,column=1,padx=20,pady=5)

adres_label = Label(root, text="Adres zamieszkania: ").grid(row=3,column=0) 
adres_box = Entry(root,width=30)
adres_box.grid(row=3,column=1,padx=20,pady=5)

kod_label = Label(root, text="Kod pocztowy: ").grid(row=4,column=0) 
kod_box = Entry(root,width=30)
kod_box.grid(row=4,column=1,padx=20,pady=5)

miasto_label = Label(root, text="Miasto: ").grid(row=5,column=0) 
miasto_box = Entry(root,width=30)
miasto_box.grid(row=5,column=1,padx=20,pady=5)

kraj_label = Label(root, text="Kraj: ").grid(row=6,column=0) 
kraj_box = Entry(root,width=30)
kraj_box.grid(row=6,column=1,padx=20,pady=5)

paszport_label = Label(root, text="Paszport/nr dowodu: ").grid(row=7,column=0) 
paszport_box = Entry(root,width=30)
paszport_box.grid(row=7,column=1,padx=20,pady=5)

tel_label = Label(root, text="Numer kontaktowy: ").grid(row=8,column=0) 
tel_box = Entry(root,width=30)
tel_box.grid(row=8,column=1,padx=20,pady=5)

przyjazd_label = Label(root, text="Przyjazd: ").grid(row=10,column=0) 
przyjazd_box = Entry(root,width=30)
przyjazd_box.grid(row=10,column=1,padx=20,pady=5)

wyjazd_label = Label(root, text="Wyjazd: ").grid(row=11,column=0) 
wyjazd_box = Entry(root,width=30)
wyjazd_box.grid(row=11,column=1,padx=20,pady=5)

pokoj_label = Label(root, text="Numer pokoju: ").grid(row=12,column=0) 
pokoj_box = Entry(root,width=30)
pokoj_box.grid(row=12,column=1,padx=20,pady=5)

gosci_label = Label(root, text="Ilość gości: ").grid(row=13,column=0) 
gosci_box = Entry(root,width=30)
gosci_box.grid(row=13,column=1,padx=20,pady=5)

noce_label = Label(root, text="Ilość nocy: ").grid(row=14,column=0) 
noce_box = Entry(root,width=30)
noce_box.grid(row=14,column=1,padx=20,pady=5)

cena_label = Label(root, text="Cena: ").grid(row=15,column=0) 
cena_box = Entry(root,width=30)
cena_box.grid(row=15,column=1,padx=20,pady=5)

platnosc_label = Label(root, text="Rodzaj płatności: ").grid(row=16,column=0) 
platnosc_box = Entry(root,width=30)
platnosc_box.grid(row=16,column=1,padx=20,pady=5)

uwagi_label = Label(root, text="Uwagi: ").grid(row=1,column=2) 
uwagi_box = Entry(root,width=30)
uwagi_box.grid(row=1,column=3,padx=20,pady=5)

#buttony
but1 = Button(root, text='Wyjdź', command=wyjdz)
but1.grid(row=25, column=1, padx=10, pady=10, sticky=E )

but2 = Button(root, width=30, fg = "red", text="Dodaj", command=dodaj)
but2.grid(row=18, column=1, padx=10, pady=10)

root.mainloop()


