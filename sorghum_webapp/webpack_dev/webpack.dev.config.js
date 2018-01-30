module.exports = {
  entry:  './index.js',
  output: {
      libraryTarget: 'var',
      library: 'showAddNewButton',
      path:     __dirname + '/../sorghum_webapp/static/js/react_components/',
      filename: 'components.js',
  },
  module: {
      loaders: [
          {
              test:   /\.js/,
              loader: 'babel-loader',
              include: __dirname,
          }
      ],
  },
};