<template>
  <aside class="illustration">
    <img
      src="../assets/images/illustration-authentication.svg"
      loading="lazy"
      alt="Login Illustration"
    />
  </aside>
</template>

<style lang="scss" scoped>
.illustration {
  display: none;
  padding: 1.25rem;
  background-color: var(--white);
  width: 40%;
  max-width: 35rem;
  max-height: calc(100vh - 2.5rem);

  img {
    width: 100%;
    border-radius: 0.75rem;
    background-color: var(--grey-900);
  }
}

@media screen and (min-width: 64rem) {
  .illustration {
    display: flex;
  }
}
</style>
