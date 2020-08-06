<template>
  <div>
    <!-- dev test!! -->

    <h1>Dev Pad</h1>
    <h2>当前用户：&nbsp;{{ this.$store.state.user.userInfo.name }}</h2>

    <!-- dev test!! -->
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
      const logined = localStorage.getItem('logined') === 'true' || false
      this.setLogined(logined)

      if (logined) {
        const token = localStorage.getItem('token') || undefined
        if (token === undefined) {
          this.$message.error('请先登录')
          this.$router.push('/auth/login')
        }
        else if (!this.$api.auth.validateToken()) {
          this.$message.error('登录信息过期，请重新登录')
          this.$router.push('/auth/login')
        }
        else {
          console.log('token有效')
          const userInfo = JSON.parse(localStorage.getItem('userInfo'))
          this.$store.commit('user/setUserInfo', userInfo)
          this.setToken(token)
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
