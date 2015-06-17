#!usr/bin/python

import plyvel

def print_artist_area(artist_name):
    artist_db = plyvel.DB('./level_db/', create_if_missing = False)
    print artist_name, artist_db.get(artist_name.encode('utf-8') )
    artist_db.close()
    


if __name__ == "__main__":
    # "Kat DeLuna"
    print 'artist_name:',; artist_name = raw_input()
    print_artist_area(artist_name) 
