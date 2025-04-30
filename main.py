import tkinter as tk
from math import *

root = tk.Tk()
root.geometry("800x500")

label = tk.Label(root, text="Калькулятор", font=("Arial", 18))
label.pack(padx=20, pady=20)

def on_button_click(value):
    if value == "=":
        try:
            print("Это равно")     
            result = eval(textbox.get("1.0", tk.END)) 
            textbox.delete("1.0", tk.END)
            print(result)
            textbox.insert(tk.END, result)
        except ZeroDivisionError:
          
            print("Ошибка: Деление на ноль!")
            textbox.delete("1.0", tk.END)
            textbox.insert(tk.END, "Ошибка: Деление на ноль!")
        except Exception as e:
    # Обработка ошибок, например логгирование с терминал
            print(f"Произошла ошибка: {e}")  

    elif value == "Clear":
        textbox.delete("1.0", tk.END)
        print("Clear")

    elif value == "√":
        try:
            hyi = eval(textbox.get("1.0", tk.END))
            sqrt_math = sqrt(hyi)
            textbox.delete("1.0", tk.END)
            textbox.insert(tk.END, sqrt_math)
        except SyntaxError as e:
            print(f"Произошла ошибка: {e}")
            textbox.delete("1.0", tk.END)
            textbox.insert(tk.END, "Ошибка")

    else:
        print(value)
        textbox.insert(tk.END, value)

        
textbox = tk.Text(root, height=3, font=("Arial", 16))
textbox.pack()
buttonFrame = tk.Frame(root)
textbox.delete("1.0", tk.END)


buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)
buttonFrame.columnconfigure(3, weight=1)



btn1x0 = tk.Button(buttonFrame, text="7", font=("Arial", 18),command=lambda v="7": on_button_click(v))
btn1x0.grid(row=1, column=0, sticky="we")
btn1x1 = tk.Button(buttonFrame, text="8", font=("Arial", 18),command=lambda v="8": on_button_click(v))
btn1x1.grid(row=1, column=1, sticky="we")
btn1x2 = tk.Button(buttonFrame, text="9", font=("Arial", 18),command=lambda v="9": on_button_click(v))
btn1x2.grid(row=1, column=2, sticky="we")
btn1x3 = tk.Button(buttonFrame, text="-", font=("Arial", 18),command=lambda v="-": on_button_click(v))
btn1x3.grid(row=1, column=3, sticky="we")

btn2x0 = tk.Button(buttonFrame, text="4", font=("Arial", 18),command=lambda v="4": on_button_click(v))
btn2x0.grid(row=2, column=0, sticky="we")
btn2x1 = tk.Button(buttonFrame, text="5", font=("Arial", 18),command=lambda v="5": on_button_click(v))
btn2x1.grid(row=2, column=1, sticky="we")
btn2x2 = tk.Button(buttonFrame, text="6", font=("Arial", 18),command=lambda v="6": on_button_click(v))
btn2x2.grid(row=2, column=2, sticky="we")
btn2x3 = tk.Button(buttonFrame, text="+", font=("Arial", 18),command=lambda v="+": on_button_click(v))
btn2x3.grid(row=2, column=3, sticky="we")

btn3x0 = tk.Button(buttonFrame, text="1", font=("Arial", 18),command=lambda v="1": on_button_click(v))
btn3x0.grid(row=3, column=0, sticky="we")
btn3x1 = tk.Button(buttonFrame, text="2", font=("Arial", 18),command=lambda v="2": on_button_click(v))
btn3x1.grid(row=3, column=1, sticky="we")
btn3x2 = tk.Button(buttonFrame, text="3", font=("Arial", 18),command=lambda v="3": on_button_click(v))
btn3x2.grid(row=3, column=2, sticky="we")
btn3x3 = tk.Button(buttonFrame, text="*", font=("Arial", 18),command=lambda v="*": on_button_click(v))
btn3x3.grid(row=3, column=3, sticky="we")

btn4x0 = tk.Button(buttonFrame, text="Clear", font=("Arial", 18),command=lambda v="Clear": on_button_click(v))
btn4x0.grid(row=4, column=0, sticky="we")
btn4x1 = tk.Button(buttonFrame, text="0", font=("Arial", 18),command=lambda v="0": on_button_click(v))
btn4x1.grid(row=4, column=1, sticky="we")
btn4x2 = tk.Button(buttonFrame, text="=", font=("Arial", 18),command=lambda v="=": on_button_click(v))
btn4x2.grid(row=4, column=2, sticky="we")
btn4x3 = tk.Button(buttonFrame, text="/", font=("Arial", 18),command=lambda v="/": on_button_click(v))
btn4x3.grid(row=4, column=3, sticky="we")
btn5x1 = tk.Button(buttonFrame, text="(", font=("Arial", 18), command=lambda v="(": on_button_click(v))
btn5x1.grid(row=0, column=0, sticky="we")
btn5x2 = tk.Button(buttonFrame, text=")", font=("Arial", 18), command=lambda v=")": on_button_click(v))
btn5x2.grid(row=0, column=1, sticky="we")
btn5x3 = tk.Button(buttonFrame, text=".", font=("Arial", 18), command=lambda v=".": on_button_click(v))
btn5x3.grid(row=0, column=2, sticky="we")
btn5x4 = tk.Button(buttonFrame, text="√", font=("Arial", 18), command=lambda v="√": on_button_click(v))
btn5x4.grid(row=0, column=3, sticky="we")
                      

buttonFrame.pack(fill="x")

root.mainloop()
