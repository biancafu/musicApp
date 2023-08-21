//bundle all js code to 1 file

const path = require("path");
const webpack = require("webpack");

module.exports = {
  entry: "./src/index.js", //relative path
  output: {
    path: path.resolve(__dirname, "./static/frontend"), //output file path
    filename: "[name].js", //with this name
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
        },
      },
    ],
  },
  optimization: {
    minimize: true,
  },
  plugins: [ //optimization
    new webpack.DefinePlugin({
      "process.env": {
        // This has effect on the react lib size
        NODE_ENV: JSON.stringify("production"),
      },
    }),
  ],
};