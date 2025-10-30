import tkinter as tk
from tkinter import messagebox

# Aplikācijas kas aprēķina gravitācijas spēku starp diviem objektiem.

# Gravitācijas konstante, kur e ir skaitlis 10 skaitlis -11 ir tā pakāpe.
G = 6.67e-11

# Definē funkciju gravitācijas spēka aprēķināšanai
def gravitacijas_speks():
    try:
        # Atlasa skaitli no pirmās ievades un pārveido to uz float formātu
        masa1 = float(ievade1.get())
        # Atlasa skaitli no otrās ievades un pārveido to uz float formātu
        masa2 = float(ievade2.get())
        # Atlasa skaitli no trešās ievades un pārveido to uz float formātu
        radius = float(ievade3.get())
        # Pārliecinās vai radius nav negatīvs skaitlis vai nulle
        if radius <= 0:
            # Ja rādisu ir negatīvs izmet kļūdu
            messagebox.showerror('Kļūda!', 'Rādius nevar būt negatīvs vai vienāds ar nulli')
            return
        # Gravitācijas spēka aprēķināšanas formula
        F = G * masa1 * masa2 / radius**2
        # Atjaunina rezultātu izmantojot config, izmantojot string formatēšanu rezultātu formatē ar 6 cipariem aiz nulles
        rezultats.config(text = f'Rezultāts: {F:.6e} N', bg='black')
            
    # Izmet kļūdu, ja nav ievadīti derīgi skaitļi
    except ValueError:
        messagebox.showerror('Kļūda!', 'Ievadi derīgus skaitļus!')


    

# Definē galveno lapu
root = tk.Tk()
# Loga virsrakts
root.title("Gravitācijas spēka aprēķināšana")
# Loga izmēri (WidthxHeight)
root.geometry('700x700')
# Fona krāsa
root.config(bg='#351b61')
# Ielādē attēlu
attels = tk.PhotoImage(file='attēls.png')

tk.Label(root, text='Ievadi pirmā objekta masu kilogramos',
         bg='black',
         fg='white',
         font=('Arial', 16)
         ).pack(anchor='w', pady=5)
#Izveido ievades lauciņu
ievade1 = tk.Entry(root, font=('Arial', 16))
ievade1.pack(anchor='w', pady=5, fill='x')
tk.Label(root, text='Ievadi otrā objekta masu kilogramos',
         bg='black',
         fg='white',
         font=('Arial', 16)
         ).pack(anchor='w')
#Izveido ievades lauciņu
ievade2 = tk.Entry(root, font=('Arial', 16))
ievade2.pack(anchor='w', pady=5, fill='x')
tk.Label(root, text='Ievadi objekta rādiusu',
         bg='black',
         fg='white',
         font=('Arial', 16)
         ).pack(anchor='w', pady=5)
#Izveido ievades lauciņu
ievade3 = tk.Entry(root, font=('Arial',16))
ievade3.pack(anchor='w', pady=5, fill='x')
# Poga lai aprēķinātu gravitācijas spēku.
tk.Button(root, text='Aprēķināt', command=gravitacijas_speks,
          bg='black',
          fg='white',
          font=('Arial', 16)
          ).pack()
rezultats = tk.Label(root, text='',
                     font=('Arial', 16),
                     bg='#351b61',
                     fg='white'
                     )
rezultats.pack()
# Izveido attēlam konteineri un to ievieto
attela_konteiners = tk.Label(root, image=attels)
# Saglabā attēla saiti, lai tas nepazustu
attela_konteiners.image = attels
# Parāda attēlu logā
attela_konteiners.pack()

# Palaiž programmu
root.mainloop()