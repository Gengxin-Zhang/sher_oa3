<template>
  <div class="AuthBox">
    <nuxt-child></nuxt-child>
  </div>
</template>
<script>
export default {
  layout: "auth"
};
</script>
<style lang="scss" scoped>
.AuthBox {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}
</style>
