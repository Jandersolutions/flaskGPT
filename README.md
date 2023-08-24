# flaskGPT

# Chatbot com Flask e OpenAI

Este é um projeto didático que demonstra como criar um frontend de chatbot utilizando o Flask, Bootstrap 5 e a API da OpenAI. O chatbot é capaz de responder às mensagens dos usuários usando o modelo de linguagem da OpenAI.

## Instalação

1. Certifique-se de ter o Python instalado (versão 3.6 ou superior).

2. Clone este repositório para o seu ambiente local:

   ```bash
   git clone https://github.com/seu-usuario/chatbot-flask-openai.git
   ```

3. Acesse o diretório do projeto:

   ```bash
   cd chatbot-flask-openai
   ```

4. Instale o flask usando o `pip`:

   ```bash
   pip install flask
   ```

## Uso

1.insira sua `'sua_chave_da_openai'` pela sua chave de API da OpenAI.

3. Execute o aplicativo Flask:

   ```bash
   python app.py
   ```

4. Abra o navegador e acesse `http://127.0.0.1:5000/` para interagir com o chatbot.

## Como Funciona

O aplicativo Flask serve como o servidor para o frontend do chatbot. A página HTML exibe uma interface onde os usuários podem digitar mensagens. Quando os usuários enviam uma mensagem, a aplicação faz uma chamada AJAX para o servidor Flask, que utiliza a API da OpenAI para obter uma resposta do chatbot. A resposta é então exibida na interface do usuário.

## Personalização

Este projeto é um ponto de partida simples e didático. Você pode personalizá-lo e expandi-lo de várias maneiras:

- Melhorar o design da interface usando mais recursos do Bootstrap.
- Adicionar lógica para lidar com diferentes cenários de conversação.
- Implementar autenticação e segurança para proteger a chave da API.
- Utilizar websockets para atualizar a conversa em tempo real.
- Melhorar o tratamento de erros e mensagens de feedback ao usuário.

## Notas

- Certifique-se de manter suas chaves de API em segurança e não as compartilhe publicamente.
- Este projeto é apenas para fins didáticos e pode não estar otimizado para uso em produção.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).


