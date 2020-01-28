<template>
  <div class="card-body shadow">
    <SelectList title="Lista de Roles" :list="list" :load="load" @selected="selectedId = $event" />

    <div class="text-left">
      <button type="button" v-on:click="open_create()" class="btn btn-sm btn-secondary mr-1">
        <plus-icon size="1.5x" class="custom-class"></plus-icon>
      </button>
      <button v-on:click="open_edit()" class="btn btn-sm btn-secondary mr-1">
        <edit-icon size="1.5x" class="custom-class"></edit-icon>
      </button>
      <button v-on:click="open_delete()" class="btn btn-sm btn-secondary mr-1">
        <trash-2-icon size="1.5x" class="custom-class"></trash-2-icon>
      </button>
    </div>

    <transition name="slide-fade">
      <div v-if="showPanel" class="alert alert-danger p-2 mt-3" role="alert">{{messagePanel}}</div>
    </transition>

    <!-- Create -->

    <ModalFormRoles
      :fields="fields[0]"
      action="Crear"
      title="Crear Rol"
      :method="this.create"
      v-if="showModalCreate"
      @close="showModalCreate = false"
      selected
      @name="name = $event"
      :message="messageModal"
      :showMessage="messageModalShow"
      :hasError="error"
      :submitStatus="status"
    />

    <!-- Edit -->

    <ModalFormRoles
      :fields="fields[1]"
      action="Guardar Cambios"
      :title="this.getTitle('Editar Rol',this.selectedName)"
      :method="this.edit"
      v-if="showModalEdit"
      @close="showModalEdit = false"
      :selected="this.selectedName"
      @name="name = $event"
      :message="messageModal"
      :showMessage="messageModalShow"
      :hasError="error"
      :submitStatus="status"
    />

    <!-- Delete -->

    <ModalDelete
      :title="this.getTitle('Eliminar Rol',this.selectedName)"
      :selected="this.selectedName"
      :method="this.delete_select"
      type="rol"
      :message="messageModal"
      :hasError="error"
      v-if="showModalDelete"
      @close="showModalDelete = false"
    />
  </div>
</template>

<script>
import { PlusIcon, EditIcon, Trash2Icon } from "vue-feather-icons";
import axios from "axios";
import SelectList from "../components/SelectList";
import ModalFormRoles from "../components/ModalFormRoles";
import ModalDelete from "../components/ModalDelete";

export default {
  name: "PanelRoles",
  props: ["list", "load", "rolesPermissions"],
  components: {
    ModalFormRoles,
    ModalDelete,
    SelectList,
    PlusIcon,
    EditIcon,
    Trash2Icon
  },
  data() {
    return {
      showPanel: false,
      messagePanel: "",
      messageModal: "",
      messageModalShow: false,
      error: false,
      selectedId: "",
      name: "",
      showModalCreate: false,
      showModalEdit: false,
      showModalDelete: false,
      status: false,
      fields: [
        [
          {
            id: "name_role_create",
            label: "Ingrese el nombre del nuevo rol"
          }
        ],
        [
          {
            id: 2,
            label: "Modificar el nombre del rol"
          }
        ]
      ]
    };
  },
  methods: {
    open_create: function() {
      this.messageModalShow = false;
      this.name = "";
      this.showModalCreate = true;
      // let message = {
      //   title: "Crear Rol",
      //   action: "Crear",
      //   fields: this.fields[0],
      //   method: this.create,
      //   selected:"",
      //   status:this.status
      // };
      // this.$dialog
      //   .confirm(message, {
      //     view: "sarasa",
      //     html: true,
      //     customClass: 'center-dialog',
      //   })
      //   .then(function() {
      //     console.log("Clicked on proceed");
      //   })
      //   .catch(function() {
      //     console.log("Clicked on cancel");
      //   });
    },
    open_edit: function() {
      if (this.selectedName == "") {
        this.messagePanel = "Debe seleccionar un rol para editar";
        this.showPanel = true;
      } else {
        this.showPanel = false;
        this.messageModalShow = false;
        this.showModalEdit = true;
      }
    },
    open_delete: function() {
      if (this.selectedName == "") {
        this.messagePanel = "Debe seleccionar el rol a eliminar";
        this.showPanel = true;
      } else {
        this.showPanel = false;
        this.messageModalShow = false;
        this.showModalDelete = true;
      }
    },
    create: function() {
      this.status = true;
      this.messageModalShow = false;
      const url = "/configuration/createRole";
      const formData = new FormData();
      formData.append("name_role", this.name);
      axios
        .post(url, formData)
        .then(response => {
          this.correct("El rol " + this.name + " fue creado exitosamente");
          this.list.push({
            name: this.name,
            id: response.data
          });
          this.rolesPermissions[response.data] = [];
        })
        .catch(error => {
          if (error.response.status == 400) {
            this.incorrect(error.response.data);
          }
        });
    },
    edit: function() {
      this.status = true;
      this.messageModalShow = false;
      const url = "/configuration/updateRole";
      const formData = new FormData();
      formData.append("name_role", this.name);
      formData.append("selected", this.selectedName);
      axios
        .post(url, formData)
        .then(response => {
          this.correct(
            "El rol " + this.selectedName + " fue modificado a " + this.name
          );
          let index = this.list.findIndex(elem => elem.id === this.selectedId);
          let update = {
            id: this.selectedId,
            name: this.name
          };
          this.list.splice(index, 1, update);
        })
        .catch(error => {
          if (error.response.status == 400) {
            this.incorrect(error.response.data);
          }
        });
    },
    delete_select: function() {
      this.status = true;
      this.messageModalShow = false;
      const url = "/configuration/deleteRole";
      const formData = new FormData();
      formData.append("selected", this.selectedName);
      axios
        .post(url, formData)
        .then(response => {
          this.correct(
            "El rol " + this.selectedName + " fue eliminado exitosamente"
          );
          let index = this.list.findIndex(elem => elem.id === this.selectedId);
          this.list.splice(index, 1);
          delete this.rolesPermissions[this.selectedId];
        })
        .catch(error => {
          if (error.response.status == 400) {
            this.incorrect(error.response.data);
          }
        });
    },
    getTitle(action, selected) {
      return action + ": " + selected;
    },
    correct(message) {
      this.status = false;
      this.messageModal = message;
      this.error = false;
      this.messageModalShow = true;
    },
    incorrect(message) {
      this.status = false;
      this.messageModal = message;
      this.error = true;
      this.messageModalShow = true;
    },
    getName() {
      let index = this.list.findIndex(elem => elem.id === this.selectedId);
      if (index > -1) {
        return this.list[index].name;
      } else {
        return "";
      }
    }
  },
  created() {
    this.$dialog.registerComponent("sarasa", ModalExample);
  },
  computed: {
    selectedName: function() {
      return this.getName();
    }
  },
  watch: {
    name() {
      this.messageModalShow = false;
    }
  }
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

.center-dialog{
  top:60% !important;
}

</style>