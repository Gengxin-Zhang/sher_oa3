<template></template>

<script>
import { mapState, mapGetters, mapActions, mapMutations } from "vuex";
export default {
  mounted() {
    this.setPageName("设置")
  },
  methods:{
      ...mapMutations(["setPageName"])
  }
};
</script>

<style lang="scss" scoped>
</style>