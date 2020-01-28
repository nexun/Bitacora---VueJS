<template>
<tbody>
    <tr :key="row.id" v-for="row in rows">
        <td data-label="Usuario"><router-link :to="'usuario/'+ row.id">{{ row.username }}</router-link></td>
        <td data-label="Nombre">{{ row.first_name }}</td>
        <td data-label="Apellido">{{ row.last_name }}</td>
        <td data-label="Email">{{ row.email }}</td>
    </tr>
</tbody>
</template>

<script>
export default {
    name: 'AdministratorList',
    props: [
        'rows'
    ]
}
</script>