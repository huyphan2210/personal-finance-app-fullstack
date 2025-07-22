<template>
  <shared-modal
    :heading="budgetModalHeadings[type](budgetCategory)"
    :message="budgetModalInstruction[type]"
    class="budget-modal"
    :is-modal-shown="isShown"
    v-on:on-close-modal="onCloseModal"
  >
    <form @submit="addNewBudget"></form>
  </shared-modal>
</template>
<script lang="ts" setup>
import { type IBudgetModal } from "~/interfaces/budgets.interface";
import {
  budgetModalHeadings,
  budgetModalInstruction,
} from "~/services/budgets.service";

const CLOSE_BUDGET_MODAL_EVENT = "on-close-modal";
const { isShown, type, budgetCategory } = defineProps<IBudgetModal>();
const emits = defineEmits([CLOSE_BUDGET_MODAL_EVENT]);
const onCloseModal = (isClosed: boolean) => {
  emits(CLOSE_BUDGET_MODAL_EVENT, isClosed);
};
const addNewBudget = (e: Event) => {
  e.preventDefault();
};

// const handleS
</script>
<style lang="scss" scoped>
.budget-modal {
  &_instruction {
    @include text-preset-4;
    color: var(--grey-500);
  }
}
</style>
