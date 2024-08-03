const { defineConfig } = require('@vue/cli-service')
const { VuetifyPlugin } = require('webpack-plugin-vuetify')
module.exports = defineConfig({
  publicPath:'./',
  transpileDependencies: [
    'vuetify'
  ],
  configureWebpack: {
    plugins: [
      new VuetifyPlugin({
        // Add your Vuetify options here
      }),
    ],
  },
})
