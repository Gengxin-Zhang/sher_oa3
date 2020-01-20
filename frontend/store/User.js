import AuthAPI from "@/api/auth"

export const state = () => ({
  info: {
    id: "",
    permission: -1,
    name: "",
    user_id: "",
  },
  signed: false,
  token: ""
})

export const mutations = {
  setUserInfo(state, user) {
    state.info = user;
    state.signed = true;
  },
  setToken(state, token) {
    state.token = token
    localStorage.setItem("token", token)
  },
  removeUserInfo(state) {
    state.info = {
      id: "",
      permission: -1,
      name: "",
      user_id: "",
    };
    state.signed = false;
  }
}

export const actions = {
  signin({
    commit
  }, credentials) {
    if (credentials.username == "" || credentials.password == "") {
      return Promise.reject("请填写完整登入信息");
    }
    return this.$api.auth.signin(credentials).then(res => {
      if (res.data.status) {
        commit("setUserInfo", res.data.data.user);
        commit("setToken", res.data.data.token)
        return Promise.resolve();
      } else {
        return Promise.reject(res.data.msg);
      }
    }, err => {
      // return Promise.resolve();
      return Promise.reject(err);
    })
  },
  signout({
    commit
  }) {
    commit("removeUserInfo");
  },

  validToken({
    commit
  }, token) {
    if (token === null || token === undefined || token === "") {
      return Promise.reject("token无效")
    }
    commit("setToken", token)
    return this.$api.auth.validToken(token).then(res => {
      if (res.data.status) {
        commit("setUserInfo", res.data.data.user);
        return Promise.resolve();
      } else {
        return Promise.reject(res.data.msg)
      }
    }, err => {
      return Promise.reject(err);
    })
  }
}
