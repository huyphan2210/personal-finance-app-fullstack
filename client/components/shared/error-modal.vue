<template>
  <SharedModal modal-heading="Error" :is-modal-shown="errorStore.isError" v-on:close-modal="closeErrorModal">
    {{ errorStore.message }}
  </SharedModal>
</template>

<script lang="ts" setup>
const errorStore = useErrorStore();
const closeErrorModal = (isClosed: boolean) => {
  if (isClosed) {
    errorStore.setErrorMessage('');
  }
}
</script>