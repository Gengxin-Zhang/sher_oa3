<template>
  <div>
    <!-- dev test!! -->

    升华OA
    <button
      :disabled="onDuty"
      @click="signBtnHdl"
    >签到</button>
    <button
      @click="logoutBtnHdl"
    >登出</button>

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
        logout: 'user/login'
      }),

      signBtnHdl() {
        if (this.onDuty) {
          return
        }

        this.signin()
          .then((res) => {
            this.$message.success('签到成功')
          })
          .catch((err) => {
            this.$message.error(`${err}`)
          })
      },
      logoutBtnHdl() {
        this.logout()
      }
    }
  }
</script>

<style lang="scss" scoped>

</style>
