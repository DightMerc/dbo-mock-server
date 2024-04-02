from aiohttp import web

from views import mobile_v2

app = web.Application()
app.add_routes(mobile_v2)

if __name__ == "__main__":
    web.run_app(app, port=5060)
