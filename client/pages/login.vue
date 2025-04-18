<template>
  <form class="form--login">
    <SharedPageHeading />
    <fieldset>
      <div class="form--login_field">
        <label class="form--login_field_label" for="email">Email</label>
        <input id="email" type="email" placeholder="johndoe@yopmail.com" />
      </div>
      <div class="form--login_field">
        <label class="form--login_field_label" for="password">Password</label>
        <input id="password" type="password" placeholder="***" />
      </div>
    </fieldset>
    <button type="submit">Login</button>
    <span>Need to create an account? <NuxtLink :to="Page.Signup">Sign Up</NuxtLink></span>
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
  display: flex;
  flex-direction: column;
  gap: 2rem;

  fieldset {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  &_field {
    &:focus-within &_label {
      color: var(--grey-900) !important;
    }
  }

  span {
    text-align: center;
    color: var(--grey-500);
    font-size: 0.875rem;

    a {
      font-weight: 700;
      color: var(--grey-900);
    }
  }
}

@media screen and (min-width: 48rem) {
  .form--login {
    padding: 2rem;
  }
}
</style>
