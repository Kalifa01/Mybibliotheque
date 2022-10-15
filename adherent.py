from tkinter import *
from subprocess import call
from PIL import ImageTk, Image
from tkinter import messagebox, ttk
import customtkinter
import mysql.connector as mysql

#Debut connection
def rechercher():
    if(txtID_adh.get() == ""):
        messagebox.showinfo("Recherche ", "Veuillez entrer l'ID de l'adherent 脿 chercher")
    else:
        con = mysql.connect(host="localhost", user="admin", password="admin", database="bibliotheque")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM adherent WHERE id_ adherent='"+ txtID_adh.get() +"'")
        rows = cursor.fetchall()

        for row in rows:
            txtNom.insert(0, row[1])
            sexe.insert(0, row[2])
            txtAge.insert(0, row[3])
            txtAdresse.insert(0, row[4])
            txtTelephone.insert(0, row[5])
            Fction.insert(0, row[6])
            Abonnement.insert(0, row[7])
        con.close()
def modifier():
    id_adherent = txtID_adh.get()
    nom_adherent = txtNom.get()
    sex = sexe.get()
    age_adherent = txtAge.get()
    adress = txtAdresse.get()
    telephone = txtTelephone.get()
    fonction =Fction.get()
    abonnement = Abonnement.get()

    if (id_adherent=="" or nom_adherent == "" or sex == "" or age_adherent == "" or adress == "" or telephone == "" or fonction == "" or abonnement == ""):
        messagebox.showinfo("Erreur:",

"Veuillez voir les champ vide")
    else:
        con = mysql.connect(host="localhost", user="admin", password="admin", database="bibliotheque")
        cursor = con.cursor()
        cursor.execute("update adherent set nom_adherent='"+ nom_adherent+"',sex='"+ sex +"',age_adherent='"+ age_adherent+"',adress='"+ adress +"',telephone='"+ telephone +"',fonction='"+ fonction +"',abonnement='"+ abonnement+"' WHERE id_adherent='"+ id_adherent +"'")
        cursor.execute("commit")

        txtID_adh.delete(0, 'end')
        txtNom.delete(0, 'end')
        sexe.delete(0, 'end')
        txtAge.delete(0, 'end')
        txtAdresse.delete(0, 'end')
        txtTelephone.delete(0, 'end')
        Fction.delete(0, 'end')
        Abonnement.delete(0, 'end')
        messagebox.showinfo("Modification ", "Modifié")

        con.close()
def ajouter():
    id_adherent = txtID_adh.get()
    nom_adherent = txtNom.get()
    sex = sexe.get()
    age_adherent = txtAge.get()
    adress = txtAdresse.get()
    telephone = txtTelephone.get()
    fonction = Fction.get()
    abonnement = Abonnement.get()

    if (id_adherent=="" or nom_adherent == "" or sex == "" or age_adherent == "" or

        adress == "" or telephone == "" or fonction == "" or abonnement == ""):
        messagebox.showinfo("Erreur:", "Veuillez remplir les champ vides")
    else:
        con = mysql.connect(host="localhost", user="root", password="6452481", database="bibliotheque")
        cursor = con.cursor()
        cursor.execute( "INSERT INTO adherent VALUES ('" + id_adherent + "','" + nom_adherent + "','" + sex + "','" + age_adherent + "','" + adress + "','" + telephone + "','" + fonction +  "','"  + abonnement + "')")
        cursor.execute("commit")

        txtID_adh.delete(0, 'end')
        txtNom.delete(0, 'end')
        sexe.delete(0, 'end')
        txtAge.delete(0, 'end')
        txtAdresse.delete(0, 'end')
        txtTelephone.delete(0, 'end')
        Fction.delete(0, 'end')
        Abonnement.delete(0, 'end')
        messagebox.showinfo("Adherent ajouter ", "Inserer avec succes")
#afficher

        con.close()
def supprimer():
    if(txtID_adh.get() == ""):
        messagebox.showinfo("Suppression ", "Spécifier l'ID de l'adhérent 脿 supprimer")
    else:
        con = mysql.connect(host="localhost", user="admin", password="admin",database="bibliotheque")
        cursor = con.cursor()

        cursor.execute("DELETE FROM adherent WHERE id_adherent ='"+ txtID_adh.get() +"'")
        cursor.execute("commit")

        txtID_adh.delete(0, 'end')
        txtNom.delete(0, 'end')
        sexe.delete(0, 'end')
        txtAge.delete(0, 'end')
        txtAdresse.delete(0, 'end')
        txtTelephone.delete(0, 'end')
        Fction.delete(0, 'end')
        messagebox.showinfo("Suppression ", "Supprimer avec succès")

        con.close()


#fin connection
#from tkcalendar import DateEntry


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
fenetre= Tk()


#parametre:
fenetre.geometry("1080x600+100+20")
fenetre.title("Accueil")
fenetre.resizable(False,False)
#fenetre.state("zoomed")
fenetre.configure(background="#FFFFFF")

#icone
fenetre.iconbitmap("C:\\Users\\SOGOBA\\Documents\\Nouveau dossier\\aa.ico")

#titre
#image logo
'''image_a=ImageTk.PhotoImage(Image.open('bk.png'))
l1 = Label(fenetre, image=image_a,width=110,height=110,bg='#4062DD').place(x=40, y=0)'''

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="GESTION ADHERENT",font=("Sans Serif bold",26, 'bold'),
                   background="silver",foreground="#000000")
