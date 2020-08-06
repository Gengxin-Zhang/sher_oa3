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
    localStorage.setItem('userInfo', JSON.stringify(newUserInfo))
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
          return Promise.reject(new Error(res.data.msg))
        }
        else {
          commit('setUserInfo', res.data.data.user)
          commit('setToken', res.data.data.token)
          commit('setLogined', true)
          return Promise.resolve()
        }
      })
      .catch((err) => {
        return Promise.reject(new Error(`${err}`.replace(/Error: /g, '')))
      })
  },
  logout({ commit }) {
    commit('setUserInfo', {
      id: '',
      nickname: '',
      name: '',
      userID: '',
      permission: -1,
      roles: []
    })
    commit('setToken', '')
    commit('setLogined', false)
    localStorage.removeItem('token')
    localStorage.setItem('logined', false)
    localStorage.removeItem('userInfo')
    this.$router.push('/auth/login')
  },
  signin({ commit }) {
    return this.$api.basic.signin()
      .then((res) => {
        console.log('signin', res)
        if (res.data.status) {
          commit('setOnDuty', true)
          return Promise.resolve()
        }
        else {
          return Promise.reject(new Error(res.data.msg))
        }
      })
      .catch((err) => {
        return Promise.reject(new Error(`${err}`.replace(/Error: /g, '')))
      })
  },
  mySigns({ commit }) {
    return this.$api.basic.myRoutine()
      .then((res) => {
        console.log('mySigns', res)
        return Promise.resolve()
      })
      .catch((err) => {
        return Promise.reject(new Error(`${err}`))
      })
  },
  exportSigns({ commit }) {
    return this.$api.basic.exportSigns()
      .then((res) => {
        console.log('exportSigns', res)
        if (res.data.status) {
          return Promise.resolve()
        }
        else {
          return Promise.reject(new Error(res.data.msg))
        }
      })
      .catch((err) => {
        return Promise.reject(new Error(`${err}`.replace(/Error: /g, '')))
      })
  },
  initRoutine({ commit }, initSignTime) {
    return this.$api.basic.initRoutine({ signtime: initSignTime })
      .then((res) => {
        console.log('initRoutine', res)
        if (res.data.status) {
          return Promise.resolve()
        }
        else {
          return Promise.reject(new Error(res.data.msg))
        }
      })
      .catch((err) => {
        return Promise.reject(new Error(`${err}`.replace(/Error: /g, '')))
      })
  },
  allRoutine({ commit }) {
    return this.$api.basic.allRoutine()
      .then((res) => {
        console.log('allRoutine', res)
        if (res.data.status) {
          return Promise.resolve()
        }
        else {
          return Promise.reject(new Error(res.data.msg))
        }
      })
      .catch((err) => {
        return Promise.reject(new Error(`${err}`.replace(/Error: /g, '')))
      })
  },
  myRoutine({ commit }) {
    return this.$api.basic.myRoutine()
      .then((res) => {
        console.log('myRoutine', res)
        return Promise.resolve()
      })
      .catch((err) => {
        return Promise.reject(new Error(`${err}`.replace(/Error: /g, '')))
      })
  }
}
