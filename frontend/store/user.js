export const state = () => ({
  userInfo: {
    id: '',
    nickname: '',
    name: '',
    user_id: '',
    permission: -1
  },
  signed: false,
  token: ''
})

export const mutations = {
  setUserInfo(state, newUserInfo) {
    state.userInfo = newUserInfo
    state.signed = true
  },
  setToken(state, newToken) {
    state.token = newToken
  },
  setNickname(state, newNickname) {
    state.nickname = newNickname
  }
}

export const actions = {
  login({ commit }, credentials) {
    if (credentials.username === '') {
      console.log('无学号')
      return Promise.reject(new Error('请填写学号'))
    }
    else if (credentials.password === '') {
      console.log('无密码')
      return Promise.reject(new Error('请输入密码'))
    }
    return this.$api.auth.login(credentials)
      .then((res) => {
        if (!res.data.status) {
          console.log('login fail')
          return Promise.reject(new Error(res.data.msg))
        }
        else {
          console.log('login succeed')
          commit('setUserInfo', res.data.user)
          commit('setToken', res.data.token)
          localStorage.setItem('token', res.data.token)
          return Promise.resolve()
        }
      })
      .catch((err) => {
        return Promise.reject(new Error(err))
      })
  }
}
