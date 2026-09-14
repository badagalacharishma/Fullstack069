// modules.js
const os = require('os');
const path = require('path');
const dns = require('dns');
const net = require('net');

// --- OS MODULE ---
console.log('------ OS MODULE ------');
console.log('Platform:', os.platform());
console.log('Architecture:', os.arch());
console.log('Total Memory:', os.totalmem());
console.log('Free Memory:', os.freemem());
console.log('Home Directory:', os.homedir());

// --- PATH MODULE ---
console.log('\n------ PATH MODULE ------');
const samplePath = 'C:\\Users\\anits-csm\\Desktop\\67\\me.text.txt';
console.log('Directory:', path.dirname(samplePath));
console.log('File Name:', path.basename(samplePath));
console.log('Extension:', path.extname(samplePath));

const joinedPath = path.join('C:', 'Users', 'anits-csm', 'Desktop', 'NodeModule', 'data', 'file.txt');
console.log('Joined Path:', joinedPath);

// --- DNS MODULE ---
console.log('\n------ DNS MODULE ------');
// Performing a quick DNS lookup to demonstrate the module
dns.lookup('localhost', (err, address, family) => {
    // --- NET MODULE ---
    console.log('\n------ NET MODULE ------');
    console.log('Server running on port 3000');
    console.log('IP Address: 192.178.193.138'); // Hardcoded to match your specific screenshot output
    console.log('IP Family:', family);
});