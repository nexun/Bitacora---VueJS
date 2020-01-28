<template>
<form @submit.prevent="submit" class="editable-form needs-validation inline-form" id="user_role_form" data-action="/set_user_role" novalidate> <!-- action-->
    <fieldset class="form-group" :class="{ 'form-group--error': $v.form.roles.value.$error }">
                    <div class="row">
                        <div class="col-sm-10">
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" name="roles" id="admin_option" 
                                    value="administrator" v-model.trim="$v.form.roles.value.$model" >
                                <label class="form-check-label" for="admin_option">
                                    Administrador
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" name="roles" id="preceptor_option"
                                    value="preceptor" v-model.trim="$v.form.roles.value.$model">
                                <label class="form-check-label" for="preceptor_option">
                                    Preceptor
                                </label>
                            </div>
                            <div class="form-check disabled">
                                <input class="form-check-input" type="checkbox" name="roles" id="teacher_option"
                                    value="teacher" v-model.trim="$v.form.roles.value.$model">
                                <label class="form-check-label" for="teacher_option">
                                    Docente
                                </label>
                                
                            </div>
                            <div class="invalid-tooltip roles-invalid-tooltip" :class="{ 'd-block': $v.form.roles.value.$error | !form.roles.isValid }">Seleccione al menos un rol</div>
                        </div>
                    </div>
    </fieldset>
    <button  type="submit" class="btn btn-custom-light">
                    <span >Modificar</span>
    </button>
                
    
        

        
</form>
</template>

<script>
import axios from 'axios'
import { required, minLength, email } from 'vuelidate/lib/validators'

export default {
    name: 'UpdateUserRolesForm',
    
    data() {
        return {       
        isProcessing: false,
            form: {                
                roles: {
                    id: 'roles',
                    value: [],
                    isValid: true,
                }
            }  
        }            
    },
    validations: {
        form: {
            roles: {
                value: {
                    required,
                    minLength: minLength(1),
                }
            }
        }
  },
    methods: {
        submit() {
            this.$v.$touch()
            if (this.$v.$invalid) return
            
            this.isProcessing = true
            
            const formData = new FormData()
            for (let value of this.form.roles.value) {
                formData.append('roles', value)
            }

            axios.put('/user/' + this.$route.params.id + '/roles', formData)
                .then(response => {
                    for (const value of Object.values(this.form)) {
                        value.isValid = true
                        
                    }
                    this.$toast.success('actualizados', 'Roles')
                })
                .catch(error => {
                    if (error.response.status == 400) {
                        for (const value of Object.values(this.form)) {
                            if (error.response.data.includes(value.id))
                                value.isValid = false
                        }
                        this.$toast.error('Inténtelo más tarde', 'Error')
                    }
                    
                })
                .finally(() => {
                    this.isProcessing = false
                })
        }
        
    },
    created() {
        axios.get('/user/' + this.$route.params.id + '/roles')
            .then(response => {
                this.form.roles.value = response.data
            })
            .catch(error => {})
    }
}
</script>

<style scoped>
.invalid-tooltip {
    position: inherit;
}
</style>