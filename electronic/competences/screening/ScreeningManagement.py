from utils.database import connect2db
from ArxivDownload import ArxivDownload

class ScreeningManagement():
    def __init__(self, date, manager, ScreeningPlan):
        self.conn = connect2db('arxiv_db')
        self.date = date
        self.manager = manager
        self.screenPlan = ScreeningPlan

    def plan(self):
        pass

    def control(self):
        pass

    def report(self):
        pass

    def screening(self):
        pass

    def save(self):
        self.conn.execute()

