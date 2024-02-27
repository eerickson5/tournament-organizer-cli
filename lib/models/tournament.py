from models.__init__ import CURSOR, CONN

class Tournament:

    all = []

    def __init__(self, name):
        self.name = name
        self.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) == str and len(name) > 0:
            self._name = name
        else:
            raise TypeError("Tournament name must be a nonempty string.")
        
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Tournament instances """
        sql = """
            CREATE TABLE IF NOT EXISTS tournaments (
            id INTEGER PRIMARY KEY,
            name STRING
            )
        """
        CURSOR.execute(sql)
        CONN.commit()