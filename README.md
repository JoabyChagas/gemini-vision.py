Transcrição de Imagem com Google Gemini Pro Vision

Este é um script Python que atua como um bot Telegram para transcrever texto de imagens e manter a formatação original. Ele utiliza a biblioteca telethon para interagir com o Telegram, a biblioteca Pillow para manipulação de imagens e uma biblioteca de inteligência artificial da Google, Gemini Pro Vision para reconhecimento e transcrição de texto em imagens.

Este código simplifica a extração de informações de texto de imagens, tornando-a mais eficiente e economizando tempo e esforço. É especialmente útil em diversas situações, tais como:

Extrair legendas de memes.
Transcrever texto de documentos ou imagens com formatação especial.
Converter texto presente em imagens em um formato de texto legível.

Configuração das Dependências:

Certifique-se de ter todas as bibliotecas necessárias instaladas antes de executar o código. Use os seguintes comandos para instalar as dependências:

pip install telethon
pip install pillow
pip install -q -U google-generativeai

Configuração da Chave de API do Google:

Você precisará de uma chave de API do Google para autenticar o acesso aos serviços de IA do Google, que são usados para transcrever o texto da imagem. Substitua GOOGLE_API_KEY com sua chave de API no código.
Acesso a GOOGLE_API_KEY: https://makersuite.google.com/app/apikey

Configuração do Bot Telegram:

Antes de executar o código, configure seu bot Telegram. Você precisará do api_id, api_hash e do bot_token. Certifique-se de seguir as instruções do Telegram para obter essas credenciais.
Acesse a documentação para mais detalhes: https://docs.telethon.dev/en/stable/basic/signing-in.html

Execução do Bot

Após configurar as dependências e as credenciais do Telegram e do Google, execute o bot. O bot ficará online e aguardará mensagens de usuários.

Envie uma imagem contendo o texto que você deseja transcrever para o bot Telegram. O bot irá processar a imagem e retornar a transcrição mantendo a formatação original da imagem.

O bot enviará a transcrição da imagem como uma mensagem de resposta.