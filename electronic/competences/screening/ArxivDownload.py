from utils import database
from microaiLibrary.article import ArxivPreprint

class ArxivDownload():
    def _init__(self, date, manager, dbconn):
        self.date = date
        self.manager = manager
        self.conn = dbconn
        self.preprints = []
        self.state = 'Started'

    def id_generation(self):
        pass

    def download(self):
        self.state = 'Executed'

    def save2db(self):
        for preprint in self.preprints:
            self.conn.execute()
