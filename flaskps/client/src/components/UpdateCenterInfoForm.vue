<template>
<form @submit.prevent="startProcessing" class="editable-form needs-validation inline-form" id="center_info_form"  novalidate> <!-- action-->
    <div class="form-row">
        <div class="form-group editable-form-group col">
            <label for="name_input" class="card-title h6">Nombre</label>
            <div class="input-group justify-content-middle d-flex flex-column">                        
                <input type="text" class="editable-input form-control w-100 disabled" name="name_input" id="name_input"
                    :class="{ disabled: !isEditing, 'is-invalid' : !form.name.isValid }" v-model="form.name.new" :disabled="!isEditing">
                <div class="invalid-tooltip mr-auto">
                    Ingrese un nombre válido.
                </div>
            </div>
        </div>
    </div>    
    <div class="form-row">
        <div class="form-group editable-form-group col">
            <label for="phone_input" class="card-title h6">Telefono:</label>
            <div class="input-group justify-content-middle d-flex flex-column">                        
                <input type="text" class="editable-input form-control w-100 disabled" name="phone_input" id="phone_input"
                    :class="{ disabled: !isEditing, 'is-invalid' : !form.phone.isValid }" v-model="form.phone.new" :disabled="!isEditing">
                <div class="invalid-tooltip mr-auto">
                    Ingrese un telefono válido.
                </div>
            </div>
        </div>
    </div>   
    <div class="form-row">
        <div class="form-group editable-form-group col">
            <label for="address_input" class="card-title h6">Direccion:</label>
            <div class="input-group justify-content-middle d-flex flex-column">                        
                <input type="text" class="editable-input form-control w-100 disabled" name="address_input" id="address_input"
                    :class="{ disabled: !isEditing, 'is-invalid' : !form.address.isValid }" v-model="form.address.new" :disabled="!isEditing">
                <div class="invalid-tooltip mr-auto">
                    Ingrese una direccion válida.
                </div>
            </div>
        </div>
    </div>    
    <div class="form-row">
        <div class="form-group editable-form-group col">
            <label for="latitud_input" class="card-title h6">Latitud:</label>
            <div class="input-group justify-content-middle d-flex flex-column">                        
                <input type="text" class="editable-input form-control w-100 disabled" name="latitud_input" id="latitud_input"
                    :class="{ disabled: !isEditing, 'is-invalid' : !form.latitud.isValid }" v-model="form.latitud.new" :disabled="!isEditing">
                <div class="invalid-tooltip mr-auto">
                    Ingrese una latitud válida.
                </div>
            </div>
        </div>
    </div>  
    <div class="form-row">
        <div class="form-group editable-form-group col">
            <label for="longitud_input" class="card-title h6">Longitud:</label>
            <div class="input-group justify-content-middle d-flex flex-column">                        
                <input type="text" class="editable-input form-control w-100 disabled" name="longitud_input" id="longitud_input"
                    :class="{ disabled: !isEditing, 'is-invalid' : !form.longitud.isValid }" v-model="form.longitud.new" :disabled="!isEditing">
                <div class="invalid-tooltip mr-auto">longitud
                    Ingrese una longitud válida.
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
    name: 'UpdateCenterInfoForm',
    components: {
        EditableInputButtonGroup,
        
    },
    data() {       
        return {
            isEditing: false,
            isProcessing: false,
            
            form: {
                name: {
                    id: 'name',
                    new: null,
                    isValid: true
                },
                address: {
                    id: 'address',
                    new: null,
                    isValid: true
                },
                phone: {
                    id: 'phone',
                    new: null,
                    isValid: true
                }, 
                latitud: {
                    id: 'latitud',
                    new: null,
                    isValid: true
                }, 
                longitud: {
                    id: 'longitud',
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
            this.form.name.new = this.form.name.actual           
            this.form.phone.new = this.form.phone.actual
            this.form.address.new = this.form.address.actual         
            this.form.latitud.new = this.form.latitud.actual            
            this.form.longitud.new = this.form.longitud.actual            
            this.isEditing = false
        },
        startProcessing() {
            this.isProcessing = true
            this.$emit('processing')
            
            const formData = new FormData()
            formData.append('name', this.form.name.new)
            formData.append('phone', this.form.phone.new)
            formData.append('address', this.form.address.new)
            formData.append('lat', this.form.latitud.new)
            formData.append('lng', this.form.longitud.new)

            

            axios.put('/center/' + this.$route.params.id, formData)
                .then(response => {
                    this.form.name.actual = this.form.name.new                    
                    this.form.address.actual = this.form.address.new
                    this.form.phone.actual = this.form.phone.new
                    this.form.latitud.actual = this.form.latitud.new
                    this.form.longitud.actual = this.form.longitud.new

                    this.isEditing = false
                    
                    for (const value of Object.values(this.form)) {
                        value.isValid = true
                    }
                    this.$toast.success('actualizado', 'Núcleo')
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
        axios.get('/center/' + this.$route.params.id)
            .then(response => {
                this.form.name.actual = response.data.center_data_name
                this.form.name.new = this.form.name.actual               
                this.form.address.actual = response.data.center_data_address
                this.form.address.new = this.form.address.actual                
                this.form.phone.actual = response.data.center_data_phone
                this.form.phone.new = this.form.phone.actual 
                this.form.latitud.actual = response.data.latitude
                this.form.latitud.new = this.form.latitud.actual  
                this.form.longitud.actual = response.data.longitude
                this.form.longitud.new = this.form.longitud.actual                
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

.invalid-tooltip {
    position: inherit;
}

.custom-control-input:checked~.custom-control-label::before {
    border-color: #73363b;
    background-color: #69262c;
}
</style>
