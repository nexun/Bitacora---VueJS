<template>
    <div >
        <ViewTitleOptions title="Usuarios" :options=options />
        
        <div class="container-fluid p-0">
            <div class="row align-items-center">
                <div class="col-xl-4 d-flex justify-content-center">        
                    <div class=" d-inline-flex shadow p-1"> 
                        <div class=" p-0">
                            <UserPie />
                        </div>
                    </div>
                </div>  
                <div class="col-xl-4 d-flex justify-content-center">        
                    <div class="d-inline-flex shadow p-1"> 
                        <div class="p-0">
                             <ConfirmPie />
                        </div>
                    </div>
                </div> 
                <div class="col-xl-4 d-flex justify-content-center">        
                    <div class="d-inline-flex shadow p-1"> 
                        <div class="p-0">
                             <BloquedPie />
                        </div>
                    </div>
                </div>           
            </div>
        </div>

       <SearchableList :listName=list :columns=columns :endpoint=endpoint :options=queryOptions class="my-4" />
    </div>
</template>

<script>
import ViewTitleOptions from '../components/ViewTitleOptions'
import SearchableList from '../components/SearchableList'
import UserList from '../components/SearchableListHeader/UserList'
import UserPie from '../components/Charts/User-Pie'
import ConfirmPie from '../components/Charts/Confirm-Pie'
import BloquedPie from '../components/Charts/Bloqued-Pie'

export default {
    name: 'User',
    components: {
        ViewTitleOptions,
        SearchableList,
        UserPie,
        ConfirmPie,
        BloquedPie
    },
    data() {
        return {
            options: [
                {
                    id: 1,
                    link: '/usuario/nuevo',
                    name: 'Agregar',
                    icon: 'user-plus'
                }
            ],
            list: UserList,
            endpoint: "/user",
            columns: ['usuario', 'nombre', 'apellido', 'email', 'bloqueado', 'confirmado'],
            queryOptions: {
                shouldSort: true,
                tokenize: true,
                threshold: 0.2,
                location: 0,
                distance: 100,
                maxPatternLength: 32,
                minMatchCharLength: 1,
                keys: [
                    'username',
                    'email'
                ]
            }
        }
    }
}
</script>
<style scoped>
.card {
    margin-top: 10px;
    margin-bottom: 10px;
}
</style>
