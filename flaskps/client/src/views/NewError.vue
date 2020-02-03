<template>
<div>
    <ViewTitleOptions title="Nuevo error" :options=options />
    <div class="card shadow col-lg-8 p-0">
        <div class="card-body">
            <form @submit.prevent="submit" class="needs-validation" novalidate>

                <!-- Titulo -->
                <div class="form-group" :class="{ 'form-group--error': $v.form.tittle.value.$error }">
                    <input type="text" class="form-control" id="tittle" name="tittle" placeholder=" " v-model.trim="$v.form.tittle.value.$model" :class="{ 'is-invalid': $v.form.tittle.value.$error | !form.tittle.isValid }">
                    <label class="form-placeholder" for="tittle">Titulo</label>
                    <div class="invalid-tooltip">Ingrese un titulo válido</div>
                </div>              

                <!-- SELECT DE BARRIOS -->
                <div class="form-group" :class="{ 'form-group--error': $v.form.category.value.$error }">
                    <select class="form-control" v-model.trim="$v.form.category.value.$model" :class="{ 'is-invalid': $v.form.category.value.$error | !form.category.isValid }">
                        <option hidden disabled :value=null >Seleccione una categoria</option>
                        <option v-for=" category in categories" :key="category.id" :value="category.name">
                        {{ category.name }}
                        </option>
                    </select>
                    <label class="form-placeholder" for="address">Categoria</label>
                    <div class="invalid-tooltip">Seleccione una categoria</div>
                </div>  
                
               
                <!-- Descripcion -->
                <div class="form-group" :class="{ 'form-group--error': $v.form.descripcion.value.$error }">
                    <textarea type="text" rows="10" cols="30" class="form-control" id="descripcion" name="descripcion" placeholder=" " v-model.trim="$v.form.descripcion.value.$model" :class="{ 'is-invalid': $v.form.descripcion.value.$error | !form.descripcion.isValid }">
                    </textarea>
                    <label class="form-placeholder" for="descripcion">Descripcion</label>
                    <div class="invalid-tooltip">Ingrese una descripcion válida</div>
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
        axios.get('/category')
                .then(response => {
                    this.categories = response.data
        })
        return {            
            options: [
                {
                    id: 1,
                    link: '/errores',
                    name: 'Volver',
                    icon: 'arrow-left'
                }
            ],
            categories: [
                {
                    id: null,                    
                    name: null,
                    
                }
            ],
            isProcessing: false,
            form: {
                tittle: {
                    id: 'tittle',
                    value: null,
                    isValid: true
                },
                descripcion: {
                    id: 'descripcion',
                    value: null,
                    isValid: true
                },
                category: {
                    id: 'category',
                    value: null,
                    isValid: true
                },                               
            }
        }            
    },
    validations(){     
        return {
            form: {
                tittle: {
                    value: {
                        required
                    }
                },                
                descripcion: {
                    value: {
                        required
                    }
                },                
                category: {
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
            formData.append('tittle', this.form.tittle.value)            
            formData.append('description', this.form.descripcion.value)            
            formData.append('id_category', this.form.category.value)           


            axios.post('/item/new', formData)
                .then(response => {
                    for (const value of Object.values(this.form)) {
                        value.isValid = true
                    }
                    this.$router.push('/errores')
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
                            title: 'El error ya existe',
                            description: 'El titulo de error que proporcionaste ya se encuentra en el sistema.'
                        }
                        this.$router.push({ name: 'feedback', params: options })
                    }
                })
                .finally(() => {
                    this.isProcessing = false
                })

        },
        cancel() {
            this.form.tittle.value = null            
            this.form.descripcion.value = null
            this.form.category.value = null
                      
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