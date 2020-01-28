<template>
<form @submit.prevent="startProcessing" class="editable-form needs-validation inline-form" id="user_info_form" data-action="/user/updateUserInfo" novalidate> <!-- action-->
    <div class="row p-0 ">
        <div  :class="[ $vssWidth > 768  ? 'col' : 'col-sm-6 col-md-4']">
            <div class="form-row">
                <div class="form-group editable-form-group col">
                    <vue-dropzone
                    v-if="isEditing"
                    ref="user_dropzone"
                    id="photo"
                    :options="dropzoneOptions"
                    :useCustomSlot="true"
                    @vdropzone-success="correctPhoto"
                    @vdropzone-error="errorPhoto"
                    @vdropzone-removed-file="removePhoto"
                    >
                        <div class="dropzone-custom-content">
                            <h3 class="dropzone-custom-title">Seleccione o arrastre una foto del instrumento</h3>
                            <div class="subtitle">Archivos aceptados: .png, .jpg y .jpeg</div>
                        </div>
                    </vue-dropzone>
                    <div v-if="!form.photo.isValid" class="invalid-tooltip d-block mt-3">
                        {{form.photo.message}}
                    </div>
                    <div id="preview" class="profile-userpic" v-if="!isEditing">
                        <img v-if="form.photo.name == null && photoAdd" src="../assets/img/user.jpg" id="img" class="img-responsive" > 
                        <img v-if="url" :src="url" id="img" class="img-responsive"  />
                    </div>
                </div>
            </div>

        </div>
        <div class="col-sm-6 col-md-8">
             <div class="form-row">
                <div class="form-group editable-form-group col">
                    <label for="first_name_input" class="card-title h6">Nombre</label>
                    <div class="input-group justify-content-middle d-flex flex-column">                        
                        <input type="text" class="editable-input form-control w-100 disabled" name="first_name_input" id="first_name_input"
                            :class="{ disabled: !isEditing, 'is-invalid' : !form.first_name.isValid }" v-model="form.first_name.new" :disabled="!isEditing">
                        <div class="invalid-tooltip mr-auto">
                            Ingrese un nombre válido.
                        </div>
                    </div>
                </div>
            </div>
            <div class="form-row">
                    <div class="form-group editable-form-group col">
                        <label for="last_name_input" class="card-title h6">Apellido</label>
                        <div class="input-group justify-content-middle d-flex flex-column">
                            
                            <input type="text" class="editable-input form-control w-100 disabled"
                                name="last_name_input" id="last_name_input"
                                :class="{ disabled: !isEditing, 'is-invalid' : !form.last_name.isValid }" v-model="form.last_name.new"  :disabled="!isEditing">

                            <div class="invalid-tooltip mr-auto">
                                Ingrese un apellido válido.
                            </div>
                        </div>
                    </div>
            </div>
            <div class="form-row">
                <div class="form-group editable-form-group col">
                    <label for="email_input" class="card-title h6">Email</label>
                    <div class="input-group justify-content-middle d-flex flex-column">
                        <input type="email" class="editable-input form-control w-100 disabled"
                            name="email_input" id="email_input"
                            :class="{ disabled: !isEditing, 'is-invalid' : !form.email.isValid }" v-model="form.email.new" :disabled="!isEditing">
                        <div class="invalid-tooltip mr-auto">
                            Ingrese un email válido.
                        </div>
                    </div>
                </div>
            </div>
            <div class="form-row">
                    <div class="form-group editable-form-group col">
                        <label for="password_input" class="card-title h6">Password</label>
                        <div class="input-group justify-content-middle d-flex flex-column">
                            <input type="password" class="editable-input form-control w-100 disabled"
                                name="password_input" id="password_input"
                                value="password" :class="{ disabled: !isEditing, 'is-invalid' : !form.password.isValid }" v-model="form.password.new" :disabled="!isEditing">
                            <div class="invalid-tooltip mr-auto">
                                Ingrese un password válido.
                            </div>
                        </div>
                    </div>
             </div>
        </div>

    </div>
    
   
        <EditableInputButtonGroup 
            @start-editing="startEditing" 
            @stop-editing="stopEditing" 
            @start-processing="startProcessing" 
            :isEditing="isEditing" 
            :isProcessing="isProcessing" />
        
    </form>
</template>

<script>
import axios from 'axios'
import EditableInputButtonGroup from './EditableInputButtonGroup'
import { required, maxLength } from "vuelidate/lib/validators";
import vue2Dropzone from "vue2-dropzone";
import "vue2-dropzone/dist/vue2Dropzone.min.css";
import VueScreenSize from 'vue-screen-size'

