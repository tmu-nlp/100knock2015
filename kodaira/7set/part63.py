#!usr/bin/python

import json
import plyvel



def make_artist_db(file_name):
    # create_if_missing: if db-file not exist, create it
    artist_db = plyvel.DB('./level_db_63/', create_if_missing = False)
    name_list = list()
    '''
    for line in open(file_name):
        tag_list = list()
        artist_dict = json.loads(line)
        if 'tags' in artist_dict:
            tag_list.append(artist_dict['tags'][0].get('value', "None").encode('utf-8') )
            tag_list.append(str(artist_dict['tags'][0]['count']).encode('utf-8'))
            artist_db.put(artist_dict['name'].encode('utf-8'), \
                json.dumps(tag_list) )    
    '''
    artists_info =  list(artist_db.iterator() )
    name = artists_info[9][0]
    area, num = json.loads(str(artist_db.get(artists_info[9][0])))
    print name, area, num
    artist_db.close()


if __name__ == "__main__":
    file_name = "artist.json"
    make_artist_db(file_name) 
