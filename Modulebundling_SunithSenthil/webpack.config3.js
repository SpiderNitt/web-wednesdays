const webpack = require('webpack');
var HtmlWebpackPlugin = require('html-webpack-plugin');

const config = {  
  entry: './src/function1.js',
  output: {
    path: __dirname + '/destination',
    filename: 'bundle1.js'
  },
  plugins: [
    new HtmlWebpackPlugin({
        title: 'Webpack Plugins',
        filename: 'application.html',
        minify:false, //Minifies project if true
        hash: true, //Helpful for cache busting
        cache: true, //Emits file only when changed
        template: './public/template.html',
    })
  ]
}

module.exports = config;