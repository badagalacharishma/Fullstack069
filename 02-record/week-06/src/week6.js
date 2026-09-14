// Import the Express module
const express = require('express');

// Create the application
const app = express();
const port = 3000;

// Route 1: The Home Page s
app.get('/', (req, res) => {
    res.send(`
        <h1>Welcome to my Express Server</h1>
        <p>This is the home page. Try visiting <b>localhost:3000/profile</b></p>
    `);
});

// Route 2: A Data API 
app.get('/profile', (req, res) => {
    
    // A simple Javascript object holding student details
    const myProfile = {
        name: "B.Charishma",
        department: "CSE (AI & ML)",
        cgpa: 8.35,
        status: "Active"
    };

    // Express automatically converts the JS object to JSON and sends it!
    res.json(myProfile);
});

// Start the server and listen for requests
app.listen(port, () => {
    console.log(`Express app running at http://localhost:${port}`);
});