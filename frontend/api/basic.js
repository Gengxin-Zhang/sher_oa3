export default $axios => ({
  signin() {
    return $axios.get('/sign/do')
  }
})
