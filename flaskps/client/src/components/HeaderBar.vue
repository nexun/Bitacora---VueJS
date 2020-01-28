<template>
<div>
<header class="navbar navbar-dark header-nav flex-md-row flex-md-nowrap shadow">
  <div class="col-10 col-md-5 col-xl-3">
      
      <router-link to="/" class="navbar-brand p-0">
          <img src="../assets/img/logo_bitacora.png" alt="Logo Bitacora 2.0"
              class="img-fluid">
      </router-link>

  </div>

  <div class="col-2 py-2 px-0 text-right d-md-none">
      <button id="user_menu_min" type="button" class="btn btn-secondary collapsed ml-auto" data-toggle="collapse" data-target="#sidebar"
          aria-controls="sidebar" :aria-expanded="false" aria-label="Menu">
          <menu-icon size="1.5x" class="custom-class" />
      </button>
  </div>
  <div class="col-12 col-md-7 col-xl-8 d-flex p-0">

      <div id="user" class="dropdown ml-auto">
          <button class="btn btn-secondary dropdown-toggle" type="button" id="user_menu_max" data-toggle="dropdown"
              aria-haspopup="true" aria-expanded="false">
                  <img v-if="getUser().photo == null" src="../assets/img/user.jpg" alt="Imagen de usuario" width="37px"
                   class="mr-3 img-thumbnail" >            
                  <img v-if="getUser().photo != null" :src="link + getUser().photo" alt="Imagen de usuario" width="37px"
                   class="mr-3 img-thumbnail" >
              
              <span id="span">{{ this.getUser().first_name +' '+ this.getUser().last_name }}</span>
          </button>
          <div class="dropdown-menu dropdown-menu-right" aria-labelledby="user_button">
              <router-link class="dropdown-item" id="user_menu_option" :to="'/usuario/' + getUser().id"><user-icon size="1.5x" class="custom-class" /> Perfil</router-link>
              <a @click="logout" class="dropdown-item" id="user_menu_option" href=#><log-out-icon size="1.5x" class="custom-class" /> Cerrar sesión</a>
          </div>
      </div>

  </div>
</header> 

</div>

</template>

<script>
import axios from 'axios'
import { MenuIcon, UserIcon, LogOutIcon } from 'vue-feather-icons'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'HeaderBar',
  components: {
      MenuIcon,
      UserIcon,
      LogOutIcon

  },
  methods: {
    ...mapGetters(['getUser']),
    ...mapActions(['destroyUser']),
    logout() {
        axios.get('/logout')
            .then(() => {})
            .catch(() => {})
            .finally(() => {
                this.destroyUser()
                this.$router.push('/login').catch(() => {})
            })
    },
    data () {
        return {
            ariaexpanded: "false",
        }
    }
  },
   data () {
        return {                       
            link: process.env.VUE_APP_URL
        }
    }
}
</script>

<style scoped>
.header-nav {
    height: 5rem;
    position: -webkit-sticky;
    position: sticky;
    top: 0;
    z-index: 1071;
    background-color: #4879bf;
}
#user_menu_min{
    color: grey;
    background-color: #ffffff;
    border-color: #ef8454;
}
#user_menu_option{
    color: grey;
}
#user_menu_max{
    color: grey;
    background-color: #ffffff;
    border-color: #69262c;
}
#span{
    color:grey;
}
@media (max-width: 767px) {
    #user {
        display: none !important;
    }
    .header-nav{
        height: auto;
    }
}

#user_menu .dropdown-item{
    font-weight: 500;
    color:white;
}


#user_menu .dropdown-item:hover{
    color: white;
    background-color: #99585db9;
}

#user_menu .dropdown-item .feather{
    color: #999;
    margin-right: 10px;
}

#user_menu .dropdown-item:hover .feather, #user_menu .dropdown-item.active .feather{
    color: inherit;
} 
</style>
