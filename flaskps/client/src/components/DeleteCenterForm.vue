<template>
<div>
    <button v-confirm="{ok: center_delete, message: 'Se eliminara el nucleo del sistema. Desea Continuar?'}" type="button" class="btn btn-custom-light" >
       <span >Eliminar</span>
    </button>
    
</div>
</template>

<script>
import axios from 'axios'
import VuejsDialog from 'vuejs-dialog';

export default {
    name: 'DeleteCenter',    
    methods: {
        center_delete() {
            this.$emit('processing')               
            axios.delete('/center/' + this.$route.params.id)
                .then(response => {
                    this.$toast.success('eliminado', 'Núcleo')
                    this.$router.push('/nucleo')
                })
                .catch(error => {
                    this.$toast.error('Inténtelo más tarde', 'Error')
                })
        }
    }
    
}
</script>

<style scoped>
.btn + .card-text {
    margin: 10px;
}
</style>