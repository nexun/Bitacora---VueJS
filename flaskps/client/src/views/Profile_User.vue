<template>

<div >
    <ViewTitleOptions title="Perfil" :options=options />
    <CardWithFeedback :cardData="cards.updateUserInfo" />    
    <CardWithFeedback :cardData="cards.updateUserRoles" />
    <CardWithFeedback :cardData="cards.updateUserBlock" />
    <CardWithFeedback :cardData="cards.deleteUser" />
</div> 

</template>

<script>
import ViewTitleOptions from '../components/ViewTitleOptions'
import EditableForm from '../components/EditableForm'
import CardWithFeedback from '../components/CardWithFeedback'
import UpdateUserInfoForm from '../components/UpdateUserInfoForm'
import UpdateUserBlockForm from '../components/UpdateUserBlockForm'
import UpdateUserRolesForm from '../components/UpdateUserRolesForm'
import DeleteUserForm from '../components/DeleteUserForm'
import axios from 'axios'





export default {
    name: 'Perfil',
    isTeacher:false,
    components: {       
        EditableForm,    
        CardWithFeedback,
        ViewTitleOptions
    },
    data() {
        return {   
            value: null, 
            options: [
                {
                    id: 1,
                    link: '/usuario',
                    name: 'Volver',
                    icon: 'arrow-left'
                }
            ],        
            cards: {                
                updateUserInfo: {
                    title: 'Información del usuario',
                    form: UpdateUserInfoForm,
                    msj: {
                        ok: 'Actualizado',
                        error: 'Error al actualizar'
                    }
                },
                updateUserBlock: {
                    title: 'Bloquear Usuario',
                    form: UpdateUserBlockForm,
                    data: 'True',
                    msj: {
                        ok: 'Actualizado',
                        error: 'Error al actualizar'
                    }
                },
                updateUserRoles: {
                    title: 'Cambiar roles',
                    form: UpdateUserRolesForm,
                    msj: {
                        ok: 'Actualizado',
                        error: 'Error al actualizar'
                    }
                },
                deleteUser: {
                    title: 'Eliminar Usuario',
                    form: DeleteUserForm,
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
