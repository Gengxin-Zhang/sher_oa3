<template>
  <div :class="['container', status.theme]">
    <div class="welcome">
      <span class="first text-focus-in">{{welcomeWord}},{{user.info.name}}</span>
      <span class="second text-focus-in">{{warmWord}}</span>
    </div>
    <!-- <div class="signBox" v-if="user.signed">
      <div class="signStatus">
        <span class="alert">当前为非值班时间</span>
        <span class="small">下一次值班时间：周一上午三四节</span>
      </div>
      <div class="optionBox">
        <button class="disable">签到</button>
      </div>
      <div class="more">
        <a-popover placement="bottomRight" trigger="click" arrowPointAtCenter>
          <template slot="content">
            <span class="title">更多操作</span>
            <div class="popoverList">
              <div class="popoverListItem">请假</div>
              <div class="popoverListItem">调班</div>
            </div>
          </template>
          <a-icon type="ellipsis" />
        </a-popover>
      </div>
    </div>-->
    <div class="Surprise text-focus-in" style="display:none">
      <div class="word">
        <span class="letter" v-for="letter,index in 'HAPPY '" :key="index">{{letter}}</span>
      </div>
      <div class="word">
        <span class="letter" v-for="letter,index in 'BIRTHDAY'" :key="index">{{letter}}</span>
      </div>
      <div>祝你生日快乐</div>
    </div>
    <calendar style="margin: 0 -.5rem; width: calc(100% + 1rem)" />
  </div>
</template>

<script>
import { mapState, mapGetters, mapActions, mapMutations } from "vuex";
import Calendar from "@/components/Calendar";
export default {
  components: {
    Calendar
  },
  data() {
    return {
      welcomeWord: "",
      warmWord: ""
    };
  },
  created(){
  },
  computed: {
    status() {
      return this.$store.state.status;
    },
    user() {
      return this.$store.state.User;
    }
  },
  mounted() {
    this.setPageName("个人中心");
    let nowHour = new Date().getHours();
    if (nowHour >= 4 && nowHour < 8) {
      this.welcomeWord = "早上好";
      this.warmWord = "一年之计在于春，一日之计在于晨";
    } else if (nowHour >= 8 && nowHour < 12) {
      this.welcomeWord = "上午好";
      this.warmWord = "开启满满活力一天";
    } else if (nowHour >= 12 && nowHour < 14) {
      this.welcomeWord = "中午好";
      this.warmWord = "及时休息，保持一天活力";
    } else if (nowHour >= 14 && nowHour <= 18) {
      this.welcomeWord = "下午好";
      this.warmWord = "你好";
    } else if (nowHour > 18 && nowHour <= 24) {
      this.welcomeWord = "晚上好";
      this.warmWord = "这里是一句晚上的问候";
    } else if (nowHour >= 0 && nowHour < 4) {
      this.welcomeWord = "夜深了";
      this.warmWord = "工作再忙，身体更重要，记得早点休息";
    }
  },
  methods: {
    ...mapMutations(["setPageName"])
  }
};
</script>

<style lang="scss" scope>
.container {
  margin: 0 auto;
  min-height: 100vh;
  &.dark {
    .welcome {
      .first {
        color: #a9a9b5;
      }
    }
  }
  .welcome {
    margin: 1rem 0;
    .first {
      font-size: 1.5rem;
      font-weight: 500;
      color: #555;
      display: block;
    }
    .second {
      font-size: 1rem;
      font-weight: 400;
      color: #777;
    }
  }
  .Surprise {
    text-align: center;
    min-height: 10rem;
    width: 100%;
    .word {
      -webkit-text-stroke: 3px #344b52;
      color: transparent;
      display: inline-block;
      font-weight: bolder;
      font-size: 4rem;
      text-shadow: 0.15rem 0.5rem 0 #bf616a;
      letter-spacing: 0.7rem;
      margin-right: 1rem;
      &:nth-last-child(1) {
        margin-right: 0;
      }
      .letter {
        transform: rotate(15deg);
        display: inline-block;
      }
    }
  }
  .signBox {
    margin-top: 2rem;
    border: 1px #81a1c155 solid;
    border-left: 5px #81a1c1 solid;
    border-radius: 0.3rem;
    padding: 1rem;
    position: relative;
    .signStatus {
      min-height: 3rem;
      line-height: 1.5rem;
      padding: 0.75rem;
      font-size: 1.1rem;
      font-weight: bolder;
      color: #666;
      .alert {
      }
      .small {
        font-size: 0.9rem;
        color: #999;
        margin-left: 0.5rem;
      }
    }
    .optionBox {
      padding: 0.2rem 0.75rem;
      button {
        border: #81a1c1;
        background-color: #5e81ac;
        font-size: 0.9rem;
        padding: 0.3rem 1.5rem;
        color: #fff;
        font-weight: bolder;
        outline: none;
        cursor: pointer;
        &.disable {
          background-color: #999;
        }
      }
    }
    .more {
      position: absolute;
      top: 0.3rem;
      right: 1.3rem;
      font-size: 1.3rem;
      font-weight: bolder;
      cursor: pointer;
    }
  }
}

@media screen and (max-width: 600px) {
  .container {
    margin: 0 auto;
    min-height: 100vh;
    .welcome {
      font-size: 1.3rem;
      font-weight: 700;
      color: #444;
    }
  }
}
</style>
