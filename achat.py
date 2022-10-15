from tkinter import *
from subprocess import call
from tkinter import messagebox,ttk
import customtkinter
from tkinter import ttk
from PIL import Image, ImageTk


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
    call(["python", "C:\\Users\\SOGOBA\\Documents\\Nouveau dossier\\employer.py"])

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

#Print
imp = ttk.Combobox(fenetre, values=["line 1", "line 2", "line 3"])
imp.place(x=2, y=0)

'''def print_file():
    print(imp.get())

imag = tkinter.PhotoImage(file="C:\\Users\\SOGOBA\\Documents\\Nouveau dossier\\Capture.png")
b = Button(fenetre, image=imag, command="")
b.pack()'''

#icone
fenetre.iconbitmap("C:\\Users\\SOGOBA\\Documents\\Nouveau dossier\\aa.ico")

#titre
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="GESTION D'ACHATS",font=("Sans Serif bold",26, 'bold'),
                   background="silver",foreground="black")
labelTitre.place(x=0,y=0,width=1080,height=60)

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,font=("Arial Bold",10),
                   background="gray",foreground="#000000")
labelTitre.place(x=0,y=60,width=200,height=90)

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="",font=("Sans Serif bold",20),
                   background="#ffffff",foreground="#000000")
labelTitre.place(x=200,y=60,width=880,height=30)

#pied de page
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="My bibliotheque/devel@ppé par Team3 ODC",font=("Arial Bold",10),
                   background="#1D314F",foreground="#000000")
labelTitre.place(x=0,y=570,width=1080,height=30)

#Nom Acheteur

Acheteur=Label(fenetre,text="Nom Acheteur :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
Acheteur.place(x=216,y=120,width=150)
txtAcheteur = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtAcheteur.place(x=400,y=120,width=180)

#NOM du livre

lblNom =Label(fenetre,text="Nom du Livre :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblNom.place(x=216,y=160,width=180)
txtNom = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtNom.place(x=400,y=160,width=180)

#Quantite

lblQtte =Label(fenetre,text="Quantite:",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblQtte.place(x=216,y=190,width=180)
txtQtte = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtQtte.place(x=400,y=190,width=180)

#Prix

lblPrix =Label(fenetre,text="Prix:",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblPrix.place(x=216,y=220,width=180)
txtPrix = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtPrix.place(x=400,y=220,width=180)
#ID ACHAT

lblID =Label(fenetre,text="ID_Achat :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblID.place(x=600,y=120,width=180)
txtID = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtID.place(x=800,y=120,width=180)

#DAte Enreg
lblDAte =Label(fenetre,text="Date Enreg:",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblDAte.place(x=600,y=160,width=180)
txtDate = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtDate.place(x=800,y=160,width=180)

#BOUTON Ajouter
btnAjouter=customtkinter.CTkButton(master=fenetre,text="Ajouter",text_font=("Arial",14),text_color="white",bg_color="#FFFFFF",fg_color="#20843C",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command="")
btnAjouter.place(x=610,y=280,width=120)
#BOUTON MODIFIER
btnModifier=customtkinter.CTkButton(master=fenetre,text="Modifier",text_font=("Arial",14),text_color="white",bg_color="#FFFFFF",fg_color="#1B3864",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command="")

btnModifier.place(x=750,y=280,width=120)
#BOUTON Annuler
btnAnnuler=customtkinter.CTkButton(master=fenetre,text="Annuler",text_font=("Arial",14),text_color="white",bg_color="#FFFFFF",fg_color="#F46464",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command="")

btnAnnuler.place(x=880,y=280,width=120)

#Liste de Presonnel
labelliste = Label(fenetre,text="LISTE ACHATS",font=("Sans Serif bold",15,'bold'),
                   background="#7DA0D6",foreground="#000000")
labelliste.place(x=200,y=350,width=880,height=23)

#Prints





#Tree View
tree= ttk.Treeview(fenetre, columns = (1,2,3,4,5), height = 8, show = "headings")
style = ttk.Style(fenetre)
style.theme_use("clam")
style.configure("Treeview.Heading", background="#D9D9D9", foreground="black")
tree.place(x=205,y=379)
tree.heading(1, text= "Nom Acheteur")
tree.heading(2, text= "Nom du livre")
tree.heading(3, text= "Quantité")
tree.heading(4, text= "ID_Achat")
tree.heading(5, text= "Date Enreg")

tree.column(1, width= 170)
tree.column(2, width= 170)
tree.column(3, width= 180)
tree.column(4, width= 170)
tree.column(5, width= 160)

# Bare de défilement du tree vew
verscrlbar = ttk.Scrollbar(fenetre,
                           orient="vertical",
                           command=tree.yview)
verscrlbar.place(x=1062,y=380,height=190)


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

#Deconnecte
btnDeconnecter=customtkinter.CTkButton(dash,text="Se deconnecter",text_font=("#000000", 15),text_color="black", bg="red",fg_color="red",hover=True,hover_color="orange",border_width=1,corner_radius=10
                      ,command=deconnection)
btnDeconnecter.place(x=10,y=440,width=180)

fenetre.mainloop()