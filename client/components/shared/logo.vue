<template>
  <NuxtLink :to="Page.Overview">
    <img class="logo_img--minimize" src="../../assets/images/logo--minimize.svg" alt="Logo" />
    <img class="logo_img" src="../../assets/images/logo.svg" alt="Logo" />
  </NuxtLink>
</template>

<style lang="scss" scoped>
a {
  container-type: inline-size;

  .logo_img {
    display: none;
  }

  @container (min-width: 88px) {
    .logo_img {
      display: unset;

      &--minimize {
        display: none;
      }
    }
  }
}
</style>
