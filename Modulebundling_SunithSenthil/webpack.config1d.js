const webpack = require('webpack');

const config = {  
  entry: './src/function1.js',
  mode: "production", //Can also be set to production or none mode
  output: {
    path: __dirname + '/destination',
    filename: 'bundle1.js'
  },
  devServer: {
    port: 3000,
    open:true, //automatically open browser
    compress: true, //enable compression
    liveReload: true, //enable live reload
    hot: true //Enable hot module replacement
  }
}

module.exports = config;