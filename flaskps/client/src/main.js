import 'animate.css'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'leaflet/dist/leaflet.css'
import 'vuejs-dialog/dist/vuejs-dialog.min.css'
import 'izitoast/dist/css/iziToast.min.css'
import "vue2-datepicker/index.css"
import './filter'
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Vuelidate from 'vuelidate'
import axios from 'axios'
import { Icon }  from 'leaflet'
import VuejsDialog from 'vuejs-dialog'
import VueIziToast from 'vue-izitoast'

delete Icon.Default.prototype._getIconUrl
Icon.Default.mergeOptions({
  iconRetinaUrl: require("leaflet/dist/images/marker-icon-2x.png"),
  iconUrl: require("leaflet/dist/images/marker-icon.png"),
  shadowUrl: require("leaflet/dist/images/marker-shadow.png")
})

Vue.use(VuejsDialog, {
  html: true,
  reverse: true,
  okText: '&#10003; Aceptar',
  cancelText: '&#10005; Cancelar',
  animation: 'zoom'
})
Vue.use(Vuelidate)
Vue.use(VueIziToast)
Vue.config.productionTip = false

axios.interceptors.response.use(function (response) {
    return response;
}, function (error) {
      if (error.response.status === 500) {
        const v = new Vue()
        v.$toast.warning('Nuestros servidores pueden estar teniendo dificultades', 'Atención', {position: 'bottomCenter'})
      }

      let options = {}
      switch (error.response.data.exception) {
        case 'UserHasNoSession':
            store.commit('setUser', {id: null, roles: [], permissions: []})
            router.push('/login').catch(error => {})
            break

        case 'RestrictedAcess':
          options = {
            title: 'Acceso restringido',
            description: 'No tiene permiso para acceder a este sitio.',
            noBacktrack: true
          }
          router.push({ name: 'feedback', params: options }).catch(error => {})
          break

        case 'UserIsBloqued':
          options = {
            title: 'Acceso restringido',
            description: 'Sus credenciales se encuentran deshabilitadas por el momento.',
            noBacktrack: true
          }
          router.push({ name: 'feedback', params: options }).catch(error => {})
          break

        case 'AppInMaintenanceMode':
          options = {
            title: 'Estamos trabajando',
            description: 'El sitio se encuentra en mantenimiento.',
            noBacktrack: true
          }
          router.push({ name: 'feedback', params: options }).catch(error => {})
          break

        default:
          break
    }
  return Promise.reject(error);
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
