# Neste projeto vamos baixar vídeos do Youtube a partir do link.

# Importe a biblioteca
from pytube import YouTube
YouTube('coloque a URL do vídeo aqui').streams.get_highest_resolution().download()

'''
PARA BAIXAR UMA PLAYLIST USE O COD:

from pytube import YouTube, Playlist

PLAYLIST_URL = 'colo que a URL da playlist aqui'
playlist = Playlist(PLAYLIST_URL)

for url in playlist:
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()
    stream.download(output_path='playlist')
'''

'''
PARA BAIXAR SOMENTE O AUDIO USE ESTE COD:
audio = yt.streams.filter(only_audio=True)[0]
audio.download()
'''

'''
yt = YouTube(VIDEO_URL)
for stream in yt.streams:
    print(stream)
'''
'''
PARA LER A STREAM DO VIDEO
yt = YouTube('https://www.youtube.com/watch?v=-KxiYQasSaQ&ab_channel=ManualdoMundo')
print(yt.streams)
'''

#DOCUMENTAÇÃO DO PYTUBE3 https://pypi.org/project/pytube3/