# Importação das bibliotecas necessárias
from telethon import TelegramClient, events
from PIL import Image
import google.generativeai as genai

# Configuração da API do Google
GOOGLE_API_KEY = ""  # Substitua pela sua chave de API do Google
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro-vision')

# Configuração do telethon
api_id = ""  # Substitua pelo seu ID de API do Telegram
api_hash = ""  # Substitua pelo seu hash de API do Telegram
bot_token = ""  # Substitua pelo token do seu bot Telegram
sessao = 'Bot'

def main():
    print('Monitoramento iniciado ...')
    client = TelegramClient(sessao, api_id, api_hash)
    
    # Definição de um manipulador de eventos para mensagens privadas
    @client.on(events.NewMessage(func=lambda e: e.is_private))
    async def enviar_mensagem(event):
        if event.media:
            # Baixa a mídia (imagem) da mensagem
            await client.download_media(event.message, file="midia.jpg")
            
            # Abre a imagem com a biblioteca Pillow
            img = Image.open("midia.jpg")

            # Envia uma mensagem indicando o processamento da imagem
            await event.reply('Processando imagem, aguarde um momento...')
            
            # Processa a imagem com o modelo de IA do Google
            response = model.generate_content(["Transcreva a imagem para texto e mantenha a formatação.", img])

            # Envia a resposta de texto extraída da imagem
            await event.reply(response.text)

        else:
            # Envia uma mensagem de erro caso a mensagem não seja uma imagem
            await event.reply("Por favor, envie apenas imagens para que possa transcrever o texto.")

    # Inicia o cliente Telegram com o token do bot
    client.start(bot_token=bot_token)
    client.run_until_disconnected()

if __name__ == "__main__":
    main()
