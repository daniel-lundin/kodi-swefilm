import base64
import re

def parse_player(html):
    atob_start = html.find('window.atob')
    base64_start = atob_start + len('window.atob(\'')
    base64_end = html.find('\'', base64_start)
    base64_string = html[base64_start : base64_end]
    content = base64.b64decode(base64_string)
    return extract_source_tags(content)


def parse_movie_page(html):
    movie_list = re.search(r'<div class="m_list(.*?)</ul>', html, re.DOTALL)
    if movie_list:
        return extract_movie_items(movie_list.group())
    return []

def get_player_link(html):
    movie_list = re.search(r'<div class="m_list(.*?)</ul>', html, re.DOTALL)
    player_link = re.search(r'<a class="icons btn_watch_detail".*?href="(.*?)"', html)
    if player_link:
        return player_link.group(1)
    return ''

def get_player_iframe_src(html):
    iframe_match = re.search(r'<iframe.*?src="(http://player.swefilm.tv.*?)"', html);
    if iframe_match:
        return iframe_match.group(1)

    return None

def parse_search(html):
    return parse_movie_page(html)

def extract_source_tags(html):
    source_tags = re.findall(r'(<source.*?\/>)', html)
    if source_tags:
        streams = []
        for source_tag in source_tags:
            match = re.search(r'src=\'(.*?)\'.*?data-res="(.*?)"', source_tag)
            if match:
                streams.append((match.group(2), match.group(1)))

        return streams

def extract_movie_item(html):
    match = re.search(r'<a.*?href="(.*?)".*?title="(.*?)".*?src="(.*?)".*?</a>', html)
    [url, title, cover] = match.groups()
    return [url, title, cover]

def extract_movie_items(html):
    items = re.findall(r'(<li>.*?</li>)', html, re.DOTALL)
    return map(extract_movie_item, items)

