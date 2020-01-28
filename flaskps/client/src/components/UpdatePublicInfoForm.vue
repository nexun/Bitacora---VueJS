<template>
<form @submit.prevent="startProcessing" class="editable-form needs-validation inline-form" data-action="/configuration/updatePublicInfo" novalidate>
    <div class="form-row">
        <div class="form-group editable-form-group col">
            <label for="public_info_title_input" class="card-title h6">Titulo</label>
            <div class="input-group justify-content-middle d-flex flex-column">
                <input type="text" class="editable-input form-control w-100" :class="{ disabled: !isEditing, 'is-invalid' : !form.title.isValid }"
                    name="public_info_title_input" v-model="form.title.new" required :disabled="!isEditing">
                <div class="invalid-tooltip mr-auto">
                    Ingrese un título válido.
                </div>
            </div>
        </div>
    </div>
    <div class="form-row">
        <div class="form-group editable-form-group col">
            <label for="public_info_description_input" class="card-title h6">Descripción</label>
            <small id="passwordHelpBlock" class="form-text text-muted ml-1 d-inline-block">
                (Máximo 255 caracteres)
            </small>
            <div class="input-group justify-content-middle d-flex flex-column">
                <textarea class="editable-input form-control w-100" :class="{ disabled: !isEditing, 'is-invalid' : !form.description.isValid }"
                    name="public_info_description_input" rows="3"
                    maxlength="255" required :disabled="!isEditing" v-model="form.description.new"></textarea>
                <div class="invalid-tooltip mr-auto">
                    Ingrese una Descripción válida.
                </div>
            </div>
        </div>
    </div>
    <div class="form-row">
        <div class="form-group editable-form-group col">
            <label for="public_info_contact_email_input" class="card-title h6">Email de contacto</label>
            <div class="input-group justify-content-middle d-flex flex-column">
                <input type="email" class="editable-input form-control w-100" :class="{ disabled: !isEditing, 'is-invalid' : !form.email.isValid }"
                    name="public_info_contact_email_input" v-model="form.email.new" required :disabled="!isEditing">
                <div class="invalid-tooltip mr-auto">
                    Ingrese un email válido.
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
    name: 'UpdatePublicInfoForm',
    components: {
        EditableInputButtonGroup
    },
    data() {
        return {
            isEditing: false,
            isProcessing: false,
            form: {
                title: {
                    id: 'public_info_title_input',
                    actual: null,
                    new: null,
                    isValid: true
                },
                description: {
                    id: 'public_info_description_input',
                    actual: null,
                    new: null,
                    isValid: true
                },
                email: {
                    id: 'public_info_contact_email_input',
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
            this.form.title.new = this.form.title.actual
            this.form.description.new = this.form.description.actual
            this.form.email.new = this.form.email.actual
            for (const value of Object.values(this.form)) {
                        value.isValid = true
                    }
            this.isEditing = false
        },
        startProcessing() {
            this.isProcessing = true
            this.$emit('processing')
            
            const formData = new FormData()
            formData.append('public_info_title_input', this.form.title.new)
            formData.append('public_info_description_input', this.form.description.new)
            formData.append('public_info_contact_email_input', this.form.email.new)    

            axios.post('/configuration/updatePublicInfo', formData)
                .then(response => {
                    this.form.title.actual = this.form.title.new
                    this.form.description.actual = this.form.description.new
                    this.form.email.actual = this.form.email.new
                    this.isEditing = false
                    for (const value of Object.values(this.form)) {
                        value.isValid = true
                    }
                    this.$toast.success('Infomación pública actualizada')
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
        axios.get('/configuration/publicInfo')
            .then(response => {
                this.form.title.actual = response.data.config_options_app_title
                this.form.title.new = this.form.title.actual
                this.form.description.actual = response.data.config_options_app_description
                this.form.description.new = this.form.description.actual
                this.form.email.actual = response.data.config_options_app_contact_email
                this.form.email.new = this.form.email.actual
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
