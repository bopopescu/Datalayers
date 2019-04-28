import datetime
from pony.orm import Database,Set
from pony.orm import select
import pony.orm as pny
from pony.orm import unicode


database = Database('mysql', host="localhost",user="root",password='',database="test")


########################################################################
class Artist(database.Entity):
    """
    Pony ORM model of the Artist table
    """
    name = pny.Required(unicode)
    albums = pny.Set("Album")


########################################################################
class Album(database.Entity):
    """
    Pony ORM model of album table
    """
    artist = pny.Required(Artist)
    title = pny.Required(unicode)
    release_date = pny.Required(datetime.date)
    publisher = pny.Required(unicode)
    media_type = pny.Required(unicode)



# turn on debug mode
#pny.sql_debug(True)

# map the models to the database
# and create the tables, if they don't exist
database.generate_mapping(create_tables=True)

@pny.db_session
def add_data():
    """"""

    new_artist = Artist(name=u"Newsboys")
    bands = [u"MXPX", u"Kutless", u"Thousand Foot Krutch"]
    for band in bands:
        artist = Artist(name=band)

    album = Album(artist=new_artist,
                  title=u"Read All About It",
                  release_date=datetime.date(1988, 12, 1),
                  publisher=u"Refuge",
                  media_type=u"CD")

    albums = [{"artist": new_artist,
               "title": "Hell is for Wimps",
               "release_date": datetime.date(1990, 7, 31),
               "publisher": "Sparrow",
               "media_type": "CD"
               },
              {"artist": new_artist,
               "title": "Love Liberty Disco",
               "release_date": datetime.date(1999, 11, 16),
               "publisher": "Sparrow",
               "media_type": "CD"
               },
              {"artist": new_artist,
               "title": "Thrive",
               "release_date": datetime.date(2002, 3, 26),
               "publisher": "Sparrow",
               "media_type": "CD"}
              ]

    for album in albums:
        a = Album(**album)


@pny.db_session
def query():
    x = 1
    print(database.select("select * from Artist where id = $x"))

if __name__ == "__main__":
    query()



    # use db_session as a context manager
    with pny.db_session:
        a = Artist(name="Skillet")