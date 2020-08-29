import youtube_dl
from os import system
while True:
    ah = input("Enter URL: ")
    lel=input('folder name: ')
    type=input('file type: ')
    playlist=input('playlist: ')
    if playlist=='true'or playlist=='yes':
        if type=='mp3'or type=='wav'or type=='ogg'or type=='flac':
            ydl_opts = {
                'ignoreerrors': True,
                'outtmpl': f'/{lel}/%(title)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': f'{type}',
                    'preferredquality': '192'
                    }],
                'prefer_ffmpeg': True,
            }
        if type=='mp4':
            ydl_opts={'ignoreerrors': True,'outtmpl':f'/{lel}/%(title)s.mp4','format':'mp4'}
    if playlist=='false'or playlist=='no':
        if type=='mp3'or type=='wav'or type=='ogg'or type=='flac':
            ydl_opts = {
                'ignoreerrors': True,
                'outtmpl': f'/{lel}/%(title)s',
                'noplaylist' : True,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': f'{type}',
                    'preferredquality': '192'
                    }],
                'prefer_ffmpeg': True,
            }
        if type=='mp4':
            ydl_opts={'ignoreerrors': True,'outtmpl':f'/{lel}/%(title)s.mp4','format':'mp4','noplaylist':True}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:  
        ydl.download([f'{ah}'])
