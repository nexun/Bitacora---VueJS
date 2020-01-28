<template>
    <div class="container-fluid">   
    
        <nav class="sidebar col-md-3 col-xl-2 px-0 collapse d-md-block shadow" id="sidebar" :data-toggle="[ $vssWidth < 768 ? 'collapse' : '']" data-target="#sidebar">
           <ul class="nav flex-column flex-md-nowrap sidebar-options border-bottom p-3 ">
            <div :class="[ $vssWidth < 768 ? 'row' : 'col-lg-13']">
                            
                    <div :class="clase" v-if="getUser.permissions.includes('home_index')">
                        <li  :class="clase_li">
                            <router-link to="/" class="nav-link">
                                <home-icon size="1.5x" class="custom-class" />
                                <span>Dashboard</span>
                            </router-link>
                        </li>
                    </div>
                    <div :class="clase" v-if="getUser.permissions.includes('center_index')">
                    <li  :class="clase_li">
                        <router-link to="/errores" class="nav-link">
                              <alert-octagon-icon size="1.5x" class="custom-class"></alert-octagon-icon>
                            <span>Errores </span>
                        </router-link>
                    </li>
                    </div>  
                     <div :class="clase" v-if="getUser.permissions.includes('center_index')">
                    <li  :class="clase_li">
                        <router-link to="/soluciones" class="nav-link">
                            <check-circle-icon size="1.5x" class="custom-class"></check-circle-icon>
                            <span>Soluciones </span>
                        </router-link>
                    </li>
                    </div> 
                    <div :class="clase" v-if="getUser.permissions.includes('center_index')">
                    <li  :class="clase_li">
                        <router-link to="/tutoriales" class="nav-link">
                            <help-circle-icon size="1.5x" class="custom-class"></help-circle-icon>
                            <span>Tutoriales </span>
                        </router-link>
                    </li>
                    </div>
                     <div :class="clase" v-if="getUser.permissions.includes('center_index')">
                    <li  :class="clase_li">
                        <router-link to="/tutoriales" class="nav-link">
                            <phone-call-icon size="1.5x" class="custom-class"></phone-call-icon>
                            <span>Telefonos </span>
                        </router-link>
                    </li>
                    </div>  
                    <div :class="clase" v-if="getUser.permissions.includes('user_index')" >
                    <li :class="clase_li">
                        <router-link to="/usuario" class="nav-link">
                            <key-icon size="1.5x" class="custom-class"></key-icon>
                            <span>Claves </span>
                        </router-link>
                    </li>
                    </div>
                                    
                </div>    
            </ul>
            <ul class="nav flex-column p-3">
                <div :class="[ $vssWidth < 768 ? 'row' : 'col-lg-13']">
                    <div :class="clase" v-if="getUser.permissions.includes('user_index')" >
                    <li :class="clase_li">
                        <router-link to="/usuario" class="nav-link">
                            <users-icon size="1.5x" class="custom-class" />
                            <span>Usuarios </span>
                        </router-link>
                    </li>
                    </div>   
                    
                    <div :class="clase" v-if="getUser.permissions.includes('center_index')">
                    <li  :class="clase_li">
                        <router-link to="/empresas" class="nav-link">
                            <archive-icon size="1.5x" class="custom-class" />
                            <span>Empresas </span>
                        </router-link>
                    </li>
                    </div>    
                    <div :class="clase" v-if="getUser.permissions.includes('center_index')">
                    <li  :class="clase_li">
                        <router-link to="/categorias" class="nav-link">
                            <list-icon size="1.5x" class="custom-class"></list-icon>
                            <span>Categorias </span>
                        </router-link>
                    </li>
                    </div> 
                    <div :class="clase" v-if="getUser.permissions.includes('configuration_index')">
                    <li :class="clase_li">
                        <router-link to="/configuracion" class="nav-link">
                            <settings-icon size="1.5x" class="custom-class" />
                            <span>Configuración </span>
                        </router-link>
                    </li>
                    </div>
                    <div :class="clase" v-if="getUser.permissions.includes('home_about')" >
                    <li :class="clase_li">
                        <router-link to="/acerca" class="nav-link">
                            <info-icon size="1.5x" class="custom-class" />
                            <span>Acerca </span>
                        </router-link>
                    </li>
                    </div>
                    <div :class="clase" v-if="getUser.permissions.includes('home_contact')">
                    <li  :class="clase_li">
                        <router-link to="/contacto" class="nav-link">
                            <inbox-icon size="1.5x" class="custom-class" />
                            <span>Contacto </span>
                        </router-link>
                    </li>
                    </div>               
                
                    
                </div>    
            </ul>
            <ul class="nav flex-column p-3">
                <div :class="[ $vssWidth < 768 ? 'row' : 'col-lg-13']">
                    <div class="col user_menu" v-if="getUser.permissions.includes('user_profile')" >
                    <li  :class="clase_li">
                            <router-link class="nav-link" :to="'/usuario/' + getUser.id">
                                <user-icon size="1.5x" class="custom-class" /> 
                                <span>Perfil </span>
                            </router-link>
                    </li>
                    </div>
                    <div class="col user_menu " v-if="getUser.permissions.includes('home_contact')">
                        <li  :class="clase_li">
                            <a @click="logout"  href=# class="nav-link">
                                <log-out-icon size="1.5x" class="custom-class" /> <span>Cerrar sesión </span></a>
                        </li>
                    </div>
                </div> 
            </ul>
           
    
        </nav>    
   
    </div>


