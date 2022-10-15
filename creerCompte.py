from tkinter import *
from tkinter import ttk
from subprocess import call
from tkinter import messagebox
from PIL import Image, ImageTk

def annuler():
    fenetre.destroy()
    call(["python","C:\\Users\\SOGOBA\\Documents\\Nouveau dossier\\connectPage.py"])

def valider():
    nom = txtNom.get()
    sex = sexe.get()
    dateN = txtDateN.get()
    contact = txtContact.get()
    fn = fonction.get()
    nomUtisateur = txtUtilisateur.get()
    mot_de_passe = txtMdp.get()
    confimer = txtConfirmer.get()
    dateIns = txtDateIns.get()
    if(nom==""or sex=="" or dateN==""or contact==""or fn=="" or nomUtisateur=="" or mot_de_passe==""
    or confimer==""or dateIns==""):
        messagebox.showinfo("Erreur:", "veuillez remplir les champs vides")
    elif (mot_de_passe != confimer):
        messagebox.showinfo("Information", "Votre mot de passe est different de celui de la confirmation")
    else:
        messagebox.showinfo("Information", "Inscrit avec succès")
        fenetre.destroy()
        call(["python","C:\\Users\\SOGOBA\\Documents\\Nouveau dossier\\connectPage.py"])
#----------------------------------------------MAIN----------------------------------------------------------
fenetre = Tk()

#parametre:
fenetre.geometry("1080x600+100+20")
fenetre.title("Creer compte")
fenetre.resizable(False,False)
fenetre.configure(background="#FFFFFF")
#icone
fenetre.iconbitmap("C:\\Users\\SOGOBA\\Documents\\Nouveau dossier\\aa.ico")

imag=ImageTk.PhotoImage(Image.open("C:\\Users\\SOGOBA\\Documents\\Nouveau dossier\\livre-a-lire.png"))
x=Label(image=imag, font=("Arial",60))
x.pack()

#titre
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="INSCRIPTION",font=("Sans Serif bold",26, 'bold'),
                   background="silver",foreground="#000000")
labelTitre.place(x=0,y=2,width=1080,height=40)

#labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,font=("Arial Bold",10),
                   #background="#1D314F",foreground="#f8f7f5")
#labelTitre.place(x=0,y=60,width=200,height=30)

'''labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="BIENVENUE SUR LA PAGE D'INSCRIPTION",font=("Sans Serif bold",20),
                   background="#22222e",foreground="#000000")
labelTitre.place(x=150,y=60,width=880,height=30)'''''
#-----------------------------------LES WIDGETS--------------------------------------------------------------
#NOM

lblNom =Label(fenetre,text="Nom_complet :",font=("Times New Roman",14),
                   bg="#0c121e",foreground="#ffffff")
lblNom.place(x=16,y=140,width=150)
txtNom = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtNom.place(x=200,y=140,width=180)

#SEXE

content =['Homme','Femme','Autre']

lblSexe =Label(fenetre,text="sexe :",font=("Times New Roman",14),
               bg="#0c121e", foreground="#ffffff")
lblSexe.place(x=16,y=180,width=150)
sexe = ttk.Combobox(fenetre,values=content)

sexe.place(x=200,y=180,width=180,height=25)

#Date naissance

lblDateN =Label(fenetre,text="Date de naissance :",font=("Times New Roman",14),
                   bg="#0c121e",foreground="#ffffff")
lblDateN.place(x=16,y=220,width=150)
txtDateN = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtDateN.place(x=200,y=220,width=180)

#Contact

lblContact =Label(fenetre,text="Contact :",font=("Times New Roman",14),
                   bg="#0c121e",foreground="#ffffff")
lblContact.place(x=16,y=260,width=150)
txtContact = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtContact.place(x=200,y=260,width=180)

#FONCTION
liste =['Admin','Bibliothecaire']

lblContact =Label(fenetre,text="Fonction :",font=("Times New Roman",15),
                   bg="#0c121e",foreground="#ffffff")
lblContact.place(x=16,y=300,width=150)
fonction = ttk.Combobox(fenetre,values=liste)

fonction.place(x=200,y=300,width=180)

#SPECIALITE

'''specialite =['Pediatre','Generaliste','Chirurgien','Pneumologue']

lblSpecialite =Label(fenetre,text="Specialite :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblSpecialite.place(x=600,y=140,width=180)
Specialite = ttk.Combobox(fenetre,values=specialite)

Specialite.place(x=800,y=140,width=180)'''

#NOM UTILISATEUR

lblUtilisateur =Label(fenetre,text="Nom_Utilisateur :",font=("Times New Roman",14),
                   bg="#0c121e",foreground="#ffffff")
lblUtilisateur.place(x=600,y=135,width=150)
txtUtilisateur = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtUtilisateur.place(x=800,y=135,width=180)

#MOT DE PASSE

lblMdp =Label(fenetre,text="Mot de passe :",font=("Times New Roman",14),
                   bg="#0c121e",foreground="#ffffff")
lblMdp.place(x=600,y=180,width=150)
txtMdp = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtMdp.place(x=800,y=180,width=180)

#MOT DE PASSE CONFIRMATION

lblConfirmer =Label(fenetre,text="Confirmer :",font=("Times New Roman",14),
                   bg="#0c121e",foreground="#ffffff")
lblConfirmer.place(x=600,y=225,width=150)
txtConfirmer = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtConfirmer.place(x=800,y=225,width=180)

#Date Insertion

lblDateIns =Label(fenetre,text="Date d'insertion :",font=("Times New Roman",14),
                   bg="#0c121e",foreground="#ffffff")
lblDateIns.place(x=600,y=270,width=150)
txtDateIns = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtDateIns.place(x=800,y=270,width=180)

#BOUTON VALIDER
btnValider=Button(fenetre,text="Valider",font=("Arial",14),bg="#4062DD",fg="white",borderwidth=0,command=valider)
btnValider.place(x=850,y=325,width=130)

#BOUTON ANNULER
btnAnnuler=Button(fenetre,text="Annuler",font=("Arial",14),bg="#4062DD",fg="white",borderwidth=0,command=annuler)
btnAnnuler.place(x=680,y=325,width=130)

#pied de page
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="My bibliotheque/devel@ppé par Team3 ODC",font=("Arial Bold",10),
                   background="#1D314F",foreground="#000000")
labelTitre.place(x=0,y=570,width=1080,height=30)
#-----------------------------------LES WIDGETS--------------------------------------------------------------

fenetre.mainloop()