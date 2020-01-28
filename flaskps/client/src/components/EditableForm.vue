<template>
<form class="editable-form needs-validation inline-form" data-action="/configuration/updatePagination" novalidate>
    <EditableFormInput :key="inputData.name" v-for="inputData in inputsData" :inputData="inputData" :isEditing="isEditing" />
    <EditableInputButtonGroup @start-editing="startEditing" @stop-editing="stopEditing" />
</form>
</template>

<script>
import EditableFormInput from './EditableFormInput'
import EditableInputButtonGroup from './EditableInputButtonGroup'

export default {
    name: 'EditableForm',
    components: {
        EditableFormInput,
        EditableInputButtonGroup
    },
    data() {
        return {
            isEditing: false,
            inputsData: [
                {
                    name: 'items_per_page_input',
                    title: 'Cantidad',
                    type: 'number',
                    actual: 5,
                    new: 5,
                }
            ]
        }
    },
    methods: {
        startEditing() {
            this.isEditing = true
        },
        stopEditing() {
            for (const inputData of this.inputsData) {
                inputData.new = inputData.actual
            }
            this.isEditing = false
        }
    }
}
</script>

<style>

</style>>
