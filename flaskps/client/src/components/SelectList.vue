<template>
  <div>
    <h5 class="card-title">{{title}}</h5>

    <div v-if="load" class="d-flex justify-content-center m-5">
      <div class="spinner-border" role="status">
        <span class="sr-only">Loading...</span>
      </div>
    </div>

    <select v-else class="custom-select mb-3" size="10" v-model="selected">
      <option v-for="item in list" :key="item.id" :value="item.id">{{item.name}}</option>
    </select>
  </div>
</template>

<script>
export default {
  name: "SelectList",
  props: ["title", "list", "load"],
  data() {
    return {
      selected: ""
    };
  },
  watch: {
    selected(newValue) {
      this.$emit("selected",newValue);
    }
  }
};
</script>