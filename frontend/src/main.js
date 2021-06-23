import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import Toaster from '@meforma/vue-toaster';

const app = createApp(App)

app.use(Toaster, {
    position: 'top'
})
app.use(router)

app.mount('#app')