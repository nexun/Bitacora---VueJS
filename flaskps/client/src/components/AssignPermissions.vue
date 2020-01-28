<template>
  <div class="card-body shadow">
    <h5 class="card-title">Asignar Permisos a Rol</h5>

    <div class="container-fluid">
      <div class="row mt-4">
        <!-- Roles List -->

        <div class="col-xl-3">
          <SelectList
            title="Roles:"
            :list="listRoles"
            :load="loadRoles"
            @selected="selectedRole = $event"
          />
        </div>

        <!-- Role Permissions List -->

        <div class="col-xl-3">
          <SelectList
            :title="this.getTitle('Permisos del rol: ',this.getRoleName())"
            :list="rolePermissions"
            :load="loadRoles"
            @selected="selectedPublic = $event"
          />
        </div>

        <!-- Arrows -->

        <div class="col-xl-1 align-self-center mb-3" id="add_remove_permissions">
          <div class="text-center">
            <button class="btn btn-sm btn-secondary m-2" v-on:click="addPermission()">
              <arrow-left-icon size="1.5x" class="custom-class" />
            </button>
            <br />
            <button class="btn btn-sm btn-secondary m-2" v-on:click="removePermission()">
              <arrow-right-icon size="1.5x" class="custom-class" />
            </button>
          </div>
        </div>

        <!-- Remaining List -->

        <div class="col-xl-5">
          <SelectList
            title="Permisos:"
            :list="remaining"
            :load="loadRoles"
            @selected="selectedRemaining = $event"
          />
        </div>
      </div>
    </div>

    <!-- Options -->

    <transition name="slide-fade">
      <div v-if="options" class="text-right pr-3">
        <button v-on:click="save()" class="btn btn-secondary mr-3">Guardar</button>
        <button v-on:click="cancel()" class="btn btn-secondary">Cancelar</button>
      </div>
    </transition>

    <!-- Notifications -->

    <transition name="slide-fade">
      <div
        v-if="showPanel"
        class="alert p-2 mt-3"
        v-bind:class="[ hasError ? 'alert-danger' : 'alert-success']"
      >{{ message }}</div>
    </transition>
  </div>
</template>

