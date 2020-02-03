<template>
<div>
    <ViewTitleOptions title="Categorias"  />      
    <div class="d-flex justify-content-start">

        <div class="col-lg-5 card-cat">
            <SearchableList :listName=list :columns=columns :endpoint=endpoint :options=queryOptions />
        </div>
        <div class="col-lg-7"> 
            
            <div class="card shadow col-lg-8 p-0">
                <div class="card-header">Agregar categoria</div>
                <div class="card-body">
                    <form @submit.prevent="submit" class="needs-validation" novalidate>

                        <!-- NOMBRE -->
                        <div class="form-group" :class="{ 'form-group--error': $v.form.name.value.$error }">
                            <input type="text" class="form-control" id="name" name="name" placeholder=" " v-model.trim="$v.form.name.value.$model" :class="{ 'is-invalid': $v.form.name.value.$error | !form.name.isValid }">
                            <label class="form-placeholder" for="name">Nombre</label>
                            <div class="invalid-tooltip">Ingrese un nombre válido</div>
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
    </div>
</div>    
</template>

<script>
import axios from 'axios'
import ViewTitleOptions from '../components/ViewTitleOptions'
import SearchableList from '../components/SearchableList'
import CategoryList from '../components/SearchableListHeader/CategoryList'
import { required, minLength } from 'vuelidate/lib/validators'


export default {
    name: 'category',
    components: {
        ViewTitleOptions,
        SearchableList,
       
    },
    data() {
        return {            
            list: CategoryList,
            endpoint: "/category",
            columns: ['CODIGO','NOMBRE'],
            queryOptions: {
                shouldSort: true,
                tokenize: true,
                threshold: 0.2,
                location: 0,
                distance: 100,
                maxPatternLength: 32,
                minMatchCharLength: 1,
                keys: [
                    'id',
                    'name'
                ]
            },        
           
            isProcessing: false,
            form: {
                name: {
                    id: 'name',
                    value: null,
                    isValid: true
                },   
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
                
            }
        }  
    } ,
    methods: {
        submit() {
            this.$v.$touch()
            if (this.$v.$invalid) return
            
            this.isProcessing = true
            
            const formData = new FormData()
            formData.append('name', this.form.name.value)            
            this.form.name.value = null                     
            this.$v.$reset() 


            axios.post('/category/new', formData)
                .then(response => {
                    for (const value of Object.values(this.form)) {
                        value.isValid = true
                    }
                    this.$router.go()
                    
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
                            title: 'La categoria ya existe',
                            description: 'El nombre de la categoria que proporcionaste ya se encuentra en el sistema.'
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
            this.$v.$reset()
        },
        
        
},
}
</script>
<style scoped>

</style>
