<template></template>

<script>
import { mapState, mapGetters, mapActions, mapMutations } from "vuex";
export default {
  mounted() {
    this.setPageName("应用工具")
  },
  methods:{
      ...mapMutations(["setPageName"])
  }
};
</script>

<style lang="scss" scoped>
</style>