<template>
  <dialog class="modal" ref="modal">
    <hgroup class="modal_heading">
      <h2>{{ heading }}</h2>
      <shared-button
        type="button"
        class="modal_heading_close-btn"
        :appearance="ButtonAppearanceEnum.Secondary"
        :on-click="handleCloseButton"
        ><img
          src="../../../assets/images/close-button.svg"
          loading="lazy"
          alt="Close Button"
      /></shared-button>
    </hgroup>
    <p class="modal_message">{{ message }}</p>
    <slot></slot>
  </dialog>
</template>

<script lang="ts" setup>
import { ButtonAppearanceEnum } from "~/interfaces/shared.interface";

const modal = ref<HTMLDialogElement>();

const props = defineProps<{
  heading: string;
  message: string;
  isModalShown: boolean;
}>();

const CLOSE_MODAL_EVENT = "on-close-modal";

const emits = defineEmits([CLOSE_MODAL_EVENT]);

const handleCloseButton = () => {
  emits(CLOSE_MODAL_EVENT, true);
};

const handleModal = (isModalShown?: boolean) => {
  if (isModalShown) {
    modal.value?.showModal();
  } else {
    modal.value?.close();
  }
};
handleModal(props.isModalShown);
watch(() => props.isModalShown, handleModal);

onMounted(() => {
  modal.value?.addEventListener("close", handleCloseButton);
});

onUnmounted(() => {
  modal.value?.removeEventListener("close", handleCloseButton);
});
</script>

<style lang="scss" scoped>
.modal {
  &[open] {
    display: grid;
    overflow: visible;
    animation: show-up 0.3s ease-in-out;
    &::backdrop {
      animation: show-up-backdrop 0.3s ease-in-out;
    }
  }

  gap: 1.25rem;
  margin: auto;
  border: none;
  border-radius: 0.75rem;
  padding: 1.5rem 1.25rem;
  width: calc(100% - 2.5rem - 2rem);
  max-width: 32.5rem;

  &_heading {
    display: flex;
    justify-content: space-between;
    align-items: center;

    h2 {
      @include text-preset-1;
      color: var(--grey-900);
    }

    &_close-btn {
      display: flex;
    }
  }

  &::backdrop {
    background-color: #000;
    opacity: 0.5;
  }

  &_message {
    @include text-preset-4;
    color: var(--grey-500);
  }
}

@media screen and (min-width: 48rem) {
  .modal {
    padding: 2rem;
    max-width: 31rem;
  }
}

@keyframes show-up-backdrop {
  from {
    opacity: 0;
  }

  to {
    opacity: 0.5;
  }
}

@keyframes show-up {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}
</style>
