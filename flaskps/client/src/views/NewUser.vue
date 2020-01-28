<template>
<div>
    <ViewTitleOptions title="Agregar usuario" :options=options />
    <div class="card shadow col-lg-8 p-0">
        <div class="card-body">
            <form @submit.prevent="submit" class="needs-validation" novalidate>
                <div class="form-group" :class="{ 'form-group--error': $v.form.first.value.$error }">
                    <input type="text" class="form-control" id="first_name" name="first_name" placeholder=" " v-model.trim="$v.form.first.value.$model" :class="{ 'is-invalid': $v.form.first.value.$error | !form.first.isValid }">
                    <label class="form-placeholder" for="first_name">Nombre</label>
                    <div class="invalid-tooltip">Ingrese un nombre válido</div>
                </div>
                <div class="form-group" :class="{ 'form-group--error': $v.form.last.value.$error }">
                    <input type="text" class="form-control" id="last_name" name="last_name" placeholder=" " v-model.trim="$v.form.last.value.$model" :class="{ 'is-invalid': $v.form.last.value.$error | !form.last.isValid }">
                    <label class="form-placeholder" for="last_name">Apellido</label>
                    <div class="invalid-tooltip">Ingrese un apellido válido</div>
                </div>
                <div class="form-group" :class="{ 'form-group--error': $v.form.email.value.$error }">
                    <input type="email" class="form-control" id="email" name="email" placeholder=" " v-model.trim="$v.form.email.value.$model" :class="{ 'is-invalid': $v.form.email.value.$error | !form.email.isValid }">
                    <label class="form-placeholder" for="email">Email</label>
                    <div class="invalid-tooltip">Ingrese un email válido</div>
                </div>
                
                <fieldset class="form-group" :class="{ 'form-group--error': $v.form.roles.value.$error }">
                    <div class="row">
                        <legend class="col-form-label col-sm-2 pt-0">Roles:</legend>
                        <div class="col-sm-10">
                             
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" name="roles"  id="admin_option"
                                        value="administrator" v-model.trim="$v.form.roles.value.$model">
                                    <label class="form-check-label" for="admin_option">
                                        Administrador
                                    </label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" name="roles"  id="preceptor_option"
                                        value="preceptor" v-model.trim="$v.form.roles.value.$model">
                                    <label class="form-check-label" for="preceptor_option">
                                        Preceptor
                                    </label>
                                </div>
                              
                                <div class="form-check disabled">
                                    <input class="form-check-input" type="checkbox" name="roles" id="teacher_option"
                                        value="teacher" v-model.trim="$v.form.roles.value.$model" @change="isTeacher = !isTeacher">
                                    <label class="form-check-label" for="teacher_option">
                                        Docente
                                    </label>
                                </div>
                            
                            <div class="invalid-tooltip roles-invalid-tooltip" :class="{ 'd-block': $v.form.roles.value.$error | !form.roles.isValid }">Seleccione al menos un rol</div>
                        </div>
                    </div>
                </fieldset>
                <div v-if="isTeacher">
                    <div class="form-group" :class="{ 'form-group--error': $v.form.birth.value.$error }">
                        <input type="date" class="form-control" id="birth" name="birth" placeholder=" " v-model.trim="$v.form.birth.value.$model" :class="{ 'is-invalid': $v.form.birth.value.$error | !form.birth.isValid }">
                        <label class="form-placeholder" for="birth">Fecha de nacimiento</label>
                        <div class="invalid-tooltip">Ingrese una fecha de nacimiento válida</div>
                    </div>
                    <div class="form-group" :class="{ 'form-group--error': $v.form.address.value.$error }">
                        <input type="text" class="form-control" id="address" name="address" placeholder=" " v-model.trim="$v.form.address.value.$model" :class="{ 'is-invalid': $v.form.address.value.$error | !form.address.isValid }">
                        <label class="form-placeholder" for="address">Dirección</label>
                        <div class="invalid-tooltip">Ingrese una direccion válida</div>
                    </div>
                    <div class="form-group" :class="{ 'form-group--error': $v.form.city.value.$error }">
                        <select class="form-control" v-model.trim="$v.form.city.value.$model" :class="{ 'is-invalid': $v.form.city.value.$error | !form.city.isValid }">
                        <option hidden disabled :value="null">Seleccione una localidad</option>
                        <option v-for=" city in citys" :key="city.id" :value="city.id">
                        {{ city.nombre }}
                        </option>
                    </select>
                        <label class="form-placeholder" for="city">Ciudad</label>
                        <div class="invalid-tooltip">Ingrese una ciudad válida</div>
                    </div>
                    <div class="form-group" :class="{ 'form-group--error': $v.form.dnitype.value.$error }">
                        <select class="form-control" v-model.trim="$v.form.dnitype.value.$model" :class="{ 'is-invalid': $v.form.dnitype.value.$error | !form.dnitype.isValid }">
                            <option hidden disabled :value="null" >Seleccione un tipo de documento</option>
                            <option v-for=" dnitype in dnitypes" :key="dnitype.id" :value="dnitype.id">
                            {{ dnitype.nombre }}
                            </option>
                        </select>
                        <label class="form-placeholder" for="dnitype">Tipo de documento</label>                   
                        <div class="invalid-tooltip">Seleccione un tipo de documento</div>

                    </div> 
                    <div class="form-group" :class="{ 'form-group--error': $v.form.dni.value.$error }">
                        <input type="text" class="form-control" id="dni" name="dni" placeholder=" " v-model.trim="$v.form.dni.value.$model" :class="{ 'is-invalid': $v.form.dni.value.$error | !form.dni.isValid }">
                        <label class="form-placeholder" for="dni">Número de documento</label>
                        <div class="invalid-tooltip">Ingrese un documento válido</div>
                    </div>
                    <div class="form-group" :class="{ 'form-group--error': $v.form.phone.value.$error }">
                        <input type="text" class="form-control" id="phone" name="phone" placeholder=" " v-model.trim="$v.form.phone.value.$model" :class="{ 'is-invalid': $v.form.phone.value.$error | !form.phone.isValid }">
                        <label class="form-placeholder" for="phone">Teléfono</label>
                        <div class="invalid-tooltip">Ingrese un teléfono válido</div>
                    </div>
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
import { required, minLength, email } from 'vuelidate/lib/validators'
import DatePicker from 'vue2-datepicker';
import 'vue2-datepicker/index.css';

