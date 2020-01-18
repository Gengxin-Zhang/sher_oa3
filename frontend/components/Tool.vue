<template>
  <nuxt-link :to="`/tools/${tool.id}`">
    <div class="toolBox">
      <div class="tool">
        <div class="logo" :style="`background-color:${tool.color}`">
          <span>{{tool.logo}}</span>
        </div>
        <div class="info">
          <div class="name">
            <span>{{tool.name}}</span>
          </div>
        </div>
      </div>
    </div>
  </nuxt-link>
</template>

<script>
export default {
  props: {
    tool: {
      type: Object,
      default() {
        return {
          id: "",
          logo: "A",
          name: "应用"
        };
      }
    }
  }
};
</script>
<style lang="scss" scoped>
.toolBox {
  width: calc(100% / 3);
  padding: 0rem 0.7rem;
  margin: 0.5rem 0rem;
  display: inline-block;
  position: relative;
  max-width: 100%;
  .tool {
    height: 4rem;
    width: 100%;
    margin: 0 auto;
    background: #fff;
    border-radius: 0.2rem;
    overflow: hidden;
    box-shadow: 0 0 5px 2px rgba(0, 0, 0, 0.1);
    position: relative;
    transition: all 0.3s;
    &:hover {
      box-shadow: 0 0 10px 2px rgba(0, 0, 0, 0.1);
    }
    .logo {
      width: 4rem;
      height: 4rem;
      background-color: #35625f;
      color: #fff;
      font-size: 2rem;
      font-weight: bolder;
      line-height: 4rem;
      text-align: center;
      vertical-align: middle;
      display: inline-block;
      transition: all 0.3s;
    }
    .info {
      width: calc(100% - 4rem);
      height: 4rem;
      padding: 0.5rem 10%;
      vertical-align: middle;
      display: inline-block;
      transition: all 0.3s;
      .name {
        font-size: 1.1rem;
        font-weight: bold;
        color: #3b4141;
        line-height: 3rem;
      }
    }
  }
}
@media screen and (max-width: 800px) {
  .Tools {
    .ToolList {
      .toolBox {
        width: calc(100% / 2);
      }
    }
  }
}
@media screen and (max-width: 500px) {
  .Tools {
    .ToolList {
      .title {
        margin-bottom: 0.5rem;
      }
      .toolBox {
        width: calc(100% / 2);
        padding: 0.5rem 0.5rem;
        margin: 0;
        .tool {
          height: 10rem;
          .logo {
            width: 100%;
            height: 5rem;
            line-height: 5rem;
            font-size: 3rem;
          }
          .info {
            height: 5rem;
            width: 100%;
            text-align: center;
            letter-spacing: 3px;

            padding: 0.7rem 13%;
            .name {
              font-size: 1.1rem;
            }
          }
        }
      }
    }
  }
}
</style>