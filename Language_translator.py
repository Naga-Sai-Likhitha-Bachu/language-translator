import tkinter as tk
from tkinter import ttk
from deep_translator import GoogleTranslator

languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "French": "fr",
    "Spanish": "es",
    "German": "de"
}

def translate_text():

    text = input_box.get("1.0", tk.END).strip()

    if not text:
        return

    target = languages[target_lang.get()]

    translated = GoogleTranslator(
        source="auto",
        target=target
    ).translate(text)

    result_box.delete("1.0", tk.END)

    result_box.insert(
        tk.END,
        translated
    )


root = tk.Tk()

root.title("Language Translator")

root.geometry("600x500")

tk.Label(
    root,
    text="Enter Text"
).pack()

input_box = tk.Text(
    root,
    height=8
)

input_box.pack(
    fill="x",
    padx=10
)

target_lang = ttk.Combobox(
    root,
    values=list(languages.keys())
)

target_lang.set("Hindi")

target_lang.pack()

tk.Button(
    root,
    text="Translate",
    command=translate_text
).pack(pady=10)

tk.Label(
    root,
    text="Translated Text"
).pack()

result_box = tk.Text(
    root,
    height=8
)

result_box.pack(
    fill="x",
    padx=10
)

root.mainloop()