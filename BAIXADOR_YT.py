# Neste projeto vamos baixar vídeos do Youtube em alta qualidade a partir do link.

# Importe a biblioteca
from pytube import YouTube

# Colete o link do vídeo.
URL = input('INSIRA O LINK DO VÍDEO: ')
VIDEO_URL = URL
print('Baixando vídeo...')

#Baixando o vídeo
YouTube(VIDEO_URL).streams.get_highest_resolution().download()
print('Video baixado com sucesso.')
