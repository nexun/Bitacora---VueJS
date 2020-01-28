<template>
<div>
    <button @click="user_block" type="button" class="btn" :class="[ isBloquedValue ? 'btn-success' : 'btn-danger' ]">
        {{ isBloquedValue ? 'Desbloquear' : 'Bloquear' }}
    </button>
    <p class="card-text text-muted d-inline-block">{{ isBloquedValue ? actionInfo.deactivate : actionInfo.activate }}</p>
</div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'UpdateUserBlock',
    props: [
        'bloquedData'
    ],
    data() {
        return {
            isBloquedValue: null,
            actionInfo: {
                activate: 'El usuario no tendra acceso',
                deactivate: 'El usuario tendra acceso al sitio'
            }
        }
    },
    methods: {
        user_block() {
            this.$emit('processing')

            const set_bloqued_button = this.isBloquedValue ? 'False' : 'True'            
            const formData = new FormData()
            formData.append('set_bloqued_button', set_bloqued_button)
            axios.put('/user/'+ this.$route.params.id + '/block', formData)
                .then(response => {
                    this.isBloquedValue = !this.isBloquedValue
                    this.$toast.success(`${this.isBloquedValue ? 'Bloqueado!' : 'Desbloqueado!'}`)
                })
                .catch(error => {
                    this.$toast.error('Inténtelo más tarde', 'Error')
                })
        }
    },
    created() {
        axios.get('/user/'+ this.$route.params.id + '/block')
            .then(response => {
                this.isBloquedValue = response.data.user_bloqued_value == 'True' ? true : false
            })
            .catch(error => {})
    }
}
</script>

<style scoped>
.btn + .card-text {
    margin: 10px;
}
</style>
