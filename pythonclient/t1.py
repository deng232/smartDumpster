
import asyncio
from glob import glob
from multiprocessing.connection import wait
from re import T
from time import sleep
from tokenize import Double
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 3000  # The port used by the server

waiting = 0
timer = 0
async def main():


    reader, writer = await asyncio.open_connection(
       '127.0.0.1', 3000,limit=1)

    async def reading():
        data = await reader.read(1024)
        global waiting
        waiting = float(data.decode())
        print('time setted'+str(waiting))

    async def sending():
        global timer

        while True:
            writer.write(bytes(str.encode(str(timer)+'\n')))
            await writer.drain()

            print('time here'+str(timer))
            sleep(waiting)
            timer=timer+1




    await reading()
    asyncio.gather(reading(),sending())




asyncio.run(main())