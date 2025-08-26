<template>
  <shared-modal
    :heading="potModalHeadings[type](targetPot?.name)"
    :message="potModalInstruction[type]"
    class="pot-modal--delete"
    :is-modal-shown="isShown"
    v-on:on-close-modal="onCloseModal"
  >
    <form class="pot-modal--delete_form" @submit="removePot">
      <shared-button
        class="pot-modal--delete_form_btn"
        type="submit"
        :is-loading="isLoading"
        :appearance="ButtonAppearanceEnum.Danger"
      >
        {{ potModalPrimaryButtonContent[type] }}
      </shared-button>
      <shared-button
        class="pot-modal--delete_form_btn"
        type="button"
        :is-loading="isLoading"
        :appearance="ButtonAppearanceEnum.Secondary"
        @click="() => onCloseModal(true)"
      >
        No, Go Back
      </shared-button>
    </form>
  </shared-modal>
</template>
<script lang="ts" setup>
import { ButtonAppearanceEnum } from "~/interfaces/shared.interface";
import { type DeletePot } from "~/api/data-contracts";
import {
  deletePot,
  potModalHeadings,
  potModalInstruction,
  potModalPrimaryButtonContent,
} from "~/services/pots.service";
import type { IDeletePotModal } from "~/interfaces/pots.interface";

const CLOSE_BUDGET_MODAL_EVENT = "on-close-modal";

const { isShown, type, targetPot } = defineProps<IDeletePotModal>();

const emits = defineEmits([CLOSE_BUDGET_MODAL_EVENT]);
const errorStore = useErrorStore();

const isLoading = ref<boolean>(false);

const onCloseModal = (isClosed: boolean, fetchData?: boolean) => {
  emits(CLOSE_BUDGET_MODAL_EVENT, fetchData);
};

const removePot = (e: Event) => {
  e.preventDefault();
  isLoading.value = true;
  const deletePotPayload: DeletePot = {
    id: targetPot?.id || "",
  };
  deletePot(deletePotPayload)
    .then(() => {
      onCloseModal(true, true);
    })
    .catch((message) => errorStore.setErrorMessage(message))
    .finally(() => {
      isLoading.value = false;
    });
};
</script>
<style lang="scss" scoped>
.pot-modal--delete {
  &_form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    &_btn {
      margin-top: 0.25rem;
    }
  }
}
</style>
