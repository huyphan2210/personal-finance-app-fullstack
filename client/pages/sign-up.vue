<template>
  <form @submit="createAccount" class="form--signup">
    <SharedPageHeading />
    <fieldset>
      <div class="form--signup_field">
        <label class="form--signup_field_label" for="name">Name</label>
        <input
          required
          v-model="name"
          id="name"
          type="text"
          placeholder="John Doe"
        />
      </div>
      <div class="form--signup_field">
        <label class="form--signup_field_label" for="email">Email</label>
        <input
          required
          v-model="email"
          id="email"
          type="email"
          placeholder="johndoe@yopmail.com"
        />
      </div>
      <div class="form--signup_field">
        <label class="form--signup_field_label" for="password">Password</label>
        <input
          required
          v-model="password"
          minlength="8"
          id="password"
          type="password"
          placeholder="********"
        />
        <small class="form--signup_field_tip"
          >Passwords must be at least 8 characters</small
        >
      </div>
    </fieldset>
    <button type="submit">Create Account</button>
    <span
      >Already have an account?
      <NuxtLink :to="Page.Login">Login</NuxtLink></span
    >
  </form>
</template>

<script lang="ts" setup>
const errorStore = useErrorStore();
const { signUp, setActive } = useSignUp();

const name = ref("");
const email = ref("");
const password = ref("");

const createAccount = async (e: Event) => {
  e.preventDefault();

  try {
    const result = await signUp.value?.create({
      emailAddress: email.value,
      password: password.value,
    });

    if (result?.status === "complete" && setActive.value) {
      await setActive.value({ session: result?.createdSessionId });
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
.form--signup {
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

  &_field {
    input {
      width: calc(100% - 2.5rem - 2px);
    }
    &:focus-within &_label {
      color: var(--grey-900) !important;
    }

    &_tip {
      display: block;
      text-align: right;
      margin-top: 0.25rem;
      color: var(--grey-500);

      @include text-preset-5;
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
  .form--signup {
    padding: 2rem;
    max-width: 31rem;
  }
}
</style>
