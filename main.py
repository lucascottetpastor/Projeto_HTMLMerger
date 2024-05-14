import os
import tkinter as tk
from tkinter import filedialog




def lerarquivos(dir):
    lista = os.listdir(dir)
    HTMLinteiro = ''
    arqHTML, arqtxt = '' , ''
    for pasta in lista:
        listaDentro = os.listdir(f'{dir}/{pasta}')
        for itens in listaDentro:
            if itens.lower().endswith(".txt"):
                nomeTXT = itens
                with open(f'{dir}/{pasta}/{nomeTXT}', 'r', encoding='utf-8') as arq:
                    arqtxt = arq.read()
                    arqtxt = arqtxt.replace('\n',  '<br>')

            if os.path.isdir(f'{dir}/{pasta}/{itens}'):
                listaDentro2 = os.listdir(f'{dir}/{pasta}/{itens}')
                for i in listaDentro2:
                    if i.lower().endswith(".html"):
                        nomeWEB = i
                        with open(f'{dir}/{pasta}/{itens}/{nomeWEB}', 'r', encoding='utf-8') as arq:
                            arqHTML = arq.read()
        HTMLinteiro = f'{HTMLinteiro} <br><hr><br> {arqHTML} <br><hr><br>{arqtxt}'
        arqHTML, arqtxt = '' , ''

    with open('FINALLL.html', 'w', encoding='utf-8') as arqF:
        arqF.write(HTMLinteiro)

def selecionar_pasta():
    pasta_selecionada = filedialog.askdirectory()
    if pasta_selecionada:
        campo_texto.insert(0, pasta_selecionada)
    else:
        campo_texto.insert(0,"Nenhuma pasta selecionada")

root = tk.Tk() 
root.title("Selecionar Pasta")
root.geometry("400x250")
root.option_add("*Font", ('Arial', 12))
root.resizable(False, False)
root.config(bg="#000000")

# Criando um botão para selecionar a pasta
btn_selecionar = tk.Button(root, text="Selecionar Pasta", command=selecionar_pasta)
btn_selecionar.pack(pady=20)


campo_texto = tk.Entry(root, width=40)
campo_texto.pack(pady=20)

enable_button = tk.Button(root, text="Transformar", bg="#0CBF0C", command=lambda: lerarquivos(campo_texto.get()))
enable_button['width'] = 30
enable_button['height'] = 2
enable_button.pack()

# Rodando o loop principal da aplicação
root.mainloop()

