#Always import tornado
import tornado.web
import tornado.ioloop
import json

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

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
    def post(self):
        try:
            fruit = self.get_argument("fruit")
            fh = open("fruits.txt","a")
            fh.write(f"{fruit}\n")
            fh.close()
            self.write(json.dumps({"message":"Fruit added successfully"}))
        except:
            self.set_status(400)
            self.write("Bad request")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/",basicRequestHandler),
        (r"/list",listTxtRequestHandler),
        
    ])
    port = 8888
    app.listen(port)
    print(f"Application is running on port {port}")
    tornado.ioloop.IOLoop.current().start()