import psycopg2


class DBStuff(object):
    def __init__(self, dbname, user, password, host, port):
       self.connection_string = "dbname={0} user={1} password={2} host={3} port={4}".format(dbname,
                                                                                            user,
                                                                                            password,
                                                                                            host,
                                                                                            port)

    def connect(self):
        self.conn = psycopg2.connect(self.connection_string)
        self.cur = self.conn.cursor()

    def query(self, query):
        self.cur.execute(query)

    def fetchone(self):
        return self.cur.fetchone()
    
    def commit(self):
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()
       
def main1():
    db = DBStuff("postgres", "postgres", "postgres", "db", "5432")
    db.connect()
    db.query("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar)")
    db.query("INSERT INTO test (num, data) VALUES (100, 'abcdef')")
    db.query("SELECT * from test")
    print db.fetchone()
    db.commit()
    db.close()

class XMLObject(object):
    def __init__(self):
        self.xml_template = """ 
        foo
        """
        
if __name__ == '__main__':
   main1() 
