class Film:

    def __init__(self, id: int, title: str):
        self._id = id
        self._title = title

    def setID(self, id: int):
        self._id = id

    def setTitle(self, title: str):
        self._title = title

    def getID(self):
        return self._id
    
    def getTitle(self):
        return self._title
    
    def isEqual(self, otherFilm):
        if self._id == otherFilm.getID():
            return True
