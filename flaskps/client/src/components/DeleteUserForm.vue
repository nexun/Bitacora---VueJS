<template>
<div>
    <button  v-confirm="{ok: user_delete, message: 'Se eliminara el usuario del sistema. Desea Continuar?'}"  type="button" class="btn btn-custom-light" >
       <span >Eliminar</span>
    </button>
    
</div>
</template>

<script>
import axios from 'axios'
import VuejsDialog from 'vuejs-dialog';



export default {
    name: 'DeleteUser', 
    okText: 'Processed',     
    methods: {
        user_delete() {
            this.$emit('processing')                       
            axios.delete('/user/' + this.$route.params.id)
                .then(response => {
                    this.$toast.success('eliminado', 'Usuario')
                    this.$router.push('/usuario')
                })
                .catch(error => {
                    this.$toast.error('Inténtelo más tarde', 'Error')
                })
        }
    },
    
    
    
}
</script>

<style scoped>
.btn + .card-text {
    margin: 10px;
}

</style>