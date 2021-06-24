import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import Toaster from '@meforma/vue-toaster';
import VueCookies from 'vue3-cookies'


const app = createApp(App)

app.use(Toaster, {
    position: 'top'
})
app.use(router)

app.use(VueCookies)

app.mount('#app')