import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np
import pandas as pd
import tkinter as tk


window =tk.Tk()
window.geometry("700x200")
label_error = tk.Label(text="Les valeurs données doivent\nêtre des nombres différents de 0 ! ",fg="red" )#uniquement en cas d'erreur



def draw(t0: float, tf: float, m_x: float, k_x: float, m_y: float, k_y: float): 

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_ylabel('')
    ax1.set_xlabel('temps')

    x = np.arange(t0,tf,0.1)
    ax1.plot(x, np.sin( np.sqrt(k_x/m_x) * x ),'r')
    if m_y != 0 and k_y != 0 :
        ax1.plot(x, np.sin( np.sqrt(k_y/m_y) * x ),'b') 

    plt.legend(['x(t)','y(t)'])
    plt.show()
    


def manageEntry():
    
    try:
        global label_error
        t0 = float(input_t0.get())
        tf = float(input_tf.get())
        k_x = float(input_KX.get())
        m_x = float(input_MX.get())
        k_y = float(input_KY.get())
        m_y = float(input_MY.get())

        if(k_x == 0 or m_x == 0):
           label_error.grid(row=6,column=3)
        else :
            label_error.grid_forget()
            draw(t0,tf,k_x,m_x,k_y,m_y)


    except ValueError:
        print( "Not a float" )
        label_error.grid(row=6,column=3)





greeting = tk.Label(text="Paramètres de calcul")
greeting.grid(row=1,column=3)

button = tk.Button(
    text="exécuter x(t)",
    width=15,
    height=2,
    bg="gray",
    fg="white",
    command=manageEntry
)
button.grid(row=5,column=3)

#partie gauche , temps
tk.Label(text="t0").grid(row=3,column=1)
input_t0 = tk.Entry();input_t0.grid(row=3,column=2);input_t0.insert(0,"0")


tk.Label(text="temps final").grid(row=4,column=1)
input_tf = tk.Entry();input_tf.grid(row=4,column=2);input_tf.insert(0,"10")


#partie droite , data
label_data = tk.Label(text="caractéristiques \n du matériau")

tk.Label(text="M").grid(row=2,column=5)
tk.Label(text="K").grid(row=2,column=6)


tk.Label(text="X").grid(row=3,column=4)
input_MX = tk.Entry();input_MX.grid(row=3,column=5);input_MX.insert(0,"0")
input_KX = tk.Entry();input_KX.grid(row=3,column=6);input_KX.insert(0,"0")

tk.Label(text="Y").grid(row=4,column=4)
input_MY = tk.Entry();input_MY.grid(row=4,column=5);input_MY.insert(0,"0")
input_KY = tk.Entry();input_KY.grid(row=4,column=6);input_KY.insert(0,"0")



window.mainloop()







