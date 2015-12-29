import urllib2

def fetch_html(url):
    request = urllib2.Request(url, headers={
        'Accept' : '*/*',
        'Accept-Encoding': '*',
        'User-Agent': 'curl/7.43.0'
    })
    contents = urllib2.urlopen(request).read()
    return contents

if __name__ == '__main__':
    print fetch_html('http://swefilm.tv/film/four-rooms_if0ec/')
