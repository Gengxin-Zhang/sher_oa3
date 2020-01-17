export const state = () => ({
  status: {
    sidebar: {
      open: true
    },
    theme: 'light'

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

  resetStatus(state) {
    console.log(state)
  },

  setStatus(state, status) {
    state.status = status;
    localStorage.setItem("status", JSON.stringify(status))
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
    } catch(e) {
      console.log(e)
      commit("resetStatus");
    }
  }
}
