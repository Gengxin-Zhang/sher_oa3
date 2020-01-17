<template>
  <div class="signoutBox">
    <span>正在注销用户信息</span>
  </div>
</template>
<script>
import { mapActions } from "vuex";
export default {
  name: "signout",
  data() {
    return {};
  },
  mounted(){
    localStorage.removeItem("token");
    localStorage.removeItem("status");
    this.$router.push("/auth/signin")
  },
  methods:{
    ...mapActions({signout: "User/signout"})
  }
};
</script>
<style lang="scss" scoped>
.signoutBox{
  text-align: center;
  span{
    font-size: 1.5rem;
    color: #4C566A;
    font-weight: bolder;
    justify-items: center;
    display: inline-block;
    vertical-align: middle;
  }
}
</style>