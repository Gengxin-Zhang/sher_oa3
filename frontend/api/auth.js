export default $axios => ({
  login(credentials) {
    return $axios.post('/auth/signin', credentials)
  },
  validateToken() {
    return $axios.get('/auth/verify')
  }
})
