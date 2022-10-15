import tkinter
from tkinter import *
from subprocess import call
from tkinter import messagebox
import customtkinter
from PIL import ImageTk, Image

def deconnection():
    mbox = messagebox.askquestion("Deconnecter","Voulez-vous vraiment vous deconnecter?")
    if(mbox=='yes'):
        fenetre.destroy()
        call(["python", "C:\\Users\\SOGOBA\\Documents\\Nouveau dossier\\connectPage.py"])

def Accueil():
    fenetre.destroy()
    call(["python", "C:\\Users\\SOGOBA\\Documents\\Nouveau dossier\\accueil.py"])

def Adherent():
    fenetre.destroy()
    call(["python", "C:\\Users\\SOGOBA\\Documents\\Nouveau dossier\\adherent.py"])

def Livre():
    fenetre.destroy()
    call(["python", "C:\\Users\\SOGOBA\\Documents\\Nouveau dossier\\livre.py"])

def Sanction ():
    fenetre.destroy()
    call(["python", "C:\\Users\\SOGOBA\\Documents\\Nouveau dossier\\sanction.py"])

def Employer():
    fenetre.destroy()
    call(["python", "employer.py"])

def Achat():
    fenetre.destroy()
    call(["python", "C:\\Users\\SOGOBA\\Documents\\Nouveau dossier\\achat.py"])

def Emprunt():
    fenetre.destroy()
    call(["python", "C:\\Users\\SOGOBA\\Documents\\Nouveau dossier\\emprunt.py"])
fenetre = Tk()


#parametre:
fenetre.geometry("1080x600+100+20")
fenetre.title("Accueil")
fenetre.resizable(False,False)
fenetre.configure(background="#FFFFFF")

#icone
fenetre.iconbitmap("C:\\Users\\SOGOBA\\Documents\\Nouveau dossier\\aa.ico")


#titre
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="BIENVENUE SUR LA PAGE D'ACCUEIL",font=("Sans Serif bold",26, 'bold'),
                   background="silver",foreground="#000000")
labelTitre.place(x=0,y=0,width=1100,height=60)

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,font=("Arial Bold",10),
                   background="gray",foreground="#000000")
labelTitre.place(x=0,y=50,width=200,height=90)

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="",font=("Sans Serif bold",25),
                   background="#FFFFFF",foreground="#000000")
labelTitre.place(x=200,y=60,width=880,height=30)

#pied de page
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="My bibliotheque/devel@ppé par Team3 ODC",font=("Arial Bold",10),
                   background="#1D314F",foreground="#000000")
labelTitre.place(x=0,y=570,width=1080,height=30)

#FRAME
dash = Frame(fenetre,background="gray")
dash.place(x=0,y=90,width=200,height=480)

#BOUTONS
imageico = PhotoImage(file="C:\\Users\\SOGOBA\\Documents\\Nouveau dossier\\ac.png")
btnAccueil= Button(dash,text="",image=imageico,font=("Arial",15),bg="gray",fg="black",borderwidth=0,command=Accueil)
btnAccueil.place(x=10,y=40,width=180,height=60)
btnAdherent=customtkinter.CTkButton(dash,text="Adherent",text_font=("#000000", 15),text_color="black", bg="light gray",fg_color="light gray",hover=True,hover_color="orange",border_width=1,corner_radius=10,command=Adherent)
btnAdherent.place(x=10,y=110,width=180)
btnlivre=customtkinter.CTkButton(dash,text="Livre",text_font=("#000000", 15),text_color="black", bg="light gray",fg_color="light gray",hover=True,hover_color="orange",border_width=1,corner_radius=10,command=Livre)
btnlivre.place(x=10,y=160,width=180)
btnSanction=customtkinter.CTkButton(dash,text="Sanction",text_font=("#000000", 15),text_color="black", bg="light gray",fg_color="light gray",hover=True,hover_color="orange",border_width=1,corner_radius=10,command=Sanction)
btnSanction.place(x=10,y=210,width=180)
btnEmployer=customtkinter.CTkButton(dash,text="Employer",text_font=("#000000", 15),text_color="black", bg="light gray",fg_color="light gray",hover=True,hover_color="orange",border_width=1,corner_radius=10,command=Employer)
btnEmployer.place(x=10,y=260,width=180)
btnAchat=customtkinter.CTkButton(dash,text="Achats",text_font=("#000000", 15),text_color="black", bg="light gray",fg_color="light gray",hover=True,hover_color="orange",border_width=1,corner_radius=10,command=Achat)
btnAchat.place(x=10,y=310,width=180)
btnEmprunt=customtkinter.CTkButton(dash,text="Emprunts",text_font=("#000000", 15),text_color="black", bg="light gray",fg_color="light gray",hover=True,hover_color="orange",border_width=1,corner_radius=10,command=Emprunt)
btnEmprunt.place(x=10,y=360,width=180)

btnDeconnecter=customtkinter.CTkButton(dash,text="Se deconnecter",text_font=("#000000", 15),text_color="black", bg="red",fg_color="red",hover=True,hover_color="orange",border_width=1,corner_radius=10
                      ,command=deconnection)
btnDeconnecter.place(x=10,y=440,width=180)

#LOGO
img = PhotoImage(file="C:\\Users\\SOGOBA\\Documents\\Nouveau dossier\\P.png")

# Create a Label Widget to display the text or Image
label = Label(fenetre, image = img)
label.place(x=200,y=50)


fenetre.mainloop()