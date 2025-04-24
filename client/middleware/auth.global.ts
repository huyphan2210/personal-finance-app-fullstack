export default defineNuxtRouteMiddleware(async (to) => {
  const {isLoaded, isSignedIn} = useAuth();
  const checkLogin = (isAuthLoaded: boolean) => {
    if (!isAuthLoaded) return;

    if (!isSignedIn.value) {
      navigateTo(Page.Login)
    }
  }
  
  checkLogin(isLoaded.value);

  watch(() => isLoaded.value, (result) => checkLogin(result))
})