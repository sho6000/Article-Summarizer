from main import *
from tkinter import tk

root = tk.Tk()
root.title("News Summerizer")
root.geometry("1200x600")

tlabel = tk.Label(root, text="Title", font="roboto 20 bold")
tlabel.pack()

title = tk.Text(root, heigth=1, width=140)
title.config(state="disabled", bg="#dddddd")
title.pack()

alabel = tk.Label(root, text="Author", font="roboto 20 bold")
alabel.pack()

author = tk.Text(root, heigth=1, width=140)
author.config(state="disabled", bg="#dddddd")
author.pack()

plabel = tk.Label(root, text="Publication Date", font="roboto 20 bold")
plabel.pack()

pub_date = tk.Text(root, heigth=1, width=140)
pub_date.config(state="disabled", bg="#dddddd")
pub_date.pack()

slabel = tk.Label(root, text="Summary", font="roboto 20 bold")
slabel.pack()

summary = tk.Text(root, heigth=20, width=140)
summary.config(state="disabled", bg="#dddddd")
summary.pack()

selabel = tk.Label(root, text="Sentiment Analysis", font="roboto 20 bold")
selabel.pack()

senti = tk.Text(root, heigth=1, width=140)
senti.config(state="disabled", bg="#dddddd")
senti.pack()

ulabel = tk.Label(root, text="URL", font="roboto 20 bold")
ulabel.pack()

url = tk.Text(root, heigth=1, width=140)
url.pack()

# Add a Text widget for URL input and name it 'utext'
utext = tk.Text(root, height=1, width=140)
utext.pack()

btn=tk.Button(root, text="Summarize")
btn.pack()


root.mainloop() 
