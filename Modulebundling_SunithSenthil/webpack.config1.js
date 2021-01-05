const webpack = require('webpack');

const config = {  
  entry: './src/function1.js',
  output: {
    path: __dirname + '/destination',
    filename: 'bundle1.js'
  },
}

module.exports = config;