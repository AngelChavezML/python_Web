#Always import tornado
import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World")

class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class queryParamRequestHandler(tornado.web.RequestHandler):
    def get(self):
        number = self.get_argument("num")
        if number.isdigit():
            r = "odd" if int(number) % 2  else "even"
            self.write(f"The integer {number} is {r}")
        else:
            self.write(f"{number} is not a valid integer.")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/",basicRequestHandler),
        (r"/animal",listRequestHandler),
        (r"/iseven", queryParamRequestHandler)
    ])

    port = 8888
    app.listen(port)
    print(f"Application is running on port {port}")
    tornado.ioloop.IOLoop.current().start()