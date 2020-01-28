<template>
  <div>
    <ViewTitleOptions title="Roles y Permisos" :options="options" />

    <div class="container-fluid">
      <div class="row">
        
        <div class="col-md-6">
          <div class="card mb-3">
            <PanelRoles :list="roles" :load="spinnerRoles" :rolesPermissions="rolesPermissions"/>
          </div>
        </div>

        <div class="col-md-6">
          <div class="card mb-3">
            <PanelPermissions :list="permissions" :load="spinnerPermissions" :rolesPermissions="rolesPermissions"/>
          </div>
        </div>

        <div class="col-md-12">
            <div class="card mb-3">
                <AssignPermissions :listRoles="roles" :loadRoles="spinnerRoles" :listRolesPermissions="rolesPermissions" :listPermissions="permissions"/>
            </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import ViewTitleOptions from "../components/ViewTitleOptions";
import PanelRoles from "../components/PanelRoles";
import PanelPermissions from "../components/PanelPermissions";
import AssignPermissions from "../components/AssignPermissions";
import axios from "axios";

export default {
  name: "Roles",
  components: {
    ViewTitleOptions,
    PanelRoles,
    PanelPermissions,
    AssignPermissions
  },
  data() {
    return {
      options: [
        {
          id: 1,
          link: "/configuracion",
          name: "Volver",
          icon: "arrow-left"
        }
      ],
      spinnerRoles: true,
      spinnerPermissions: true,
      roles: [],
      permissions: [],
      rolesPermissions: [],
    };
  },
  created() {
    let url_roles = "/configuration/showRoles";
    let url_permissions = "/configuration/showPermissions";
    let url_roles_permissions="/configuration/showRolesPermissions"
    axios
      .get(url_roles)
      .then(response => {
        this.roles = response.data;
        this.spinnerRoles = false;
      })
      .catch(e => {});
    axios
      .get(url_permissions)
      .then(response => {
        this.permissions = response.data;
        this.spinnerPermissions = false;
      })
      .catch(e => {});
    axios
      .get(url_roles_permissions)
      .then(response => {
        this.rolesPermissions = response.data;
      })
      .catch(e => {});
  }
};
</script>

<style scoped>
/* Enter and leave animations can use different */

/* durations and timing functions.              */

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

.fade-enter-active {
  transition: all 0.5s ease;
}

.fade-leave-active {
  transition: all 0s cubic-bezier(1, 0.5, 0.8, 1);
}

.fade-enter, .fade-leave-to
/* .slide-fade-leave-active below version 2.1.8 */

 {
  transform: translateX(10px);
  opacity: 0;
}
</style>