import  asyncio
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 15555))
server.listen()