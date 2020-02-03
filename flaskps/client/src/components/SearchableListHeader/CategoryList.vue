<template>
<tbody class="table">
    <tr :key="row.id" v-for="row in rows">
        <td data-label="Codigo">{{ row.id }}</td>
        <td data-label="Nombre">{{ row.name }}</td>
      
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