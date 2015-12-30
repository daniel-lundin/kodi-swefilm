import utils
import urllib
import parsers

BASE_URL = 'http://swefilm.tv'
MOVIES_URL = 'http://swefilm.tv/list/film/page-%s'
SEARCH_URL = 'http://swefilm.tv/search/%s'

def list_movies(page):
    html = utils.fetch_html(MOVIES_URL % page)
    return parsers.parse_movie_page(html)

def get_movie_streams(movie_url):
    movie_html = utils.fetch_html(movie_url)
    player_link =  parsers.get_player_link(movie_html)
    player_frame = utils.fetch_html(player_link)
    player_frame_src = parsers.get_player_iframe_src(player_frame)
    player_html = utils.fetch_html(player_frame_src)
    return parsers.parse_player(player_html)

def search(q):
    search_url = SEARCH_URL % urllib.quote_plus(q)
    html_result = utils.fetch_html(search_url)
    return parsers.parse_search(html_result)

if __name__ == '__main__':
    print list_movies()
