#Always import tornado
import tornado.web
import tornado.ioloop
import json

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World")

class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class resoruceParamRequestHandler(tornado.web.RequestHandler):
    def get(self,studentName,courseID):
        self.write(f"Student: {studentName} Course: {courseID}")

class queryParamRequestHandler(tornado.web.RequestHandler):
    def get(self):
        number = self.get_argument("num")
        if number.isdigit():
            r = "odd" if int(number) % 2  else "even"
            self.write(f"The integer {number} is {r}")
        else:
            self.write(f"{number} is not a valid integer.")

class listTxtRequestHandler(tornado.web.RequestHandler):
    def get(self):
        #Open the file that is in the same directory
        try :
            fh = open("fruits.txt","r")
        except FileNotFoundError:
            self.set_status(404)
            self.write("File not found")
            return
        
        #Option r is for read
        fruits = fh.read().splitlines() #this is an array
        fh.close()
        self.write(json.dumps(fruits)) #Converts the array to a JSON string

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/",basicRequestHandler),
        (r"/animal",listRequestHandler),
        (r"/iseven", queryParamRequestHandler),
        (r"/student/([a-z]+)/([0-9]+)", resoruceParamRequestHandler), #Regular expression to Resource Params, with + is infinite
        (r"/list",listTxtRequestHandler)
    ])

    port = 8888
    app.listen(port)
    print(f"Application is running on port {port}")
    tornado.ioloop.IOLoop.current().start()