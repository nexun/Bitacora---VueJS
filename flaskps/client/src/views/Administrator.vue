<template>
    <div>
        <ViewTitleOptions title="Administradores" />
        <SearchableList :listName=list :columns=columns :endpoint=endpoint :options=queryOptions />
    </div>
</template>

<script>
import ViewTitleOptions from '../components/ViewTitleOptions'
import SearchableList from '../components/SearchableList'
import AdministratorList from '../components/SearchableListHeader/AdministratorList'

export default {
    name: 'Administrator',
    components: {
        ViewTitleOptions,
        SearchableList
    },
    data() {
        return {
            list: AdministratorList,
            endpoint: "/administrator",
            columns: ['usuario', 'nombre', 'apellido', 'email'],
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

<style>

</style>
