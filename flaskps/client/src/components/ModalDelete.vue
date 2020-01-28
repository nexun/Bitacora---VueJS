<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">{{title}}</h5>
            </div>

            <div class="modal-body">
              <p v-if="!submit">
                ¿Esta seguro que quiere eliminar el {{type}}
                <strong>{{selected}}</strong> ?
              </p>
              <transition name="slide-fade">
                <div
                  v-if="submit"
                  class="position-relative d-block"
                  v-bind:class="[ hasError ? 'invalid-tooltip' : 'valid-tooltip']"
                >{{message}}</div>
              </transition>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" @click="$emit('close')">{{cancel}}</button>
              <button
                v-if="!submit"
                v-on:click="method"
                @click="submit=true,cancel='Salir'"
                type="button"
                class="btn btn-primary"
              >Si</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: "ModalDelete",
  props: ["title", "selected", "method", "type","message","hasError"],
  data() {
    return {
      submit:false,
      cancel: "No",
    };
  },
};
</script>

<style scoped>
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
  transition: all 0.8s ease;
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