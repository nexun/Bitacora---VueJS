<template>
<tbody>
    <tr :key="row.id" v-for="row in rows">
        <td data-label="Usuario"><router-link :to="'empresa/'+ row.id">{{ row.name }}</router-link></td>
        <td data-label="Direccion">{{ row.address }}</td>
        <td data-label="Telefono">{{ row.phone_number }}</td>       
    </tr>
</tbody>
</template>

<script>
export default {
    name: 'CenterList',
    props: [
        'rows'
    ]
}
</script>