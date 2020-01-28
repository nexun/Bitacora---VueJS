<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
    
}
</script>

<style>
html, body, #app {
    height: 100%;
}

body {
    background-color: #fdfdfd!important;
}

.dg-btn,
.btn-custom-light,
.btn-custom-light:hover,
.btn-custom-light:focus {
    text-shadow: none;
    background-color: #fff;
    border: .1rem solid #333;
    color: #333;
}

.dg-btn:hover,
.btn-custom-light:hover,
.btn-custom-light:focus {
    text-shadow: none;
    background-color: #333;
    border: .1rem solid #333;
    color: #fff;
}

.dg-btn:not(:disabled):not(.disabled):active,
.btn-custom-light:not(:disabled):not(.disabled).active,
.btn-custom-light:not(:disabled):not(.disabled):active,
.show>.btn-custom-light.dropdown-toggle {
    text-shadow: none;
    background-color: #69262c;
    border: .1rem solid #69262c;
    color: #fff;
}

.btn-custom-dark,
.btn-custom-dark:hover,
.btn-custom-dark:focus {
    text-shadow: none;
    background-color: #333;
    border: .1rem solid #fff;
    color: #fff;
}

.btn-custom-dark:hover,
.btn-custom-dark:focus {
    text-shadow: none;
    background-color: #fff;
    border: .1rem solid #fff;
    color: #333;
}

.btn-custom-dark:not(:disabled):not(.disabled).active,
.btn-custom-dark:not(:disabled):not(.disabled):active,
.show>.btn-custom-dark.dropdown-toggle {
    text-shadow: none;
    background-color: #69262c;
    border: .1rem solid #69262c;
    color: #fff;
}

.btn-custom-light.focus, .btn-custom-light:focus,
.btn-custom-dark.focus, .btn-custom-dark:focus {
    outline: 0;
    box-shadow: 0 0 0 0.2rem #73363b;
}

.btn-custom-light:disabled,
.btn-custom-dark:disabled {
    background-color: #333;
    color: #fff;
    border: .1rem solid #333;
}

.v-enter-active {
    display: none;
}

.form-control,
.mx-input {
    border: none;
    border-bottom: 1px solid #93989c;
    -webkit-box-shadow: none;
    box-shadow: none;
    border-radius: 0;
}

.form-control:focus,
.mx-input:focus {
    border-color: #69262c;
    border-bottom: 4px solid #69262c;
    -webkit-box-shadow: none;
    box-shadow: none;
}

.mx-datepicker.is-invalid {
    border: none;
    border-bottom: 1px solid #dc3545;
}

.form-group {
    position: relative;
    margin-bottom: 1.5rem;
}

.form-placeholder {
  position: absolute;
  top: 0;
  padding: 7px 0 0 13px;
  transition: all 200ms;
  opacity: 0.75;
}

.form-control:focus + .form-placeholder,
.form-control:not(:placeholder-shown) + .form-placeholder {
  font-size: 75%;
  transform: translate3d(0, -100%, 0);
  opacity: 1;
}

.form-control.is-invalid:focus, .was-validated .form-control:invalid:focus {
    -webkit-box-shadow: none;
    box-shadow: none;
}

.form-group + .form-group {
    margin-top: 2rem;
}

.dg-content {
    text-align: center;
}

.invalid-tooltip {
    position: inherit;
}

.form-control.is-invalid~.invalid-tooltip {
    display: inline-block;
}
</style>
