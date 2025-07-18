<template>
  <shared-modal
    modal-heading="Error"
    :is-modal-shown="errorStore.isError"
    v-on:on-close-modal="closeErrorModal"
  >
    {{ errorStore.message }}
  </shared-modal>
</template>

<script lang="ts" setup>
const errorStore = useErrorStore();
const closeErrorModal = (isClosed: boolean) => {
  if (isClosed) {
    errorStore.setErrorMessage("");
  }
};
</script>
