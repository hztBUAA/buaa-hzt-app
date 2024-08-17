const { defineConfig } = require('@vue/cli-service');
const { VuetifyPlugin } = require('webpack-plugin-vuetify');

module.exports = defineConfig({
  publicPath: '/',
  transpileDependencies: ['vuetify'],
  configureWebpack: {
    plugins: [
      new VuetifyPlugin({
        // Add your Vuetify options here
      })
    ]
  },
  devServer: {
    historyApiFallback: true,  // This tells the server to serve index.html for all 404 routes
  }
});
