<template>
  <div class="SigninContainer">
    <div class="SigninBox">
        <div class="SigninBox__Head">
            <div class="logo">OIKii<span>beta</span></div>
        </div>
        <div class="SigninBox__Body">
            <div class="inputBox">
                <span>用户名</span>
                <input type="text" v-model="name">
            </div>
            <div class="inputBox">
                <span>密码</span>
                <input type="password" v-model="password">
            </div>
            
        </div>
        <div class="SigninBox__Foot">
            <button class="button" @click="signin">登入</button>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: "",
      password: ""
    };
  },
  created(){
    this.$store.dispatch("signout");
  },
  methods: {
    signin() {
      // this.$axios.
      this.$axios.post(this.GLOBAL.API_URL+"/auth/signin",{name: this.name, password:this.password}).then(res=>{
        if (res.data.status === true){
          this.$store.dispatch("signin", res.data.data.userData)
          this.$router.push({name:"home"})
        }else{
          this.$message.warning(res.data.msg)
        }
      })
    }
  }
};
</script>

<style lang="scss" scoped>
.SigninContainer {
  width: 100vw;
  height: 100vh;
  padding: 5rem 1rem;
  background-color: #fff;
  .SigninBox {
      width: 25rem;
      height: auto;
      max-width: 100%;
      padding:2rem 1rem;
      margin: 0 auto;
      background: rgba(255,255,255,1);
      backdrop-filter: bulr(3px);
      box-shadow: 0 2px 15px rgba(0,0,0,0.1);
      border-radius: .3rem;
      .SigninBox__Head{
          .logo{
              font-size: 2.5rem;
              font-weight: bolder;
              color: #444;
              position: relative;
              span{
                  position: absolute;
                  font-size: 1rem; 
                  color: #fff;
                  bottom: 1rem;
                  background: #81A1C1aa;
                  border-radius: 1rem;
                  padding: 0 .5rem;
              }
          }
      }
      .SigninBox__Body{
          padding: 1rem;
          text-align: left;
          .inputBox{
              position: relative;
              margin-bottom: 1rem;
              &:nth-last-child(1){
                  margin-bottom: 0;
              }
              span{
                display: block;
                font-size: .9rem;
                line-height: 1.4rem;
                color: #888;
                margin-left: .5rem;
              }
              input{
                  width: 100%;
                  border: none;
                  outline: none;
                  border-radius: 1.5rem;
                  padding: .5rem 1rem;
                  font-size: 1rem;
                  line-height: 1.5rem;
                  font-weight: 500;
                  border: 1px #f0f0f0 solid;
              }
          }
      }
      .SigninBox__Foot{
          margin: 1rem;
          .button{
              width: 100%;
              background: #4C566Acc;
              border-radius: 5rem;
              padding: .5rem;
              font-size: 1rem;
              line-height: 2rem;
              font-weight: bolder;
              color: #fff;
              text-align: center;
              outline: none;
            //   margin: .5rem;
          }
      }
  }
}
</style>