<template>
  <div :class="['NavbarBox', status.theme]">
    <div class="NavbarList">
      <div
        :class="['openSidebarButton', 'NavbarList__Item']"
        v-if="!status.sidebar.open"
        @click="openSidebar"
      >
        <a-icon type="double-right" />
      </div>
      <div class="pageName NavbarList__Item">
        <span>{{pageName}}</span>
      </div>
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
    user(){
      return this.$store.state.User
    },
    pageName() {
      return this.$store.state.pageName;
    }
  },
  methods: {
    ...mapActions(["closeSidebar", "openSidebar"])
  }
};
</script>

<style lang="scss" scoped>
$navbar-height: 3.5rem;
.NavbarBox {
  height: $navbar-height;
  position: fixed;
  width: 100%;
  background-color: #fff;
  z-index: 99;
  box-shadow: 0 3px 5px rgba(0, 0, 0, 0.1);
  &.dark {
    background-color: #252627;
    box-shadow: none;
    color: #fff;
    .NavbarList {
      .NavbarList__Item {
        &.pageName {
          color: #a9a9b3;
        }
      }
    }
  }
  .NavbarList {
    padding: 0.6rem;
    .NavbarList__Item {
      display: inline-block;
      font-size: 1rem;
      line-height: 2.3rem;
      padding: 0 0.5rem;
      &.pageName {
        font-size: 1.1rem;
        color: #555;
        font-weight: bolder;
        padding: 0 1rem;
      }
      &.openSidebarButton {
        cursor: pointer;
        height: 2rem;
        width: 2rem;
        top: 0.8rem;
        left: 0.5rem;
        font-size: 0.9rem;
        line-height: 2rem;
        text-align: center;
        border-radius: 0.3rem;
        transition: all 0.3s;
        &:hover {
          background: rgba(0, 0, 0, 0.1);
        }
      }
    }
  }
}
@media screen and (max-width: 600px) {
  .NavbarBox {
    .NavbarList {
      text-align: center;
      .NavbarList__Item {
        &.pageName {
        }
        &.openSidebarButton {
          position: absolute;
        }
      }
    }
  }
}
</style>