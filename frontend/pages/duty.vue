<template>
  <div>
    <!-- dev test!! -->

    <h3>签到</h3>
    <div>
      <button
        :disabled="onDuty"
        @click="signBtnHdl"
      >签到</button>
    </div>
    <div>
      <input
        v-model="initSignTime"
        placeholder="签到时间"
      />
      <button
        @click="initBtnHdl"
      >提交</button>
    </div>
    <div>
      <button
        @click="allRoutineBtnHdl"
      >全部时间表</button>
      <button
        @click="myRoutineBtnHdl"
      >我的时间表</button>
    </div>
    <router-link to="/">主页</router-link>

    <!-- dev test!! -->
  </div>
</template>

<script>
  import { mapActions, mapState } from 'vuex'

  export default {
    name: 'sign',
    data() {
      return {
        initSignTime: ''
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
        initRoutine: 'user/initRoutine',
        allRoutine: 'user/allRoutine',
        myRoutine: 'user/myRoutine'
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
      initBtnHdl() {
        this.initRoutine(this.initSignTime)
          .then((res) => {
            this.$message.success('初始化值班时间成功')
          })
          .catch((err) => {
            console.log('err', err)
            this.$message.error(`${err}`.replace(/Error: /g, ''))
          })
      },
      allRoutineBtnHdl() {
        this.allRoutine()
          .then((res) => {
            console.log('时间表列出')
          })
          .catch((err) => {
            this.$message.error(`${err}`.replace(/Error: /g, ''))
          })
      },
      myRoutineBtnHdl() {
        this.myRoutine()
          .then((res) => {
            console.log('我的时间表获取成功')
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
