import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 1

# ESTEJA COM O NOTEBOOK ABERTO COM A PAGINA DO CIC

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
pyautogui.write("n")
time.sleep(1) # noite
pyautogui.press("enter")
pyautogui.press("tab")

time.sleep(60) # COLAR AQUI TITULO e RESUMO

pyautogui.click(x=-1166, y=631) # CONFIRMANDO...
time.sleep(3)
pyautogui.click(x=-1544, y=348) # Incluir participante
time.sleep(3)

# importando a bd
tabela = pd.read_csv("dados_pime.csv")
print(tabela)

linha = 0
for linha in tabela.index:
    pyautogui.click(x=-1388, y=265) # CADASTRO
    time.sleep(3)
    # codigo
    cpf = tabela.loc[linha, "cpf"]
    pyautogui.write(str(cpf))
    pyautogui.press("tab")

    nome = tabela.loc[linha, "nome"]
    pyautogui.write(str(nome))
    pyautogui.press("tab")

    sobrenome = tabela.loc[linha, "sobrenome"]
    pyautogui.write(str(cpf))
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
    time.sleep(60) # SELECIONE E INCLUA MANUALMENTE SÃO CARLOS


 # FINALIZAR INSCRIÇÃO MANUALMENTE


#cpf,nome,sobrenome,citacao_bibliografica,email,confirmar_email,telefone