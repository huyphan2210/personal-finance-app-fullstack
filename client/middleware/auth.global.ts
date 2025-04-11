export default defineNuxtRouteMiddleware((to) => {

  const excludeRoutes = [Page.Login, Page.Signup]
  if (excludeRoutes.includes(to.path as Page)) {
    return
  }

  const {isLoaded, isSignedIn} = useAuth();
  const checkLogin = (isAuthLoaded: boolean) => {
    if (!isAuthLoaded) return;

    if (!isSignedIn.value) {
      navigateTo(Page.Login)
    } else {

    }
  }

  watch(() => isLoaded.value, (result) => checkLogin(result))
})