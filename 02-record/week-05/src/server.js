// server.js
const http = require('http');

const server = http.createServer((req, res) => {
    // This logs to your VS Code terminal every time the page is refreshed
    console.log('Request received from client');
    
    // This sends the HTML content to the browser
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.write('<h1>Welcome to charishmas my node.js Website</h1>');
    res.write('<h2>Client Request Accepted by Server!</h2>');
    res.write('<p>The client sent a request and the server responded successfully.</p>');
    res.end();
});

server.listen(3000, () => {
    console.log('Server is running at http://localhost:3000');
});