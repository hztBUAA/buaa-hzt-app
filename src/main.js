import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
import { createApp } from 'vue';
import App from './App.vue';
import vuetify from './plugins/vuetify';
import router from './router';
// createApp(App).mount('#app')
const app = createApp(App)
app.use(vuetify)
app.use(router)
app.use(ElementPlus)
app.mount('#app')