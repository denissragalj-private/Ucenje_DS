import tkinter as tk

def create_styled_text_window_with_buttons():
    """
    Kreira Tkinter prozor s tk.Text widgetom, gumbima s i bez boja,
    i demonstrira primjenu različitih stilova (tagova) na tekstu.
    """
    root = tk.Tk()
    root.title("Primjer Stiliziranog Teksta i Gumba")
    root.geometry("600x600") # Povećana visina prozora
    root.resizable(False, False) # Onemogući promjenu veličine prozora od strane korisnika

    # Kreiranje Text widgeta gdje ćemo prikazivati stilizirani tekst
    text_area = tk.Text(root, wrap="word", font=("Arial", 12), bg="#2B2B2B", fg="white")
    text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    # --- DEFINIRANJE TAGOVA ---
    text_area.tag_configure("naslov", foreground="gold", font=("Consolas", 16, "bold"))
    text_area.tag_configure("uspjeh", foreground="lime green", font=("Arial", 12, "bold"))
    text_area.tag_configure("upozorenje", foreground="orange", font=("Arial", 12, "italic"))
    text_area.tag_configure("greska", foreground="red", font=("Courier New", 12, "bold"))
    text_area.tag_configure("istaknuto", foreground="cyan", font=("Arial", 12), underline=True)
    text_area.tag_configure("highlight", foreground="black", background="yellow", font=("Arial", 12, "bold"))
    text_area.tag_configure("plavi_underline", foreground="blue", underline=True)
    text_area.tag_configure("info", foreground="lightgray", font=("Arial", 11))
    # NOVI TAG: Za centrirani zeleni tekst
    text_area.tag_configure("centrirani_zeleni", foreground="lime green", font=("Arial", 12), justify="center")


    # --- UMETANJE TEKSTA S TAGOVIMA ---
    text_area.config(state=tk.NORMAL) 

    text_area.insert(tk.END, "--- DOBRODOŠLI U DEMO TAGOVA I GUMBA ---\n\n", "naslov")
    text_area.insert(tk.END, "Operacija je uspješno završena!\n", "uspjeh")
    text_area.insert(tk.END, "Podaci su uspješno spremljeni u bazu.\n\n", "uspjeh")
    text_area.insert(tk.END, "Upozorenje: Provjerite mrežnu vezu.\n", "upozorenje")
    text_area.insert(tk.END, "Neki podaci možda nisu ažurirani.\n\n", "upozorenje")
    text_area.insert(tk.END, "GREŠKA: Datoteka nije pronađena! (Error 404)\n\n", "greska")
    text_area.insert(tk.END, "Ovo je ", None)
    text_area.insert(tk.END, "važna riječ", "istaknuto")
    text_area.insert(tk.END, " u rečenici.\n\n", None)
    text_area.insert(tk.END, "Ovaj red je ", None)
    text_area.insert(tk.END, "istaknut žutom pozadinom", "highlight")
    text_area.insert(tk.END, ".\n\n", None)
    text_area.insert(tk.END, "Plavo i podcrtano!\n\n", "plavi_underline")

    text_area.config(state=tk.DISABLED) # Onemogućavamo Text widget

    # --- OKVIR ZA GUMBE (POSTAVLJEN NA DNO) ---
    button_frame = tk.Frame(root, pady=10) 
    button_frame.pack(side=tk.BOTTOM, fill=tk.X) 

    # --- FUNKCIJE ZA GUMBE ---
    def on_default_button_click():
        text_area.config(state=tk.NORMAL)
        text_area.insert(tk.END, "Kliknuli ste na 'Gumb Bez Boje'!\n", "info") 
        text_area.config(state=tk.DISABLED)
        text_area.see(tk.END) 

    def on_colored_button_click():
        text_area.config(state=tk.NORMAL)
        text_area.insert(tk.END, "Kliknuli ste na 'Obojeni Gumb'!\n", "uspjeh") 
        text_area.config(state=tk.DISABLED)
        text_area.see(tk.END) 

    def on_centered_green_button_click():
        text_area.config(state=tk.NORMAL)
        # Dodajemo nove redove prije i poslije da bi centriranje bilo jasnije
        text_area.insert(tk.END, "\n", None) 
        text_area.insert(tk.END, "Ovo je centrirani zeleni tekst!\n", "centrirani_zeleni")
        text_area.insert(tk.END, "---------------\n\n", "info") # Dodaj crtice kao separator
        text_area.config(state=tk.DISABLED)
        text_area.see(tk.END)

    def on_exit_button_click():
        text_area.config(state=tk.NORMAL)
        text_area.insert(tk.END, "Kliknuli ste 'Izlaz iz Demo-a' gumb. Zatvaram prozor...\n", "greska") 
        text_area.config(state=tk.DISABLED)
        text_area.see(tk.END) 
        root.after(1000, root.destroy) 

    # --- GUMBI NA PROZORU ---
    default_button = tk.Button(button_frame, text="Gumb Bez Boje", command=on_default_button_click, height=1) 
    default_button.pack(side=tk.LEFT, padx=5) 

    colored_button = tk.Button(button_frame, text="Obojeni Gumb", 
                               command=on_colored_button_click, 
                               fg="white", bg="dodgerblue", height=1) 
    colored_button.pack(side=tk.LEFT, padx=5)

    # NOVI GUMB: Za centrirani zeleni tekst
    centered_green_button = tk.Button(button_frame, text="Centrirani Zeleni Tekst",
                                       command=on_centered_green_button_click,
                                       fg="white", bg="darkgreen", height=1)
    centered_green_button.pack(side=tk.LEFT, padx=5)


    exit_button = tk.Button(button_frame, text="Izlaz iz Demo-a", 
                            command=on_exit_button_click, 
                            fg="white", bg="firebrick", height=1) 
    exit_button.pack(side=tk.RIGHT, padx=5) 

    # Pokretanje Tkinter event petlje
    root.mainloop()

# Poziv funkcije za kreiranje prozora
create_styled_text_window_with_buttons()