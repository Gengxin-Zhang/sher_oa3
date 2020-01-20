<template>
  <div class="Calendar">
    <div class="head">
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
                      v-for="theme in calendarThemes"
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
          <div class="title">
            <span
              :class="['dayNumber', day.year === nowDate.getFullYear() && day.month === nowDate.getMonth() && day.day === nowDate.getDate()?'thisDay':'']"
            >{{day.day}}</span>
            <span class="todoCount" v-if="day.todo.length==0">{{day.todo.length}}</span>
          </div>
          <div class="todoList">
            <div
              class="todo"
              style="background-color: #D08770;"
              v-for="todo,index in day.todo"
              :key="index"
            >加班</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dayNameList: ["日一二三四五六七", "一二三四五六日"],
      // 当前时间
      weekMode: 1,
      nowDate: null,
      // 日历显示时间
      currentDate: null,
      // 日历
      calendar: [],
      // 显示课表
      showClass: false,
      // 日历主题
      calendarThemes: [
        {
          background: "#3B4252",
          font: "#fff"
        },
        {
          background: "#B48EAD",
          font: "#fff"
        },
        {
          background: "#D8DEE9",
          font: "#2E3440"
        },
        {
          background: "#5E81AC",
          font: "#fff"
        },
        {
          background: "#8FBCBB",
          font: "#fff"
        }
      ]
      //   TimeUpdateService: null,
    };
  },
  created() {
    this.backToNowTime();
  },
  mounted() {
    this.backToNowTime();
    this.createCalendar(this.currentDate);
  },
  destroyed() {},
  methods: {
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
      background: #b48ead;
      text-align: center;
      box-shadow: 0 1px 5px 2px #4c566a;
      font-size: 1.1rem;
      line-height: $calendar-head-date-height;
      color: #fff;
      font-weight: bolder;
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
      left: .7rem;
      line-height: 2.5rem;
      font-size: 1.1rem;
      color: #AAA;
      position: absolute;
      vertical-align: middle;
      top: 0;
    }
    span {
      position: relative;
      padding-left: 1.5rem;
      color: #4C566A;
    }
  }
}
</style>