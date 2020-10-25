import io
import matplotlib.pyplot as plt
import math
import tkinter as tk
from tkinter import filedialog



def filename():
    global file_path
    file_path = filedialog.askopenfilename()
    label = tk.Label(text=file_path)
    label.pack()


def main():
    with io.open(file_path,'r',encoding='utf8') as f:
        text = f.read()

    textTab = []
    words = {}
    sortedWords = {}

    textStr = text.lower()
    textTab = textStr.replace(".", "").replace(",", "").replace("?", "").replace('"', "").replace("'", "").replace("!", "").replace("-", "").replace("—", "").split()

    for x in textTab:
        if x in words:
            words[x] += 1
        else:
            words[x] = 1

    sortedWords = sorted(words.items(), key=lambda x: x[1], reverse=True)

    rank = 1
    ranga = {}

    for x in sortedWords:
        ranga[x] = rank
        rank += 1
        
    iloscslow = 0
    ilosc = []
    
    for x in sortedWords:
        ilosc.append(x[1])
        iloscslow += x[1]

    plt.plot(ranga.values(), ilosc, label="Funkcja ze słów z podanego pliku")
    plt.yscale('log')
    plt.xscale('log')

    plt.xlabel("Ranga")
    plt.ylabel("Częstotliwość")

    plt.legend()
    plt.show()


root = tk.Tk()
root.geometry("700x200")
root.title("ClearMind")

button = tk.Button( text="Wybór Pliku", command = filename)
button1 = tk.Button( text="Start", command = main)
manualText = tk.Label(text="Instrukcja obsługi programu ClearMind \n 1. Należy wybrać plik z rozszerzeniem .txt, w którym znajduje się próbka badawcza tekstu \n 2. Należy wybrać opcję Start \n 3. Interpretacja wyników polega na sprawdzeniu odchyłów na wykresie, możliwe odchyły mogą być oznaką potencjalnej choroby.")


button.pack()
button1.pack()
manualText.pack()
root.mainloop()



