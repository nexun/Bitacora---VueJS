<template>
    
</template>

<script>
import Feedback from './Feedback'

export default {
    name: 'NotFound',
    created() {
        const options = {
            title: 'Página no encontrada',
            description: 'La página que estás buscando no existe.',
            noBacktrack: true
        }
        this.$router.push({ name: 'feedback', params: options })
    }
}
</script>