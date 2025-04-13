<template>
  <aside class="illustration"></aside>
</template>

<style lang="scss" scoped>
.illustration {
  display: none;
  padding: 1.25rem;
  background-color: var(--white);
}

@media screen and (min-width: 96rem) {
  .illustration {
    display: unset;
  }
}
</style>