labelTitre.place(x=0,y=0,width=1080,height=60)

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,font=("Arial Bold",10),
                   background="gray",foreground="#000000")
labelTitre.place(x=0,y=60,width=200,height=90)

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="",font=('Arial', 20, 'bold'),
                   background="#ffffff",foreground="#000000")
labelTitre.place(x=200,y=60,width=880,height=30)


#pied de page
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="My bibliotheque/devel@ppé par Team3 ODC",font=("Arial Bold",10),
                   background="#1D314F",foreground="#000000")
labelTitre.place(x=0,y=570,width=1080,height=30)

#ID

ID_adh=Label(fenetre,text="ID_Adherent :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
ID_adh.place(x=216,y=120,width=150)
txtID_adh = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtID_adh.place(x=400,y=120,width=180)

#NOM et Prenom du Personnel

lblNom =Label(fenetre,text="Prénom_Nom :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblNom.place(x=216,y=160,width=180)
txtNom = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtNom.place(x=400,y=160,width=180)

#SEXE

content =['Homme','Femme','Autre']

lblSexe =Label(fenetre,text="sexe :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblSexe.place(x=216,y=190,width=180)
sexe = ttk.Combobox(fenetre,values=content)
sexe.place(x=400,y=190,width=180)

#Age_Personnel

lblAge =Label(fenetre,text="Date de Naissance :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblAge.place(x=216,y=220,width=180)
txtAge = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtAge.place(x=400,y=220,width=180)
#Adresse

lblAdresse =Label(fenetre,text="Adresse :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblAdresse.place(x=600,y=120,width=180)
txtAdresse = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtAdresse.place(x=800,y=120,width=180)
#Télephone

lblTelephone =Label(fenetre,text="Tel :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblTelephone.place(x=600,y=160,width=180)
txtTelephone = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtTelephone.place(x=800,y=160,width=180)

#FONCTION Adherent
liste =['Entrepreneur','Etudiant(e)','Enseignant','Autre']

lblFction =Label(fenetre,text="Fonction :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblFction.place(x=600,y=190,width=180)
Fction = ttk.Combobox(fenetre,values=liste)
Fction.place(x=800,y=190,width=180)

#Abonnement
mois=['1Mois/1500F','2Mois/3500F','3Mois/5000F','4 Mois/6000F']

lblAbonnement =Label(fenetre,text="Abonnement/Tarifs :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblAbonnement.place(x=600,y=220,width=180)
Abonnement = ttk.Combobox(fenetre,values=mois)
Abonnement.place(x=800,y=220,width=180)

#BOUTON Ajouter
btnAjouter=customtkinter.CTkButton(master=fenetre,text="Ajouter",text_font=("Arial",14),text_color="white",bg_color="#FFFFFF",fg_color="#20843C",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=ajouter)
btnAjouter.place(x=250,y=300,width=180)
#BOUTON MODIFIER
btnModifier=customtkinter.CTkButton(master=fenetre,text="Modifier",text_font=("Arial",14),text_color="white",bg_color="#FFFFFF",fg_color="#1B3864",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=modifier)

btnModifier.place(x=450,y=300,width=180)
#BOUTON SUPPRIMER
btnSupprimer=customtkinter.CTkButton(master=fenetre,text="Supprimer",text_font=("Arial",14),text_color="white",bg_color="#FFFFFF",fg_color="#F46464",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=supprimer)

btnSupprimer.place(x=650,y=300,width=180)
#BOUTON RECHERCHER
btnRechercher=customtkinter.CTkButton(master=fenetre,text="Rechercher",text_font=("Arial",14),text_color="white",bg_color="#FFFFFF",fg_color="#DC8014",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=rechercher)
btnRechercher.place(x=850,y=300,width=180)

#Liste Adherent
labelliste = Label(fenetre,text="LISTE ADHERENT",font=("Sans Serif bold",15,'bold'),
                   background="#7DA0D6",foreground="#000000")
labelliste.place(x=200,y=350,width=880,height=23)

#Tree View
tree= ttk.Treeview(fenetre, columns = (1,2,3,4,5,8,9), height = 8, show = "headings")
style = ttk.Style(fenetre)
style.theme_use("clam")
style.configure("Treeview.Heading", background="#D9D9D9", foreground="black")
tree.place(x=205,y=379)
tree.heading(1, text= "ID_Adherent")
tree.heading(2, text= "Nom et Prenom")
tree.heading(3, text= "Sexe")
tree.heading(4, text= "Date de naissance")
tree.heading(5, text= "Fonction")

tree.heading(8, text= "Adresse")
tree.heading(9, text= "Abonnement/Tarifs")
tree.column(1, width= 120)
tree.column(2, width= 120)
tree.column(3, width= 120)
tree.column(4, width= 120)
tree.column(5, width= 120)

tree.column(8, width= 120)
tree.column(9, width= 130)

# Bare de défilement du tree vew
verscrlbar = ttk.Scrollbar(fenetre,
                           orient="vertical",
                           command=tree.yview)
verscrlbar.place(x=1060,y=380,height=190)
#FRAME
#FRAME
dash = Frame(fenetre,background="gray")
dash.place(x=0,y=90,width=200,height=800)
image_a=ImageTk.PhotoImage(Image.open('bk.png'))
l1 = Label(fenetre, image=image_a,width=110,height=85,bg='#4062DD').place(x=40, y=0)

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



fenetre.mainloop()