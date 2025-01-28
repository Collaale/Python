#Importar as bibliotecas necessárias
import pandas as pd
import pyautogui
import time


#Iniciando a automação
pyautogui.PAUSE = 0.5
# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
# entrar no link 
time.sleep(1)
pyautogui.write("http://www.sauer.pro.br/python/automacao/index.html")
pyautogui.press("enter")
time.sleep(5)


#breakpoint()

# Passo 2: Fazer login
# selecionar o campo de login
pyautogui.click(x=-1071, y=574)
# escrever o usuário na posição capturada
time.sleep(2)
pyautogui.write("admin")
pyautogui.press("tab") # passando pro próximo campo
#esrever a senha na posição capturada
time.sleep(2)
pyautogui.write("SimplificaPython")
pyautogui.click(x=-1031, y=683) # clique no botao de login

# Passo 3: Importar a base de alunos pra cadastrar
tabela = pd.read_csv("D:/Python/SIMPLIFICA PYTHON EXPRESS/02. AULA 02/Códigos/alunos.csv")
#print(tabela)

time.sleep(2)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    
    # clicar no campo de cliente/aluno
    pyautogui.click(x=-1076, y=346)
    # pegar da tabela o valor do campo que a gente quer preencher
    nome = tabela.loc[linha, "Nome"]
    # preencher o campo
    pyautogui.write(str(nome))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo Email
    pyautogui.write(str(tabela.loc[linha, "Email"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "Endereco"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "Telefone"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim
    