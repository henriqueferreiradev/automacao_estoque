import time
import pyautogui
import pyperclip
import pandas as pd
import os
import customtkinter
from tkinter import filedialog
import shutil

arquivo_selecionado = ''

def abrir_arquivo():
    global arquivo_selecionado
    arquivo_selecionado = filedialog.askopenfilename(
        title='Selecione um arquivo Excel',
        filetypes=[('Arquivos Excel','*.xlsx')]
    )
    if arquivo_selecionado:
        label_arquivo.configure(text=f'Selecionando: {arquivo_selecionado}')
def comecar():
    global arquivo_selecionado 
    if not arquivo_selecionado:
        label_arquivo.configure(text="Erro, nenhum arquivo selecionado")
        return
    
    caminho_arquivo = arquivo_selecionado
    caminho_arquivo_novo =  'C:/Users/henri/Desktop/consulta precos/CONCLUIDOS' 

    if not os.path.exists(caminho_arquivo_novo):
        os.makedirs(caminho_arquivo_novo)

    nome_arquivo = os.path.basename(caminho_arquivo)
    destino_final = os.path.join(caminho_arquivo_novo, nome_arquivo)
    columns = [0]
    df = pd.read_excel(caminho_arquivo, usecols=columns, header=None, dtype=str) 
    df.dropna(inplace=True) 

    print("Você tem 5 segundos para abrir o sistema...")
    time.sleep(5)

    for index, row in df.iterrows():
        codigo = str(row[0]).zfill(6)
        if len(codigo) == 5:
            codigo += "0"
        print(f"Processando código: {codigo}")

        
        pyperclip.copy(codigo)
        time.sleep(1)

        pyautogui.doubleClick(202, 155)
        pyautogui.press('backspace', presses=3)
 
        
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2)
        
        pyautogui.doubleClick(1176, 531)
        time.sleep(2) 
        
        pyautogui.click(932, 510)
        time.sleep(1)
        
        pyautogui.press('backspace')
        time.sleep(1)
        
        pyautogui.click(1176, 531)
        time.sleep(3) 
        
        pyautogui.click(648, 204)
        time.sleep(1)

        pyautogui.write("EST2025")
        time.sleep(2)

        pyautogui.click(1176, 531)
        time.sleep(3) 

    shutil.move(caminho_arquivo, destino_final)   
    label_final.configure(text=f"Tarefa concluída!\n Arquivo movido para {destino_final}") 

app = customtkinter.CTk()
app.geometry("500x200")

button = customtkinter.CTkButton(app, text="Abrir arquivo", command=abrir_arquivo)
button.pack(padx=20, pady=20)
label_arquivo = customtkinter.CTkLabel(app, text="Nenhum arquivo selecionado", wraplength=300)
label_arquivo.pack()

botao_iniciar = customtkinter.CTkButton(app, text="Começar", width=40, command=comecar)
botao_iniciar.pack()

label_final = customtkinter.CTkLabel(app, text='', width=120)
label_final.pack()
app.mainloop()