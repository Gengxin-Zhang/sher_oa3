<template>
  <div :class="['Calendar']">
    <div
      class="head"
      :style="`--bg-color:${currentTheme.background}; --font-color:${currentTheme.font}`"
    >
      <div class="date">
        <div class>
          <div class="controler left" @click="toLastMonth()">
            <a-icon type="left" />
          </div>
          <div class="name">
            <span>{{currentDate.getFullYear()}}年</span>,
            <span>{{currentDate.getMonth()+1}}月</span>
          </div>
          <div class="controler right" @click="toNextMonth()">
            <a-icon type="right" />
          </div>
          <div class="optionList left">
            <div class="option" @click="backToNowTime">
              <a-icon type="environment" />
            </div>
          </div>
          <div class="optionList right">
            <div class="option">
              <a-icon type="plus" />
            </div>
            <div class="option">
              <a-popover placement="bottomRight" trigger="click" arrowPointAtCenter>
                <template slot="content" class="calendarMoreOptions">
                  <div class="themeSelector">
                    <div
                      class="theme"
                      :style="`background-color:${theme.background}`"
                      v-for="theme,index in calendarThemes"
                      :data-background="theme.background"
                      :data-font="theme.font"
                      :key="index"
                      @click="handleCalendarThemeSelect"
                    ></div>
                  </div>
                  <div class="popoverList calendar__popoverList" style="text-align:left">
                    <div class="popoverListItem">
                      <a-icon type="check" />
                      <span>显示课表</span>
                    </div>
                    <div class="popoverListItem">
                      <a-icon type="sync" />
                      <span>同步课表</span>
                    </div>
                    <div class="popoverListItem">
                      <a-icon type="cloud-download" />
                      <span>导出</span>
                    </div>
                  </div>
                </template>
                <a-icon type="ellipsis" />
              </a-popover>
            </div>
          </div>
        </div>
      </div>
      <div class="days">
        <div class="day" v-for="day, index in dayNameList[weekMode]" :key="index">
          <span>周{{day}}</span>
        </div>
      </div>
    </div>
    <div class="body">
      <div class="week" v-for="week,index in calendar" :key="index">
        <div
          :class="['day', day.month === currentDate.getMonth() && day.year === currentDate.getFullYear() ? '':'mask']"
          v-for="day,index in week.days"
        >
          <div class="title" @click="handleDayClick(day)">
            <span
              :class="['dayNumber', 
                        day.year === nowDate.getFullYear() && 
                        day.month === nowDate.getMonth() && 
                        day.day === nowDate.getDate()?'thisDay':'']"
            >{{day.day}}</span>
            <span class="todoCount" v-if="day.todo.length==0">{{day.todo.length}}</span>
          </div>
          <div class="todoList">
            <div
              class="todo"
              style="background-color: #D08770;"
              v-for="todo,index in day.todo"
              :key="index"
            >{{todo.name}}</div>
          </div>
        </div>
      </div>
    </div>
    <transition name="modelAnimation">
      <div class="model" v-if="showDayModel">
        <div class="mask" @click="showDayModel=false"></div>
        <div class="left">
          <div class="title">
            <span>{{currentDay.day.year}},</span>
            <span>{{currentDay.day.month+1}},</span>
            <span>{{currentDay.day.day}}</span>
          </div>
          <div class="title__sub">星期{{dayNameList[0][currentDay.date.getDay()]}}</div>
        </div>
        <transition name="modelPartAnimation">
          <div class="right">
            <div class="title">本日任务</div>
            <div class="title__sub">共有{{currentDay.day.todo.length}}项任务等待完成</div>
            <div class="newTask" @click="handleNewTodayTodo">
              <a-icon type="plus" />
            </div>
            <div class="taskList">
              <div class="task" style="--bg-color:#89a1ef;animation-delay: -.5s;">
                <div class="name"></div>
                <div class="content"></div>
                <div class="info"></div>
              </div>
              <div class="task" style="--bg-color:#b9e6ff;animation-delay: -.4s;">
                <div class="name"></div>
                <div class="content"></div>
                <div class="info"></div>
              </div>
              <div class="task" style="--bg-color:#f5d491;animation-delay: -.3s;">
                <div class="name"></div>
                <div class="content"></div>
                <div class="info"></div>
              </div>
              <div class="task" style="--bg-color:#B48EAD;animation-delay: -.2s;">
                <div class="name"></div>
                <div class="content"></div>
                <div class="info"></div>
              </div>
              <div class="task" style="--bg-color:#8FBCBB;animation-delay: -.1s;">
                <div class="name"></div>
                <div class="content"></div>
                <div class="info"></div>
              </div>
              <div class="task" style="--bg-color:#3B4252;animation-delay: 0s;">
                <div class="name"></div>
                <div class="content"></div>
                <div class="info"></div>
              </div>
              <div class="task" style="--bg-color:#3B4252;animation-delay: .1s;">
                <div class="name"></div>
                <div class="content"></div>
                <div class="info"></div>
              </div>
              <div class="task" style="--bg-color:#3B4252;animation-delay: .2s;">
                <div class="name"></div>
                <div class="content"></div>
                <div class="info"></div>
              </div>
              <div class="task" style="--bg-color:#3B4252;animation-delay: .3s;">
                <div class="name"></div>
                <div class="content"></div>
                <div class="info"></div>
              </div>
              <div class="task" style="--bg-color:#3B4252;animation-delay: .4s;">
                <div class="name"></div>
                <div class="content"></div>
                <div class="info"></div>
              </div>
              <div class="task" style="--color:#3B4252;animation-delay: .5s;">
                <div class="name"></div>
                <div class="content"></div>
                <div class="info"></div>
              </div>
              <div class="task" style="--color:#3B4252;animation-delay: .6s;">
                <div class="name"></div>
                <div class="content"></div>
                <div class="info"></div>
              </div>
            </div>
          </div>
        </transition>
        <div class="closeButton" @click="showDayModel=false">
          <a-icon type="close-circle" />
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  data() {
    return {
      dayNameList: ["日一二三四五六七", "一二三四五六日"],
      weekMode: 1,
      // 选中的日期
      currentDay: null,
      // 当前时间
      nowDate: null,
      // 展示天窗口
      showDayModel: false,
      // 日历显示时间
      currentDate: null,
      // 日历
      calendar: [],
      // 显示课表
      showClass: false,
      // 日历主题
      calendarThemes: [
        {
          name: "grey",
          background: "#ECEFF4",
          font: "#2E3440"
        },
        {
          name: "black",
          background: "#3B4252",
          font: "#fff"
        },
        {
          name: "purple",
          background: "#7776bc",
          font: "#fff"
        },
        {
          name: "blue",
          background: "#5c95ff",
          font: "#fff"
        },

        {
          name: "orange",
          background: "#f87575",
          font: "#fff"
        }

        // {
        //   name: "blue",
        //   background: "#5E81AC",
        //   font: "#fff"
        // },
      ]
      //   TimeUpdateService: null,
    };
  },
  created() {
    this.backToNowTime();
  },
  mounted() {
    this.loadCalendarTheme();
    this.backToNowTime();
    this.createCalendar(this.currentDate);
  },
  computed: {
    currentTheme() {
      return this.$store.state.calendarTheme;
    }
  },
  destroyed() {},
  watch:{
    showDayModel(after, before){
      if (after){
        document.getElementsByTagName("html")[0].style.overflow ="hidden"
      }else{
        document.getElementsByTagName("html")[0].style.overflow ="auto"
      }
    }
  },
  methods: {
    ...mapActions(["loadCalendarTheme", "changeCalendarTheme"]),
    getWeek(id) {
      return {
        week: id,
        days: []
      };
    },
    getDay(year, month, day, todo) {
      return {
        year: year,
        month: month,
        day: day,
        todo: []
      };
    },
    setNowTime() {
      this.nowDate = new Date();
    },
    backToNowTime() {
      this.setNowTime();
      this.currentDate = this.nowDate;
      this.createCalendar(this.currentDate);
    },
    toNextMonth() {
      this.currentDate = new Date(
        this.currentDate.getFullYear(),
        this.currentDate.getMonth() + 1,
        1
      );
      this.createCalendar(this.currentDate);
    },
    toLastMonth() {
      this.currentDate = new Date(
        this.currentDate.getFullYear(),
        this.currentDate.getMonth() - 1,
        1
      );
      this.createCalendar(this.currentDate);
    },
    handleDayClick(day) {
      this.currentDay = {
        date: new Date(day.year, day.month, day.day),
        day: day
      };
      this.showDayModel = true;
    },
    handleNewTodo() {},
    handleNewTodayTodo() {},
    handleCalendarThemeSelect(e) {
      this.changeCalendarTheme({
        background: e.target.dataset.background,
        font: e.target.dataset.font
      });
    },
    createCalendar(date) {
      this.calendar = [];
      let currentMonth = new Date(date.getFullYear(), date.getMonth(), 1);
      let lastMonth = new Date(date.getFullYear(), date.getMonth(), 0);
      let currentMonthFirstDay =
        currentMonth.getDay() == 0 ? 7 : currentMonth.getDay();
      let currentMonthLastDate = new Date(
        currentMonth.getFullYear(),
        currentMonth.getMonth() + 1,
        0
      ).getDate();
      let weekNumber = 0;
      let tempDayNumber = 2 - currentMonthFirstDay;
      while (tempDayNumber < currentMonthLastDate) {
        this.calendar.push(this.getWeek());
        for (let i = 0; i < 7; i++) {
          let tempDay = new Date(
            currentMonth.getFullYear(),
            currentMonth.getMonth(),
            tempDayNumber + i,
            []
          );
          this.calendar[weekNumber].days.push(
            this.getDay(
              tempDay.getFullYear(),
              tempDay.getMonth(),
              tempDay.getDate(),
              []
            )
          );
        }
        tempDayNumber += 7;
        weekNumber++;
      }
    }
  }
};
</script>

