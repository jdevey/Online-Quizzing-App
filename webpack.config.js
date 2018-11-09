var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,

  entry: {
    nonauthindex: './quizme/quizmeapp/static/js/nonauthindex',
    authindex: './quizme/quizmeapp/static/js/authindex',
    quizcreation: './quizme/quizmeapp/static/js/quiz-creation',
    questioncreation: './quizme/quizmeapp/static/js/question-creation'
  },

  output: {
      path: path.resolve('./quizme/quizmeapp/static/bundles/'),
      filename: "[name]-[hash].js",
  },

  plugins: [
    new BundleTracker({filename: './quizme/quizme/webpack-stats.json'}),
  ],
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: ['babel-loader']
      }
    ]
  },
  resolve: {
    extensions: ['*', '.js', '.jsx']
  }

};
