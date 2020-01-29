<template>
    <div >
        <ViewTitleOptions title="Listado de Soluciones"  />      
        <SearchableList :listName=list :columns=columns :endpoint=endpoint :options=queryOptions class="my-4" />
    </div>
</template>

<script>
import ViewTitleOptions from '../components/ViewTitleOptions'
import SearchableList from '../components/SearchableList'
import SolutionList from '../components/SearchableListHeader/SolutionList'


export default {
    name: 'Error',
    components: {
        ViewTitleOptions,
        SearchableList,
       
    },
    data() {
        return {
            options: [
                {
                    id: 1,
                    link: '/error/nuevo',
                    name: 'Agregar',
                    icon: 'alert-octagon'
                }
            ],
            list: SolutionList,
            endpoint: "/user",
            columns: ['CODIGO', 'CATEGORIA', 'DESCRIPCION', 'ELIMINAR'],
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
