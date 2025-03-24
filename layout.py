import customtkinter as ctk
import time

# Função que atualiza o relógio
def atualizar_relogio():
    hora_atual = time.strftime(f'%H:%M:%S')  # Obtém a hora atual no formato HH:MM:SS
    label_relogio.configure(text=hora_atual)  # Atualiza o texto do label
    # Chama a função novamente a cada 1000ms (1 segundo)
    janela.after(1000, atualizar_relogio)

# Criação da janela principal
janela = ctk.CTk()
janela.title("Relógio Digital")
janela.geometry("300x150")
janela.configure(bg='black')
janela._set_appearance_mode("dark")

# Criando o label do relógio
label_relogio = ctk.CTkLabel(janela, text="", font=("Arial", 90), text_color="green", fg_color="black")
label_relogio.pack(pady=50)  # Adiciona o label à janela e centraliza

# Inicia a atualização do relógio
atualizar_relogio()

# Executa a aplicação
janela.mainloop()
