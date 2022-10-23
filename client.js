var net = require('net')



server = net.createServer(socket => {
    socket.on('connection', console.log('some client connected'))
    socket.on('data', Buffer => {
        console.log(Buffer.toString())
        socket.write(readLine("write to send:"))
    })


}
)
server.listen(3000)