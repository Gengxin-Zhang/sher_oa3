<template></template>

<script>
import { mapState, mapGetters, mapActions, mapMutations } from "vuex";
export default {
  mounted() {
    this.setPageName("快速查找")
  },
  methods:{
      ...mapMutations(["setPageName"])
  }
};
</script>

<style lang="scss" scoped>
</style>