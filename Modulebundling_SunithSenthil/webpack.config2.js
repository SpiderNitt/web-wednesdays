const webpack = require('webpack');

const config = {  
  entry: './src/function2.js',
  output: {
    path: __dirname + '/destination',
    filename: 'bundle2.js'
  },
  module:{
    rules: [
      {
        test: /\.css$/,
        use: [ 'style-loader', 'css-loader' ]
      }
    ]
  }
}

module.exports = config;