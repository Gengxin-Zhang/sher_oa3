import Auth from '@/api/auth'
import Basic from '@/api/basic'

export default (context, inject) => {
  // Initialize API repositories
  const repositories = {
    auth: Auth(context.$axios),
    basic: Basic(context.$axios)
  }
  inject('api', repositories)
}
