<template>
  <div>
    <!-- dev test!! -->

    <h3>升华OA</h3>
    <div>
      <button
        :disabled="onDuty"
        @click="signBtnHdl"
      >签到</button>
      <button
        @click="logoutBtnHdl"
      >登出</button>
      <button
        @click="mySignsBtnHdl"
      >列出我的签到</button>
      <button
        @click="exportBtnHdl"
      >导出全部签到</button>
    </div>
    <router-link to="/duty">签到页面</router-link>

    <!-- dev test!! -->
  </div>
</template>

<script>
  import { mapActions, mapState } from 'vuex'

  export default {
    name: 'SherOA',
    data() {
      return {

      }
    },
    computed: {
      ...mapState({
        onDuty: 'user/onDuty'
      })
    },
    methods: {
      ...mapActions({
        signin: 'user/signin',
        logout: 'user/logout',
        mySigns: 'user/mySigns',
        exportSigns: 'user/exportSigns'
      }),

      signBtnHdl() {
        if (this.onDuty) {
          this.$message.warn('正在值班中！')
          return
        }

        this.signin()
          .then((res) => {
            this.$message.success('签到成功')
          })
          .catch((err) => {
            this.$message.error(`${err}`.replace(/Error: /g, ''))
          })
      },
      logoutBtnHdl() {
        this.logout()
          .then((res) => {
            this.$message.success('登录已退出')
          })
          .catch((err) => {
            this.$message.error(`${err}`.replace(/Error: /g, ''))
          })
      },
      mySignsBtnHdl() {
        this.mySigns()
          .then((res) => {
            console.log('我的签到列出')
          })
          .catch((err) => {
            this.$message.error(`${err}`.replace(/Error: /g, ''))
          })
      },
      exportBtnHdl() {
        this.exportSigns()
          .then((res) => {
            this.$message.success('导出签到成功')
          })
          .catch((err) => {
            this.$message.error(`${err}`.replace(/Error: /g, ''))
          })
      }
    }
  }
</script>

<style lang="scss" scoped>

</style>
