# Tela incial 
    # titulo: Moraozap
    # botão: iniciar chat
        # quando clicar no botão, 
        # ele vai abrir um popup/modal/alerta
            # bem vindo ao moraozap
            # caixa der texto: escreva seu nome no chat
            # botão: entrar no chat
                # quando clicar no botão
                # fechar o popup
                # sumir com o titulo
                # sumir com o botão inciar chat
                    # carregar o chat
                    # carregar o campo de enviar mensagem: "Digite sua mensagem"
                    # botão enviar
                        # envia a mensagem
                        # limpa a caixa de mensagem

import flet as ft

# criar uma função principal para rodar o seu aplicativo

def main(pagina):
    # titulo
    titulo = ft.Text("Morãozap")

    # websocket - tunel de comunicação entre 2 usuários

    def enviar_mensagem_tunel(mensagem):
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)


    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        mensagem = f"{nome_usuario}: {texto_campo_mensagem}"
        pagina.pubsub.send_all(mensagem)
        campo_enviar_mensagem = "" # limpa a caixa 
        chat.controls.append(texto)
        pagina.update()

    campo_enviar_mensagem = ft.TextField(label="Digite aqui sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])
    
    chat =  ft.Column()

    def entrar_chat(evento):
        # fechar o popup
        popup.open = False
        # sumir com o titulo
        pagina.remove(titulo)
        # sumir com o botão inciar chat
        pagina.remove(botao)
        # carregar o chat
        pagina.add(chat)
        # # carregar o botao enviar
        pagina.add(linha_enviar)
        # # adiciona a mensagem de entrou no chat
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou no chat"
        pagina.pubsub.send_all()
        chat.controls.append()

        pagina.update()

    # criar popup
    titulo_popup = ft.Text("Bem vindao ao Morãozap")
    caixa_nome = ft.TextField(label="Digite o seu nome")
    botao_popup = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)

    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_popup])

    #botao inicial
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.uptade()

    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    # coloca os elementos na pagina
    pagina.add(titulo)
    pagina.add(botao)

# executar essa função com o flet
ft.app(main, view=ft.WebView) # control c no terminal para interromper a execução