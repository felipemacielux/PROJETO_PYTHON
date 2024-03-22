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

import flet as ft # Costumam dar um apelido para o flet com o ft e importando a biblioteca

#criar uma função

def main(pagina): #função principal do site e onde a execução do codigo começa, passa o argumento de pagina que vai rodar e a primeira que será aberta
    texto = ft.Text("Hashzap")

    chat = ft.Column()# chat funciona como uma coluna em que vai sendo armazenado as mensagens

    #Essa função é responsável por adicionar a mensagem recebida no chat.
    def enviar_mensagem_tunel(mensagem): 
        print(mensagem)
          #adiciona a mensagem no chat
        texto_mensagem = ft.Text(mensagem) #ft.Text provavelmente é usada para criar um elemento de texto que será exibido no chat, assim será adicionado na interface do chat
        chat.controls.append(texto_mensagem) # utilizado para adicionar a mensagem na coluna do chat
# fazendo o que está abaixo vai rodar para todos os usuários ao mesmo tempo
        pagina.update()
    pagina.pubsub.subscribe(enviar_mensagem_tunel)  # é o tunel de comunicação, precisa dizer qual é a função que deverá ser rodada/ faz a inscrição da função enviar_mensagem_tunel para receber mensagens

    def enviar_mensagem(evento):
        print("Enviar mensagem") 
        pagina.pubsub.send_all(f"{nome_usuario.value}: {mensagem.value}") #pubsub se resume ao sistema de publicação e o send all vai enviar para todos conectados a pagina. Quando rodar a função send all vai chamar a função enviar_mensagem_tunel / fazendo o processo de colocar o nome do usuário e a mensagem vai fazer com que apareça ambas as informações quando o user mandar mensagem
        # limpe o campo mensagem
        mensagem.value = "" # O "" serve para atribuir uma string vazia para o campo, ou seja, limpar o campo
        pagina.update() # assim nesse caso sempre que uma mensagem for enviada a pagina vai ser atualizada
    
    mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)# criação do campo para digitar a mensagem/ o on_submit função que roda quando usuário clica enter para envio
    botao_enviar = ft.ElevatedButton("Enviar" , on_click=enviar_mensagem)# criação do botão para enviar a mensagem
#Para fazer com que tanto mensagem quanto o botão estejam na mesma linha um ao lado do outro
    linha_enviar = ft.Row([mensagem, botao_enviar]) # criação da linha para o botão e a mensagem
    def entrar_chat(evento): #função para entrar no chat
        print("Entrar no chat")
    # fechar pop-up
        popup.open = False # vai fechar o pop-up, diferente do que esta na linha 53 que está true
    # Tirar o botão iniciar chat
        pagina.remove(botao_iniciar) # Faz com que o botão seja removido da tela / o remove tira os elementos da tela(interface)
    # Tirar titulo do pop-up
        pagina.remove(texto)
    # criar o chat / feito de forma parecida quando foi criado o pop-up, usando as mesma estrutura
        pagina.add(chat)
        pagina.pubsub.send_all(f"{nome_usuario.value} entrou no chat")
    # precisa ser adicionado o nome do usuário na página assim que o usuário colocar o nome dele
        chat.controls.append(ft.Text(f"{nome_usuario.value} entrou no chat")) # um valor dinamico é o nome_usuario.value
        
    # colocar o botão enviar junto com a mensagem
        pagina.add(linha_enviar)
        pagina.update()#Sempre colocar assim que for feita uma edição visual na tela

    titulo_popup = ft.Text("Bem vindo ao Hashzap")
    nome_usuario = ft.TextField(label="Escreva seu nome") # criação do campo para o usuário vai preencher / label é utilizado para mostrar o nome do que ficará ao lado do campo
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat) # aqui faz a criação do botão para iniciar o chat, dentro do botão vai chamar a função entrar_chat

    popup = ft.AlertDialog(# criação do pop-up com alert.dialog
        open = False, # para que o pop-up possa ser aberto e não comece com ele aberto (true)
        modal = True, # o modal faz com que abra o pop-up como uma janela e não no canto da tela
        # Precisa ser fornecido os dados acima, como o titulo, nome do usuário e botão para que apareça dentro do pop-up
        title = titulo_popup,
        content=nome_usuario, #conteudo do pop-up
        actions = [botao_entrar] # tem que ser passado dentro de uma lista, quando tem botão
    )

    def abrir_popup(evento): # função para abrir o que é chamada abaixo, para todos os botãos deve ser passado como parametro o evento e as outras funções do que deve ter em questão de layout ou informação como pagina
        pagina.dialog = popup # vai executar o pop-up que foi atribuido logo acima
        popup.open = True # Para que o pop-up possa ser aberto
        #sempre que editar a pagina depois que a pagina tiver carregada, tem que:
        pagina.update()#atualizar a pagina sem precisar que o usuário precise apertar o F5

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click= abrir_popup) # o que está no botão vai aparecer Iniciar Chat, entendo que com um click vai chamar a função abrir_popup, ela não está sendo chamada com (), porque cria uma função anônima que recebe um argumento (que o PySimpleGUI passará automaticamente quando o botão for clicado, a função anonima nesse caso
    pagina.add(texto) # vai adicionar o texto acima na pagina
    pagina.add(botao_iniciar)
    


# dentro da função vai colocando as 
ft.app(target=main, view = ft.WEB_BROWSER) # O app tem que executar a função main para criação do app
#ft.app(target=main, view=ft.WEB_BROWSER) pode passar o formato de site
# Aqui nesse caso foi alterado para que possamos fazer com o que o código rode simultaneamente com o outro

# Dividido em três planos: entre importação de biblioteca, função e a execução da função

# O fluxo dos códigos (programação) acontece de baixo para cima