export default {
    name: 'UpdateUserInfoForm',
    components: {
        EditableInputButtonGroup,
        vueDropzone: vue2Dropzone
    },
    mixins: [VueScreenSize.VueScreenSizeMixin],  
    data() {
        return {
            link: process.env.VUE_APP_URL,
            photoAdd:true,
            dropzoneOptions: {
                url: "https://httpbin.org/post",
                thumbnailWidth: 180,
                thumbnailHeight: 250,
                maxFilesize: 2,
                acceptedFiles: ".png,.jpg,.jpeg",
                addRemoveLinks: true,
                dictRemoveFile: "Eliminar imagen",
                dictFileTooBig:
                "El tamaño del archivo es muy grande ({{filesize}} MB). La capacidad maxima es de 2MB",
                dictInvalidFileType:
                "El tipo de archivo seleccionado es incorrecto. Asegurese de seleccionar una imagen .png, .jpg, .jpeg",
                accept: function(file, done) {
                var ext = file.name.split(".")[1]; // get extension from file name
                if (ext == "png" || ext == "jpg" || ext == "jpeg") {
                    var files = this.getAcceptedFiles();
                    if (files.length > 0) {
                    this.removeFile(files[0]);
                    }
                    done();
                }
                }
            },
            isEditing: false,
            isProcessing: false,
            url:null,
            form: {
                first_name: {
                    id: 'first_name_input',
                    actual: null,
                    new: null,
                    isValid: true
                },
                last_name: {
                    id: 'last_name_input',
                    actual: null,
                    new: null,
                    isValid: true
                },
                email: {
                    id: 'email_input',
                    actual: null,
                    new: null,
                    isValid: true
                }, 
                password: {
                    id: 'password_input',
                    actual: null,
                    new: null,
                    isValid: true
                },
                photo: {
                    id: "photo",
                    name: "",
                    new: null,
                    isValid: true,
                    message: ""
                    }   
            }  
            
        }
    },
    methods: {
        startEditing() {
            this.isEditing = true
        },
        stopEditing() {
            this.form.first_name.new = this.form.first_name.actual
            this.form.last_name.new = this.form.last_name.actual
            this.form.email.new = this.form.email.actual,
            this.form.photo.new = null,
            this.form.photo.isValid=true,
            this.$refs.user_dropzone.removeAllFiles()  
            for (const value of Object.values(this.form)) {
                        value.isValid = true
                    }
            this.isEditing = false          
        },
        startProcessing() {
            this.isProcessing = true
            this.$emit('processing')            
            const formData = new FormData()
            formData.append('first_name_input', this.form.first_name.new)
            formData.append('last_name_input', this.form.last_name.new)
            formData.append('email_input', this.form.email.new)    
            formData.append('password_input', this.form.password.new)  
            if (this.form.photo.new) {
                formData.append("photo", this.form.photo.new);
                formData.append("photo_size", this.form.photo.new.size);
            }
            axios.put('/user/' + this.$route.params.id, formData)
                .then(response => {
                    this.form.first_name.actual = this.form.first_name.new
                    this.form.last_name.actual = this.form.last_name.new
                    this.form.email.actual = this.form.email.new
                    this.form.password.actual = this.form.password.new
                    if(this.form.photo.new){
                        this.url = URL.createObjectURL(this.form.photo.new);
                        this.photoAdd = false;

                    }
                    this.form.photo.new = null;
                    this.isEditing = false
                    this.$refs.user_dropzone.removeAllFiles();
                    for (const value of Object.values(this.form)) {
                        value.isValid = true
                    }
                    this.$toast.success('actualizado', 'Usuario')
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
        },
        correctPhoto(file) {
            this.form.photo.new = file;
            this.form.photo.isValid = true;
        },
        errorPhoto(file, msg) {
            this.$refs.user_dropzone.removeFile(file);
            this.form.photo.isValid = false;
            this.form.photo.message = msg;
        },
        removePhoto(file) {
            if (this.form.photo.new) {
                if (file.name == this.form.photo.new.name) {
                this.form.photo.new = null;
                }
            }
        }
    },
    
    created() {
        axios.get('/user/'+this.$route.params.id)
            .then(response => {
                this.form.first_name.actual = response.data.user_data_first_name
                this.form.first_name.new = this.form.first_name.actual
                this.form.last_name.actual = response.data.user_data_last_name
                this.form.last_name.new = this.form.last_name.actual
                this.form.email.actual = response.data.user_data_email
                this.form.email.new = this.form.email.actual
                this.form.password.actual = "password"
                this.form.password.new = this.form.password.actual
                this.form.photo.name = response.data.photo;
                if (this.form.photo.name) {
                    this.url =
                        this.link +
                        this.form.photo.name;
                    }


                            
            })
            .catch(error => { this.$emit(console.log('sadd')) })
    }    
}
</script>

<style scoped>

#img {
    width: 150px!important;
    border-style: outset;
    padding: 10px;
}
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
