# Utilizar flet permite criar site ou app

# Titulo: Hashzap
#Botão de iniciar chat
    #clicou no botão aparece o pop-up/modal
        # Titulo: Bem vindo ao Hashzap
        # Campo: Escreva seu nome no chat
        #botão: Entrar no chat

#chat
    #embaixo do chat
        #campo de digite sua mensagem
        #botão enviar


#flet = framework do python, a estrutura do site será baseada nesse framework, cada um tem suas caracteristicas como django ou flask
# precisa instalar a biblioteca com pip install flet

import flet as ft # Costumam dar um apelido para o flet com o ft

#criar uma função

def main(pagina): #função principal do site e onde a execução do codigo começa, passa o argumento de pagina que vai rodar e a primeira que será aberta
    texto = ft.Text("Hashzap")


    titulo_popup = ft.Text("Bem vindo ao Hashzap")
    nome_usuario = ft.TextField(label="Escreva seu nome") # criação do campo para digitar o nome / label é utilizado para mostrar o nome do que ficará ao lado do campo
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat) # aqui faz a criação do botão para iniciar o chat, dentro do botão vai chamar a função entrar_chat

    popup = ft.AlertDialog()(# criação do pop-up
        open = False,
        modal = True, # o modal faz com que abra o pop-up como uma janela e não no canto da tela
    )



    def abrir_popup(evento): # função para abrir o que é chamada abaixo, para todos os botãos deve ser passado como parametro o evento e as outras funções do que deve ter em questão de layout ou informação como pagina
        pagina.dialog = popup # vai executar o pop-up que foi atribuido logo acima
        popup.open = True # Para que o pop-up possa ser aberro
        #sempre que editar a pagina depois que a pagina tiver carregada, tem que:
        pagina.update()#atualizar a pagina sem precisar que o usuário precise apertar o F5

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click= abrir_popup) # o que está no botão vai aparecer Iniciar Chat, entendo que com um click vai chamar a função abrir_popup, ela não está sendo chamada com (), porque cria uma função anônima que recebe um argumento (que o PySimpleGUI passará automaticamente quando o botão for clicado, a função anonima nesse caso
    pagina.add(texto) # vai adicionar o texto acima na pagina
    pagina.add(botao_iniciar)
    


# dentro da função vai colocando as 
ft.app(target=main) # O app tem que executar a função main para criação do app
#ft.app(target=main, view=ft.WEB_BROWSER) pode passar o formato de site

# Dividido em três planos: entre importação de biblioteca, função e a execução da função

# O fluxo dos códigos (programação) acontece de baixo para cima