<style lang="scss" scoped>
$calendar-head-date-height: 3rem;
.Calendar {
  width: 100%;
  box-shadow: 0 0 3px 1px rgba(0, 0, 0, 0.1);
  position: relative;
  border-radius: 0.3rem;
  overflow: hidden;
  .head {
    width: 100%;
    .date {
      height: $calendar-head-date-height;
      background: var(--bg-color);
      text-align: center;
      box-shadow: 0 1px 5px 2px #4c566a;
      font-size: 1.1rem;
      line-height: $calendar-head-date-height;
      color: var(--font-color);
      font-weight: bolder;
      transition: all 0.3s;
      .controler {
        display: inline-block;
        cursor: pointer;
        padding: 0 0.5rem;
        height: $calendar-head-date-height;
        transition: all 0.3s;
        &:hover {
          transform: translateY(-1px);
        }
      }
      .optionList {
        position: absolute;
        top: 0;
        font-size: 1.3rem;
        font-weight: bolder;
        &.right {
          right: 0.5rem;
          .option {
            margin-right: 0.5rem;
            &::nth-last-child(1) {
              margin-right: 0;
            }
          }
        }
        &.left {
          left: 0.5rem;
          .option {
            margin-left: 0.5rem;
            &::nth-child(1) {
              margin-left: 0;
            }
          }
        }
        .option {
          display: inline-block;
          cursor: pointer;
          transition: all 0.3s;
          &:hover {
            transform: translateY(-1px);
          }
        }
      }
      .name {
        display: inline-block;
        transition: all 0.3s;
        span {
          cursor: pointer;
          display: inline-block;
          transition: all 0.3s;
          &:hover {
            transform: translateY(-1px);
          }
        }
      }
    }
    .days {
      height: 1.5rem;
      background: #eceff4;
      font-size: 0;
      word-spacing: -6px;
      box-shadow: 0 1px 3px 1px rgba(0, 0, 0, 0.1);
      .day {
        width: calc(100% / 7);
        display: inline-block;
        font-size: 0.9rem;
        line-height: 1.5rem;
        color: #4c566add;
        text-align: center;
        border-left: 1px #4c566a00 solid;
        &:nth-child(1) {
          border-left: none;
        }
      }
    }
  }
  .body {
    position: relative;
    width: 100%;
    .week {
      font-size: 0;
      word-spacing: -6px;
      border-bottom: 1px #4c566a44 solid;
      &:nth-child(2n + 1) {
        //   background-color: rgba(0,0,0,0.1);
      }
      &:nth-last-child(1) {
        border-bottom: none;
      }
      .day {
        height: 7rem;
        width: calc(100% / 7);
        border-left: 1px #4c566a44 solid;
        display: inline-block;
        margin: 0;
        font-weight: bold;
        padding: 0.3rem 0;
        position: relative;

        .title {
          display: block;
          height: 1.5rem;
          width: 100%;
          //   text-align: center;
          padding: 0 0.3rem;
          .dayNumber {
            width: 1.5rem;
            height: 1.5rem;
            line-height: 1.5rem;
            position: relative;
            display: inline-block;
            text-align: center;
            color: #666;
            font-size: 0.9rem;
            cursor: pointer;
            &.thisDay {
              background: #a3be8c;
              border-radius: 100%;
              color: #fff;
            }
          }
          .todoCount {
            visibility: hidden;
            display: inline-block;
            height: 1rem;
            margin-left: 0.2rem;
            font-size: 0.8rem;
            line-height: 1rem;
            background: #bf616a;
            color: #fff;
            border-radius: 0.3rem;
            padding: 0 0.1rem;
          }
        }
        .todoList {
          padding: 0.1rem;
          .todo {
            height: 1.1rem;
            background: #4c566a;
            border-radius: 0.2rem;
            font-size: 0.8rem;
            letter-spacing: 1px;
            line-height: 1.1rem;
            color: #fff;
            padding: 0 0.2rem;
            font-weight: 400;
            margin-bottom: 0.05rem;
            word-wrap: none;
            overflow: hidden;
            cursor: pointer;
          }
        }
        &.mask {
          opacity: 0.4;
          transition: all 0.3s;
          //   &::after {
          //     content: "";
          //     position: absolute;
          //     top:0;
          //     left: 0;
          //     width: 100%;
          //     height: 100%;
          //     background: rgba(0,0,0,0.1);
          //   }
          &:hover {
            opacity: 1;
          }
        }
        &:nth-child(1) {
          border-left: none;
        }
      }
    }
  }
  .model {
    width: 60%;
    height: auto;
    border-radius: 0.8rem;
    position: fixed;
    /* margin: 0 auto; */
    background: #fff;
    top: 10%;
    min-height: 70%;
    max-height: 70%;
    left: 20%;
    z-index: 999;
    overflow: hidden;
    box-shadow: 0 5px 25px 5px rgba(0, 0, 0, 0.1);
    .mask {
      position: fixed;
      height: 100%;
      width: 100%;
      background-color: rgba(0, 0, 0, 0.4);
      backdrop-filter: blur(10px);
      animation: blurAnimation 1.5s;
      top: 0;
      left: 0;
    }
    .left {
      width: 40%;
      height: 100%;
      position: absolute;
      background: #4c566a;
      padding: 1rem;
      .title {
        padding: 0.5rem 1rem;
        font-size: 2.3rem;
        line-height: 2.5rem;
        font-weight: bolder;
        color: #fff;
        word-wrap: break-word;
      }
      .title__sub {
        font-size: 1.4rem;
        color: #ddd;
        padding: 0.5rem 1rem;
      }
    }
    .right {
      width: 60%;
      height: 100%;
      position: absolute;
      left: 40%;
      padding: 1rem;
      overflow-x: hidden;
      overflow-y: auto;
      background: #eceff4;
      .title {
        font-size: 1.4rem;
        padding: 0.5rem 1rem 0rem 1rem;
        font-weight: bold;
        line-height: 2rem;
        color: rgb(53, 60, 73);
      }
      .title__sub {
        font-size: 0.9rem;
        padding: 0.2rem 1rem 0.5rem 1rem;
        font-weight: 450;
        color: #898f9b;
      }
      .newTask {
        width: 95%;
        margin: 0.4rem auto;
        height: 2rem;
        // background: linear-gradient( #fff, #ddd);
        transition: all 0.3s;
        border-radius: 0.2em;
        line-height: 2rem;
        font-size: 1.1rem;
        color: #777;
        font-weight: bolder;
        text-align: center;
        cursor: pointer;
        background: #d8dee9;
        box-shadow: 0 0 2px 1px #d8dee922;
        &:hover {
          background: #fff;
          box-shadow: 0 0 2px 1px rgba(0, 0, 0, 0.1);
        }
      }
      scroll-behavior: smooth;
      .taskList {
        height: calc(100% - 8.5rem);
        width: 95%;
        margin: 0 auto 0.5rem auto;
        overflow-y: auto;
        transition: all 0.3s;
        scroll-behavior: smooth;
        &::-webkit-scrollbar {
          width: 0 !important;
        }
        .task {
          height: 3rem;
          border-radius: 0.3rem;
          background-color: var(--bg-color);
          // background-color: #fff;
          border: 1px rgba(0, 0, 0, 0.1) solid;
          margin-bottom: 0.2rem;
          transition: all 0.3s;
          animation: modelPartAnimation-in 0.8s;
        }
      }
    }
    .closeButton {
      top: 1rem;
      right: 1rem;
      font-size: 1.5rem;
      height: 1.5rem;
      text-align: center;
      width: 1.5rem;
      line-height: 1.5rem;
      color: #4c566a;
      cursor: pointer;
      font-weight: bolder;
      transition: all 0.3s;
      position: absolute;
      &:hover {
        transform: rotate(180deg);
      }
    }
  }
}
.themeSelector {
  min-height: 2.5rem;
  padding: 0.3rem;
  position: relative;
  border-bottom: 1px rgba(0, 0, 0, 0.05) solid;
  .theme {
    height: 1.5rem;
    width: 1.5rem;
    margin: 0.1rem 0.2rem;
    border-radius: 50%;
    display: inline-block;
    position: relative;
    background: #4c566a;
    cursor: pointer;
  }
}
.calendar__popoverList {
  .popoverListItem {
    position: relative;
    i {
      width: 1rem;
      height: 2rem;
      left: 0.7rem;
      line-height: 2.5rem;
      font-size: 1.1rem;
      color: #aaa;
      position: absolute;
      vertical-align: middle;
      top: 0;
    }
    span {
      position: relative;
      padding-left: 1.5rem;
      color: #4c566a;
    }
  }
}
@media screen and (max-width: 600px) {
  .Calendar {
    .model {
      width: 100%;
      height: 100%;
      max-height: 100%;
      max-width: 100%;
      border-radius: 0;
      left: 0;
      top: 0;
      overflow: hidden;
      .left {
        position: fixed;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        .title {
        }
        .title__sub {
          padding: 0rem 1rem;
          font-size: 1.3rem;
        }
      }
      .right {
        position: relative;
        width: 100%;
        margin-top: 15vh;
        border-radius: 1rem 1rem 0 0;
        height: 85%;
        left: 0;
        .newTask {
          width: 100%;
        }
        .taskList {
          width: 100%;
        }
      }
      .closeButton {
        color: #fff;
      }
    }
  }
}
.modelAnimation-enter-active {
  animation: modelAnimation-in 0.4s;
}
.modelAnimation-leave-active {
  animation: modelAnimation-out 0.4s;
}
@media screen and (max-width: 600px) {
  .modelAnimation-enter-active {
    animation: none;
  }
  .modelAnimation-leave-active {
    animation: none;
  }
  .model > .right {
    animation: modelPartAnimation-in 0.4s;
  }
}
@keyframes modelAnimation-in {
  0% {
    transform: translateY(100vh);
  }
  50% {
    transform: translateY(-2rem);
  }
  100% {
    transform: translateY(0rem);
  }
}
@keyframes modelAnimation-out {
  0% {
    transform: translateY(0rem);
  }
  50% {
    transform: translateY(-2rem);
  }
  100% {
    transform: translateY(100vh);
  }
}
@keyframes modelPartAnimation-in {
  0% {
    transform: translateY(100vh);
  }
  100% {
    transform: translateY(0rem);
  }
}
@keyframes blurAnimation {
  0% {
    backdrop-filter: blur(0px);
    background: rgba(255, 255, 255, 0.1);
  }
  100% {
    backdrop-filter: blur(10px);
    background: rgba(0, 0, 0, 0.4);
  }
}
</style>