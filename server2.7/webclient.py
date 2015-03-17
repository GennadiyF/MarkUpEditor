import web

urls = ('/', 'index')

class index:
    def GET(self):
        return "Hello, world! This is our trial page."

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()