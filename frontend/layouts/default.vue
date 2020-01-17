<template>
  <div :class="['Main', status.theme]">
    <div :class="['SideBar', status.sidebar.open?'open':'close']">
      <sidebar />
    </div>
    <div :class="['MainColumn', status.sidebar.open?'min':'max']">
      <navbar />
      <div class="MainContainer">
        <nuxt />
      </div>
    </div>
  </div>
</template>
<script>
import Sidebar from "@/components/Sidebar";
import Navbar from "@/components/Navbar";
import { mapState, mapGetters, mapActions, mapMutations } from "vuex";
export default {
  middleware: "auth",
  components: {
    Sidebar,
    Navbar
  },
  data() {
    return {
      isWindowWidthUnder600: false
    };
  },
  computed: {
    status() {
      return this.$store.state.status;
    }
  },
  mounted() {
    console.log("升华OA");
    let authToken = localStorage.getItem("token");
    if (!authToken) {
      this.$router.push("/auth/signin");
      return;
    }
    this.loadStatus();
    this.validToken(authToken)
      .then(res => {})
      .catch(err => {
        this.$message.error("身份验证失败，请重新登入:" + err);
        this.$router.push("/auth/signin");
      })
      .finally();

    this.isWindowWidthUnder600 = window.innerWidth <= 600;
    window.onresize = this.handleWindowResize;
  },
  methods: {
    ...mapActions(["closeSidebar", "openSidebar", "loadStatus"]),
    ...mapActions({ validToken: "User/validToken" }),
    handleWindowResize(e) {
      if (e.target.innerWidth <= 600 && !this.isWindowWidthUnder600) {
        this.closeSidebar();
        this.isWindowWidthUnder600 = true;
      } else if (e.target.innerWidth > 600 && this.isWindowWidthUnder600) {
        this.openSidebar();
        this.isWindowWidthUnder600 = false;
      }
    }
  }
};
</script>
<style lang="scss">
$sidebar-width: 15rem;
html,
body {
  font-family: "Source Sans Pro", -apple-system, BlinkMacSystemFont, "Segoe UI",
    Roboto, "Helvetica Neue", Arial, sans-serif;
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  height: 100%;
  width: 100%;
}

*,
*:before,
*:after {
  box-sizing: border-box;
  margin: 0;
}
.Main {
  width: 100%;
  height: 100%;
  position: relative;
  overflow-x: hidden;
  overflow-y: auto;
  background-color: #fff;
  &.dark {
    background-color: #292a2d;
  }
  .SideBar {
    height: 100vh;
    width: $sidebar-width;
    position: fixed;
    z-index: 100;
    transition: all 0.3s;
    &.close {
      margin-left: 0 - $sidebar-width;
    }
    &.open {
      margin-left: 0;
    }
  }
  .MainColumn {
    width: 100%;
    height: 100%;
    position: relative;
    transition: all 0.3s;
    .MainContainer {
      padding: 4.5rem 10% 5rem 10%;
      min-height: 100vh;
      position: relative;

      box-sizing: border-box;
    }
    &.min {
      padding-left: $sidebar-width;
    }
    &.max {
      padding-left: 0;
    }
  }
}
@media screen and(max-width: 600px) {
  .Main {
    .MainColumn {
      .MainContainer {
        padding: 4.5rem 1rem 1rem 1rem;
      }
      &.min {
        width: 100%;
        padding-left: 0;
        margin-left: $sidebar-width;
      }
    }
  }
}
</style>
