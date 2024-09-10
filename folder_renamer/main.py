import tkinter as tk
from tkinter import filedialog
import os

def chosedir():
    #metodo para extrair o dir do user
    folder_path = filedialog.askdirectory(title="Selecione uma pasta")
    #complemento do dir extraido
    path = folder_path + '/'
    #extracao do nome para o ficheiro
    file = entry_file.get()
    #condicao de segurança
    try:
        #metodo 'os.listdir' para encontrar tudo o que está no dir
        for filename in os.listdir(path):
            #nome do ficheiro
            new_name = file + str(i) + '.png'
            source = path + filename
            new_name = path + new_name
            #rename do ficheiro
            os.rename(source,new_name)
            i+=1
    except:
        print('Ocorreu um erro, tente novamente...')

# Cria uma instância da aplicação Tkinter
root = tk.Tk()
root.title('Folder Renamer')
root.configure(background="white")
root.geometry('320x471')

btn_dir = tk.Button(root,bg='#F1F1F1',text='Escolha a sua pasta',command=chosedir)
btn_dir.pack(padx=10,pady=10)

label_file = tk.Label(root,bg='white',text='Escolha o nome para o seu ficheiro:')
label_file.pack(padx=10,pady=10)

entry_file = tk.Entry(root,bg='#F1F1F1')
entry_file.pack(padx=10,pady=10)
root.mainloop()
