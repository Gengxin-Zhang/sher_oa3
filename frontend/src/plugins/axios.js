import axios from 'axios'

axios.interceptors.request.use(
  config => {
    if (localStorage.token) {
      config.headers.common['Authorization'] = `token ${localStorage.token}`
    }
    return config
  },
  err => {
    return Promise.reject(err)
  })

axios.interceptors.response.use(
  request => {
    return request
  },
  response => {
    return response
  }
)

export default {
  install (Vue) {
    Object.defineProperty(Vue.prototype, '$axios', {
      value: axios
    })
  }
}
