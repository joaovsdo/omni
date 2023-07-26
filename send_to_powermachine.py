import paramiko

def enviar_arquivo_para_maquina_remota(caminho_arquivo_local, usuario_remoto, endereco_remoto, caminho_destino):
    try:
        # Cria uma instância do cliente SSH
        ssh_client = paramiko.SSHClient()

        # Define a política padrão para adicionar chaves SSH desconhecidas automaticamente
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Conecta-se à máquina remota
        ssh_client.connect(hostname=endereco_remoto, username=usuario_remoto, password='@power#123@2023')

        # Abre uma conexão SFTP para transferência de arquivo
        sftp = ssh_client.open_sftp()

        # Envia o arquivo para a máquina remota
        sftp.put(caminho_arquivo_local, caminho_destino)

        # Fecha a conexão SFTP
        sftp.close()

        # Fecha a conexão SSH
        ssh_client.close()

        print("Arquivo enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar o arquivo: {e}")

# Caminho local do arquivo token.json credentials.json
token = "/home/joaovsdo/Projects/scraper/geraToken/token.json"
credentials = "/home/joaovsdo/Projects/scraper/geraToken/credentials.json" 
# Informações da máquina remota
usuario_remoto = "Powermachine"
endereco_remoto = "172.171.241.111"
token_destino = "/home/Powermachine/Documents/scraper/salesforce/token.json"
credentials_destino= "/home/Powermachine/Documents/scraper/credentials.json"

enviar_arquivo_para_maquina_remota(token, usuario_remoto, endereco_remoto, token_destino)
enviar_arquivo_para_maquina_remota(credentials, usuario_remoto, endereco_remoto, credentials_destino)

