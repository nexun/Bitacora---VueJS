<template>
<tbody>
    <tr :key="row.id" v-for="row in rows">
        <td data-label="Usuario"><router-link :to="'usuario/'+ row.id">{{ row.username }}</router-link></td>
        <td data-label="Nombre">{{ row.first_name }}</td>
        <td data-label="Apellido">{{ row.last_name }}</td>
        <td data-label="Email">{{ row.email }}</td>
        <td data-label="Bloqueado">{{ row.bloqued | capitalize }}</td>
        <td data-label="Confirmado">{{ row.confirmed | capitalize }}</td>
    </tr>
</tbody>
</template>

<script>
export default {
    name: 'UserList',
    props: [
        'rows'
    ]
}
</script>