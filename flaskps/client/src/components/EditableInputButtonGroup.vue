<template>
<div class="editable-input-button-group">
    <button v-if="!isEditing" @click="$emit('start-editing')" type="button" class="btn btn-custom-light">Editar</button>
    <div v-if="isEditing" class="btn-group" role="group">
        <button :disabled="isProcessing" type="submit" class="btn btn-custom-light">
            <span v-if="!isProcessing" >Guardar</span>
            <span v-if="isProcessing" class="spinner-border spinner-border-sm" role="status"></span>
        </button>
        <button @click="$emit('stop-editing')" :disabled="isProcessing" type="button" class="btn btn-custom-light">
            <span>Cancelar</span>
        </button>
    </div>
</div>
</template>

<script>
export default {
    name: 'EditableInputButtonGroup',
    props: [
        'isEditing',
        'isProcessing'
    ]
}
</script>

<style scoped>

</style>
