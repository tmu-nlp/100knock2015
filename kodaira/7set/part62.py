#!usr/bin/python

import plyvel

def count_artist_area(artist_area):
    artist_db = plyvel.DB('./level_db/', create_if_missing = False)
    count = 0
    for name, area in artist_db:
        if area == artist_area:
            print area
            count += 1

    artist_db.close()
    return count 


if __name__ == "__main__":
    area = "Japan"
    count = count_artist_area(area) 
    print count
