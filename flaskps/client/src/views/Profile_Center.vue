<template>
<div v-if="value == 'True'">
    <ViewTitleOptions title="Empresa" :options=options />
    <CardWithFeedback :cardData="cards.updateCenterInfo" />
    <div class="card shadow col-lg-10 p-0">
        <div class="card-header d-flex align-items-center">
            <h5 class="mb-0">Ubicacion</h5>        
        </div>
        <div class="card-body map-box">
            <MapCenter /> 
        </div>
    </div>    
    <br>
    <CardWithFeedback :cardData="cards.deleteCenter" />
</div>         
<div v-else>
    <ViewTitleOptions title="Empresa no encontrada" :options=options />
</div>
</template>

<script>
import ViewTitleOptions from '../components/ViewTitleOptions'
import EditableForm from '../components/EditableForm'
import CardWithFeedback from '../components/CardWithFeedback'
import UpdateCenterInfoForm from '../components/UpdateCenterInfoForm'
import DeleteCenterForm from '../components/DeleteCenterForm'
import MapCenter from '../components/MapCenter'
import VuejsDialog from 'vuejs-dialog';

import axios from 'axios'

export default {
    name: 'Perfil',
    components: {       
        EditableForm,    
        CardWithFeedback,
        ViewTitleOptions,
        MapCenter
    },
    data() {
        return {   
            value: null, 
            options: [
                {
                    id: 1,
                    link: '/nucleo',
                    name: 'Volver',
                    icon: 'arrow-left'
                }         
                         
            ],        
            cards: {                
                updateCenterInfo: {
                    title: 'Información de la empresa',
                    form: UpdateCenterInfoForm,
                    msj: {
                        ok: 'Actualizado',
                        error: 'Error al actualizar'
                    }
                },
                deleteCenter: {
                    title: 'Eliminar empresa',
                    form: DeleteCenterForm,
                    msj: {
                        ok: 'Actualizado',
                        error: 'Error al actualizar'
                    }
                },
                
                
            }          
        }
    },
    created(){
        axios.get('/center/exist/' + this.$route.params.id)
            .then(response => {
                this.value = response.data.value
            })
            .catch(error => {})
    }
}
</script>

<style scoped>
.map-box {
    height: 500px;
}
</style>
