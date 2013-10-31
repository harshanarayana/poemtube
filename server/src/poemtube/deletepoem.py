
from poemtube.errors import InvalidRequest

def deletepoem( db, id ):
    if id not in db.poems:
        raise InvalidRequest(
            '"%s" is not the ID of an existing poem.' % id, 404 )

    del db.poems[id]

