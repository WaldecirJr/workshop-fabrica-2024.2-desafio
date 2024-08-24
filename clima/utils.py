import requests
from .models import Clima, Viagem

def buscar_clima(viagem_id):
    API_KEY = '4a8f30028068e14cb1f644e456b291b4'
    viagem = Viagem.objects.get(id=viagem_id)
    response = requests.get('https://api.openweathermap.org/data/2.5/weather', params={
        'q': viagem.nome_destino,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'pt'
    })
    data = response.json()
    
    clima, criated = Clima.objects.update_or_create(
        viagem=viagem,
        defaults={
            'temperatura': data['main']['temp'],
            'condicoes': data['weather'][0]['description']  # Corrigido para 'weather'
        }
    )
    return clima