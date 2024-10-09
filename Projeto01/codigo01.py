# Passo 1: entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pip install pyautogui
import pyautogui
import time
import pandas

# pyautogui.write - escreve um texto
# pyautogui.click - clicar com o mouse
# pyautogui.press - apertar uma tecla
# pyautogui.hotkey - apertar um atalho de teclado (ctrl, C)
pyautogui.PAUSE = 0.5

# abrir o navegador
# apertar a tecla win

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Passo 2: fazer login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3) # quero dar uma pausa de 3 segundos
pyautogui.click(x=684, y=407) # RPA = robotin programing automation
pyautogui.write("daniellymoro12@gmail.com")
pyautogui.press("tab")
pyautogui.write("minhasenha")
pyautogui.click(x=837, y=568)
time.sleep(3)

# Passo 3: importar a base de dados
# pip install pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4: cadastrar 1 produto


linha = 0
for linha in tabela.index:
    pyautogui.click(x=814, y=290)
    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str("obs"))
    pyautogui.press("tab")
 
    pyautogui.press("enter")
    pyautogui.scroll(100000)

# Passo 5: repetir o processo de cadastro até acabar os produtos

