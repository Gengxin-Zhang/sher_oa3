<template>
  <div>
    <!-- dev test!! -->

    <h3>登录</h3>
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

    <!-- dev test!! -->
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
    mounted() {

    },
    methods: {
      ...mapActions({ login: 'user/login' }),

      loginBtnHdl() {
        if (this.signing) {
          this.$message.warn('登录中')
          return
        }
        this.signing = true
        this.login(this.credentials)
          .then((res) => {
            this.$message.success('登录成功')
            this.$router.push('/')
          })
          .catch((err) => {
            this.$message.error(`${err}`)
          })
          .finally(() => {
            this.signing = false
            this.credentials.password = ''
          })
      }
    },
    head() {
      return {
        title: '登录 - 升华OA'
      }
    }
  }
</script>

<style lang="scss" scoped>

</style>
