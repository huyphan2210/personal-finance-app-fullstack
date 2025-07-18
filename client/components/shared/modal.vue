<template>
  <dialog class="modal" ref="modal">
    <hgroup>
      <h2>{{ modalHeading }}</h2>
      <button @click="handleCloseButton" type="button">
        <img
          src="../../assets/images/close-button.svg"
          loading="lazy"
          alt="Close Button"
        />
      </button>
    </hgroup>
    <slot></slot>
  </dialog>
</template>

<script lang="ts" setup>
const modal = ref<HTMLDialogElement>();

const props = defineProps<{
  modalHeading: string;
  isModalShown: boolean;
}>();

const CLOSE_MODAL_EVENT = "on-close-modal";

const emits = defineEmits([CLOSE_MODAL_EVENT]);

const handleCloseButton = () => {
  emits(CLOSE_MODAL_EVENT, true);
};

watch(
  () => props.isModalShown,
  (isModalShown) => {
    if (isModalShown) {
      modal.value?.showModal();
    } else {
      modal.value?.close();
    }
  }
);
</script>

<style lang="scss" scoped>
.modal {
  @include modal-style;
}
</style>
