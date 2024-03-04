from models.__init__ import CURSOR, CONN

class Tournament:

    all = {}

    def __init__(self, name):
        self.name = name

    #get rid of this
    def __repr__(self):
        return f"Tournament:(id={self.id}, name={self.name})"

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

    @classmethod
    def drop_table(cls):
        sql = """
        DROP TABLE IF EXISTS tournaments
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create_tournament(cls, name):
        tournament = cls(name)
        tournament.save()
        return tournament
    
    @classmethod
    def instance_from_row(cls, row):
        tournament = cls.all[row[0]]
        if tournament:
            tournament.name = row[1]
        else:
            tournament = cls(row[1])
            tournament.id = row[0]
            cls.all[tournament.id] = tournament
        return tournament

    @classmethod
    def display_all_tournaments(cls):
        sql = """
        SELECT * FROM tournaments
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_row(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM tournaments
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_row(row)
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
        SELECT * FROM tournaments
        WHERE name LIKE ?
        """
        rows = CURSOR.execute(sql, (f"%{name}%",))
        return [cls.instance_from_row(row) for row in rows]


    def save(self):
        sql = """
        INSERT INTO tournaments (name)
        VALUES (?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def delete_tournament(self):
        sql = """
        DELETE FROM tournaments
        WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None
    