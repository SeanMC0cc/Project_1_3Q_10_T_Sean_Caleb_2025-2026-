from pyscript import document, display

def show_players(event):
    document.getElementById("output").innerHTML = ""
    players = ["Abdullah", "Abeleda", "Arce", "Arias", "Bonzon", "Cajucom", "Catimbang", "Choi", "Cotioco", "Daradal", "Enriquez", "Escobar", "Espina", "Gano", "Garcia", "Kaur", "Ong", "Rufo", "Sanchez", "Santos", "Tan", "Vilale", "Yao", "Zosa",]

    for player in players:
        display(f"- {player}", target="output")