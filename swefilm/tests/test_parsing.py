from swefilm import parsers


def test_player_parsing():
    with open('swefilm/tests/fixtures/player.html') as f:
        streams = parsers.parse_player(f.read())
        assert len(streams) == 2

def test_movie_page_parsing():
    with open('swefilm/tests/fixtures/movie_page.html') as f:
        assert False
