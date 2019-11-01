<template>
  <div id="app" class="app">
    <Header></Header>
    <div class="MainContainer" v-if="signStatus == true">
      <Sidebar></Sidebar>
      <div class="MainContent">
        <router-view />
      </div>
    </div>
    <div class="MainContainer" v-else>
      <router-view />
    </div>
  </div>
</template>

<script>
import Header from "@/components/Header";
import Sidebar from "@/components/Sidebar";
import { mapState } from "vuex";
export default {
  name: "App",
  components: {
    Header,
    Sidebar
  },
  data() {
    return {};
  },
  computed: {
    ...mapState({
      signStatus: state => state.signStatus
    })
  },
  beforeCreate() {
    let token = localStorage.getItem("token");
    // this.$store.dispatch("signin", {})
    if (!token) {
      this.$router.push("/signin");
    } else {
      this.$axios
        .get(this.GLOBAL.API_URL + "/auth/verify")
        .then(
          res => {
            this.$store.dispatch("signin", res.data.data.userData);
          },
          err => {
            localStorage.removeItem("token");
            this.$router.push("/signin");
          }
        )
        .catch(error => {
          localStorage.removeItem("token");
          this.$router.push("/signin");
        });
    }
  }
};
</script>

<style lang="scss" scoped>
.app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  min-height: 100vh;
  .MainContainer {
    height: 100vh;
    width: 100vw;
    padding-top: 3.5rem;
    position: relative;
    overflow: hidden;
    .MainContent {
      margin-left: 5rem;
      overflow-x: hidden;
      overflow-y: auto;
    }
  }
}
html,
body {
  width: 100vw;
  min-height: 100vh;
  padding: 0;
  margin: 0;
}
</style>
