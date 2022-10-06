try:
    from pytube import YouTube
except ImportError:
    from pip._internal import main as pip
    pip(['install', '--user', 'pytube'])
    from pytube import YouTube

from sys import argv

link = argv[1]
output = argv[2]
yt = YouTube(link)

print("Title:", yt.title)
print("Views:", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download(output)
