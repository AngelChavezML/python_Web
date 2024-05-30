#Always import tornado
import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World")
if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/",basicRequestHandler)
    ])

    port = 8888
    app.listen(port)
    print(f"Application is running on port {port}")
    tornado.ioloop.IOLoop.current().start()