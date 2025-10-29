import tkinter as tk
from tkinter import messagebox

# Aplikācijas kas aprēķina gravitācijas spēku starp diviem objektiem

# Gravitācijas konstante, kur e ir skaitlis 10
G = 6.67e-11

# Definē funkciju gravitācijas spēka aprēķināšanā
def gravitacijas_speks():
    try:
        # Atlasa skaitli no pirmās ievades
        masa1 = float(ievade1.get())
        # Atlasa skaitli no otrās ievades
        masa2 = float(ievade2.get())
        # Atlasa skaitli no trešās ievades
        radius = float(ievade3.get())
        # Pārliecinās vai radius nav negatīvs skaitlis vai nulle
        if radius <= 0:
            # Ja rādisu ir negatīvs izmet kļūdu
            messagebox.showerror('Kļuda: Rādius nevar būt nulle vai negatīvs!')
        else:
            # Gravitācijas spēka aprēķināšanas formula
            F = G * masa1 * masa2 / radius**2
            # Atjaunina rezultātu izmantojot config
            rezultats.config(text = 'Rezultāts: {F} N')
    # Izmet kļūdu ja nav ievadīti skaitļi
    except ValueError:
        messagebox.showerror('Kļūda: Ievadi skaitļus!')


    

# Definē galveno lapu
root = tk.Tk()
# Loga virsrakts
root.title("Gravitācijas spēka aprēķināšana")
# Loga izmēri (WidthxHeight)
root.geometry('700x700')

attels = tk.PhotoImage(file='attēls2.png')

tk.Label(root, text='Ievadi pirmā objekta masu kilogramos').pack()
#Izveido ievades lauciņu
ievade1 = tk.Entry(root)
ievade1.pack()
tk.Label(root, text='Ievadi otrā objekta masu kilogramos').pack()
#Izveido ievades lauciņu
ievade2 = tk.Entry(root)
ievade2.pack()
tk.Label(root, text='Ievadi objekta rādiusu').pack()
#Izveido ievades lauciņu
ievade3 = tk.Entry(root)
ievade3.pack()
# Poga lai aprēķinātu gravitācijas spēku.
tk.Button(root, text='Aprēķināt', command=gravitacijas_speks).pack()
rezultats = tk.Label(root, text='Rezultāts: ').pack()

attela_konteiners = tk.Label(root, image=attels)
attela_konteiners.image = attels
attela_konteiners.pack()

# Palaiž programmu
root.mainloop()