from pytube import YouTube

link = input('Enter the link: ')
yt = YouTube(link)

print('Title: ',yt.title)
print('Number of views: ',yt.views)
ys = yt.streams.get_highest_resolution()
ys.download()