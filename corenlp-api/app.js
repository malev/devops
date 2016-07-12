var fs = require('fs');
var path = require('path');
var express = require('express');
var path = require('path');
var favicon = require('serve-favicon');
var logger = require('morgan');
var bodyParser = require('body-parser');
var NLP = require('stanford-corenlp');

var accessLogStream = fs.createWriteStream(
  path.join('/tmp', 'corenlp.log'), { flags: 'a' });
var app = express();

app.use(logger('dev', { stream: accessLogStream }));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

var routes = require('./api/index');
app.use('/api', routes);

var nlpPath = './corenlp';
var NLPconfig = {
  nlpPath: nlpPath,
  version: '3.6.0',
  annotators: ['tokenize', 'lemma', 'ner', 'parse'],
  language: {
    jar: nlpPath + '/stanford-spanish-corenlp-2015-10-14-models.jar',
    properties: 'StanfordCoreNLP-spanish.properties',
  },
};

module.exports.coreNLP = new NLP.StanfordNLP(NLPconfig, function (err, result) {
  console.log('Error: ' + err);
  console.log('NPL loaded');
});

// catch 404 and forward to error handler
app.use(function (req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  next(err);
});

// error handlers
var sendJSONresponse = function (res, status, content) {
  res.status(status);
  res.json(content);
};

// development error handler
// will print stacktrace
if (app.get('env') === 'development') {
  app.use(function (err, req, res, next) {
    var errorCode = err.status || 500;
    sendJSONresponse(res, errorCode, {
      message: err.message,
      error: err,
    });
  });
}

// production error handler
// no stacktraces leaked to user
app.use(function (err, req, res, next) {
  var errorCode = err.status || 500;
  sendJSONresponse(res, errorCode, {
    message: err.message,
    error: err,
  });
});

module.exports = app;
