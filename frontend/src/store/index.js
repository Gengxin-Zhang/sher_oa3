import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
const Store = new Vuex.Store({
  state: {
    signStatus: false,
    userInfo: {}
  },
  getters: {
    getSignStatus: (state) => {
      return state.signStatus
    },
    getPermission: (state) => {
      // console.log(state.userInfo.permission)
      return state.userInfo.permission || -1
    },
    getUserInfo: (state) => {
      return state.userInfo
    }
  },
  mutations: {
    signin (state, userInfo) {
      state.signStatus = true
      state.userInfo = userInfo
    },
    signout (state) {
      state.signStatus = false
      state.userInfo = {}
    }
  },
  actions: {
    signin (context, userInfo) {
      if (localStorage.token !== userInfo.token && userInfo.token !== undefined) {
        localStorage.setItem('token', userInfo.token)
      }
      context.commit('signin', userInfo)
    },
    signout (context) {
      localStorage.removeItem('token')
      context.commit('signout')
    }
  }
})
export default Store
