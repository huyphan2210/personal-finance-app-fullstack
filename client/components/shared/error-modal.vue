<template>
  <dialog class="error-modal" ref="modal">
    {{ errorStore.message }}
  </dialog>
</template>

<script lang="ts" setup>
const modal = ref<HTMLDialogElement>()

const errorStore = useErrorStore();
watch(() => errorStore.isError, (isError) => {
  if (isError) {
    modal.value?.showModal();
  } else {
    modal.value?.close();
  }
})
</script>

<style lang="scss" scoped>
.error-modal {
  margin: auto;

  &::backdrop {
    background-color: #000;
    opacity: 0.5;
  }
}
</style>