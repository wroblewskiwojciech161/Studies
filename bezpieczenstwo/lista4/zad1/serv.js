const https = require("https");
const fs = require("fs");
const path = require("path");
const express = require("express");

const options = {
  key: fs.readFileSync("privkeyA.pem"),
  cert: fs.readFileSync("certA.crt"),
};

const app = express();
app.use(express.urlencoded({ extended: true }));

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname + "/index.html"));
});

app.post("/hack", (req, res) => {
  res.send(
    `Hello, ${req.body.username}, I'm really sorry but you've been hacked. Here's your password as a proof: ${req.body.password}. I also have video footage from your webcam. Donate money to account 14 1140 1010 0000 5244 4400 1007 if you don't want anybody to find out what you're doing at night.`
  );
});

https
  .createServer(options, app)
  .listen(443, () => console.log("app is listening (https)"));
app.listen(80, () => console.log("app is listening (http)"));
