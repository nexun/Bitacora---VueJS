<template>
    <div>
        <ViewTitleOptions title="Contacto"/>
         <p> Teléfono de Contacto: +54 9 221 654-8890 </p>       
        <p> Email de Contacto: {{ this.email }} </p>
    </div>
</template>    

<script>
import ViewTitleOptions from '../components/ViewTitleOptions'
import axios from 'axios'

export default {
    email: null,
    name: 'Contacto',
    components: {
        ViewTitleOptions,
    },
    data() {
        return {
            email: null
        }
    },
    mounted() {
        axios.get('/getPublicInfo')
            .then(response => {
                this.email = response.data[2].value
           
            })
            .catch(error => {})
    }  

}
</script>