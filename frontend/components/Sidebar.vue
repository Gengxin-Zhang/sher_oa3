<template>
  <div :class="['SidebarBox', status.sidebar.open?'open':'close']">
    <div class="Profile">
      <a-avatar
        shape="square"
        size="small"
        :style="{backgroundColor: '#f46f60', verticalAlign: 'middle', margin: '0 .2rem' }"
      >{{user.signed&&user.info.name&&user.info.name!==''?user.info.name[0]:"升华"}}</a-avatar>
      <span style="vertical-align: middle; margin: 0 .2rem;">{{user.info.name}}</span>

      <a-icon style="color: #777; vertical-align: middle;font-size: .8rem;" type="caret-down" />

      <div class="closeButton" @click="closeSidebar">
        <a-icon type="double-left" />
      </div>
    </div>
    <div class="SidebarList">
      <nuxt-link to="/" class="exact-active">
        <div class="SidebarListItem">
          <a-icon type="compass" />
          <span>个人中心</span>
        </div>
      </nuxt-link>
      <nuxt-link to="search" class="link-active">
        <div class="SidebarListItem">
          <a-icon type="search" style />
          <span>快速查找</span>
        </div>
      </nuxt-link>
      <nuxt-link to="check" class="link-active">
        <div class="SidebarListItem">
          <a-icon type="smile" />
          <span>考勤</span>
        </div>
      </nuxt-link>

      <nuxt-link to="setting" class="link-active">
        <div class="SidebarListItem">
          <a-icon type="setting" />
          <span>设置</span>
        </div>
      </nuxt-link>

      <div class="SidebarListItem split">
        <span>其他</span>
      </div>
      <nuxt-link to="/tools" class="link-active">
        <div class="SidebarListItem">
          <a-icon type="appstore" />
          <span>应用工具</span>
        </div>
      </nuxt-link>
      <div class="SidebarListItem split" v-if="user.info.permission>=2">
        <span>权限操作</span>
      </div>
      <nuxt-link to="/globalsetting" class="link-active" v-if="user.info.permission>=2">
        <div class="SidebarListItem">
          <a-icon type="audit" />
          <span>全局设置</span>
        </div>
      </nuxt-link>
    </div>
  </div>
</template>

<script>
import { mapState, mapGetters, mapActions, mapMutations } from "vuex";
export default {
  computed: {
    status() {
      return this.$store.state.status;
    },
    user() {
      return this.$store.state.User;
    }
  },
  methods: {
    ...mapActions(["closeSidebar", "openSidebar"])
  }
};
</script>

<style lang="scss" scoped>
$sidebar-width: 15rem;
.SidebarBox {
  z-index: 100;
  transition: all 0.3s;
  &.open {
    background-color: #f3f1ec;
    width: $sidebar-width;
    height: 100vh;
  }
  &.close {
  }
  &:hover {
    .Profile {
      .closeButton {
        visibility: visible;
        opacity: 1;
      }
    }
  }
  .Profile {
    height: 3.5rem;
    transition: all 0.3s;
    font-size: 1rem;
    line-height: 3.3rem;
    font-weight: bolder;
    padding: 0 1rem;
    vertical-align: middle;
    color: #3b4141;
    cursor: pointer;
    &:hover {
      color: #333;
      background-color: rgba(0, 0, 0, 0.1);
    }
    .closeButton {
      position: absolute;
      top: 0.8rem;
      right: 1rem;
      font-size: 0.9rem;
      line-height: 2rem;
      height: 2rem;
      width: 2rem;
      text-align: center;
      border-radius: 0.3rem;
      visibility: hidden;
      opacity: 0;
      transition: all 0.3s;
      cursor: pointer;
      &:hover {
        background: rgba(0, 0, 0, 0.1);
      }
    }
  }

  .SidebarList {
    width: $sidebar-width;
    a {
      text-decoration: none;
      &.link-active {
        &.nuxt-link-active {
          .SidebarListItem {
            background-color: rgba(0,0,0,0.1);
          }
        }
      }
      &.exact-active {
        &.nuxt-link-exact-active {
          .SidebarListItem {
            background-color: rgba(0,0,0,0.1);
          }
        }
      }
    }
    .SidebarListItem {
      height: 2rem;
      padding: 0.5rem 1rem;
      line-height: 1rem;
      font-size: 0.9rem;
      font-weight: 500;
      color: #666;
      transition: all 0.3s;
      text-decoration: none;
      cursor: pointer;
      i {
        vertical-align: middle;
        margin: 0 0.5rem 0 0.2rem;
        width: 24px;
        font-size: 1.1rem;
        font-weight: 800;
        color: #999;
        text-align: center;
      }
      span {
        vertical-align: middle;
        margin: 0;
      }
      &.split {
        height: 1.5rem;
        padding: 0 1rem;
        margin-top: 0.5rem;
        cursor: inherit;
        span,
        i {
          margin: 0;
          line-height: 1.5rem;
          font-size: 0.8rem;
          color: #999;
        }
        &:hover {
          background: none;
        }
      }
      &:hover {
        background: rgba(0, 0, 0, 0.1);
        span {
          color: #3b4747;
        }
      }
    }
  }
}
@media screen and (max-width: 600px) {
  .SidebarBox {
    .Profile {
      .closeButton {
        opacity: 1;
        visibility: visible;
      }
    }
  }
}
</style>