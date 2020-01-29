<template>
<div class="login-container">
  <div class='card shadow w-auto py-5 px-4'>
      <form class='form-signin' @submit.prevent="submit">
          <h1 class="h2 mb-4 font-weight-normal text-center">Acceso Bitacora 2.0</h1>
          <div class="form-group mt-1">
            <input autocomplete='off' type="email" name='inputEmail' id="inputEmail" class="form-control"
              placeholder=" " required autofocus v-model="form.inputEmail">
            <label for="inputEmail" class="form-placeholder">Email</label>
          </div>
          <div class="form-group mt-0">
            <input type="password" name='inputPassword' id="inputPassword" class="form-control" placeholder=" " required v-model="form.inputPassword">
            <label for="inputPassword" class="form-placeholder">Contraseña</label>
          </div>
          <span style="color:red" class="d-none" :class="{ 'd-block' : form.invalid }">Los datos ingresados son incorrectos</span>
          <div class="checkbox mb-3">
            <label>
              <input type="checkbox" value="remember-me"> Recordar contraseña
            </label>
          </div>
          <button :disabled="isProcessing" type="submit" class="btn btn-lg btn-custom-light btn-block">
              <span v-if="!isProcessing" >Ingresar</span>
              <span v-if="isProcessing" class="spinner-border" role="status"></span>
          </button>
      </form>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import { mapActions} from 'vuex'

export default {
    name: 'Login',
    data() {
      return {
        form: {
          inputEmail: null,
          inputPassword: null,
          invalid: false
        },
        isProcessing: false,
      }
    },
    methods: {
      ...mapActions(['newUser']),
      submit: async function() {
        this.isProcessing = true
        this.form.invalid = false

        const formData = new FormData()
        formData.append('inputEmail', this.form.inputEmail)
        formData.append('inputPassword', this.form.inputPassword)

        try {
          await this.newUser(formData)
          this.$router.push('/')
        } catch (error) {
          if (error.response.status == 400) {
            this.form.invalid = true
          }
        }

        this.isProcessing = false
      }
    }
}
</script>

<style scoped>
.login-container {
  width: 100%;
  height: 100%;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  padding-top: 40px;
  padding-bottom: 40px;
  background-color: white;
  background-image: url("../assets/img/background.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: bottom;
  justify-content: center;
}

.card {
  border-radius: 2em;
}

.form-group {
  width: 90%;
}

.form-signin {
  max-width: 500px;
  padding: 15px;
  margin: 0 auto;
  display: flex;
  flex-direction: column; 
  align-items: center; 
  justify-content: center;
}

.form-signin .checkbox {
  font-weight: 400;
}

.form-signin .form-control {
  position: relative;
  box-sizing: border-box;
  height: auto;
  padding: 10px;
  font-size: 16px;
}

.form-signin .form-control:focus {
  z-index: 2;
}

.form-signin input[type="email"] {
  width: 100%;
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.form-signin input[type="password"] {
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
</style>