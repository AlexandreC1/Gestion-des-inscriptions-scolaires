import tkinter as tk
from tkinter import ttk, messagebox
from NewInscription import inscriptions
from database import Database


root = tk.Tk()
root.title("Eleve Database")
root.geometry("600x400")
root.configure(background="#a9cddb")

# Styling
style = ttk.Style()
style.configure("TButton", background="#FF6B6B", foreground="#4949c6")
style.configure("TLabel", background="#F4F4F4", foreground="#4949c6")
style.configure("TEntry", background="#FFFFFF", fieldbackground="#4949c6")
style.configure("TText", background="#FFFFFF", foreground="#4949c6")

# Input Form Interface
def switch_to_input_form():
    display_frame.pack_forget()
    input_frame.pack()


db = Database('Eleve.db')

def ajouter_eleve():
    nomEcole = nomEcole_entry.get()
    adresse = adresse_entry.get()
    niveauScolaire = niveauScolaire_entry.get()
    directeur  = directeur_entry.get()
    nombreEleves =  nombreEleves_entry.get()

    if nomEcole and adresse and niveauScolaire  and directeur  and  nombreEleves:
        try:
             nombreEleves = int( nombreEleves)  # Make sure age is a valid integer
        except ValueError:
            messagebox.showerror("Invalid Age", "Please enter a valid integer for age.")
            return
        db.ajouter_Eleves(nomEcole, adresse, niveauScolaire, directeur , nombreEleves)
        result_label.configure(text="Les informations ont été sauvegardées avec succès dans la base de données 'personnes.db'.")
        clear_input_fields()
        switch_to_display_form()  # Refresh the display table
    else:
        result_label.configure(text="Veuillez remplir tous les champs.", foreground="red")



# In the Database class:
def clear_input_fields():
    nomEcole_entry.delete(0, tk.END)
    adresse_entry.delete(0, tk.END)
    niveauScolaire_entry.delete(0, tk.END)
    directeur_entry.delete(0, tk.END)
    nombreEleves_entry.delete(0, tk.END)
    
# Display Form Interface
def switch_to_display_form():
    input_frame.pack_forget()
    display_frame.pack()
    afficher_eleve()

def afficher_eleve():
    eleve = db.recuperer_Eleves()

    for row in table.get_children():
        table.delete(row)

    for eleves in eleve:
        table.insert("", "end", values=(eleves.id,eleves.nomEcole,eleves.adresse,eleves.niveauScolaire,eleves.directeur,eleves.nombreEleves))

    result_label.configure(text="Les informations ont été récupérées avec succès depuis la base de données 'eleve.db'.")
# Input Form
input_frame = tk.Frame(root, bg="#F4F4F4")
input_label = ttk.Label(input_frame, text="Nouvelle Incription ", font=("Helvetica", 20), background="#F4F4F4")

input_label.pack(pady=5)
result_label = ttk.Label(input_frame, text="", background="#F4F4F4")
result_label.pack()

nomEcole_label = ttk.Label(input_frame, text="nomEcole:", background="#F4F4F4")
nomEcole_label.pack()
nomEcole_entry = ttk.Entry(input_frame)
nomEcole_entry.pack()

adresse_label = ttk.Label(input_frame, text="adresse:", background="#F4F4F4")
adresse_label.pack()
adresse_entry = ttk.Entry(input_frame)
adresse_entry.pack()

niveauScolaire_label = ttk.Label(input_frame, text="niveauScolaire:", background="#F4F4F4")
niveauScolaire_label.pack()
niveauScolaire_entry = ttk.Entry(input_frame)
niveauScolaire_entry.pack()

directeur_label = ttk.Label(input_frame, text="directeur:", background="#F4F4F4")
directeur_label.pack()
directeur_entry = ttk.Entry(input_frame)
directeur_entry.pack()

nombreEleves_label = ttk.Label(input_frame, text="nombreEleves_label:", background="#F4F4F4")
nombreEleves_label.pack()
nombreEleves_entry = ttk.Entry(input_frame)
nombreEleves_entry.pack()

ajouter_button = ttk.Button(input_frame, text="Ajouter", command=ajouter_eleve)
ajouter_button.pack(pady=10)

switch_to_display_button = ttk.Button(input_frame, text="Afficher", command=switch_to_display_form)
switch_to_display_button.pack()

# Display Form
display_frame = tk.Frame(root, bg="#53a8c9")

display_label = ttk.Label(display_frame, text="eleve inscrits", font=("Helvetica", 16), background="#F4F4F4")
display_label.pack(pady=10)

table_frame = ttk.Frame(display_frame)
table = ttk.Treeview(table_frame, columns=("id","nomEcole","adresse", "niveauScolaire", "directeur", "nombreEleves"), show="headings")
table.heading("id", text="ID")
table.heading("nomEcole", text="nomEcole")
table.heading("adresse", text="adresse")
table.heading("niveauScolaire", text="niveauScolaire")
table.heading("directeur", text="directeur")
table.heading("nombreEleves", text="nombreEleves")

table.column("id", width=50)
table.column("nomEcole", width=150)
table.column("adresse", width=150)
table.column("niveauScolaire", width=80)
table.column("directeur", width=150)
table.column("nombreEleves", width=150)



table.tag_configure("oddrow", background="#E8E8E8")
table.tag_configure("evenrow", background="#FFFFFF")

table.pack(padx=10, pady=10)
table_frame.pack(padx=10, pady=5)

switch_to_input_button = ttk.Button(display_frame, text="Retour", command=switch_to_input_form)
switch_to_input_button.pack(pady=10)

# Other Functions
def on_quit():
    db.fermer_connexion()
    root.destroy()

# Quit Button
quit_button = ttk.Button(root, text="Quitter", command=on_quit)
quit_button.pack(pady=10)

# Start the program
switch_to_input_form()
root.mainloop()

print("Fin du programme.")


