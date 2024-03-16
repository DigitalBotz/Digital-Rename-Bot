from aiohttp import web

Rkn_FileRenameBot = web.RouteTableDef()

@Rkn_FileRenameBot.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("RknDeveloper")


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(Rkn_FileRenameBot)
    return web_app
