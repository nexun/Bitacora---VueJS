<template>
<tbody class="table">
    <tr :key="row.id" v-for="row in rows">
        <td data-label="Codigo"><router-link :to="'error/'+ row.id">{{ row.code }}</router-link></td>
        <td data-label="Categoria">{{ row.id_category}}</td>
        <td data-label="Nombre">{{ row.tittle }}</td>
        <td data-label="Resolver" > <button class="btn btn-resolve"> <check-icon size="1.5x" class="custom-class"></check-icon></button></td>
        <td data-label="Eliminar">  <button class="btn btn-resolve-2"> <Trash2Icon size="1.5x" class="custom-class"></Trash2Icon></button> </td>
    </tr>
</tbody>
</template>

<script>
import { DeleteIcon, SendIcon, Trash2Icon, CheckIcon } from 'vue-feather-icons'

export default {
    components: {
        DeleteIcon,
        SendIcon,
        Trash2Icon,
        CheckIcon
    },
    name: 'ErrorList',
    props: [
        'rows'
    ]
    
}
</script>

<style scoped>
.btn-resolve{
    color: #49853e;
}
.btn-resolve-2{
    color: #ff1c1c;
}
</style>
