<template>
  <div class="card-body shadow">
    <SelectList
      title="Lista de Permisos"
      :list="list"
      :load="load"
      @selected="selectedId = $event"
    />

    <div class="text-left">
      <button v-on:click="open_create()" class="btn btn-sm btn-secondary mr-1">
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

    <ModalFormPermissions
      :fields="fields[0]"
      action="Crear"
      title="Crear Permiso"
      :method="this.create"
      v-if="showModalCreate"
      selectedName=""
      selectedCode=""
      @close="showModalCreate = false"
      @name="name = $event"
      @code="code=$event"
      :message="messageModal"
      :showMessage="messageModalShow"
      :hasError="error"
      :submitStatus="status"
    />

    <!-- Edit -->

    <ModalFormPermissions
      :fields="fields[1]"
      action="Guardar Cambios"
      :title="this.getTitle('Editar Permiso',this.selectedName)"
      :method="this.edit"
      v-if="showModalEdit"
      @close="showModalEdit = false"
      :selectedName="selectedName"
      :selectedCode="selectedCode"
      @name="name = $event"
      @code="code=$event"
      :message="messageModal"
      :showMessage="messageModalShow"
      :hasError="error"
      :submitStatus="status"
    />

    <!-- Delete -->

    <ModalDelete
      :title="this.getTitle('Eliminar Permiso',this.selectedName)"
      :selected="selectedName"
      :method="this.delete_select"
      type="permiso"
      :message="messageModal"
      :hasError="error"
      v-if="showModalDelete"
      @close="showModalDelete = false"
    />
  </div>
</template>

<script>
import { PlusIcon,EditIcon,Trash2Icon} from 'vue-feather-icons'
import axios from "axios";
import SelectList from "../components/SelectList";
import ModalFormPermissions from "../components/ModalFormPermissions";
import ModalDelete from "../components/ModalDelete";
export default {
  name: "PanelPermissions",
  props: ["list", "load", "rolesPermissions"],
  components: {
    ModalFormPermissions,
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
      // selectedName: "",
      // selectedCode: "",
      name: "",
      code: "",
      showModalCreate: false,
      showModalEdit: false,
      showModalDelete: false,
      status: false,
      fields: [
        [
          {
            id: 4,
            label: "Ingrese el nombre del nuevo permiso",
          },
          {
            id: 3,
            label: "Ingrese el codigo asociado al nuevo permiso",
          }
        ],
        [
          {
            id: 6,
            label: "Modificar el nombre del permiso",
          },
          {
            id: 5,
            label: "Modificar el codigo del permiso",
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
    },
    open_edit: function() {
      if (this.selectedName == "") {
        this.messagePanel = "Debe seleccionar un permiso para editar";
        this.showPanel = true;
      } else {
        this.showPanel = false;
        this.messageModalShow = false;
        this.showModalEdit = true;
        this.name=this.selectedName;
        this.code=this.selectedCode;
      }
    },
    open_delete: function() {
      if (this.selectedName == "") {
        this.messagePanel = "Debe seleccionar el permiso a eliminar";
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
      const url = "/configuration/createPermission";
      const formData = new FormData();
      formData.append("name_permission", this.name);
      formData.append("code_permission", this.code);
      axios
        .post(url, formData)
        .then(response => {
          this.correct("El permiso " + this.name + " fue creado exitosamente");
          this.list.push({
            name:this.name,
            code:this.code,
            id:response.data
          });
          // this.selectedCode = this.code;
          // this.selectedName = this.name;
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
      const url = "/configuration/updatePermission";
      const formData = new FormData();
      formData.append("name_permission", this.name);
      formData.append("code_permission", this.code);
      formData.append("selected_code", this.selectedCode);
      formData.append("selected", this.selectedName);
      axios
        .post(url, formData)
        .then(response => {
          this.correct("El permiso " + this.selectedName + " fue modificado");
          let index = this.list.findIndex(elem => elem.id === this.selectedId);
          let update={
            id:this.selectedId,
            name: this.name,
            code:this.code
          }
          this.list.splice(index, 1, update);
          //if code changed
          if (this.name != this.selectedName) {
            let update_content={
              id:this.selectedId,
              name:this.name,
            }
            for (const key in this.rolesPermissions) {
              if (this.rolesPermissions.hasOwnProperty(key)) {
                const element = this.rolesPermissions[key];
                index = element.findIndex(elem => elem.id === this.selectedId);
                if(index > -1){
                  element.splice(index, 1, update_content);
                }
              }
            }
          }
          // this.selectedName = this.name;
          // this.selectedCode = this.code;
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
      const url = "/configuration/deletePermission";
      const formData = new FormData();
      formData.append("selected", this.selectedCode);
      axios
        .post(url, formData)
        .then(response => {
          this.correct(
            "El permiso " + this.selectedName + " fue eliminado exitosamente"
          );
          let index = this.list.findIndex(elem => elem.id === this.selectedId);
          this.list.splice(index,1);
          for (const key in this.rolesPermissions) {
            if (this.rolesPermissions.hasOwnProperty(key)) {
              const element = this.rolesPermissions[key];
              index = element.findIndex(elem => elem.id === this.selectedId);
              if (index > -1) {
                element.splice(index, 1);
              }
            }
          }
          // this.selected=""
          // this.selectedCode=""
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
    getName(){
      let index = this.list.findIndex(elem => elem.id === this.selectedId);
      if(index > -1){
        return this.list[index].name
      }
      else{
        return ""
      }
    },
    getCode(){
      let index = this.list.findIndex(elem => elem.id === this.selectedId);
      if(index > -1){
        return this.list[index].code
      }
      else{
        return ""
      }
    }
  },
  computed:{
    selectedName:function(){
      return this.getName()
    },
    selectedCode:function(){
      return this.getCode()
    }
  },
  watch: {
    name() {
      this.messageModalShow = false;
    },
    code() {
      this.messageModalShow = false;
    },
    // selectedId(){
    //   this.selectedName=this.getName()
    //   this.selectedCode=this.getCode()
    // }
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
</style>