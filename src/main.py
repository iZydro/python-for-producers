import tornado.ioloop
import tornado.web
import tornado.httpserver

from index_handler import IndexHandler

import os

from database import DatabaseManager
from menu import Menu


class main:

    web_handler = None

    app = tornado.web.Application([
        (r'/', IndexHandler),
        (r'/add', IndexHandler),
        (r'/nfc', IndexHandler),
    ], cookie_secret="los androllos comen pollo")

    def launch_server(self):

        try:
            os.stat("ini")
        except:
            os.mkdir("ini")

        server = tornado.httpserver.HTTPServer(self.app)

        server.listen(9080)

        ioloop = tornado.ioloop.IOLoop.instance()
        ioloop.start()

    def ping(self):

        print("pong!")

# =============================================================================================================

_main = None
_db = None
#_menu = None

if __name__ == "__main__":

    print("main")
    _main = main()

    #Menu.Instance().number = 10
    print("creating menu")
    _menu = Menu()
    print("created menu")
    _menu.number = 10

    _db = DatabaseManager()
    _db.connect()

    _main.launch_server()

    _main.show_index()
