from jinja2 import Environment, FileSystemLoader

import tornado.web
from singleton import Singleton

@Singleton
class Menu:

    number = 0

    def __init__(self):
        print('Menu created')

    def ping(self):

        print("Menu pong!")

    def print_number(self, handler: tornado.web.RequestHandler):

        handler.write("<br />Number: " + str(self.number))

    def show_index(self, handler):
        env = Environment(loader=FileSystemLoader("templates"))
        template = env.get_template('login_template.html')
        handler.write(template.render())

