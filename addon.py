from xbmcswift2 import Plugin, xbmc
import swefilm
import utils

plugin = Plugin()
        
@plugin.route('/')
def index():
    return [
        {
            'label': 'Search',
            'path': plugin.url_for('search')
        },
        {
            'label': 'List movies',
            'path': plugin.url_for('movies')
        }
    ]

@plugin.route('/movies')
def movies():
    movies = swefilm.list_movies()
    return map(to_kodi_item, movies)

@plugin.route('/play_movie/<url>/')
def play_movie(url):
    streams = swefilm.get_movie_streams(url)
    stream = streams[0][1]
    plugin.set_resolved_url(stream)

@plugin.route('/search/')
def search():
    kb = xbmc.Keyboard('', 'Search', False)
    kb.doModal()
    if kb.isConfirmed():
        text = kb.getText()
    else:
        return
    items = swefilm.search(text)
    return map(to_kodi_item, items)


def to_kodi_item(item):
    return {
        'label': utils.safe_decode(item.title),
        'path': plugin.url_for('play_movie', url=item.player_url),
        'thumbnail': swefilm.BASE_URL + item.poster,
        'is_playable': True
    }

if __name__ == '__main__':
    plugin.run()
