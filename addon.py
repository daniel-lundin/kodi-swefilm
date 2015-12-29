from xbmcswift2 import Plugin
import swefilm
import HTMLParser

plugin = Plugin()

def safe_decode(word):
    h = HTMLParser.HTMLParser()
    word = h.unescape(word)
    s = ''
    for letter in word:
        if ord(letter) > 127:
            s += '_'
        else:
            s += letter
    return s
        
@plugin.route('/')
def index():
    item = {
        'label': 'List movies',
        'path': plugin.url_for('movies')
    }
    return [item]

@plugin.route('/movies')
def movies():
    movies = swefilm.list_movies()

    def to_kodi_item(item):
        url, label, poster = item
        return {
            'label': safe_decode(label),
            'path': plugin.url_for('play_movie', url=url),
            'is_playable': True
        }
    return map(to_kodi_item, movies)

@plugin.route('/play_movie/<url>/')
def play_movie(url):
    print 'playing, ', url
    streams = swefilm.get_movie_streams(url)
    print 'streams', streams
    stream = streams[0][1]
    print 'stream', stream
    plugin.set_resolved_url(stream)

if __name__ == '__main__':
    plugin.run()
