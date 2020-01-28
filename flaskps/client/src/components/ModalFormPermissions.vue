<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">{{title}}</h5>
            </div>

            <div class="modal-body p-0">
              <form @submit.prevent="submit" novalidate>
                <div
                  :class="{ 'p-3 m-0':!showMessage, 'py-2 px-3 m-0':showMessage}"
                  class="form-group"
                >
                  <label :for="fields[0].id">{{fields[0].label}}</label>
                  <input
                    v-model.trim="$v.name.$model"
                    :id="fields[0].id"
                    type="text"
                    class="form-control"
                    :class="{'is-invalid':$v.name.$error,'is-valid':!$v.name.$invalid}"
                    placeholder="Nombre del permiso"
                  />

                  <div class="invalid-tooltip">
                    <div class="error" v-if="!$v.name.required">{{errors[0]}}</div>
                    <div class="error" v-if="!$v.name.minLength">{{errors[1]}}</div>
                    <div class="error" v-if="!$v.name.regexName">{{errors[2]}}</div>
                    <div class="error" v-if="!$v.name.maxLength">{{errors[3]}}</div>
                  </div>
                </div>

                <div
                  :class="{ 'pb-3 px-3 m-0':!showMessage, 'py-2 px-3 m-0':showMessage}"
                  class="form-group"
                >
                  <label :for="fields[1].id">{{fields[1].label}}</label>
                  <input
                    v-model.trim="$v.code.$model"
                    :id="fields[1].id"
                    type="text"
                    class="form-control"
                    :class="{'is-invalid':$v.code.$error,'is-valid':!$v.code.$invalid}"
                    placeholder="Codigo del permiso"
                  />

                  <div class="invalid-tooltip">
                    <div class="error" v-if="!$v.code.required">{{errors[4]}}</div>
                    <div class="error" v-if="!$v.code.minLength">{{errors[5]}}</div>
                    <div class="error" v-if="!$v.code.regexCode">{{errors[6]}}</div>
                    <div class="error" v-if="!$v.code.maxLength">{{errors[7]}}</div>
                  </div>
                </div>

                <transition name="slide-fade">
                  <div
                    v-if="showMessage"
                    class="position-relative mb-3 mx-3 d-block mb-3"
                    :class="{ 'invalid-tooltip':hasError, 'valid-tooltip':!hasError}"
                  >{{message}}</div>
                </transition>

                <div class="modal-footer">
                  <button type="button" class="btn btn-secondary" @click="$emit('close')">Cancelar</button>
                  <button v-if="submitStatus" type="buttton" class="btn btn-primary">
                    <div class="spinner-border spinner-border-sm" role="status">
                      <span class="sr-only">Loading...</span>
                    </div>
                  </button>
                  <button
                    v-else
                    type="submit"
                    :disabled="$v.name.$error || $v.code.$error || (name==selectedName && code==selectedCode) || showMessage"
                    class="btn btn-primary"
                  >{{action}}</button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import { required, minLength, maxLength, helpers } from "vuelidate/lib/validators";
const regexName = helpers.regex('regex', /^[A-Za-z\s]*$/)
const regexCode = helpers.regex('regex', /^[A-Za-z_]*$/)
export default {
  name: "ModalFormPermissions",
  props: [
    "title",
    "fields",
    "action",
    "method",
    "selectedName",
    "selectedCode",
    "message",
    "showMessage",
    "hasError",
    "submitStatus"
  ],
  data() {
    return {
      name: this.selectedName,
      code: this.selectedCode,
      errors: [
        "Debe completar el nombre del permiso",
        "El nombre del permiso debe tener como minimo 4 caracteres",
        "El nombre del permiso no debe contener numeros ni caracteres especiales",
        "El nombre del permiso debe tener como máximo 20 caracteres",
        "Debe completar el codigo del permiso",
        "El codigo debe tener como minimo 4 caracteres",
        "El codigo no debe contener numeros, espacios ni caracteres especiales (a excepcion del '_')",
        "El codigo debe tener como máximo 20 caracteres"
      ]
    };
  },
  validations: {
    name: {
      required,
      minLength: minLength(4),
      maxLength: maxLength(20),
      regexName
    },
    code: {
      required,
      minLength: minLength(4),
      maxLength: maxLength(20),
      regexCode
    }
  },
  methods: {
    submit() {
      this.$v.$touch();
      this.method();
    }
  },
  watch: {
    name(newValue) {
      this.$emit("name", newValue);
    },
    code(newValue) {
      this.$emit("code", newValue);
    }
  }
};
</script>

<style scoped>
.valid-message {
  color: white;
  background-color: rgb(166, 214, 93);
  height: 2em;
  border-radius: 0.5em;
}

.invalid-message {
  color: white;
  background-color: rgb(247, 90, 90);
  height: 2em;
  border-radius: 0.5em;
}

.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-content,
.modal-leave-active .modal-content {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}

.slide-fade-enter-active {
  transition: all 0.5s ease;
}

.slide-fade-leave-active {
  transition: all 0.5s /*cubic-bezier(1.0, 0.5, 0.8, 1.0)*/ ease;
}

.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active below version 2.1.8 */

 {
  transform: translateX(10px);
  opacity: 0;
}
</style>