import base64
import re

def parse_player(html):
    atob_start = html.find('window.atob')
    base64_start = atob_start + len('window.atob(\'')
    base64_end = html.find('\'', base64_start)
    base64_string = html[base64_start : base64_end]
    content = base64.b64decode(base64_string)
    return _extract_source_tags(content)

def _extract_source_tags(html):
    source_tags = re.findall(r'(<source.*?\/>)', html)
    if source_tags:
        streams = []
        for source_tag in source_tags:
            match = re.search(r'src=\'(.*?)\'.*?data-res="(.*?)"', source_tag)
            if match:
                streams.append((match.group(2), match.group(1)))

        return streams
