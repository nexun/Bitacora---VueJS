<template>
<div>
    <ViewTitleOptions title="Nuevo Nucleo" :options=options />
    <div class="card shadow col-lg-8 p-0">
        <div class="card-body">
            <form @submit.prevent="submit" class="needs-validation" novalidate>

                <!-- NOMBRE -->
                <div class="form-group" :class="{ 'form-group--error': $v.form.name.value.$error }">
                    <input type="text" class="form-control" id="name" name="name" placeholder=" " v-model.trim="$v.form.name.value.$model" :class="{ 'is-invalid': $v.form.name.value.$error | !form.name.isValid }">
                    <label class="form-placeholder" for="name">Nombre</label>
                    <div class="invalid-tooltip">Ingrese un nombre válido</div>
                </div>               

                <!-- TELEFONO -->
                <div class="form-group" :class="{ 'form-group--error': $v.form.phone.value.$error }">

                    <input type="text" class="form-control" id="phone" name="phone" placeholder=" " v-model.trim="$v.form.phone.value.$model" :class="{ 'is-invalid': $v.form.phone.value.$error | !form.phone.isValid }">
                    <label class="form-placeholder" for="phone">Teléfono</label>
                    <div class="invalid-tooltip">Ingrese un teléfono válido</div>
                </div>
               
                <!-- DIRECCION -->
                <div class="form-group" :class="{ 'form-group--error': $v.form.address.value.$error }">
                    <input type="text" class="form-control" id="address" name="address" placeholder=" " v-model.trim="$v.form.address.value.$model" :class="{ 'is-invalid': $v.form.address.value.$error | !form.address.isValid }">
                    <label class="form-placeholder" for="address">Dirección</label>
                    <div class="invalid-tooltip">Ingrese una direccion válida</div>
                </div>               
                
                <!-- SELECT DE BARRIOS -->
                <div class="form-group" :class="{ 'form-group--error': $v.form.neighborhood.value.$error }">
                    <select class="form-control" v-model.trim="$v.form.neighborhood.value.$model" :class="{ 'is-invalid': $v.form.neighborhood.value.$error | !form.neighborhood.isValid }">
                        <option hidden disabled :value=null >Seleccione un barrio</option>
                        <option v-for=" neighborhood in neighborhoods" :key="neighborhood.id" :value="neighborhood.name">
                        {{ neighborhood.name }}
                        </option>
                    </select>
                    <label class="form-placeholder" for="address">Barrio</label>
                    <div class="invalid-tooltip">Seleccione un barrio</div>
                </div>  

                <button :disabled="isProcessing" type="submit" class="btn btn-custom-light">
                    <span v-if="!isProcessing" >Aceptar</span>
                    <span v-if="isProcessing" class="spinner-border spinner-border-sm" role="status"></span>
                </button>
                <button @click="cancel" :disabled="isProcessing" type="button" class="btn btn-custom-light ml-2">
                    <span>Cancelar</span>
                </button>
            </form>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios'
import ViewTitleOptions from '../components/ViewTitleOptions'
import { required, minLength } from 'vuelidate/lib/validators'

export default {
    name: 'NewCenter',
    components: {
        ViewTitleOptions
    },
    data() {       
        axios.get('/neighborhood')
                .then(response => {
                    this.neighborhoods = response.data
        })
        return {            
            options: [
                {
                    id: 1,
                    link: '/nucleo',
                    name: 'Volver',
                    icon: 'arrow-left'
                }
            ],
            neighborhoods: [
                {
                    id: null,                    
                    name: null,
                    
                }
            ],
            isProcessing: false,
            form: {
                name: {
                    id: 'name',
                    value: null,
                    isValid: true
                },
                address: {
                    id: 'address',
                    value: null,
                    isValid: true
                },
                neighborhood: {
                    id: 'neighborhood',
                    value: null,
                    isValid: true
                },
                phone: {
                    id: 'phone',
                    value: null,
                    isValid: true
                }                
            }
        }            
    },
    validations(){     
        return {
            form: {
                name: {
                    value: {
                        required
                    }
                },                
                address: {
                    value: {
                        required
                    }
                },
                phone: {
                    value: {
                        required
                    }
                },
                neighborhood: {
                    value: {
                        required
                    }
                },
            }
        }
        
    },   
 
    methods: {
        submit() {
            this.$v.$touch()
            if (this.$v.$invalid) return
            
            this.isProcessing = true
            
            const formData = new FormData()
            formData.append('name', this.form.name.value)            
            formData.append('address', this.form.address.value)            
            formData.append('phone', this.form.phone.value)                   
            formData.append('city', this.form.neighborhood.value)           


            axios.post('/center/new', formData)
                .then(response => {
                    for (const value of Object.values(this.form)) {
                        value.isValid = true
                    }
                    this.$router.push('/nucleo')
                })
                .catch(error => {
                    if (error.response.status == 400) {
                        for (const value of Object.values(this.form)) {
                            if (error.response.data.includes(value.id))
                                value.isValid = false
                        }
                    }
                    if (error.response.status == 501) {
                        const options = {
                            title: 'Nucleo ya existe',
                            description: 'El nombre de nucleo que proporcionaste ya se encuentra en el sistema.'
                        }
                        this.$router.push({ name: 'feedback', params: options })
                    }
                })
                .finally(() => {
                    this.isProcessing = false
                })

        },
        cancel() {
            this.form.name.value = null            
            this.form.address.value = null
            this.form.phone.value = null
            this.form.neighborhood.value = null
                      
            this.$v.$reset()
        },
        
        
},
 
}
</script>

<style scoped>
.invalid-tooltip {
    position: inherit;
}
</style>
<style scoped>
.card {
    margin-top: 10px;
    margin-bottom: 10px;
}