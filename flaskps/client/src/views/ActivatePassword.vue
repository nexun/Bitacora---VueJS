<template>
<div class="activate-container">
    <div class="card shadow  py-5 px-5"> 
        <div v-if="isValid" >   
          <div v-if="isActive" >
              <form @submit="checkForm" class="form-change-password pass-validation">
                  <div class="text-center"> <img :src="logo" class="img-fluid" /> </div>  

                  <h1 class="h3 mb-3 font-weight-normal text-center"></h1> 
                  <h1 class="h3 mb-3 font-weight-normal text-center">Crear contraseña</h1>
                  <label for="inputPassword"  class="sr-only ">Contraseña</label>
                  <input type="password" v-model="inputPassword"  name='inputPassword' id="inputPassword" class="form-control" placeholder="Contraseña"  autofocus>
                  <label for="inputPassword" class="sr-only">Reingrese la contraseña</label>
                  <input type="password" v-model="inputPassword2"   name='inputPassword2' id="inputPassword2" class="form-control" placeholder="Reingrese contraseña"  autofocus>
                  
                  <button class="btn btn-lg btn-outline-info btn-block" type="submit"  >Crear</button>
                              
                  <div class="" v-cloak>
                      <div v-if="errors.length">
                          <div v-if="errors.length" class="alert alert-danger" role="alert">
                          
                          <b>Por favor corrija el/los siguiente/s error/es:</b>
                          <ul>
                          <li :key="error" v-for="error in errors"> {{ error }} </li>
                          </ul>
                          
                          </div>
                      </div>
                  </div>
              </form>
          </div>
          <div v-else>
          
              <div v-if="!itsDone">    
                <div class="text-center"> <img :src="uploading" class="img-fluid" /> </div>  
                <br>
                <br>
                <h1 class="h3 mb-3 font-weight-normal text-center">Activando su cuenta</h1>

              </div>
              <div v-else> 
                <div class="text-center"> <img :src="success" class="img-fluid" /> </div>  

                <br>
                <br>
                <h1 class="h3 mb-3 font-weight-normal text-center">¡Su cuenta ha sido activada correctamente!</h1>
                <br>
                <br>
                <!-- <input type="button" class="btn btn-lg btn-outline-info btn-block" onclick="location.href='/login';" value="Ir a Login" /> -->
                <router-link class="btn btn-lg btn-outline-info btn-block" to="/login">Ir a Login</router-link>

              </div>  

        </div>
        </div>
    </div> 
</div>

</template>

<script>
import axios from 'axios'

export default {
    name: 'ActivatePassword',
    data() {
        return{
            ntoken: this.$route.query.hash,
            nid: this.$route.query.id,
            ok:null,
            isValid:false,
            inputPassword: null,
            inputPassword2: null,
            errors: [],
            error: null,      
            logo: "/static/img/logo_alt.png",
            uploading: "/static/img/upload.gif",
            success: "/static/img/upload2.gif",
            isActive:true,
            itsDone:false
        }      
    },
    methods: {
      change:function () {
        this.logo = this.uploading
      },
      checkForm: function (e) {            
            this.errors = [];

            if (!this.inputPassword ) {
                this.errors.push('Debe ingresar una clave');                  
            }else{
              if (this.inputPassword.length < 8) {
                this.errors.push('Debe contener como minimo 8 caracteres');
              }
            }            
            if (!this.inputPassword2) {
                this.errors.push('Debe volver a ingresar la clave');
            }            
            
            if (this.inputPassword && this.inputPassword && (this.inputPassword != this.inputPassword2 )) {
                
                this.errors.push('Las claves no coinciden');                         
                
            }
            
            if (!this.errors.length) {
              this.isActive = false       
              this.submit()
            }
            
            e.preventDefault();        
        },        
        submit: async function() {            
            var password = this.inputPassword
            var action = '/user/activate'
            var formData = new FormData();
            formData.append("id", this.nid);
            formData.append("token", this.ntoken);
            formData.append("password", password);

            var promesa = new Promise(function(resolve, reject) {
                const response = 
                  fetch(action, {
                      method: 'post',
                      body: formData})
                      .catch(e => new Response().status = 503)                    
                  if (response.status=200) {
                      resolve();
                    }
                  else {
                      reject();
                    }
                    
              });        
            promesa
            .then(()=>setTimeout(()=>{ this.itsDone = true; }, 2500))
            .catch(e => console.error("Critical failure: " + e.message))
        }
    },
    created() {
            
            const formData = new FormData()
            formData.append('id', this.nid)    
            formData.append('hash', this.ntoken)  

            axios.post('/check', formData)
                .then(response => {               
                    if (response.data.valid == 'False'){
                      const options = {
                      title: 'Esta página no existe',
                      description: 'La pagina a la que desea acceder no existe.',
                      noBacktrack: true
                      }
                    this.$router.push({ name: 'feedback', params: options })
                    } else{
                      this.isValid = true
                    }                  
                })
                .catch(error => {                 
                    const options = {
                      title: 'Esta página no existe',
                      description: 'La pagina a la que desea acceder no existe.',
                      noBacktrack: true
                    }
                    this.$router.push({ name: 'feedback', params: options })
                })
                
    }    
}
</script>

<style scoped>
.hasError label {
  color: red;
}

.activate-container {
  width: 100%;
  height: 100%;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  padding-top: 40px;
  padding-bottom: 40px;
  background-color: white;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: bottom;
  justify-content: center;
  background-image: url("../assets/img/orquesta.jpg");
}

div {
  width: 100%;
}

.card {
  width: 440px;
  min-height: 550px;
  border-radius: 2em;
}

.form-change-password {
  max-width: 500px;
  padding: 15px;
  margin: 0 auto;
  display: flex;
  flex-direction: column; 
  align-items: center; 
  justify-content: center;
}

.form-change-password .checkbox {
  font-weight: 400;
}

.form-change-password .form-control {
  position: relative;
  box-sizing: border-box;
  height: auto;
  padding: 10px;
  font-size: 16px;
}

.form-change-password .form-control:focus {
  z-index: 2;
}

.form-change-password input[type="email"] {
  width: 100%;
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.form-change-password input[type="password"] {
  width: 100%;
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}

.image {
  width: 100px;
}

.form-check {
  padding-bottom: 5px;
}

.preloader {
  width: 70px;
  height: 70px;
  border: 10px solid #eee;
  border-top: 10px solid #666;
  border-radius: 50%;
  animation-name: girar;
  animation-duration: 2s;
  animation-iteration-count: infinite;
  animation-timing-function: linear;
}

@keyframes girar {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
</style>