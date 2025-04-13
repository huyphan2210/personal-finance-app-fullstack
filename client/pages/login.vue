<template>
  <form class="form--login">
    <SharedPageHeading />
  </form>
</template>

<script lang="ts" setup></script>

<style lang="scss" scoped>
.form--login {
  background-color: var(--white);
  padding: 1.5rem 1.25rem;
  width: clamp(303px, 73vw, 31rem);
  margin: auto;
  border-radius: 0.75rem;
}

@media screen and (min-width: 48rem) {
  .form--login {
    padding: 2rem;
  }
}
</style>
