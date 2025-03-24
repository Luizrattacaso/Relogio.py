import customtkinter as ctk
import time

# Função que atualiza o relógio
def atualizar_relogio():
    hora_atual = time.strftime(f'%H:%M:%S')
    label_relogio.configure(text=hora_atual)
    janela.after(1000, atualizar_relogio)

# Criação da janela principal
janela = ctk.CTk()
janela.title("Relógio Digital")
janela.geometry("400x250")
janela.configure(bg='black')
janela._set_appearance_mode("dark")

# Criando o label do relógio
label_relogio = ctk.CTkLabel(janela, text="", font=("Arial", 90), text_color="green", fg_color="black")
label_relogio.pack(pady=50)

atualizar_relogio()

janela.mainloop()
