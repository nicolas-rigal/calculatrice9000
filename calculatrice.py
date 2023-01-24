from tkinter import *
import tkinter as tk

formule = "" 
apostrof ="'"

def click(num): 
    global formule 
    formule = formule + str(num) 
    equation.set(formule) 

def egalclick(): 
    try: 
        global formule 
        resultat = str(eval(formule))
        memoire(formule + "=" + str(resultat))
        equation.set(resultat) 
        formule = resultat

    except: 
        equation.set(" error ") 
        formule = "" 

def effacer(): 
    global formule 
    formule = "" 
    equation.set("") 

def supprimer_dernier_caractere():
    global formule
    calculatrice.delete(len(calculatrice.get())-1, END)
    formule = calculatrice.get()

def memoire(formule):
    tableau = []
    tableau += formule
    historique.insert(END, formule)
    
def acc_historique():
    suprimehistorique.configure(state=NORMAL, background='red')

def sup_historique():
    suprimehistorique.configure(state=DISABLED, background='#383B44')
    historique.delete(0, END)


#############   parametre de ma fenetre  ############################

fenetre = tk.Tk() 
fenetre.title("Calculatrice") 
fenetre.geometry("410x550")
# pour executer iconbitmap doit être il doit etre seul ouvert dans svcode  
fenetre.iconbitmap('@logo.xbm')
fenetre.configure(background="#4A4650")
equation = StringVar()


calculatrice = Entry(fenetre, textvariable=equation, background="#E0E722", fg = 'black', border=0)
calculatrice.grid(columnspan=5,  pady= 30 , padx = 20 , ipadx = 100 , ipady = 10)

#############   bloc 2  historique  ############################
historique = Listbox(fenetre, height = 4,
                     background="#1E2026",
                     fg = 'white',
                     border=0,
                     highlightthickness=0)
historique.grid(row=1, columnspan=5,pady= 10, ipadx = 100 , ipady = 10)

#############   block  3/lingne 1   ############################


chiffre_1 = Button(fenetre, text=' 1 ',
                   command=lambda: click(1),
                   height=2, width=10,
                   background='#4D4DFF',
                   fg='white',
                   font='bold') 
chiffre_1.grid(row=6, column=0) 

chiffre_2 = Button(fenetre, text=' 2 ',
                   command=lambda: click(2),
                   height=2, width=10,
                   background='#4D4DFF',
                   fg='white',
                   font='bold') 
chiffre_2.grid(row=6, column=1) 

chiffre_3 = Button(fenetre, text=' 3 ',
                   command=lambda: click(3),
                   height=2, width=10,
                   background='#4D4DFF',
                   fg='white',
                   font='bold') 
chiffre_3.grid(row=6, column=2) 

chiffre_4 = Button(fenetre, text=' 4 ',
                   command=lambda: click(4),
                   height=2, width=10,
                   background='#4D4DFF',
                   fg='white',
                   font='bold') 
chiffre_4.grid(row=5, column=0) 

chiffre_5 = Button(fenetre, text=' 5 ',
                   command=lambda: click(5),
                   height=2, width=10,
                   background='#4D4DFF',
                   fg='white',
                   font='bold') 
chiffre_5.grid(row=5, column=1) 

chiffre_6 = Button(fenetre, text=' 6 ',
                   command=lambda: click(6),
                   height=2, width=10,
                   background='#4D4DFF',
                   fg='white',
                   font='bold') 
chiffre_6.grid(row=5, column=2) 

chiffre_7 = Button(fenetre, text=' 7 ',
                   command=lambda: click(7),
                   height=2, width=10,
                   background='#4D4DFF',
                   fg='white',
                   font='bold') 
chiffre_7.grid(row=4, column=0) 

chiffre_8 = Button(fenetre, text=' 8 ',
                   command=lambda: click(8),
                   height=2, width=10,
                   background='#4D4DFF',
                   fg='white',
                   font='bold') 
chiffre_8.grid(row=4, column=1) 

chiffre_9 = Button(fenetre, text=' 9 ',
                   command=lambda: click(9),
                   height=2, width=10,
                   background='#4D4DFF',
                   fg='white',
                   font='bold') 
chiffre_9.grid(row=4, column=2)

