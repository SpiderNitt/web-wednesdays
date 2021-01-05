const webpack = require('webpack');
var HtmlWebpackPlugin = require('html-webpack-plugin');

const config = {  
  entry: './src/function2.js',
  mode: "production", 
  output: {
    path: __dirname + '/destination',
    filename: 'bundle3.js'
  },
  module:{
    rules: [
      {
        test: /\.css$/,
        use: [ 'style-loader', 'css-loader' ]
      }
    ]
  },
  devServer: {
    port: 3000,
  },
  plugins: [
    new HtmlWebpackPlugin({
        filename: 'final.html',
        hash: true,
        template: './public/template.html',
    })
  ]
}

module.exports = config;