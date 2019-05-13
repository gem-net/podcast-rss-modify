# SoundCloud RSS Modification

This simple Python script lets you customize the metadata of a 
SoundCloud RSS feed in order to work with Google Play Podcasts and 
many other RSS aggregators.


### Customizing your feed

The script is set up to overwrite the following metadata:
- primary podcast image (`avatar_url`)
- email address (`itunes:email`)
- web master name (`webMaster`)
- podcast description (`description`)

It can also replace links, specified as 'before' and 'after' pairs (`link_replace`).

You can specify these values directly at the start of the script:

```python
# --------- CUSTOMIZATION VARIABLES ---------
feed_url = 'http://feeds.soundcloud.com/playlists/soundcloud:playlists:543996543/sounds.rss'
out_path = 'podcast2.rss'  # New RSS feed will be exported here
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

# --------- END OF CUSTOMIZATION VARIABLES ---------
```

### Python package dependencies

This python script assumes a Python 3 environment, and has only two 
dependencies: `requests` (for downloading the text content of your RSS feed), 
and `BeautifulSoup4` (for XML parsing and modification). These dependencies
are listed in the `requirements.txt` file. Install with `pip` using:

```bash
pip install -r requirements.txt
```

### Run the script

Run the script in bash with the following command, 
updating the path as appropriate.:

```bash
python /path/to/podcast_rss_modify.py
```

This will download the RSS feed into memory, overwrite variables based on your
customization, and create a new file that you can host on your website.
