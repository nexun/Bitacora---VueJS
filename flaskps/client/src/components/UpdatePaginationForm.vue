<template>
<form @submit.prevent="startProcessing" class="editable-form needs-validation inline-form" data-action="/configuration/updatePagination" novalidate>
    <div class="form-row">
        <div class="form-group editable-form-group col">
            <label for="items_per_page_input" class="card-title h6">Cantidad</label>
            <div class="input-group justify-content-middle d-flex flex-column">
                <input type="number" class="editable-input form-control w-100 col-lg-3" :class="{ disabled: !isEditing, 'is-invalid' : !form.paginationNumber.isValid }"
                    name="items_per_page_input" v-model="form.paginationNumber.new" required min="1" pattern="^[0-9]+$"
                    :disabled="!isEditing">
                <div class="invalid-tooltip mr-auto">
                    Ingrese un número válido.
                </div>
            </div>
        </div>
    </div>
    <EditableInputButtonGroup @start-editing="startEditing" @stop-editing="stopEditing" @start-processing="startProcessing" :isEditing="isEditing" :isProcessing="isProcessing" />
</form>
</template>

<script>
import axios from 'axios'
import EditableInputButtonGroup from './EditableInputButtonGroup'

export default {
    name: 'UpdatePaginationForm',
    components: {
        EditableInputButtonGroup
    },
    data() {
        return {
            isEditing: false,
            isProcessing: false,
            form: {
                paginationNumber: {
                    id: 'items_per_page_input',
                    actual: null,
                    new: null,
                    isValid: true
                }
            } 
        }
    },
    methods: {
        startEditing() {
            this.isEditing = true
        },
        stopEditing() {
            this.form.paginationNumber.new = this.form.paginationNumber.actual
            for (const value of Object.values(this.form)) {
                        value.isValid = true
                    }
            this.isEditing = false
        },
        startProcessing() {
            this.isProcessing = true
            this.$emit('processing')

            const formData = new FormData()
            formData.append('items_per_page_input', this.form.paginationNumber.new)

            axios.post('/configuration/updatePagination', formData)
                .then(response => {
                    this.form.paginationNumber.actual = this.form.paginationNumber.new
                    this.isEditing = false
                    for (const value of Object.values(this.form)) {
                        value.isValid = true
                    }
                    this.$toast.success('Paginación actualizada')
                })
                .catch(error => {
                    if (error.response.status == 400) {
                        for (const value of Object.values(this.form)) {
                            if (error.response.data.includes(value.id))
                                value.isValid = false
                        }
                    } else {
                        this.isEditing = false
                        this.$toast.error('Inténtelo más tarde', 'Error')
                    }
                })
                .finally(() => {
                    this.isProcessing = false
                })
        }
    },
    created() {
        axios.get('/configuration/pagination')
            .then(response => {
                this.form.paginationNumber.actual = response.data.config_options_items_per_page
                this.form.paginationNumber.new = this.form.paginationNumber.actual
            })
            .catch(error => {})
    }    
}
</script>

<style scoped>
input.disabled {
    border: 0;
    background-color: transparent !important;
}

form.needs-validation input {
    padding-right: 36px;
}

textarea.editable-input:disabled {
    background-color: transparent;
    border: none;
}

.custom-control-input:checked~.custom-control-label::before {
    border-color: #73363b;
    background-color: #69262c;
}
</style>
