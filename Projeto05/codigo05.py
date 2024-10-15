import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 2

# ESTEJA COM O NOTEBOOK À ESQUERDA DO MONITOR PRINCIPAL, ABERTO NA PAGINA DO CIC

pyautogui.click(x=-1762, y=143)
time.sleep(2)
pyautogui.click(x=-1623, y=284)
time.sleep(2)
pyautogui.click(x=-1190, y=558) # inicia a inscrição
time.sleep(2)
pyautogui.click(x=-1453, y=307) # titulo
pyautogui.write("VISIONTECH")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.write("e")
time.sleep(1) # engenharias
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.write("m")
time.sleep(1) # manhã
pyautogui.press("enter")
pyautogui.press("tab")

time.sleep(15) # COLAR AQUI TITULO e RESUMO

pyautogui.click(x=-1166, y=631) # CONFIRMANDO...
time.sleep(3)
pyautogui.click(x=-1544, y=348) # Incluir participante
time.sleep(3)

# importando a bd
tabela = pd.read_csv("dadospime.csv", delimiter=';')
print(tabela)

linha = 0
for linha in tabela.index:
 # CADASTRO
    pyautogui.click(x=-1388, y=265)
    time.sleep(3)
    # codigo
    cpf = tabela.loc[linha, "cpf"]
    pyautogui.write(str(cpf))
    pyautogui.press("tab")

    nome = tabela.loc[linha, "nome"]
    pyautogui.write(str(nome))
    pyautogui.press("tab")

    sobrenome = tabela.loc[linha, "sobrenome"]
    pyautogui.write(str(sobrenome))
    pyautogui.press("tab")

    citacao_bibliografica = tabela.loc[linha, "citacao_bibliografica"]
    pyautogui.write(str(citacao_bibliografica))
    pyautogui.press("tab")

    email = tabela.loc[linha, "email"]
    pyautogui.write(str(email))
    pyautogui.press("tab")

    confirmar_email = tabela.loc[linha, "confirmar_email"]
    pyautogui.write(str(confirmar_email))
    pyautogui.press("tab")

    telefone = tabela.loc[linha, "telefone"]
    pyautogui.write(str(telefone))
    pyautogui.press("tab")
 
    time.sleep(2)
    
    pyautogui.press("enter")
    pyautogui.click(x=-959, y=538)  #coautor
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("s", presses=3, _pause=True) # seleciona sp
    time.sleep(3)
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.press("enter") # escolha a cidade
    pyautogui.press("s", presses=47, _pause=True) # seleciona são carlos
    time.sleep(3)
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.click(x=-1347, y=392)

    time.sleep(20) # Confira os dados...

    pyautogui.click(x=-1231, y=641) # incluindo os dados
    time.sleep(3)
    pyautogui.press("tab", presses=7)
    pyautogui.press("enter") # iniciando a proxima inscrição
    time.sleep(5)
    
    # FINALIZAR INSCRIÇÃO MANUALMENTE
