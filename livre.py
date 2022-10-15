from tkinter import *
from subprocess import call
from tkinter import messagebox,ttk
import customtkinter
import mysql.connector as Mysql



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

#icone
fenetre.iconbitmap("C:\\Users\\SOGOBA\\Documents\\Nouveau dossier\\aa.ico")

#titre
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="GESTION DES LIVRES",font=("Sans Serif bold",26, 'bold'),
                   background="silver",foreground="#000000")
labelTitre.place(x=0,y=0,width=1080,height=60)

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,font=("Arial Bold",10),
                   background="gray",foreground="#000000")
labelTitre.place(x=0,y=60,width=200,height=90)

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="",font=("Sans Serif bold",20),
                   background="#ffffff",foreground="#000000")
labelTitre.place(x=200,y=60,width=970,height=30)

#pied de page
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="My bibliotheque/devel@ppé par Team3 ODC",font=("Arial Bold",10),
                   background="#1D314F",foreground="#000000")
labelTitre.place(x=0,y=570,width=1080,height=30)

#ID

ID_livre=Label(fenetre,text="ID_livre :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
ID_livre.place(x=216,y=120,width=150)
txtID_livre = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtID_livre.place(x=400,y=120,width=180)

#NOM et Prenom du Personnel

lblNom =Label(fenetre,text="Nom du livre:",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblNom.place(x=216,y=160,width=180)
txtNom = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtNom.place(x=400,y=160,width=180)

#GENRE LIVRE

content =['Romain','Poesie','Conte','Autre']

lblGenre =Label(fenetre,text="Genre :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblGenre.place(x=216,y=190,width=180)
Genre = ttk.Combobox(fenetre,values=content)
Genre.place(x=400,y=190,width=180)

#Date ajout

lbldate =Label(fenetre,text="Date Enreg:",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lbldate.place(x=216,y=220,width=180)
txtdate = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtdate.place(x=400,y=220,width=180)
#Auteur

lblAuteur =Label(fenetre,text="Auteur :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblAuteur.place(x=600,y=120,width=180)
txtAuteur = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtAuteur.place(x=800,y=120,width=180)
#Nombre

lblNombre =Label(fenetre,text="Nombre :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblNombre.place(x=600,y=160,width=180)
txtNombre = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtNombre.place(x=800,y=160,width=180)


#DISCIPLINE du livre
liste =['Mathematique','Biologie','Physique','Chimie','Anglais','Francais','Géologie','Autre']

lblDiscipline=Label(fenetre,text="Discipline:",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblDiscipline.place(x=600,y=190,width=180)
Discipline = ttk.Combobox(fenetre,values=liste)
Discipline.place(x=800,y=190,width=180)

#Tarifs

lblTarifs =Label(fenetre,text="Tarifs :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblTarifs.place(x=600,y=220,width=180)
txtTarifs = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtTarifs.place(x=800,y=220,width=180)


#cadrage des données livre

labelliste = Label(fenetre,text="LISTE DES LIVRES",font=("Sans Serif bold",15,'bold'),
                   background="#7DA0D6",foreground="#000000")
labelliste.place(x=200,y=350,width=880,height=23)

#BOUTON Ajouter
btnAjouter=customtkinter.CTkButton(master=fenetre,text="Ajouter",text_font=("Arial",14),text_color="white",bg_color="#FFFFFF",fg_color="#20843C",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command="")
btnAjouter.place(x=250,y=300,width=180)
#BOUTON MODIFIER
btnModifier=customtkinter.CTkButton(master=fenetre,text="Modifier",text_font=("Arial",14),text_color="white",bg_color="#FFFFFF",fg_color="#1B3864",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command="")

btnModifier.place(x=450,y=300,width=180)
#BOUTON SUPPRIMER
btnSupprimer=customtkinter.CTkButton(master=fenetre,text="Supprimer",text_font=("Arial",14),text_color="white",bg_color="#FFFFFF",fg_color="#F46464",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command="")

btnSupprimer.place(x=650,y=300,width=180)
#BOUTON RECHERCHER
btnRechercher=customtkinter.CTkButton(master=fenetre,text="Rechercher",text_font=("Arial",14),text_color="white",bg_color="#FFFFFF",fg_color="#DC8014",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command="")
btnRechercher.place(x=850,y=300,width=180)


#Tree View
tree= ttk.Treeview(fenetre, columns = (1,2,3,4,5,6,7), height = 8, show = "headings")
style = ttk.Style(fenetre)
style.theme_use("clam")
style.configure("Treeview.Heading", background="#D9D9D9", foreground="black")
tree.place(x=200,y=379)
tree.heading(1, text= "ID_livre")
tree.heading(2, text= "Nom du livre")
tree.heading(3, text= "Genre")
tree.heading(4, text= "Date Enreg")
tree.heading(5, text= "Auteur")
tree.heading(6, text= "Discipline")
tree.heading(7, text= "Tarifs")

tree.column(1, width= 120)
tree.column(2, width= 120)
tree.column(3, width= 120)
tree.column(4, width= 130)
tree.column(5, width= 120)
tree.column(6, width= 130)
tree.column(7, width=120)


# Bare de défilement du tree vew
verscrlbar = ttk.Scrollbar(fenetre,
                           orient="vertical",
                           command=tree.yview)
verscrlbar.place(x=1064,y=380,height=190)

#FRAME
dash = Frame(fenetre,background="gray")
dash.place(x=0,y=90,width=200,height=480)

#BOUTONS
imageico = PhotoImage(file="ac.png")
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
#Boutton deconnecter
btnDeconnecter=customtkinter.CTkButton(dash,text="Se deconnecter",text_font=("#000000", 15),text_color="black", bg="red",fg_color="red",hover=True,hover_color="orange",border_width=1,corner_radius=10
                      ,command=deconnection)
btnDeconnecter.place(x=10,y=440,width=180)

fenetre.mainloop()