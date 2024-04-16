'''
import tkinter as tk

# 1 - Criando a janela
window = tk.Tk()
window.geometry("300x150")
window.title("Gerenciador de Frases")

# 2 - Adicionando o frame
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='x', expand=True)

# 3 - Adicionando o label
label=tk.Label(frame, text="Hello, World")
label.pack(fill='x', expand=True)

# 4 - Adicionando o input text
frase_lab = tk.Label(frame, text="Frase")
frase_lab.pack(fill='x', expand=True)

frase_input = tk.Entry(frame)
frase_input.pack(fill='x', expand=True)

# 5 - Função para alterar o texto do label
def click():
    label.config(text=frase_input.get())

# Adicionando o botão
button = tk.Button(frame, text="Enviar", command=click)
button.pack()

window.mainloop()
'''
def high_and_low(numbers):
    resp = numbers.split()
    for i in resp:
        int(i)
    maxx = max(resp)
    minn = min(resp)
    return f"{maxx} {minn}"
    

print(high_and_low('-122 474 -443 490 -701 712 -211 -622 36 -373 -495 39 493 -668 -883'))