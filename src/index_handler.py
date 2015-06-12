from menu import Menu

import tornado
from database import DatabaseManager


class IndexHandler(tornado.web.RequestHandler):

    menu = None
    db = None

    def initialize(self):
        print("Initialize IndexHandler")
        self.menu = Menu.Instance()
        self.db = DatabaseManager.Instance()

    def data_received(self, chunk):
        pass

    def get(self):
        self.menu.show_index(self)
        self.write(self.request.remote_ip)
        print("Index!")

        self.menu.ping()
        self.menu.print_number(self)

        self.menu.number += 1

        self.db.show_projects()

    def post(self):
        print(" - nfc")

