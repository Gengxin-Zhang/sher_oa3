export const state = () => ({
  status: {
    sidebar: {
      open: true
    },
    theme: 'light'
  },
  calendarTheme: {
    background: "#ECEFF4",
    font: "#434C5E"
  },
  pageName: ""
})

export const mutations = {
  setSidebarStatus(state, status) {
    state.status.sidebar.open = status;
    localStorage.setItem("status", JSON.stringify(state.status))
  },

  setPageName(state, pageName) {
    state.pageName = pageName;
  },

  resetStatus(state) {},

  setStatus(state, status) {
    state.status = status;
    localStorage.setItem("status", JSON.stringify(status))
  },

  initCalendarTheme(state) {
    state.calendarTheme = {
      background: "#ECEFF4",
      font: "#434C5E"
    };
    localStorage.setItem("calendar", JSON.stringify(state.calendarTheme))
  },

  setCalendarTheme(state, theme) {
    state.calendarTheme = theme;
    localStorage.setItem("calendar", JSON.stringify(theme))
  }
}

export const actions = {
  closeSidebar({
    commit
  }) {
    commit("setSidebarStatus", false)
  },
  openSidebar({
    commit
  }) {
    commit("setSidebarStatus", true)
  },
  changePageName({
    commit
  }, pagename) {
    commit("setPageName", pagename)
  },
  changeCalendarTheme({
    commit
  }, calendarTheme) {
    commit("setCalendarTheme", calendarTheme);
  },
  loadCalendarTheme({
    commit
  }) {
    let raw_theme = localStorage.getItem("calendar");
    if (!raw_theme) {
      commit("initCalendarTheme");
    }
    try {
      let theme = JSON.parse(raw_theme);
      if (theme && theme.hasOwnProperty("background") && theme.hasOwnProperty("font")) {
        commit("setCalendarTheme", theme)
      } else {
        commit("initCalendarTheme");
      }
    } catch {
      commit("initCalendarTheme");
    }
  },
  loadStatus({
    commit
  }) {
    let raw_status = localStorage.getItem("status");
    try {
      let status = JSON.parse(raw_status);
      if (status && status.hasOwnProperty("sidebar") && status.hasOwnProperty("theme"))
        commit("setStatus", status);
      else {
        commit("resetStatus")
      }
    } catch (e) {
      commit("resetStatus");
    }
  }
}
