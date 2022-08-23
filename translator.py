from tkinter import *
import googletrans
import textblob
from tkinter import ttk,messagebox

root = Tk()
root.geometry("880x300")

def translate_it():
    translated_text.delete(1.0,END)

    try:
        for key,value in languages.items():
            if(value == original_combo.get()):
                from_langauge_key = key
        for key,value in languages.items():
            if(value == translated_combo.get()):
                to_langauge_key = key

        words = textblob.TextBlob(original_text.get(1.0,END))
        words = words.translate(from_lang = from_langauge_key,to=to_langauge_key)
        translated_text.insert(1.0,words)

    except Exception as e:
        messagebox.showerror("Translator",e)
        
def clear_it():
    original_text.delete(1.0,END)
    translated_text.delete(1.0,END)
        

    
languages = googletrans.LANGUAGES
languages_list = list(languages.values())

original_text = Text(root,height=10,width=40)
original_text.grid(row=0,column=0,padx=20,pady=10)

translate_button = Button(root,text = "Translate",font=("Helvetica",24),
                          command=translate_it)
translate_button.grid(row=0,column=1,padx=10)

translated_text = Text(root,height=10,width=40)
translated_text.grid(row=0,column=2,padx=20,pady=10)

original_combo = ttk.Combobox(root,width=50,value=languages_list)
original_combo.current(21)
original_combo.grid(row=1,column=0)

translated_combo = ttk.Combobox(root,width=50,value=languages_list)
translated_combo.current(26)
translated_combo.grid(row=1,column=2)


clear_button = Button(root,text="Clear",width=20,command=clear_it)
clear_button.grid(row=1,column=1)

root.mainloop()


