var express = require('express');
var router = express.Router();
var app = require('../app');

var sendJSONresponse = function (res, status, content) {
  res.status(status);
  res.json(content);
};

var processAPI = function (req, res) {
  var txt = req.body.txt || '';
  console.log('Processing:', txt.slice(0, 10));
  app.coreNLP.process(txt, function (err, result) {
    sendJSONresponse(res, 200, result);
  });
};

router.post('/process', processAPI);
router.get('/hello', function (req, res) {
  sendJSONresponse(res, 200, { foo: 'bar' });
});

module.exports = router;
