<template>
<div>
    <button @click="toggleMaintenanceMode" type="button" class="btn" :class="[ isMaintenanceMode ? 'btn-success' : 'btn-danger' ]">
        {{ isMaintenanceMode ? 'Desactivar' : 'Activar' }}
    </button>
    <p class="card-text text-muted d-inline-block">{{ isMaintenanceMode ? actionInfo.deactivate : actionInfo.activate }}</p>
</div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'UpdateMaintenanceMode',
    data() {
        return {
            isMaintenanceMode: null,
            actionInfo: {
                activate: 'Solo los administradores tendrán acceso',
                deactivate: 'Todos los usuarios tendrán acceso'
            }
        }
    },
    methods: {
        toggleMaintenanceMode() {
            this.$emit('processing')

            const set_maintenance_mode = this.isMaintenanceMode ? 'false' : 'true'
            const formData = new FormData()
            formData.append('set_maintenance_mode', set_maintenance_mode)

            axios.post('/configuration/toggleMaintenanceMode', formData)
                .then(response => {
                    this.isMaintenanceMode = !this.isMaintenanceMode
                    this.$toast.success('modo mantenimiento', `${this.isMaintenanceMode ? 'Desactivado' : 'Activado'}`)
                })
                .catch(error => {
                    this.$toast.error('Inténtelo más tarde', 'Error')
                })
        }
    },
    created() {
        axios.get('/configuration/maintenanceMode')
            .then(response => {
                this.isMaintenanceMode = response.data.config_options_is_maintenance_mode == 'true' ? true : false
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
