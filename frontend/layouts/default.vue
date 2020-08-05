<template>
  <div>
    <Nuxt />
  </div>
</template>

<script>
  import { mapMutations } from 'vuex'

  export default {
    data() {
      return {

      }
    },
    mounted() {
      const logined = localStorage.getItem('logined') || false
      this.setLogined(logined)

      if (logined) {
        const token = localStorage.getItem('token') || undefined
        if (token === undefined) {
          this.$message.error('请先登录')
          this.$router.push('auth/login')
        }
        else if (!this.$api.auth.validateToken(token)) {
          this.$message.error('登录信息过期，请重新登录')
          this.$router.push('auth/login')
        }
        else {
          this.$router.push('/')
        }
      }
      else {
        this.$router.push('/auth/login')
      }
    },
    methods: {
      ...mapMutations({
        setLogined: 'user/setLogined',
        setToken: 'user/setToken'
      })
    }
  }
</script>

<style>

</style>
