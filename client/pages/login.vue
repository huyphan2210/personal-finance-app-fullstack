<template>
  <form @submit="login" class="form--login">
    <SharedPageHeading />
    <fieldset>
      <shared-input
        :type="InputEnumType.Email"
        v-on:on-value-change="setEmail"
      />
      <shared-input
        :type="InputEnumType.Password"
        v-on:on-value-change="setPassword"
      />
    </fieldset>
    <button type="submit">Login</button>
    <span
      >Need to create an account?
      <NuxtLink :to="Page.Signup">Sign Up</NuxtLink></span
    >
  </form>
</template>

<script lang="ts" setup>
import { InputEnumType } from "~/interfaces/shared.interface";

const errorStore = useErrorStore();
const { signIn, setActive } = useSignIn();

const email = ref("");
const password = ref("");

const setEmail = (value: string) => {
  email.value = value;
};

const setPassword = (value: string) => {
  password.value = value;
};

const login = async (e: Event) => {
  e.preventDefault();

  try {
    const result = await signIn.value?.create({
      identifier: email.value,
      password: password.value,
      redirectUrl: Page.Overview,
    });

    if (result?.status === "complete" && setActive.value) {
      await setActive.value({ session: result?.createdSessionId });
      navigateTo(Page.Overview);
    }
  } catch (error) {
    const err = error as any;
    if (err.status && err.status === 422) {
      errorStore.setErrorMessage("Your email or password is incorrect.");
    }
  }
};
</script>

<style lang="scss" scoped>
.form--login {
  background-color: var(--white);
  padding: 1.5rem 1.25rem;
  width: calc(100% - 2.5rem);
  max-width: 32.5rem;
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

  button {
    @include button-style;
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
    width: calc(100% - 4rem);
    max-width: 31rem;
  }
}
</style>
