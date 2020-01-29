<template>
    <div>
        <ViewTitleOptions title="Empresas" :options=options />
        <SearchableList :listName=list :columns=columns :endpoint=endpoint :options=queryOptions />
    </div>
</template>

<script>
import ViewTitleOptions from '../components/ViewTitleOptions'
import SearchableList from '../components/SearchableList'
import CenterList from '../components/SearchableListHeader/CenterList'

export default {
    name: 'Center',
    components: {
        ViewTitleOptions,
        SearchableList
    },
    data() {
        return {
            options: [
                {
                    id: 1,
                    link: '/nucleo/nuevo',
                    name: 'Agregar',
                    icon: 'plus'
                }
            ],
            list: CenterList,
            endpoint: "/center",
            columns: ['Nombre','Direccion','Telefono' ],
            queryOptions: {
                shouldSort: true,
                tokenize: true,
                threshold: 0.2,
                location: 0,
                distance: 100,
                maxPatternLength: 32,
                minMatchCharLength: 1,
                keys: [
                    'name',
                    'address',
                    'phone_number'                    
                ]
            }
        }
    }
}
</script>

<style>

</style>
