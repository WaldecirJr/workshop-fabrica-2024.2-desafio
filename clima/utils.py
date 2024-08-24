import requests
from .models import Clima, Viagem

def buscar_clima(viagem_id):
    API_KEY = '4a8f30028068e14cb1f644e456b291b4'
    
    try:
        viagem = Viagem.objects.get(id=viagem_id)
        destino = viagem.destinos.first()
        if not destino:
            print(f"Nenhum destino encontrado para a viagem com id {viagem_id}.")
            return None
        cidade = destino.nome_destino
    except Viagem.DoesNotExist:
        print(f"Viagem com id {viagem_id} não encontrada.")
        return None
    
    try:
        response = requests.get('https://api.openweathermap.org/data/2.5/weather', params={
            'q': cidade,
            'appid': API_KEY,
            'units': 'metric',
            'lang': 'pt'
        })
        
        if response.status_code == 200:
            data = response.json()
            clima, created = Clima.objects.update_or_create(
                viagem=viagem,
                defaults={
                    'temperatura': data['main']['temp'],
                    'condicoes_climaticas': data['weather'][0]['description']
                }
            )
            return clima
        else:
            print(f"Erro ao buscar os dados da API: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Erro na requisição para a API: {e}")
        return None