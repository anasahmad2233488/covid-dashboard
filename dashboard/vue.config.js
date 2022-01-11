//module.exports = {
//	transpileDependencies: [
//   'vuetify'
//	]
//}


const path = require('path');

module.exports = {
    publicPath: '/', // Should be STATIC_URL + path/to/build
    outputDir: path.resolve(__dirname, '../static/'), // Output to a directory in STATICFILES_DIRS
    filenameHashing: false, // Django will hash file names, not webpack
    runtimeCompiler: true, // See: https://vuejs.org/v2/guide/installation.html#Runtime-Compiler-vs-Runtime-only
    devServer: {
        writeToDisk: true, // Write files to disk in dev mode, so Django can serve the assets
    },
	transpileDependencies: [
    'vuetify'
	],
	  chainWebpack: config => {
		config.plugins.delete('html')
		config.plugins.delete('preload')
		config.plugins.delete('prefetch')
	  }
};