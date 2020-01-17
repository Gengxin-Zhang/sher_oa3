export default ({
  $axios,
  redirect,
  store
}) => {
  $axios.onRequest(config => {
    if (process.client) {
      if (store.state.User.token) {
        config.headers.authorization = 'Bearer ' + store.state.User.token
      }
    }
  })
}
