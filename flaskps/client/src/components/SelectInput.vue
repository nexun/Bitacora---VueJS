<template>
  <div class="form-group">
    <label :for="id">{{title}}</label>
    <select @change="update" v-model="selected" :id="id" class="form-control" :disabled="!otherSelected">
      <option v-for="item in list" :key="item.id" :value="item.id">{{ item.name | capitalize }}</option>
    </select>
  </div>
</template>

<script>
export default {
  name: "SelectInput",
  props: ["title", "list", "id", "otherSelected"],
  data() {
    return {
      selected: "",
      show:true,
    };
  },
  methods:{
    update(){
      this.$emit("show",false)
      this.$emit("selected", this.selected);
    }
  }
};
</script>