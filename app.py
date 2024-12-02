import customtkinter as ctk

#configurando aparência
ctk.set_appearance_mode('dark')

#criando funcionalidades
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()
    
    #verificar se o usuário é git e a senha 123456
    if usuario == 'git' and senha == '123456':
        resultado_login.configure(text='Login feito com sucesso!',
        text_color='green')
    else:
        resultado_login.configure(text='Login incorreto',
        text_color='red')

#criação da janela principal
app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x300')

#Criando campos
#Label
label_usuario = ctk.CTkLabel(app,text='Login:')
label_usuario.pack(pady=10)
#Entry
campo_usuario = ctk.CTkEntry(app,placeholder_text='Digite seu Login')
campo_usuario.pack(pady=10)
#Label
label_senha = ctk.CTkLabel(app,text='Senha:')
label_senha.pack(pady=10)
#Entry
campo_senha = ctk.CTkEntry(app,placeholder_text='Digite Sua Senha', show='*')
campo_senha.pack(pady=10)
#Button
campo_entrar = ctk.CTkButton(app,text='Entrar', command=validar_login)
campo_entrar.pack(pady=20)
#campo msg de login
resultado_login = ctk.CTkLabel(app,text='')
resultado_login.pack(pady=10)




#Iniciar Aplicação
app.mainloop()