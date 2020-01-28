<template>
<div>
    <ViewTitleOptions title="Configuración" :options=options />
    <CardWithFeedback :cardData="cards.updatePublicInfo" />
    <CardWithFeedback :cardData="cards.updatePagination" />
    <CardWithFeedback :cardData="cards.updateMaintenanceMode" />
</div> 
</template>

<script>
import ViewTitleOptions from '../components/ViewTitleOptions'
import EditableForm from '../components/EditableForm'
import CardWithFeedback from '../components/CardWithFeedback'
import UpdatePaginationForm from '../components/UpdatePaginationForm'
import UpdatePublicInfoForm from '../components/UpdatePublicInfoForm'
import UpdateMaintenanceMode from '../components/UpdateMaintenanceMode'

export default {
    name: 'Configuration',
    components: {
        ViewTitleOptions,
        EditableForm,
        CardWithFeedback
    },
    data() {
        return {
            options: [
                {
                    id: 1,
                    link: '/roles',
                    name: 'Roles y Permisos',
                    icon: 'shield'
                }
            ],
            cards: {
                updatePagination: {
                    title: 'Items por página',
                    form: UpdatePaginationForm,
                    msj: {
                        ok: 'Actualizado',
                        error: 'Error al actualizar'
                    }
                },
                updatePublicInfo: {
                    title: 'Información pública',
                    form: UpdatePublicInfoForm,
                    msj: {
                        ok: 'Actualizado',
                        error: 'Error al actualizar'
                    }
                },
                updateMaintenanceMode: {
                    title: 'Modo mantenimiento',
                    form: UpdateMaintenanceMode,
                    msj: {
                        ok: 'Actualizado',
                        error: 'Error al actualizar'
                    }
                }
            }
        }
    }
}
</script>

<style scoped>

</style>