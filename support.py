from pytube import YouTube, Search, Playlist
from io import BytesIO

def urlID_to_Buffer(id):
    url = "https://www.youtube.com/watch?v="+id
    music = BytesIO()
    stream = YouTube(url).fmt_streams[-1]
    stream.stream_to_buffer(music)
    music.seek(0)
    return {
        'music' : music,
        'mime' : stream.mime_type
    }



def searchYotube(q):
    res = []
    for search in Search(q).results:
        res.append({
            'title' : search.title,
            'image' : search.thumbnail_url,
            'id' : search.video_id
        })
    return res

def playlistFetch(url):
    playlist_ = Playlist(url)
    res = []
    for video in playlist_:
        videoOBJ = YouTube(video)
        res.append({
            'title': videoOBJ.title,
            'image': videoOBJ.thumbnail_url,
            'id': videoOBJ.video_id
        })
    return res
