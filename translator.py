import tkinter as tk
from googletrans import Translator

class LanguageTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")

        self.translator = Translator()

        self.languages = ['English', 'French', 'Spanish', 'German', 'Telugu', 'Hindi', 'Tamil', 'Kannada']
        self.language_vars = [tk.BooleanVar() for _ in self.languages]
        self.checkboxes = [tk.Checkbutton(root, text=lang, variable=self.language_vars[i]) for i, lang in enumerate(self.languages)]
        for i, checkbox in enumerate(self.checkboxes):
            row = i // 2 + 2
            col = i % 2
            checkbox.grid(row=row, column=col, padx=10, pady=5, sticky=tk.W)

        self.input_text = tk.Text(root, height=10, width=50)
        self.input_text.grid(row=10, column=0, columnspan=2, padx=10, pady=5)
        self.set_placeholder(self.input_text, "Enter Text...")

        self.output_text = tk.Text(root, height=10, width=50, state="disabled")
        self.output_text.grid(row=11, column=0, columnspan=2, padx=10, pady=5)
        self.set_placeholder(self.output_text, "Translated Text...")

        self.translate_button = tk.Button(root, text="Translate", command=self.translate_text)
        self.translate_button.grid(row=12, column=0, columnspan=2, padx=10, pady=10, sticky=tk.E+tk.W)

    def set_placeholder(self, text_widget, placeholder):
        text_widget.insert("1.0", placeholder)
        text_widget.bind("<FocusIn>", lambda event: self.clear_placeholder(event, placeholder))
        text_widget.bind("<FocusOut>", lambda event: self.restore_placeholder(event, placeholder))

    def clear_placeholder(self, event, placeholder):
        text_widget = event.widget
        if text_widget.cget("state") == "normal" and text_widget.get("1.0", "end-1c") == placeholder:
            text_widget.delete("1.0", "end")

    def restore_placeholder(self, event, placeholder):
        text_widget = event.widget
        if text_widget.cget("state") == "normal" and text_widget.get("1.0", "end-1c").strip() == "":
            self.clear_placeholder(event, placeholder)

    def translate_text(self):
        input_text = self.input_text.get("1.0", "end-1c")

        self.output_text.config(state="normal")
        self.output_text.delete("1.0", "end")
        try:
            for i, lang_var in enumerate(self.language_vars):
                if lang_var.get():
                    target_lang = self.languages[i].lower()
                    translation = self.translator.translate(input_text, dest=target_lang)
                    translated_text = f"Translated to {self.languages[i]}:\n{translation.text}\n\n"
                    self.output_text.insert("end", translated_text)
        except Exception as e:
            self.output_text.insert("end", "Translation Error\n")
            print("Translation Error:", e)
        self.output_text.config(state="disabled")

def main():
    root = tk.Tk()
    app = LanguageTranslatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
