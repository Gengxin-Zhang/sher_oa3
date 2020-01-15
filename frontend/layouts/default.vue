<template>
  <div class="Main">
    <div class="SideBar"></div>
    <div class="MainColumn"></div>
    <nuxt />
  </div>
</template>
<script>
import Sidebar from "@/components/Sidebar";
import Navbar from "@/components/Navbar";
export default {
  components: {
    Sidebar,
    Navbar
  },
  data() {
    return {};
  },
  mounted() {
    console.log("升华OA");
    let authToken = localStorage.getItem("token")
    let status = localStorage.getItem("status")
    if (status === null){

    }
  }
};
</script>
<style lang="scss">
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
  .SideBar {
  }
  .MainColumn {
  }
}
</style>
