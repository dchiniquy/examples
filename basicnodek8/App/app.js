// Simple node.js web app for demonstrating containerizing apps
'use strict';
var express = require('express'),
    app = express();

app.set('views', 'views');
app.set('view engine', 'pug');

app.get('/', function(req, res) {
  res.send(`hello ${process.env.MESSAGE}`)  
  // res.render(`hello ${process.env.MESSAGE}`, {
  // });
});

app.listen(8080);
module.exports.getApp = app;