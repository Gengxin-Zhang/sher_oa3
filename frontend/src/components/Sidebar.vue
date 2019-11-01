<template>
  <div class="Sidebar">
    <a-menu
      :defaultSelectedKeys="['data']"
      v-model="selectedKeys"
      mode="inline"
      theme="light"
      :inlineCollapsed="true"
      style="height: 100%"
    >
      <a-menu-item key="data">
        <a-icon type="area-chart" />
        <span>数据看板</span>
      </a-menu-item>
      <a-menu-item key="wiki">
        <a-icon type="read" />
        <span>Wiki管理</span>
      </a-menu-item>
      <a-menu-item key="blog">
        <a-icon type="robot" />
        <span>博客管理</span>
      </a-menu-item>
      <a-menu-item key="report">
       <a-icon type="smile" theme="outlined" />
        <span>违规管理</span>
      </a-menu-item>
      <a-menu-item key="user">
        <a-icon type="user" />
        <span>用户管理</span>
      </a-menu-item>
      <a-menu-item key="setting">
        <a-icon type="setting" />
        <span>OIKii设置</span>
      </a-menu-item>
    </a-menu>
  </div>
</template>

<script>
export default {
  data () {
    return {
      selectedKeys: []
    }
  },
  created(){
    if (this.$route.name) this.selectedKeys = [this.$route.name]
  },
  watch: {
    selectedKeys (after, before) {
      this.$router.push({name:after[0]})
    },
    '$route.name' (after, before) {
      if (after && (this.selectedKeys.length == 0 || after != this.selectedKeys[0])){
        this.selectedKeys = [after];
      }
    }
  }
};
</script>

<style lang="scss" scoped>
.Sidebar {
  text-align: left;
  width: 5rem;
  height: 100%;
  position: fixed;
  background: #fff;
}
</style>