const webpack = require('webpack');

const config = {
    entry:  __dirname + '/static/js/index.jsx',
    output: {
        path: __dirname + '/static/dist',
        filename: 'bundle.js',
    },
    resolve: {
        extensions: ['.js', '.jsx', '.css']
    },
};

module: {
  rules: [
    {
      test: /\.js$/,
      exclude: /node_modules/,
      use: 'babel-loader',
      query: {
        // presets: ['babel/preset-env','@babel/preset-react']
        presets: ['env', 'react']
      }
    }
  ]
}

module.exports = config;