import random
import tkinter as tk
from PIL import Image, ImageTk
import pygame


# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Pierre - Papier - Ciseaux")
fenetre.geometry("1024x768")

# Charger la musique de fond
pygame.mixer.init()
pygame.mixer.music.load("Rush_E.mp3")  

# Baisser le volume
pygame.mixer.music.set_volume(0.1)

# Musique de fond en continue 
pygame.mixer.music.play(-1)

# Ajouter un bruitages pour les boutons
pierre_sound = pygame.mixer.Sound("SonPierre.wav")
papier_sound = pygame.mixer.Sound("SonVent.wav")
ciseaux_sound = pygame.mixer.Sound("SonCiseaux.wav")



# Fonction qui choisi au hasard pour l'ordinateur

def computer_choice():
    choices = ["Pierre", "Papier", "Ciseaux"]
    return random.choice(choices)




# Fonction qui permet de lancer le jeu
def play(user_choice):
    
    #test pour les btuitage des boutons quand c'est appuyé
    if user_choice == "Pierre":
        pierre_sound.play()
    elif user_choice == "Papier":
        papier_sound.play()
    elif user_choice == "Ciseaux":
        ciseaux_sound.play()
        
        
        
    nombre_de_coup.set(nombre_de_coup.get() + 1)
    
    computer = computer_choice() #Fait appel à la fonction qui choisi aléatoirement pour le PC

    # Logique pour déterminer le gagnant
    if user_choice == computer:
        result_var.set("Egalité !")
    elif (
        (user_choice == "Pierre" and computer == "Ciseaux") 
        or (user_choice == "Papier" and computer == "Pierre")
        or (user_choice == "Ciseaux" and computer == "Papier")
        ): 
        result_var.set("Vous avez gagné !")
        player_score_var.set(player_score_var.get() + 1)
    else:
        result_var.set("Vous avez perdu !")
        computer_score_var.set(computer_score_var.get() + 1)
       
    
    # Charger les images correspondantes aux choix
    user_img_label.config(image=get_image(user_choice))
    computer_img_label.config(image=get_image(computer))
  

    # Ajouter les choix à l'historique (du plus récent au plus ancien)
    history_listbox.insert(0, f"Vous : {user_choice} - Ordinateur : {computer}")
    verify_victory()


# permet de savoir si l'utilisateur peut continuer a jouer
def  verify_victory():
    
    if nombre_de_coup.get() >= 10:
        # il faut decidé quoi faire une fois les 10 coups 
        
        if player_score_var.get() > computer_score_var.get():
            result_var.set("Bien joué ! ")
        
        elif player_score_var.get() < computer_score_var.get(): 
            result_var.set("Dommage c'est perdu... ")
            
        else:
            result_var.set("égalité ")
            
        # désactiver les boutons
        rock_button.config(state=tk.DISABLED)
        paper_button.config(state=tk.DISABLED)
        scissors_button.config(state=tk.DISABLED)
        
        # boutton pour la réinitialisation
        reset_button.pack(pady=10)
        
def reset_scores():
    # Réinitialiser toutes les variables à 0 ou ""
    result_var.set("")
    player_score_var.set(0)
    computer_score_var.set(0)
    nombre_de_coup.set(0)
    history_listbox.delete(0, tk.END)
    user_img_label.config(image=empty_img)
    computer_img_label.config(image=empty_img)
    

    # Réactiver les boutons
    rock_button.config(state=tk.NORMAL)
    paper_button.config(state=tk.NORMAL)
    scissors_button.config(state=tk.NORMAL)
    # supprimer le bouton reset
    reset_button.pack_forget()
      


# Afficher une image en fonction du choix
def get_image(choice):
    if choice == "Pierre":
        return rock_img
    elif choice == "Papier":
        return paper_img
    else:
        return scissors_img


# Fonction a appeler lors de l'appui sur une touche

def on_key_press(e):
    if nombre_de_coup.get() < 10:
        if e.char.lower()== "p":
            play("papier")
        
        if e.char.lower()== "r":
            play("pierre")
                
        if e.char.lower()== "s":
            play("ciseaux")
                
    
    
# Associer la fonction on_key_press à l'evenement <key>
fenetre.bind("<Key>", on_key_press)






   
# Définition des variables
result_var = tk.StringVar()
player_score_var = tk.IntVar()
computer_score_var = tk.IntVar()
nombre_de_coup = tk.IntVar(value=0)
    
# Charger les images
rock_img = ImageTk.PhotoImage(Image.open("pierre.gif"))
paper_img = ImageTk.PhotoImage(Image.open("papier.gif"))
scissors_img = ImageTk.PhotoImage(Image.open("ciseaux.gif"))
empty_img = ImageTk.PhotoImage(Image.new("RGBA", (0,0),(0,0,0,0))) # création image vide et transparente

# Création des widget avec les images
user_label = tk.Label(fenetre, text="Choisissez : ")
user_label.pack(pady=10)

rock_button = tk.Button(fenetre, image=rock_img, command=lambda : play("Pierre"))
rock_button.pack(side=tk.LEFT, padx=10)
              
paper_button = tk.Button(fenetre, image=paper_img, command=lambda : play("Papier"))
paper_button.pack(side=tk.LEFT, padx=10)

scissors_button = tk.Button(fenetre, image=scissors_img, command=lambda : play("Ciseaux"))
scissors_button.pack(side=tk.LEFT, padx=10)

reset_button = tk.Button(fenetre, text="Nouvelle Partie", command=reset_scores)


# Etiqueetes pour afficher les images jouées
user_img_label = tk.Label(fenetre, image=None) # Pas d'image de départ
user_img_label.pack(pady=10)

computer_img_label = tk.Label(fenetre, image=None) # Pas d'image de départ
computer_img_label.pack(pady=10)

result_label = tk.Label(fenetre, textvariable=result_var)
result_label.pack(pady=20)

# Création d'une frame pour les score
score_frame = tk.Frame(fenetre)
score_frame.pack()

player_score_label = tk.Label(score_frame, text="Score J1 :")
player_score_label.pack(side=tk.LEFT, padx=10)

player_score_display = tk.Label(score_frame, textvariable=player_score_var)
player_score_display.pack(side=tk.LEFT, padx=10)

computer_score_label = tk.Label(score_frame, text="Score Ordinateur :")
computer_score_label.pack(side=tk.LEFT, padx=10)

computer_score_display = tk.Label(score_frame, textvariable=computer_score_var)
computer_score_display.pack(side=tk.LEFT, padx=10)

# Gestion de l'historique et de l'affichage
history_label = tk.Label(fenetre, text="Historique des coups : ")
history_label.pack(pady=10)

history_listbox = tk.Listbox(fenetre, width=40, height=6)
history_listbox.pack()


fenetre.mainloop()




