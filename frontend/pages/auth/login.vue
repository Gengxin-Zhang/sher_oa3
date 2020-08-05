<template>
  <div>
    <input
      v-model="credentials.username"
      type="text"
      placeholder="学号"
    />
    <input
      v-model="credentials.password"
      type="text"
      placeholder="密码"
    />
    <button @click="loginBtnHdl">提交</button>
  </div>
</template>

<script>
  import { mapActions } from 'vuex'

  export default {
    name: 'login',
    data() {
      return {
        credentials: {
          username: '',
          password: ''
        },
        signing: false
      }
    },
    methods: {
      ...mapActions({ login: 'user/login' }),

      loginBtnHdl() {
        if (this.signing) {
          return
        }
        this.signing = true
        this.login(this.credentials)
          .then((res) => {
            this.$message.success('test')
            this.$router.push('/')
          })
          .catch((err) => {
            this.$message.error(err)
          })
          .finally(() => {

          })
      }
    }
  }
</script>

<style lang="scss" scoped>

</style>
