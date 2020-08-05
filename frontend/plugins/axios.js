export default ({
  $axios,
  redirect,
  store
}) => {
  $axios.onRequest((config) => {
    if (process.client) {
      if (store.state.user.token) {
        config.headers.Authorization = `${store.state.user.token}`
      }
    }
  })
}
