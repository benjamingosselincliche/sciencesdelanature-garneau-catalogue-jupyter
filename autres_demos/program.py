import cv2
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import ttkthemes as th
import matplotlib.pyplot as plt
import pickle
from cvzone.HandTrackingModule import HandDetector

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reconnaissance Roche-Papier-Ciseaux")
        self.classes = ["Roche", "Papier", "Ciseaux"]

        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 640)
        self.cap.set(4, 480)

        self.sign_to_capture = None
        self.capture_count = 0
        self.is_playing = False
        self.image_data = []
        self.detector = HandDetector(detectionCon=0.5, maxHands=2)  # Initialisation du détecteur de main

        self.style = th.ThemedStyle(self.root)
        self.style.set_theme("adapta")

        self.create_interface()
        self.create_model()
        self.update_camera()

    def create_interface(self):
        main_frame = ttk.Frame(self.root)
        main_frame.pack(padx=20, pady=20)

        ttk.Label(main_frame, text="Capturez les images :").pack()

        capture_frame = ttk.Frame(main_frame)
        capture_frame.pack(pady=10)

        # Ajout d'un Label pour afficher la vidéo de la caméra
        self.camera_label = ttk.Label(main_frame)
        self.camera_label.pack()

        #création des boutons roche,papier,Ciseaux
        for classe in self.classes:
            self.create_capture_button(capture_frame, classe)


        ttk.Label(main_frame, text="Capturer :").pack(side=tk.LEFT)
        self.label_var = tk.StringVar()
        self.label_var.set("0")
        ttk.Label(main_frame, textvariable=self.label_var).pack(side=tk.LEFT)

        
        ttk.Label(main_frame, text="Prédiction :").pack(side=tk.RIGHT)
        self.prediction_label = ttk.Label(main_frame, text="")
        self.prediction_label.pack(side=tk.RIGHT)

        ttk.Label(main_frame, text="Confiance :").pack(side=tk.RIGHT)
        self.confidence_label = ttk.Label(main_frame, text="")
        self.confidence_label.pack(side=tk.RIGHT)

        train_button = ttk.Button(main_frame, text="Entraîner le modèle", command=self.train_model)
        train_button.pack()

        play_button = ttk.Button(main_frame, text="Jouer", command=self.play_game)
        play_button.pack()

        play_button = ttk.Button(main_frame, text="Stop", command=self.stop_game)
        play_button.pack()

        reset_button = ttk.Button(main_frame, text="Réinitialiser", command=self.reset_data)
        reset_button.pack()


    def create_capture_button(self, parent, sign):
        button = ttk.Button(parent, text=sign, command=lambda: self.capture_10_images(sign))
        button.pack(side="left", padx=10)

    def create_model(self):

        # Créez un modèle séquentiel
        self.model = Sequential()

        # Ajoutez des couches au modèle
        self.model.add(Dense(128, activation="relu", input_shape=(63,)))  # Adapté à la forme des vecteurs de caractéristiques
        self.model.add(Dense(64, activation="relu"))
        self.model.add(Dense(3, activation="softmax"))

        # Compilez le modèle
        self.model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

    def capture_10_images(self, sign):
        for i in range(10):
            self.capture_image(sign)

    def capture_image(self, sign):
        ret, frame = self.cap.read()
        if ret:
            # Détectez les mains dans le cadre
            hands, _ = self.detector.findHands(frame)

            if hands:
                # Obtenez les points de repère des mains détectées
                landmarks = hands[0]["lmList"]

                # Formatez les points de repère en un vecteur de caractéristiques
                features = np.array(landmarks).flatten()

                # Ajoutez le vecteur de caractéristiques avec l'étiquette aux données d'entraînement
                self.image_data.append((features, sign))

                # Incrémentez le compteur de captures
                self.capture_count += 1
                self.label_var.set(str(self.capture_count))

    def train_model(self):
        if len(self.image_data) == 0:
            messagebox.showerror("Erreur", "Aucune donnée à entraîner.")
            return

        data = np.array([item[0] for item in self.image_data], dtype=np.float32)
        labels = np.array([item[1] for item in self.image_data])

        labels = np.where(labels == 'Roche', 0, labels)
        labels = np.where(labels == 'Papier', 1, labels)
        labels = np.where(labels == 'Ciseaux', 2, labels)

        labels = tf.keras.utils.to_categorical(labels, 3)

        self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        history = self.model.fit(data, labels, epochs=5, batch_size=32)

        self.plot_training_history(history)

        messagebox.showinfo("Entraînement terminé", "Le modèle a été entraîné avec succès.")

    def plot_training_history(self, history):
        # Tracez la courbe de perte (loss)
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.plot(history.history['loss'], label='Perte (Loss)')
        plt.title('Courbe de perte (Loss)')
        plt.xlabel('Époque (Epoch)')
        plt.ylabel('Perte (Loss)')
        plt.legend()

        # Tracez la courbe de précision (accuracy)
        plt.subplot(1, 2, 2)
        plt.plot(history.history['accuracy'], label='Précision (Accuracy)')
        plt.title('Courbe de précision (Accuracy)')
        plt.xlabel('Époque (Epoch)')
        plt.ylabel('Précision (Accuracy)')
        plt.legend()

        plt.tight_layout()
        plt.show()

    def predict(self):
        
        ret, frame = self.cap.read()
        
        if ret:
            # Détectez les mains dans le cadre
            hands, _ = self.detector.findHands(frame)

            if hands:
                # Obtenez les points de repère des mains détectées
                landmarks = hands[0]["lmList"]

                # Formatez les points de repère en un vecteur de caractéristiques
                features = np.array(landmarks).flatten()

                # Utilisez le modèle pour prédire le geste (Roche, Papier, Ciseaux)
                prediction = self.model.predict(features.reshape(1, -1))

                # Convertissez la prédiction en une classe (Roche, Papier, Ciseaux)
                signe = self.classes[np.argmax(prediction)]

                # Affichez la prédiction
                self.prediction_label.config(text=f"{signe}")

                # Affichez le pourcentage de confiance
                confidence = prediction[0][np.argmax(prediction)] * 100
                self.confidence_label.config(text=f"{confidence:.2f}%")

                if self.is_playing:
                    self.root.after(1000, self.predict) 

    def play_game(self):
        self.is_playing = True
        self.predict()

    def stop_game(self):
        self.is_playing = False

    def reset_data(self):
        self.sign_to_capture = None
        self.capture_count = 0
        self.image_data = []
        self.label_var.set("0")
        self.prediction_label.config(text="")
        self.confidence_label.config(text="")

    def update_camera(self):
        ret, frame = self.cap.read()
        if ret:
            # Détectez les mains dans le cadre
            hands, image = self.detector.findHands(frame)

            if hands:
                # Dessinez les marqueurs des mains (cercles verts) sur l'image
                for hand in hands:
                    for point in hand["lmList"]:
                        x, y = point[0], point[1]
                        cv2.circle(image, (x, y), 5, (0, 255, 0), -1)
            
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = Image.fromarray(frame)
            photo = ImageTk.PhotoImage(image=frame)
            self.camera_label.config(image=photo)
            self.camera_label.image = photo
            self.root.after(10, self.update_camera)


    
        

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    app.run()
