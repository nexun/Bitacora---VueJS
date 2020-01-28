<template>
  <div
    class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom" id="opt"
  >
    <div id="text">
      <h2 class="h2 d-inline">{{ title }}</h2>
    </div>      
      <div v-if="options" class="btn-toolbar mb-2 mb-md-0" id="opt">
        <div v-for="option in options" :key="option.id" >
          <button v-if="option.isButton" class="btn btn-custom-light ml-2" @click="option.method">
            <component :is="option.icon+'-icon'" size="1.5x" class="custom-class" />
            {{ option.name }}
          </button>
          <router-link v-else class="btn btn-custom-light ml-2" :to="option.link">
            <component :is="option.icon+'-icon'" size="1.5x" class="custom-class" />
            {{ option.name }}
          </router-link>
        </div>
      </div>
  </div>
</template>

<script>
import { PlusIcon } from 'vue-feather-icons'

export default {
  name: "ViewTitleOptionsMixed",
  components: {
    PlusIcon
  },
  props: ["title", "options"]
};
</script>

<style scoped>
.btn + .btn {
    margin-left: 10px;
}
@media(max-width: 768px){
    
    #opt{
        justify-content: center!important;
    }

    .btn{
            font-size: 0.9rem;
            padding-bottom: 10px;
            border:none;

    }
    #text{
        padding-right: 10px;
        display: inline-grid;
    }
}
</style>