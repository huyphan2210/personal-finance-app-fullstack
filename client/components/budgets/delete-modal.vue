<template>
  <shared-modal
    :heading="budgetModalHeadings[type](deleteBudgetInfo?.category)"
    :message="budgetModalInstruction[type]"
    class="budget-modal--delete"
    :is-modal-shown="isShown"
    v-on:on-close-modal="onCloseModal"
  >
    <form class="budget-modal--delete_form" @submit="removeBudget">
      <shared-button
        class="budget-modal--delete_form_btn"
        type="submit"
        :is-loading="isLoading"
        :appearance="ButtonAppearanceEnum.Danger"
      >
        {{ budgetModalPrimaryButtonContent[type] }}
      </shared-button>
      <shared-button
        class="budget-modal--delete_form_btn"
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
import {
  type DeleteBudget,
} from "~/api/data-contracts";
import { type IBudgetDeleteModal } from "~/interfaces/budgets.interface";
import {
  budgetModalHeadings,
  budgetModalInstruction,
  budgetModalPrimaryButtonContent,
  deleteBudget,
} from "~/services/budgets.service";

const CLOSE_BUDGET_MODAL_EVENT = "on-close-modal";

const { isShown, type, deleteBudgetInfo } = defineProps<IBudgetDeleteModal>();

const emits = defineEmits([CLOSE_BUDGET_MODAL_EVENT]);
const errorStore = useErrorStore();

const isLoading = ref<boolean>(false);

const onCloseModal = (isClosed: boolean, fetchData?: boolean) => {
  emits(CLOSE_BUDGET_MODAL_EVENT, fetchData);
};

const removeBudget = (e: Event) => {
  e.preventDefault();
  isLoading.value = true;
  const deleteBudgetPayload: DeleteBudget = {
    id: deleteBudgetInfo?.id || "",
  };
  deleteBudget(deleteBudgetPayload)
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
.budget-modal--delete {
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
