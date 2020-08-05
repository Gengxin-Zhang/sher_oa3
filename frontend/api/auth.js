export default $axios => ({
  login(credentials) {
    return $axios.post('/auth/signin', credentials)
  },
  validateToken(token) {
    return $axios.get('/auth/verify')
  }
})
