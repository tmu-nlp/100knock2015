#!usr/bin/python
# reference: http://blog.liris.org/2010/10/python3mongodb.html
# http://qiita.com/tomotaka_ito/items/60c65dd5261fdfc6e71a

import json
import plyvel

def make_artist_db(file_name):
    # create_if_missing: if db-file not exist, create it
    artist_db = plyvel.DB('./level_db/', create_if_missing = True)
    for line in open(file_name):
        artist_dict = json.loads(line)
        artist_db.put(artist_dict['name'].encode('utf-8'), \
            artist_dict.get('area', 'None').encode('utf-8' ) )
    artist_db.close()
    


if __name__ == "__main__":
    file_name = "artist.json"
    make_artist_db(file_name) 
