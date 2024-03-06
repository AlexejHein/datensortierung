import os
import shutil
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


def sort_files_in_directory(directory):
    # Liste aller Dateien im ausgewählten Verzeichnis
    files = os.listdir(directory)

    for file in files:
        # Extrahiere die Dateiendung
        extension = os.path.splitext(file)[1][1:].lower()  # Umwandlung in Kleinbuchstaben für Konsistenz
        if extension == "":  # Für den Fall, dass keine Erweiterung vorhanden ist
            extension = "Andere"

        # Erstelle den Pfad zum neuen Ordner
        new_dir_path = os.path.join(directory, extension)

        # Überprüfe, ob der Ordner existiert, wenn nicht, erstelle ihn
        if not os.path.exists(new_dir_path):
            os.makedirs(new_dir_path)

        # Ziel für die Dateiverschiebung festlegen
        destination_path = os.path.join(new_dir_path, file)

        # Überprüfe, ob die Datei im Zielordner bereits existiert
        if os.path.exists(destination_path):
            # Dateiname und Erweiterung extrahieren
            base_name = os.path.splitext(file)[0]
            counter = 1  # Zähler für Umbenennung

            # Generiere neuen Dateinamen, bis einer verfügbar ist
            while True:
                new_base_name = f"{base_name}_{counter}"
                new_file_name = f"{new_base_name}.{extension}"
                destination_path = os.path.join(new_dir_path, new_file_name)
                if not os.path.exists(destination_path):
                    break
                counter += 1

        # Verschiebe die Datei in den neuen Ordner
        shutil.move(os.path.join(directory, file), destination_path)


def on_select(event=None):
    # Holt den Namen des ausgewählten Ordners
    selected_directory = folder_var.get()
    if selected_directory:
        directory_path = filedialog.askdirectory(initialdir=os.path.expanduser(f'~/{selected_directory}'))
        if directory_path:
            sort_files_in_directory(directory_path)
            messagebox.showinfo("Erfolg", "Dateien wurden erfolgreich sortiert.")


# Erstelle das Hauptfenster
root = tk.Tk()
root.title("Dateien sortieren")

# Erstelle eine Variable für das ausgewählte Verzeichnis
folder_var = tk.StringVar(root)

# Erstelle ein Dropdown-Menü mit den Optionen
folder_choices = ['Desktop', 'Downloads']
folder_var.set(folder_choices[0])  # setze die Standardauswahl

popupMenu = ttk.Combobox(root, textvariable=folder_var, values=folder_choices)
popupMenu.pack()

# Button, um die Auswahl zu bestätigen
select_button = tk.Button(root, text="Ordner auswählen und sortieren", command=on_select)
select_button.pack(pady=10)

# Starte die Tkinter event loop
root.mainloop()
