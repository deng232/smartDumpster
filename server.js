var net = require('net')

const readline = require('readline').createInterface({
   input: process.stdin,
   output: process.stdout
})
 const prompt = require("prompt-sync")({ sigint: true });

server = net.createServer(socket => {
   console.log('some client connected')
   //socket.on('connection', x => console.log('some client connected'))
   socket.write('dasfdag')
   socket.on('data', Buffer => {
      console.log(Buffer.toString())
     const sc = prompt('wtc')
     socket.write(sc)

   })
   socket.on('error', error => console.log(error))
   socket.on('end', x => {
      console.log('some client disconnected')
      server.getConnections((x, y) => console.log(y))
   })

}
)
server.listen(3000, '127.0.0.1')