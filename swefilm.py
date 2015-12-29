import utils
import parsers

BASE_URL = 'http://swefilm.tv'
MOVIES_URL = 'http://swefilm.tv/list/film/'

def list_movies():
    html = utils.fetch_html(MOVIES_URL)
    return parsers.parse_movie_page(html)

def get_movie_streams(movie_url):
    movie_html = utils.fetch_html(movie_url)
    player_link =  parsers.get_player_link(movie_html)
    player_frame = utils.fetch_html(player_link)
    player_frame_src = parsers.get_player_iframe_src(player_frame)
    player_html = utils.fetch_html(player_frame_src)
    print player_html
    print 'link: ', player_link
    return parsers.parse_player(player_html)


if __name__ == '__main__':
    print list_movies()
