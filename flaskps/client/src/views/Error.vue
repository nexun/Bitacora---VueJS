<template>
    <div >
        <ViewTitleOptions title="Errores por solucionar" :options=options />      
        <SearchableList :listName=list :columns=columns :endpoint=endpoint :options=queryOptions class="my-4" />
    </div>
</template>

<script>
import ViewTitleOptions from '../components/ViewTitleOptions'
import SearchableList from '../components/SearchableList'
import ErrorList from '../components/SearchableListHeader/ErrorList'


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
                    link: '/errores/nuevo',
                    name: 'Agregar',
                    icon: 'alert-octagon'
                }
            ],
            list: ErrorList,
            endpoint: "/item",
            columns: ['CODIGO', 'CATEGORIA', 'DESCRIPCION', 'SOLUCIONAR', 'ELIMINAR'],
            queryOptions: {
                shouldSort: true,
                tokenize: true,
                threshold: 0.2,
                location: 0,
                distance: 100,
                maxPatternLength: 32,
                minMatchCharLength: 1,
                keys: [
                    'code',
                    'tittle'
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
