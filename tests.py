import parsers


def test_player_parsing():
    with open('fixtures/player.html') as f:
        streams = parsers.parse_player(f.read())
        assert len(streams) > 1

def test_player_parsing_with_subs():
    with open('fixtures/player_with_subs.html') as f:
        streams, subs = parsers.parse_player(f.read())
        assert len(subs) == 1



def test_movie_page_parsing():
    with open('fixtures/movies_page.html') as f:
        items = parsers.parse_movie_page(f.read())
        assert len(items) == 25


def test_movie_details_parsing():
    with open('fixtures/movie_detail.html') as f:
        item = parsers.extract_movie_item(f.read())
        assert item.title == 'Mean Machine (2001)'
        assert item.player_url == 'http://swefilm.tv/film/mean-machine_if0ey/'
        assert item.year == '2001'
        assert item.length == '99 min'
        assert item.resolution == '1080P'


def test_find_player_link_from_movie_page():
    with open('fixtures/movie_page.html') as f:
        player_link = parsers.get_player_link(f.read())
        assert player_link.startswith('http://swefilm.tv/watch/')

def test_find_iframe_src_from_player():
    with open('fixtures/player_page.html') as f:
        player_source = parsers.get_player_iframe_src(f.read())
        assert player_source.startswith('http://player.swefilm.tv/player')

def test_parse_search_results():
    with open('fixtures/search.html') as f:
        result = parsers.parse_search(f.read())
        assert len(result) == 8


def test_parse_episodes():
    with open('fixtures/series_page.html') as f:
        result = parsers.parse_episodes(f.read())
        assert len(result) == 3
