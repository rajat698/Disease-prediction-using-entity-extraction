const fs = require('fs');
const http = require('http');

http.createServer((request, response) => {
    if (request.method === 'GET' && request.url === '/') {
        fs.readFile('index.html', function (error, index) {
            if (error) {
                response.writeHead(404);
                response.write('Content you are looking for not found! :(');
            } else {
                response.writeHead(200, { 'Content-Type': 'text/html' });
                response.write(index);
            }
            response.end();
        });
    }
}).listen(8080, function() {
    console.log('diseases-server listening on port 8080...');
});