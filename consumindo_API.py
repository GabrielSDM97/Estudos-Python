import requests

# endpoint = Local na API onde a chamada será atendida.
def fetch_data(endpoint, filter = {}):
    # URL da API
    url = f"https://rickandmortyapi.com/api/{endpoint}"

    # Método GET para receber dados da API. Segundo parâmetro serve para filtrar um tipo de chave/valor do dicionário.
    response = requests.get(url, filter)

    ''' O método ".json" converte os dados recebidos da API em um dicionário Python, já que dados de arquivo
        JSON geralmente são valores pares (valor1:valor2) ou arrays. '''
    
    # Retorna os dados JSON convertidos se o status do código for 200 (concluído com sucesso)
    return response.json() if response.status_code == 200 else f"erro {response.status_code}"

data = fetch_data("character", {"name":"Rick"})

print(data)
