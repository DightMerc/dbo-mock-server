from aiohttp import web

mobile_v2 = web.RouteTableDef()


@mobile_v2.get("/api/mobile/v2/offer/link")
async def get_handler(_):
    return web.Response(text="<html>Offer content</html>")
