import tkinter as tk
from tkinter import ttk
from googletrans import Translator

class LanguageTranslatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Language Translator")
        master.geometry("800x600")
        master.configure(bg="#f0f4f7")

       
        self.title_label = tk.Label(master, text="🌐 Language Translator", font=("Arial", 24, "bold"), bg="#f0f4f7", fg="#333")
        self.title_label.pack(pady=20)

        
        self.label1 = tk.Label(master, text="Enter text to translate:", font=("Arial", 14), bg="#f0f4f7")
        self.label1.pack()
        self.entry = tk.Text(master, height=6, width=80, font=("Arial", 12))
        self.entry.pack(pady=10)

        
        self.label2 = tk.Label(master, text="Select language to translate to:", font=("Arial", 14), bg="#f0f4f7")
        self.label2.pack(pady=5)

        self.languages = {
            "English": "en",
            "Tamil": "ta",
            "French": "fr",
            "Spanish": "es",
            "German": "de",
            "Chinese (Simplified)": "zh-cn",
            "Japanese": "ja",
            "Hindi": "hi",
            "Arabic": "ar",
            "Portuguese": "pt",
            "Russian": "ru",
            "Korean": "ko",
            "Italian": "it",
            "Dutch": "nl",
            "Greek": "el",
            "Turkish": "tr",
            "Polish": "pl",
            "Vietnamese": "vi",
            "Indonesian": "id",
            "Thai": "th",
            "Hebrew": "iw"
        }

        self.language_var = tk.StringVar(master)
        self.language_var.set("English")
        self.language_dropdown = ttk.Combobox(master, textvariable=self.language_var, values=list(self.languages.keys()), font=("Arial", 12))
        self.language_dropdown.pack(pady=10)

        
        self.translate_button = tk.Button(master, text="Translate", font=("Arial", 14), bg="#007acc", fg="white", command=self.translate)
        self.translate_button.pack(pady=10)

        
        self.label3 = tk.Label(master, text="Translated text:", font=("Arial", 14), bg="#f0f4f7")
        self.label3.pack()
        self.translation_output = tk.Text(master, height=6, width=80, font=("Arial", 12), bg="#e8f0fe")
        self.translation_output.pack(pady=10)

    def translate(self):
        text = self.entry.get("1.0", tk.END).strip()
        target_lang = self.language_var.get()
        target_code = self.languages[target_lang]

        if text:
            try:
                translator = Translator()
                translated = translator.translate(text, dest=target_code)
                self.translation_output.delete("1.0", tk.END)
                self.translation_output.insert(tk.END, translated.text)
            except Exception as e:
                self.translation_output.delete("1.0", tk.END)
                self.translation_output.insert(tk.END, "Error: " + str(e))

def main():
    root = tk.Tk()
    app = LanguageTranslatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
