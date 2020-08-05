export const state = () => ({
  userInfo: {
    id: '',
    nickname: '',
    name: '',
    userID: '',
    permission: -1,
    roles: []
  },
  logined: false,
  token: '',
  onDuty: false
})

export const mutations = {
  setUserInfo(state, newUserInfo) {
    const { id, name, roles } = newUserInfo
    state.userInfo = { id, name, roles }
    state.userInfo.userID = newUserInfo.user_id
    state.logined = true
  },
  setToken(state, newToken) {
    state.token = newToken
    localStorage.setItem('token', newToken)
  },
  setLogined(state, newLogined) {
    state.logined = newLogined
    localStorage.setItem('logined', newLogined)
  },
  setOnDuty(state, newOnDuty) {
    state.onDuty = newOnDuty
  },
  setNickname(state, newNickname) {
    state.nickname = newNickname
  }
}

export const actions = {
  login({ commit }, credentials) {
    if (credentials.username === '') {
      return Promise.reject(new Error('请填写学号'))
    }
    else if (credentials.password === '') {
      return Promise.reject(new Error('请输入密码'))
    }
    return this.$api.auth.login(credentials)
      .then((res) => {
        if (!res.data.status) {
          return Promise.reject(new Error('actions status error'))
        }
        else {
          commit('setUserInfo', res.data.data.user)
          commit('setToken', res.data.data.token)
          commit('setLogined', true)
          return Promise.resolve()
        }
      })
      .catch((err) => {
        return Promise.reject(new Error(`${err}`))
      })
  },
  logout({ commit }) {
    localStorage.removeItem('token')
    localStorage.setItem('logined', false)
    this.$router.push('/auth/login')
  },
  signin({ commit }) {
    return this.$api.basic.signin()
      .then((res) => {
        commit('setOnDuty', true)
        console.log('signin', res)
        return Promise.resolve()
      })
      .catch((err) => {
        return Promise.reject(new Error(`${err}`))
      })
  }
}
