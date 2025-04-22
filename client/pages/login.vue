<template>
  <form @submit="login" class="form--login">
    <SharedPageHeading />
    <fieldset>
      <div class="form--login_field">
        <label class="form--login_field_label" for="email">Email</label>
        <input required v-model="email" id="email" type="email" placeholder="johndoe@yopmail.com" />
      </div>
      <div class="form--login_field">
        <label class="form--login_field_label" for="password">Password</label>
        <input required v-model="password" id="password" type="password" placeholder="***" />
      </div>
    </fieldset>
    <button type="submit">Login</button>
    <span>Need to create an account? <NuxtLink :to="Page.Signup">Sign Up</NuxtLink></span>
  </form>
</template>

<script lang="ts" setup>
const errorStore = useErrorStore();
const { signIn, setActive } = useSignIn();

const email = ref('');
const password = ref('');

const login = async (e: Event) => {
  e.preventDefault();

  try {
    const result = await signIn.value?.create({
      identifier: email.value,
      password: password.value,
    })

    if (result?.status === 'complete' && setActive.value) {
      await setActive.value({ session: result?.createdSessionId })
    }
  } catch (error) {
    const err = error as any;
    if (err.status && err.status === 422) {
      errorStore.setErrorMessage("Your email or password is incorrect.");
    }
  }
}

</script>

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
    @include text-preset-4;

    a {
      color: var(--grey-900);
      @include text-preset-4-bold;
    }
  }
}

@media screen and (min-width: 48rem) {
  .form--login {
    padding: 2rem;
  }
}
</style>
