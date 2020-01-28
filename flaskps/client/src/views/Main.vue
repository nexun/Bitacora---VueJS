<template>
<div>
    <HeaderBar />
    <div class="container-fluid">
        <Sidebar />        
        <div class="row main"> 
            <div id="content" class="col-md-9 col-xl-10 pr-0">  
                <main class="content">
                    <transition mode="out-in" leave-active-class="animated fadeOut faster" enter-active-class="animated fadeIn faster">
                        <router-view/>
                    </transition>
                </main>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import HeaderBar from '../components/HeaderBar'
import Sidebar from '../components/Sidebar'

export default {
    name: 'Main',
    components: {
        HeaderBar,
        Sidebar,

    },
   
    
}
</script>

<style scoped>
/* Main */
.main {
    height: calc(100vh - 5rem);
}
#content{
    margin-left: auto;
}

/* Content */
.content {
    padding-right: 40px;
    padding-top: 10px;
    overflow-y: auto;
    height: calc(100vh - 6rem);
    text-align: justify;
}

@media(max-width: 767px){
    .content{
        overflow-y: hidden;
        height: auto;
       
    }
    #content{
        margin-left: auto;
    }
}



.sidebar_wrapper{
    position: fixed;
    bottom: 0px;
    right: 0px;
    margin: 30px;
    border-radius: 40px 40px 40px 40px;
    z-index: 1000;
    display: none;
}

.sidebar_wrapper .feather{
    width: 40px;
    height: 50px;
}

/* Footer */
.footer {
    height: 4rem;
    box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, .05), inset 0 -1px 0 rgba(0, 0, 0, .1);
    position: fixed;
    bottom: 0;
    z-index: 1071;
}
</style>