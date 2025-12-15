import requests

# Recebe a URL longa do usuário
link_original = input("Cole aqui sua URL gigante: ")

# API do TinyURL para encurtar URLs
api = "http://tinyurl.com/api-create.php?url="

# Concatena a URL da API com a URL longa fornecida pelo usuário
url_final = f"{api}{link_original}"

print("Encurtando...")

# Faz a requisição para a API do TinyURL
response = requests.get(url_final)

# Obtém o link curto da resposta
link_curto = response.text

# Exibe o link curto para o usuário
print("Link curto:", link_curto)