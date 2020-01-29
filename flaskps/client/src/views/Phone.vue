<template>
    <div>
        <ViewTitleOptions title="Acerca de nosotros" />
        <p> {{ this.info }} </p>
        <p> {{ this.description }} </p>
    </div>
</template>    

<script>
import ViewTitleOptions from '../components/ViewTitleOptions'
import axios from 'axios'

export default {
    info: null,
    name: 'About',
    components: {
        ViewTitleOptions,
    },
    /* uwu whats this
    created() {
        const options = {
            title: 'Página en construcción',
            description: 'Esta página estará disponible próximamente.',
            noBacktrack: true
        }
        this.$router.push({ name: 'feedback', params: options })
    }
    */
    data() {
        return {
            info: null,
            description: null
        }
    },
    mounted() {
        axios.get('/getPublicInfo')
            .then(response => {
                this.info = response.data[0].value
                this.description = response.data[1].value              
            })
            .catch(error => { this.info = "me mato"})
    }  

}
</script>