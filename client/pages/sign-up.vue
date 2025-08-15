<template>
  <form @submit="createAccount" class="form--signup">
    <SharedPageHeading />
    <fieldset>
      <shared-input
        label="Name"
        :type="InputEnumType.Text"
        v-on:on-value-change="setName"
      />
      <shared-input
        :type="InputEnumType.Email"
        v-on:on-value-change="setEmail"
      />
      <shared-input
        label="Create Password"
        :type="InputEnumType.Password"
        v-on:on-value-change="setPassword"
      >
        <small class="form--signup_field_tip">
          Passwords must be at least 8 characters
        </small>
      </shared-input>
    </fieldset>
    <shared-button
      type="submit"
      :appearance="ButtonAppearanceEnum.Primary"
      :is-loading="isLoading"
    >
      Create Account
    </shared-button>
    <span
      >Already have an account?
      <NuxtLink :to="Page.Login">Login</NuxtLink></span
    >
  </form>
</template>

<script lang="ts" setup>
import {
  InputEnumType,
  ButtonAppearanceEnum,
} from "~/interfaces/shared.interface";
const errorStore = useErrorStore();
const { signUp, setActive } = useSignUp();

const name = ref("");
const email = ref("");
const password = ref("");
const isLoading = ref<boolean>(false);

const setName = (value: string) => {
  name.value = value;
};

const setEmail = (value: string) => {
  email.value = value;
};

const setPassword = (value: string) => {
  password.value = value;
};

const createAccount = async (e: Event) => {
  e.preventDefault();
  isLoading.value = true;
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
  } finally {
    isLoading.value = false;
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

  &_field {
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
