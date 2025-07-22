<template>
  <dialog class="modal" ref="modal">
    <hgroup class="modal_heading">
      <h2>{{ heading }}</h2>
      <button @click="handleCloseButton" type="button">
        <img
          src="../../assets/images/close-button.svg"
          loading="lazy"
          alt="Close Button"
        />
      </button>
    </hgroup>
    <p class="modal_message">{{ message }}</p>
    <slot></slot>
  </dialog>
</template>

<script lang="ts" setup>
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
</script>

<style lang="scss" scoped>
.modal {
  &[open] {
    display: grid;
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

    button {
      cursor: pointer;
      border: none;
      background: none;
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
