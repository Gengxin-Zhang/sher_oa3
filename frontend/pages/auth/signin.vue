<template>
  <div class="SigninBox">
    <div class="head">
      <span>中南大学升华工作室</span>
    </div>
    <div class="body">
      <div class="clo">
        <input
          type="text"
          placeholder="学号"
          id="username"
          name="username"
          v-model="credentials.username"
          class="input"
        />
      </div>
      <div class="clo">
        <input
          type="password"
          placeholder="密码"
          id="password"
          name="password"
          v-model="credentials.password"
          class="input"
        />
      </div>
      <div class="clo">
        <button :class="['signin', signing?'signing':'']" @click="handleSigninButton">
          <a-icon type="loading" v-if="signing" style="margin-right:.5rem" />登入
        </button>
      </div>
    </div>
    <div class="footer">
      <span class="powerby">Build with ♥ in CSU｜ Power by Sher-Coder</span>
    </div>
  </div>
</template>

<script>
import { mapState, mapGetters, mapActions, mapMutations } from "vuex";
export default {
  name: "signin",
  data() {
    return {
      credentials: {
        username: "",
        password: ""
      },
      signing: false
    };
  },
  mounted() {},
  methods: {
    ...mapActions({ signin: "User/signin" }),

    handleSigninButton() {
      if (this.signing) {
        return;
      }
      this.signing = true;
      const hide = this.$message.loading("正在登入", 0);
      this.signin(this.credentials)
        .then(res => {
          this.$message.success("登入成功，即将跳转个人中心");
          this.$router.push("/")
        })
        .catch(err => {
          this.$message.error("登入失败:" + err);
        })
        .finally(() => {
          hide();
          setTimeout(() => {
            this.signing = false;
          }, 500);
        });
    }
  }
};
</script>

<style lang="scss" scoped>
.SigninBox {
  width: 25rem;
  max-width: 100%;
  padding: 1rem;
  background-color: #fff;
  border-radius: 0.5rem;
  margin-top: -5rem;
  box-shadow: 0 5px 20px -10px rgba(0, 0, 0, 0.3);
  .head {
    font-size: 1.5rem;
    color: #666;
    font-weight: bolder;
    text-align: center;
    margin: 0.5rem 0;
    position: relative;
  }
  .body {
    padding: 1rem 3.5rem;
    text-align: left;
    .clo {
      position: relative;
      margin-bottom: 0.7rem;
      .input {
        width: 100%;
        height: 2.5rem;
        border: 1px #d8dee9 solid;
        border-radius: 0.3rem;
        outline: none;
        padding: 0 0.5rem;
        font-weight: 500;
        color: #777;
        &::-webkit-input-placeholder {
          color: #ccc;
        }
      }
      .signin {
        background: #5e81ac;
        border: 1px #5e81ac solid;
        width: 100%;
        border-radius: 0.3rem;
        color: #fff;
        height: 2.5rem;
        font-weight: 500;
        outline: none;
        cursor: pointer;
        transition: all 0.3s;
        &.signing {
          border: 1px #7ea6d6 solid;
          background: #7ea6d6;
        }
      }
    }
  }
  .footer {
    .powerby {
      font-size: 0.8rem;
      color: #999;
    }
  }
}
</style>