from sqlalchemy.orm import sessionmaker
from chidoplus.models import ChidoplusDB, db_connect, create_table


class ChidoplusPipeline(object):

    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        chidoplusdb = ChidoplusDB()
        chidoplusdb.magazine = item['magazine']
        chidoplusdb.title = item['title']
        chidoplusdb.summary = item['summary']
        chidoplusdb.link = item['link']

        try:
            session.add(chidoplusdb)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return item