import PySimpleGUI as sg

# Define o tema da interface gráfica
sg.theme('DarkBlue')

# Define o layout da tela de cadastro
layout_cadastro = [
    [sg.Text('Nome:', font=('Helvetica', 14)), sg.InputText(key='nome', size=(20, 1))],
    [sg.Text('E-mail:', font=('Helvetica', 14)), sg.InputText(key='email', size=(20, 1))],
    [sg.Text('Senha:', font=('Helvetica', 14)), sg.InputText(key='senha', password_char='*', size=(20, 1))],
    [sg.Button('Cadastrar', font=('Helvetica', 14)), sg.Button('Cancelar', font=('Helvetica', 14))]
]

# Define a janela da tela de cadastro
janela_cadastro = sg.Window('Tela de Cadastro', layout_cadastro)

# Loop para processar os eventos da tela de cadastro
while True:
    evento, valores = janela_cadastro.read()
    if evento == sg.WINDOW_CLOSED or evento == 'Cancelar':
        break
    if evento == 'Cadastrar':
        sg.popup('Parabéns,', valores['nome'], '!\nCadastro realizado com sucesso!\n\nBem-vindo(a) à nossa plataforma!')

# Fecha a janela da tela de cadastro
janela_cadastro.close()

#armazena dados inseridos
if evento == 'Cadastrar':
    nome = valores['nome']
    sg.popup('Parabéns,', nome, '!\nCadastro realizado com sucesso!\n\nBem-vindo(a) à nossa plataforma!')


# Define o layout da tela de login
layout_login = [
    [sg.Text('Usuário:', font=('Helvetica', 14)), sg.InputText(key='usuario', size=(20, 1))],
    [sg.Text('Senha:', font=('Helvetica', 14)), sg.InputText(key='senha', password_char='*', size=(20, 1))],
    [sg.Checkbox('Lembrar-me', font=('Helvetica', 12))],
    [sg.Button('Entrar', font=('Helvetica', 14)), sg.Button('Cancelar', font=('Helvetica', 14))]
]

# Define a janela da tela de login
janela_login = sg.Window('Tela de Login', layout_login)

# Loop para processar os eventos da tela de login
while True:
    evento, valores = janela_login.read()
    if evento == sg.WINDOW_CLOSED or evento == 'Cancelar':
        break
    if evento == 'Entrar':
        if valores['usuario'] == 'admin' and valores['senha'] == 'admin':
            sg.popup('Login realizado com sucesso!')
        else:
            sg.popup('Usuário ou senha inválidos')

# Fecha a janela da tela de login
janela_login.close()

if evento == 'Entrar':
    if valores['usuario'] == 'admin' and valores['senha'] == 'admin':
        if valores['usuario'] == nome:
            sg.popup('Olá,', nome)
        else:
            sg.popup('Bem-vindo(a) à nossa plataforma!')
    else:
        sg.popup('Usuário ou senha inválidos')
