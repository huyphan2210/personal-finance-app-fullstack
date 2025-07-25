<template>
  <shared-modal
    :heading="budgetModalHeadings[type](budgetCategory)"
    :message="budgetModalInstruction[type]"
    class="budget-modal"
    :is-modal-shown="isShown"
    v-on:on-close-modal="onCloseModal"
  >
    <form @submit="addNewBudget">
      <shared-input-text
        :type="InputEnumType.Number"
        prefix="$"
        label="Maximum Spending"
      />
    </form>
  </shared-modal>
</template>
<script lang="ts" setup>
import { BudgetCategoryEnum, BudgetColorThemeEnum } from "~/api/data-contracts";
import { type IBudgetModal } from "~/interfaces/budgets.interface";
import { InputEnumType } from "~/interfaces/shared.interface";
import {
  budgetModalHeadings,
  budgetModalInstruction,
} from "~/services/budgets.service";

const CLOSE_BUDGET_MODAL_EVENT = "on-close-modal";
const { isShown, type, budgetCategory } = defineProps<IBudgetModal>();
const emits = defineEmits([CLOSE_BUDGET_MODAL_EVENT]);

const form = ref<{
  category: BudgetCategoryEnum;
  maximumSpend: number;
  theme: BudgetColorThemeEnum;
}>();

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
