import sqlite3
from NewInscription import inscriptions

class Database:
    def __init__(self, db_name):
        self.connexion = sqlite3.connect(db_name)
        self.cursor = self.connexion.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Inscriptions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nomEcole TEXT,
                adresse TEXT,
                niveauScolaire TEXT,
                directeur TEXT,
                nombreEleves INTEGER
            )''')
        self.connexion.commit()

    def ajouter_Eleves(self, nomEcole, adresse, niveauScolaire, directeur, nombreEleves):
        self.cursor.execute("""
            INSERT INTO Inscriptions (nomEcole, adresse, niveauScolaire, directeur, nombreEleves) VALUES (?, ?, ?, ?, ?)
        """, (nomEcole, adresse, niveauScolaire, directeur, nombreEleves))
        self.connexion.commit()

    def recuperer_Eleves(self):
        self.cursor.execute('''
            SELECT * FROM Inscriptions
        ''')
        rows = self.cursor.fetchall()
        inscription = []
        for row in rows:
            inscriptionF = inscriptions(*row)  # Constructing the Inscription object
            inscription.append(inscriptionF)
        return inscription

    def fermer_connexion(self):
        self.connexion.close()
