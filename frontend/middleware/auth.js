export default function ({
    route,
    redirect
  }) {
    if (process.client) {
      const token = localStorage.getItem('token');
      if (!token) {
        let paths = route.path.split('/');
        if (route.path !== '/auth/signin' && paths[0] !== 'tools') {
          redirect('/auth/signin');
        }
      }
    } else if (process.server) {}
  }
  