plus_moins = Button(fenetre, text=' \U0000207A/\U0000208B ',
                    command=lambda: click("-"),
                    height=2, width= 10,
                    background='#DB3EB1',
                    fg='white',
                    font='bold')
plus_moins.grid(row= 7, column=0)

chiffre_0 = Button(fenetre, text=' 0 ',
                   command=lambda: click(0),
                   height=2, width=10,
                   background='#4D4DFF',
                   fg='white',
                   font='bold') 
chiffre_0.grid(row=7, column=1) 

plus = Button(fenetre, text=' + ',
              command=lambda: click("+"),
              height=2, width=10,
              background='#44D62C',
              fg='white',
              font='bold') 
plus.grid(row=6, column=3) 

soustrac = Button(fenetre, text=' - ',
                  command=lambda: click("-"),
                  height=2, width=10,
                  background='#44D62C',
                  fg='white',
                  font='bold') 
soustrac.grid(row=5, column=3) 

multipl = Button(fenetre, text=' x ',
                 command=lambda: click("*"),
                 height=2, width=10,
                 background='#44D62C',
                 fg='white',
                 font='bold') 
multipl.grid(row=4, column=3) 

divide = Button(fenetre, text=' \U000000F7 ',
                command=lambda: click("/"),
                height=2, width=10,
                background='#44D62C',
                fg='white',
                font='bold') 
divide.grid(row=3, column=3) 
    
racine_carree = Button(fenetre, text="\U0000221A",
                command=lambda: click("**0.5"),
                height=2, width=10,
                background='#DB3EB1',
                fg='white',
                font='bold') 
racine_carree.grid(row=3, column=2) 

puissance_carree = Button(fenetre, text="x\U000000B2",
                command=lambda: click("**2"),
                height=2, width=10,
                background='#DB3EB1',
                fg='white',
                font='bold') 
puissance_carree.grid(row=3, column=1) 

puissance = Button(fenetre, text="x\U0000207F",
                command=lambda: click("**"),
                height=2, width=10,
                background='#DB3EB1',
                fg='white',
                font='bold') 
puissance.grid(row=3, column=0) 

egal = Button(fenetre, text=' = ',
                command=egalclick,
                height=2, width=10,
                background='#FFAD00',
                font='bold',
                fg='white')
egal.grid(row=7, column=3) 

effacer = Button(fenetre, text='C',
                command=effacer,
                height=2, width=10,
                background='#D22730',
                fg='white',
                font='bold') 
effacer.grid(row=2, column=2)  

supprimer_soft = Button(fenetre,
                text="\U0000232B",
                command=supprimer_dernier_caractere,
                height=2, width=10,
                background='#D22730',
                fg='white',
                font='bold') 
supprimer_soft.grid(row=2, column=3) 

Decimal= Button(fenetre, text=',',
                command=lambda: click('.'),
                height=2, width=10,
                background='#44D62C',
                fg='white',
                font='bold') 
Decimal.grid(row=7, column=2) 
   
pourcent= Button(fenetre, text='%',
                command=lambda: click('/100'),
                height=2, width=10,
                background='#DB3EB1',
                fg='white',
                font='bold') 
pourcent.grid(row=2, column=1)  
    
memo= Button(fenetre, text='M',
             command= lambda: acc_historique(),
             height=2, width=10,
             background='#D22730',
             fg='white',
             font='bold') 
memo.grid(row=2, column=0)

parenthese_ouverante= Button(fenetre, text='(',
                command=lambda: click('('),
                height=2, width=10,
                background='#44D62C',
                fg='white',
                font='bold') 
parenthese_ouverante.grid(row=8, column=0)

parenthese_fermente= Button(fenetre, text=')',
                command=lambda: click(')'),
                height=2, width=10,
                background='#44D62C',
                fg='white',
                font='bold')
parenthese_fermente.grid(row=8, column=1)

suprimehistorique= Button(fenetre, text= 'Suppression de l'+ apostrof +'historique',
                       command= lambda: sup_historique(),
                       height=2, width=23, 
                       background='#D22730',
                       fg='white',
                       font='bold',
                       state=DISABLED)
suprimehistorique.grid(row=8, column=2, columnspan = 2)


    
fenetre.mainloop()