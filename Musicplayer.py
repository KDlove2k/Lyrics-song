import lyricsgenius

# Thay thế 'your_access_token' bằng API Key của bạn
genius = lyricsgenius.Genius("GC6M41Djyz1eATtk5kU5yd8BaCs0_xZCmdGfrpsHpkszoUO64qMhiC7HG847HLqv")

def get_lyrics(artist, title):
    song = genius.search_song(title, artist)
    if song:
        return song.lyrics
    else:
        return "Không tìm thấy bài hát nào"

# Thay thế artist và title bằng tên nghệ sĩ và tiêu đề bài hát bạn muốn
artist_name = input("Nhập tên ca sĩ: ")
song_title = input("Nhập tên bài hát: ")

lyrics = get_lyrics(artist_name, song_title)
print(lyrics)
