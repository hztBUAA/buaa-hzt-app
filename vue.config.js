const { defineConfig } = require('@vue/cli-service');
const { VuetifyPlugin } = require('webpack-plugin-vuetify');
const path = require('path'); // Add this line

module.exports = defineConfig({
  publicPath: '.',
  transpileDependencies: ['vuetify'],
  configureWebpack: {
    plugins: [
      new VuetifyPlugin({
        // Add your Vuetify options here
      })
    ],
    resolve: {
      alias: {
        '@': path.resolve(__dirname, 'src')
      }
    }
  },
  devServer: {
    historyApiFallback: true // This tells the server to serve index.html for all 404 routes
  }
});
