import json
import sqlite3

# Merci chatgpt je vais te marier <3
with open("movies.json", "r", encoding="utf-8") as file:
    movies = json.load(file)


conn = sqlite3.connect("movies.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT,
    dateDeSortie TEXT,
    realisateur TEXT,
    note INT,
    notePublic INT,
    compagnie TEXT,
    origine TEXT,
    description TEXT,
    lienImage TEXT
)
""")


for movie in movies:
    cursor.execute("""
    INSERT INTO movies (nom, dateDeSortie, realisateur, note, notePublic, compagnie, origine, description, lienImage)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        movie.get("nom"),
        movie.get("dateDeSortie"),
        movie.get("realisateur"),
        movie.get("note"),
        movie.get("notePublic"),
        movie.get("compagnie"),
        movie.get("origine"),
        movie.get("description"),
        movie.get("lienImage")
    ))


conn.commit()
conn.close()

print("Base de données créée avec succès !")
