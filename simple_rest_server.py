import sys
from asyncio import sleep
from aiohttp import web


def get_digit(digit: str, default: int = 0) -> int:
    """
    :return: converted string to integer or default
    """
    digit = str(digit)
    return int(digit) if digit.isdigit() else default


async def handle(request: web.Request) -> web.json_response:
    """
    request params:
    - code (http code)
    - time (sec)
    :return: json with code and time
    """
    data = {
        'code': get_digit(request.query.get('code'), 200),
        'time': get_digit(request.query.get('time'), 0)
    }

    if data['time']:
        await sleep(delay=int(data['time']))

    return web.json_response(data, status=data['code'])

app = web.Application()
routes = [web.get('/get-response', handle)]
app.add_routes(routes)

if __name__ == '__main__':
    port = 8080
    if len(sys.argv) > 2 and sys.argv[1] == '-p':
        port = get_digit(sys.argv[2], port)
    web.run_app(app, port=port)
