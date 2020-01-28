<template>
<div class="form-row">
    <div class="form-group editable-form-group col">
        <label :for="inputData.name" class="card-title h6">{{ inputData.title }}</label>
        <div class="input-group justify-content-middle d-flex flex-column">
            <input :type="inputData.type" class="editable-input form-control w-100 col-lg-3" :class="{ disabled: !isEditing }"
                :name="inputData.name" v-model="inputData.new" required min="1" pattern="^[0-9]+$"
                :disabled="!isEditing">
            <div class="invalid-tooltip mr-auto">
                {{ inputData.tooltip }}
            </div>
        </div>
    </div>
</div>
</template>

<script>
export default {
    name: 'EditableFormInput',
    props: ['isEditing', 'inputData']
}
</script>

<style>

</style>