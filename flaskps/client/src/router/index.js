import ActivatePassword from '../views/ActivatePassword.vue'
import About from '../views/About.vue'
import Administrator from '../views/Administrator.vue'
import axios from 'axios'
import Center from '../views/Center.vue'
import Configuration from '../views/Configuration.vue'
import Contact from '../views/Contact.vue'
import Feedback from '../views/Feedback.vue'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import NewCenter from '../views/NewCenter.vue'
import NewUser from '../views/NewUser.vue'
import NotFound from '../views/NotFound.vue'
import Profile_User from '../views/Profile_User.vue'
import Profile_Center from '../views/Profile_Center.vue'
import Roles from '../views/Roles.vue'
import store from '../store'
import User from '../views/User.vue'
import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '../views/Main.vue'
import Solutions from '../views/Solutions.vue'
import Tutorials from '../views/Tutorials.vue'
import Categories from '../views/Categories.vue'



Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/feedback',
    name: 'feedback',
    component: Feedback,
    props: true
  },
  {
    path: '/activate',
    name: 'activate',
    component: ActivatePassword 
  },
  {
    path: '/',
    component: Main,
    children: [
      {
        path: '/usuario',
        name: 'user_index',
        component: User,
        beforeEnter: requiresAuth
      },
      {
        path: '/usuario/nuevo',
        name: 'user_new',
        component: NewUser,
        beforeEnter: requiresAuth
      },
      {
        path: '/usuario/:id',
        name: 'user_profile',
        component: Profile_User,
        beforeEnter: requiresAuth
      },
      {
        path: '/administrador',
        name: 'administrator_index',
        component: Administrator,
        beforeEnter: requiresAuth
      },
      {
        path: '/configuracion',
        name: 'configuration_index',
        component: Configuration,
        beforeEnter: requiresAuth
      },
      {
        path: '/roles',
        name: 'roles_index',
        component: Roles,
        beforeEnter: requiresAuth
      },
      {
        path: '/contacto',
        name: 'home_contact',
        component: Contact,
        beforeEnter: requiresAuth
      },
      {
        path: '/acerca',
        name: 'home_about',
        component: About,
        beforeEnter: requiresAuth
      },
      {
        path: '/empresa',
        name: 'center_index',
        component: Center,
        beforeEnter: requiresAuth
      },      
      {
        path: '/empresa/nuevo',
        name: 'center_new',
        component: NewCenter,
        beforeEnter: requiresAuth
      },
      {
        path: '/empresa/:id',
        name: 'center_profile',
        component: Profile_Center,
        beforeEnter: requiresAuth
      },     
      {
        // This is the default view for Main
        // It has to be the last children
        path: '',
        name: 'home_index',
        component: Home,
        beforeEnter: requiresAuth
      }
    ]
  },
  {
    path: '*',
    name: 'not-found',
    component: NotFound
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

function requiresAuth(to, from, next) {
    if (store.getters.getStatus != 1) {
      if (!store.getters.getUser) {
        store.dispatch('destroyUser')
        router.push('/login').catch(error => {})
      }
    }
    axios.get('/authorize/' + to.name)
      .then(response => next())
      .catch(error => {
        let options = {}
        switch (error.response.data.exception) {
          case 'UserHasNoSession':
            store.dispatch('destroyUser')
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
      })
}

export default router
