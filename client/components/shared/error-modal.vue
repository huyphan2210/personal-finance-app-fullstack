<template>
  <shared-modal
    heading="Error"
    :is-modal-shown="errorStore.isError"
    :message="errorStore.message"
    v-on:on-close-modal="closeErrorModal"
  />
</template>

<script lang="ts" setup>
const errorStore = useErrorStore();
const closeErrorModal = (isClosed: boolean) => {
  if (isClosed) {
    errorStore.setErrorMessage("");
  }
};
</script>