</template>

<script>
import axios from 'axios'
import { mapGetters, mapActions} from 'vuex'
import { Minimize2Icon, KeyIcon, HelpCircleIcon, ListIcon, PhoneCallIcon, CheckCircleIcon, HomeIcon,AlertOctagonIcon, UsersIcon, UserIcon, ArchiveIcon, MusicIcon, FolderIcon, SettingsIcon, InfoIcon, InboxIcon,CalendarIcon,BookOpenIcon,LogOutIcon } from 'vue-feather-icons'
import VueScreenSize from 'vue-screen-size'

export default {
    name: 'Sidebar',
    components: {
        Minimize2Icon,
        HomeIcon,
        UsersIcon,
        UserIcon,
        ArchiveIcon,
        MusicIcon,
        FolderIcon,
        SettingsIcon,
        InfoIcon,
        InboxIcon,
        CalendarIcon,
        BookOpenIcon,
        LogOutIcon,
        AlertOctagonIcon,
        CheckCircleIcon,
        HelpCircleIcon,
        KeyIcon,
        PhoneCallIcon,
        ListIcon
    },
    mixins: [VueScreenSize.VueScreenSizeMixin],    
    methods: {
    ...mapActions(['destroyUser']),
    logout() {
        axios.get('/logout')
            .then(() => {})
            .catch(() => {})
            .finally(() => {
                this.destroyUser()
                this.$router.push('/login').catch(() => {})
            })
    }
    },
    data(){
        return{
            clase:"col option",
            clase_li:"nav-item "
        }
    },
    computed: {
      ...mapGetters(['getUser'])
    }
}
</script>

<style scoped>
.sidebar {
    position: fixed;
    top: 4.5rem;
    bottom: 0;
    left: 0;
    z-index: 1000;
    background-color: white;
    box-shadow: inset -1px 0 0 rgba(0, 0, 0, .1);
    justify-content: space-between;
    width: auto;
}

.sidebar .nav-link {
    font-weight: 500;
    color: #333;
}

.sidebar .nav-link .feather {
    margin-right: 10px;
    color: #999;
}

.sidebar .nav-link.active {
    color: #7d2c33;
}

.sidebar .nav-link:hover .feather, .sidebar .nav-link.active .feather {
    color: inherit;
}

.sidebar-heading {
    font-size: .75rem;
    text-transform: uppercase;
}

.minimize .feather {
    width: 16px;
    height: 16px;
}

.minimize{
    position: absolute;
    top: 0px;
    right: 0px;
    height: auto;
    width: auto;
}

.sidebar-options {
    height: calc(100vh - 20rem);
    padding-bottom: 3px;
    overflow-y: auto;
}

.col {
    font-size: 100%;
}

.nav-link{
    padding: .5rem 0rem;
}

.row {
    font-size: 80%;
}

.user_menu{
    visibility: hidden;
}

@media(max-width: 767px){
    .sidebar{
        position: initial;        
    }   

    .sidebar-options {
    height: auto;
    
    }

    .sidebar .nav-link .feather {
    margin-right: 0px;
    color: #999;
    }

    .nav-link {
        display: block;
    }

    .user_menu{
        visibility: visible;
        color: inherit;
    }

    span {
        font-size: 10px;
    }
    
    .col{
        max-width: 70px;
    }

    .row{
        font-size: 110%;
        justify-content: center;
        padding: 10px;
    }

    a {
        text-align: center; 
    }

    ul {
        padding: 0.5rem!important;
    }
    
    .container-fluid{
        width: 100%;
        padding-right: 15px;
        padding-left: 15px;
        margin-right: auto;
        margin-left: auto;
    }
}
@media(max-height: 835px) and (min-width: 800px){
    .sidebar{
        font-size: 13px;
            }
    .option{
        height: 30px;
    }

    
    
}



</style>