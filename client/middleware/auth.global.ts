export default defineNuxtRouteMiddleware(async (to) => {
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
  
  checkLogin(isLoaded.value);

  watch(() => isLoaded.value, (result) => checkLogin(result))
})