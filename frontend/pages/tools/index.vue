<template>
  <div class="Tools">
    <div class="ToolList">
      <span class="title">所有应用</span>
      <tool :tool="tool" v-for="tool,index in tools" :key="index" />
    </div>
  </div>
</template>

<script>
import { mapState, mapGetters, mapActions, mapMutations } from "vuex";
import Tool from '@/components/Tool'
export default {
  components:{
    Tool
  },
  data() {
    return {
      tools: [
        {
          name: "问卷",
          logo: "📋",
          id: "questions",
          color: "#3b3b47"
        },
        {
          name: "文档",
          logo: "📃",
          id: "documents",
          color: "#a0b5d0"
        },
        {
          name: "统计",
          logo: "📎",
          id: "numbers",
          color: "#0f4c81"
        },
        {
          name: "模板库",
          logo: "模",
          id: "templates",
          color: "#cea8bf"
        }
      ]
    };
  },
  mounted() {
    this.setPageName("应用工具");
  },
  methods: {
    ...mapMutations(["setPageName"])
  }
};
</script>

<style lang="scss" scoped>
.Tools {
  .ToolList {
    margin: 1rem 0;
    font-size: 0;
    word-spacing: -6px;
    .title {
      display: block;
      font-size: 1rem;
      color: #777;
      margin-bottom: 0.5rem;
    }
    
  }
}
</style>