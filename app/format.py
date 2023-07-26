import json

from content import getContent
from connection import updateValues

from datetime import datetime, timedelta


def main():   
    data = json.loads(getContent())
    data=data['messages']
    data=data[0]
    data=data['message']
    data=data['allAgents']
    print(len(data))
    print(datetime.now())
    

    values=[]
    for associado in data:
        nome_atendente = associado['user']['name']
        tempo_logado = datetime.now() - datetime.fromtimestamp(associado['loggedInTime']/ 1000)
        tempo_logado_segundos = int(tempo_logado.total_seconds())
        tempo_logado_formatado = str(timedelta(seconds=tempo_logado_segundos))

        tempo_aceite = datetime.now() - datetime.fromtimestamp(associado['lastWorkAcceptedTime']/ 1000)
        tempo_aceite_segundos = int(tempo_aceite.total_seconds())
        tempo_aceite_formatado = str(timedelta(seconds=tempo_aceite_segundos))
        tempo_alvo = timedelta(days=1, hours=15, minutes=50, seconds=7)
        tempo_aceite_formatado_segundos =tempo_aceite.total_seconds()
        if tempo_aceite > tempo_alvo:
            tempo_aceite_formatado='--'
            tempo_aceite_formatado_segundos=0

        tempo_status = datetime.now() - datetime.fromtimestamp(associado['lastStatusUpdatedTime']/ 1000)
        tempo_status_segundos = int(tempo_status.total_seconds())
        tempo_status_formatado = str(timedelta(seconds=tempo_status_segundos))
        try:
            fila = associado['queues'][0]['name']
        except:
            fila = None
        status = associado['status']['name']

        values.append([nome_atendente, tempo_logado_formatado, tempo_aceite_formatado, fila, status, tempo_status_formatado, tempo_logado.total_seconds(), tempo_aceite_formatado_segundos, tempo_status.total_seconds()])
    updateValues(linha=len(data)+1, values=values)