<script>
import { ArrowLeftIcon, ArrowRightIcon } from "vue-feather-icons";
import SelectList from "../components/SelectList";
import axios from "axios";
export default {
  name: "AssignPermissions",
  components: {
    SelectList,
    ArrowLeftIcon,
    ArrowRightIcon
  },
  props: ["listRoles", "loadRoles", "listRolesPermissions", "listPermissions"],
  data() {
    return {
      options: false,
      showPanel: false,
      hasError: false,
      message: "",
      selectedRole: "",
      selectedRoleName:"",
      selectedPublic: "",
      selectedRemaining: "",
      rolePermissions: [],
      remaining: [],
      add: [],
      remove: []
    };
  },
  methods: {
    getTitle: function(action, selected) {
      return action + selected;
    },
    getRoleName(){
      let index = this.listRoles.findIndex(elem => elem.id === this.selectedRole);
      if(index > -1){
        return this.listRoles[index].name
      }
      else{
        return ""
      }
    },
    getRolePermissions(){
      return this.listRolesPermissions[this.selectedRole].slice();
    },
    getRemaining: function() {
      let myKeys = [];
      this.rolePermissions.forEach(element => {
        myKeys.push(element.id);
      });
      return this.listPermissions.filter(elem=> !myKeys.includes(elem.id))
    },
    addPermission: function() {
      this.showPanel = false;
      if (
        this.selectedRole != "" &&
        this.selectedRemaining != "" &&
        this.rolePermissions.findIndex(
          element => element.id === this.selectedRemaining
        ) == -1
      ) {
        if (!this.add.includes(this.selectedRemaining)) {
          if (this.remove.includes(this.selectedRemaining)) {
            this.remove = this.remove.filter(x => x != this.selectedRemaining);
          } else {
            this.add.push(this.selectedRemaining);
          }
        }
        let indexAdd = this.listPermissions.findIndex(
          element => element.id === this.selectedRemaining
        );
        let indexRemove = this.remaining.findIndex(
          element => element.id === this.selectedRemaining
        );

        // Update publics
        this.rolePermissions.push({
          id: this.selectedRemaining,
          name: this.listPermissions[indexAdd].name
        });
        //Update remaining
        this.remaining.splice(indexRemove, 1);

      } else {
        this.message =
          "Para agregar un permiso asegurese de seleccionar el rol asociado y el permiso que desea agregar";
        this.hasError = true;
        this.showPanel = true;
      }
    },
    removePermission: function() {
      this.showPanel = false;
      if (
        this.selectedRole != "" &&
        this.selectedPublic != "" &&
        this.remaining.findIndex(
          element => element.id === this.selectedPublic
        ) == -1
      ) {
        if (!this.remove.includes(this.selectedPublic)) {
          if (this.add.includes(this.selectedPublic)) {
            this.add = this.add.filter(x => x != this.selectedPublic);
          } else {
            this.remove.push(this.selectedPublic);
          }
        }
        let indexAdd = this.listPermissions.findIndex(
          element => element.id === this.selectedPublic
        );
        let indexRemove = this.rolePermissions.findIndex(
          element => element.id === this.selectedPublic
        );
        // Update publics
        this.rolePermissions.splice(indexRemove, 1);
        //Update remaining
        this.remaining.push({
          id: this.selectedPublic,
          name: this.listPermissions[indexAdd].name
        });
        
      } else {
        this.message =
          "Para eliminar un permiso asegurese de seleccionar el rol asociado y el permiso que desea eliminar";
        this.hasError = true;
        this.showPanel = true;
      }
    },
    save: function() {
      this.showPanel = false;
      this.hasError = false;
      const formData = new FormData();
      formData.append("role", this.selectedRole);
      formData.append("adds", JSON.stringify(this.add));
      formData.append("removes", JSON.stringify(this.remove));
      const url = "/configuration/assignPermissions";
      axios
        .post(url, formData)
        .then(response => {
          this.message = "Cambios realizados correctamente";
          //Update permision list
          this.changeRolesPermissions(this.add,this.remove)
          //Reset add & remove arrays
          this.add = [];
          this.remove = [];
          this.showPanel = true;
        })
        .catch(error => {
          if (error.response.status == 400) {
            this.hasError = true;
            this.message = error.response.data;
            this.showPanel = true;
          }
        });
    },
    cancel: function() {
      this.showPanel = false;
      this.add = [];
      this.remove = [];
      if (this.selectedRole != "") {
        /* Update role permissions */
        this.rolePermissions = this.getRolePermissions();
        /* Update remaining */
        this.remaining = this.getRemaining();
      }
    },
    changeRolesPermissions(adds,removes){
      let index;
      let newList;
      adds.forEach(element => {
        index = this.listPermissions.findIndex(elem => elem.id === element);
        this.listRolesPermissions[this.selectedRole].push({
          id: element,
          name: this.listPermissions[index].name,
        });
      });
      newList=this.listRolesPermissions[this.selectedRole].filter(x => !removes.includes(x.id))
      this.listRolesPermissions[this.selectedRole]=newList
    },
  },
  watch: {
    selectedRole(newValue) {
      this.showPanel = false;
      this.add = [];
      this.remove = [];
      if (this.selectedRole != "") {
        this.selectedRoleName=this.getRoleName()
       /* Update role permissions */
        this.rolePermissions = this.getRolePermissions();
        /* Update remaining */
        this.remaining = this.getRemaining();
      }
    },
    add(newVal) {
      if (newVal.length > 0 || this.remove.length > 0) {
        this.options = true;
      } else {
        this.options = false;
      }
    },
    remove(newVal, oldVal) {
      if (newVal.length > 0 || this.add.length > 0) {
        this.options = true;
      } else {
        this.options = false;
      }
    }
  },
};
</script>

<style scoped>
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