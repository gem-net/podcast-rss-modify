import requests

from bs4 import BeautifulSoup

feed_url = 'http://feeds.soundcloud.com/playlists/soundcloud:playlists:543996543/sounds.rss'
feed = requests.get(feed_url).content

soup = BeautifulSoup(feed, features="lxml-xml", from_encoding='utf8')

out_path = 'podcast2.rss'

avatar_url = 'http://i1.sndcdn.com/artworks-000362660322-opta98-original.jpg'

changes = [
    ('itunes:email', 'info@gem-net.net'),
    ('itunes:author', 'C-GEM'),
    ('webMaster', 'Stephen Gaffney'),
    ('description', 'Your audio guide to the world of chemical polymers, brought to you by C-GEM.')
    ]

link_replace = dict([
    ('https://soundcloud.com/yaleuniversity/sets/center-for-genetically-encoded', 'http://gem-net.net/podcast'),
    ('http://www.yale.edu', 'http://gem-net.net/podcast'),
    ])

changed = []
for field_name, new_val in changes:
    field = soup.find(field_name)
    orig = field.string
    if orig != new_val:
        field.string = new_val
        print('Changed {} from {} to {}.'.format(field_name, orig, new_val))

links = soup.find_all('link')
n_links_modified = 0
for link in links:
    if link.string in link_replace:
        link.string = link_replace[link.string]
        n_links_modified += 1
print('Modified {} links.'.format(n_links_modified))    

main_im = soup.find('itunes:image')
main_im['href'] = avatar_url

with open(out_path, 'wb') as out:
    encoded = soup.encode(encoding='utf-8', formatter="minimal")
    encoded = encoded.replace(b'\n\n \n\n', b'\n\n')
    out.write(encoded)
print('RSS written to {}'.format(out_path))