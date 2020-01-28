const path = require('path')
process.env.VUE_APP_UPLOAD = "http://localhost:5000/static/uploads/"

module.exports = {
    devServer: {
        proxy: 'http://localhost:5000/',
    },
    outputDir: process.env.NODE_ENV === 'production'
    ? path.resolve(__dirname, '../templates')
    : 'dist',
    assetsDir: process.env.NODE_ENV === 'production'
    ? '../static'
    : '',
    publicPath: process.env.NODE_ENV === 'production'
    ? './'
    : '/'
}