export default {
    name: 'NewUser',
    components: {
        ViewTitleOptions,
        DatePicker
    },
    data() {
        axios.get('https://api-referencias.proyecto2019.linti.unlp.edu.ar/tipo-documento')
                .then(response => {
                    this.dnitypes = response.data
        })
        axios.get('https://api-referencias.proyecto2019.linti.unlp.edu.ar/localidad')
                .then(response => {
                    this.citys = response.data
        })
        return {
            options: [
                {
                    id: 1,
                    link: '/usuario',
                    name: 'Volver',
                    icon: 'arrow-left'
                }
            ],
            citys: [
                {
                    id: null,                    
                    name: null,
                    
                }
            ],
            dnitypes: [
                {
                    id: null,                    
                    name: null,
                    
                }
            ],
            isProcessing: false,
            isTeacher:false,            
            form: {
                first: {
                    id: 'first_name',
                    value: null,
                    isValid: true
                },
                last: {
                    id: 'last_name',
                    value: null,
                    isValid: true
                },
                email: {
                    id: 'email',
                    value: null,
                    isValid: true
                },
                roles: {
                    id: 'roles',
                    value: [],
                    isValid: true
                },
                city: {
                    id: 'city',
                    value: null,
                    isValid: true
                },
                address: {
                    id: 'address',
                    value: null,
                    isValid: true
                },
                dnitype: {
                    id: 'dnitype',
                    value: null,
                    isValid: true
                },
                dni: {
                    id: 'dni',
                    value: null,
                    isValid: true
                },
                birth: {
                    id: 'birth',
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
    if (!this.isTeacher) {
      return { 
            form: {
                    first: {
                        value: {
                            required
                        }
                    },
                    last: {
                        value: {
                            required
                        }
                    },
                    email: {
                        value: {
                            required,
                            email
                        }
                    },
                    roles: {
                        value: {
                            required,
                            minLength: minLength(1),
                        }
                    }            
                }
            }
    } else {
            return {
                form: {
                    first: {
                        value: {
                            required
                        }
                    },
                    last: {
                        value: {
                            required
                        }
                    },
                    email: {
                        value: {
                            required,
                            email
                        }
                    },
                    roles: {
                        value: {
                            required,
                            minLength: minLength(1),
                        }
                    },
                    address: {
                        value: {
                            required
                        }
                    },
                    birth: {
                        value: {
                            required
                        }
                    },
                    city: {
                        value: {
                            required
                        }
                    },
                    dnitype: {
                        value: {
                            required
                        }
                    },
                    dni: {
                        value: {
                            required
                        }
                    },
                    phone: {
                        value: {
                            required
                        }
                    }
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
            formData.append('first_name', this.form.first.value)
            formData.append('last_name', this.form.last.value)
            formData.append('email', this.form.email.value)
            for (let value of this.form.roles.value) {
                formData.append('roles', value)
            }
            if(this.isTeacher){
                formData.append('dni', this.form.dni.value)
                formData.append('dnitype', this.form.dnitype.value)
                formData.append('address', this.form.address.value)
                formData.append('city', this.form.city.value)
                formData.append('phone', this.form.phone.value)
                formData.append('birth', this.form.birth.value)
            }

            axios.post('/user/new', formData)
                .then(response => {
                    for (const value of Object.values(this.form)) {
                        value.isValid = true
                    }
                    this.$toast.success('creado', 'Usuario')
                    this.$router.push('/usuario')
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
                            title: 'Usuario ya existe',
                            description: 'La dirección de email que proporcionaste ya se encuentra en el sistema asociada a un usuario.'
                        }
                        this.$router.push({ name: 'feedback', params: options })
                    }
                })
                .finally(() => {
                    this.isProcessing = false
                })
        },
        cancel() {
            this.form.first.value = null
            this.form.last.value = null
            this.form.email.value = null
            this.form.roles.value = []
            this.isTeacher = false
            this.$v.$reset()
        }
    }
}
</script>

<style scoped>
.invalid-tooltip {
    position: inherit;
}
</style>