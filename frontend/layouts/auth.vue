<template>
  <div class="Auth">
    <client-only>
      <vue-particles color="#81A1C1" :particlesNumber="30" :particleSize="6" :lineLinked="false" class="particles-bg"></vue-particles>
    </client-only>
    <nuxt />
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.Auth {
  width: 100%;
  height: 100%;
  .particles-bg {
    position: absolute;
    width: 100%;
    height: 100%;
    background-repeat: no-repeat;
    background-size: cover;
    background-position: 50% 50%;
    z-index: -1;
  }
}
</style>