<template>
  <div class="Header">
    <div class="Container">
      <router-link to="/" class="nav-list logo">OIKii</router-link>
      <div class="nav-list nav-right" v-if="signStatus">
        <a>你好，{{$store.getters.getUserInfo.name}}</a>
        <router-link to="/signin">退出</router-link>
      </div>
      <div class="nav-list nav-right" v-else>
        <router-link to="/signin">登入</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import {mapState} from 'vuex'
export default {
  components: {},
  data() {
    return {};
  },
  computed:{
    ...mapState({
      signStatus: state=>state.signStatus
    })
  }
};
</script>

<style lang="scss" scoped>
.Header {
    height: 3.5rem;
    width: 100vw;
    box-shadow: 0 3px 10px rgba(0,0,0,0.1);
    position: fixed;
    z-index: 999;
  .Container {
    .logo{
      border-right: 2px rgba(0,0,0,0.1) solid;
      left: 0;
      width: 5rem;
      font-size: 1.5rem;
    }
    .nav-list{
      position: absolute;
      top: 0;
      margin: .5rem 0;
      height: 2.5rem;
      text-align: center;
      line-height: 2.5rem;
      color: #333;
      font-weight: 500;
      font-size: 1.1rem;
      text-decoration: none;
      a{
        text-decoration: none;
        color: #333;
      }
    }
    .nav-right{
      right: 0;
      padding: 0 2rem;
      a{
        padding: 0 1rem;
      }
    }
  }
}
</style>