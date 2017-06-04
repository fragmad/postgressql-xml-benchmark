from string import Template
import psycopg2

beers = [("The Curse of Threepwood", "Silchester (Near Reading), United Kingdom"),
         ("Vixen", "Loughborough, United Kingdom"),
         ("West End Stout", "Leicester, United Kingdom"),
         ("Guiness", "Dublin, Ireland"),
         ("Cloudwater Bergamot Sour", "Manchester, United Kingdom")]


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

    def fetchall(self):
        return self.cur.fetchall()
    
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
        self.template_string = """<beer><name>$name</name><location>$location</location></beer>"""
        self.xml_template = Template(self.template_string)

    def stamp_xml(self, name, location):
        return self.xml_template.substitute(name=name, location=location)

def main2():
    beer = XMLObject()
    print beer.stamp_xml("The Curse of Threepwood", "Silchester (Near Reading), United Kingdom")

def main3():
    beer_xml = XMLObject()
    db = DBStuff("postgres", "postgres", "postgres", "db", "5432")
    db.connect()
    db.query("CREATE TABLE beers (id serial PRIMARY KEY,  beer_xml xml, beer_name varchar)")
    db.query("INSERT INTO beers (beer_xml, beer_name) VALUES ('{}', '{}')".format(beer_xml.stamp_xml(beers[0][0], beers[0][1]), beers[0][0]))
    db.query("INSERT INTO beers (beer_xml, beer_name) VALUES ('{}', '{}')".format(beer_xml.stamp_xml(beers[1][0], beers[1][1]), beers[1][0]))
    db.query("INSERT INTO beers (beer_xml, beer_name) VALUES ('{}', '{}')".format(beer_xml.stamp_xml(beers[2][0], beers[2][1]), beers[2][0]))
    db.query("INSERT INTO beers (beer_xml, beer_name) VALUES ('{}', '{}')".format(beer_xml.stamp_xml(beers[3][0], beers[3][1]), beers[3][0]))
    db.query("INSERT INTO beers (beer_xml, beer_name) VALUES ('{}', '{}')".format(beer_xml.stamp_xml(beers[4][0], beers[4][1]), beers[4][0]))
    db.query("SELECT * from beers")
    beer_list = db.fetchall()
    db.commit()
    db.close()

    for beer in beer_list:
        print beer[0], beer[1], beer[2] 
if __name__ == '__main__':
   main3() 
