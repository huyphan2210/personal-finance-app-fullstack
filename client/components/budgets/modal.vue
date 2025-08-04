<template>
  <shared-modal
    :heading="budgetModalHeadings[type](targetBudgetCategory)"
    :message="budgetModalInstruction[type]"
    class="budget-modal"
    :is-modal-shown="isShown"
    v-on:on-close-modal="onCloseModal"
  >
    <form class="budget-modal_form" @submit="addNewBudget">
      <shared-modal-dropdown
        :settings="dropdownSettingsRecords[ModalDropdownEnumType.Text]"
        label="Category"
      />
      <shared-input
        :type="InputEnumType.Number"
        prefix="$"
        label="Maximum Spending"
      />
      <shared-modal-dropdown
        :settings="dropdownSettingsRecords[ModalDropdownEnumType.Color]"
        label="Color Tag"
      />
    </form>
  </shared-modal>
</template>
<script lang="ts" setup>
import { ModalDropdownEnumType } from "~/interfaces/shared.interface";
import { BudgetCategoryEnum, BudgetColorThemeEnum } from "~/api/data-contracts";
import { type IBudgetModal } from "~/interfaces/budgets.interface";
import {
  InputEnumType,
  ModalDropdownItemStatus,
  type IModalColorDropdownSettings,
  type IModalTextDropdownSettings,
} from "~/interfaces/shared.interface";
import {
  budgetModalHeadings,
  budgetModalInstruction,
} from "~/services/budgets.service";
import { Color } from "~/types/color";

const CLOSE_BUDGET_MODAL_EVENT = "on-close-modal";
const { isShown, type, targetBudgetCategory, usedBudgets } =
  defineProps<IBudgetModal>();
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

const dropdownSettingsRecords: Record<
  ModalDropdownEnumType,
  IModalColorDropdownSettings | IModalTextDropdownSettings
> = {
  [ModalDropdownEnumType.Text]: {
    type: ModalDropdownEnumType.Text,
    options: Object.keys(BudgetCategoryEnum).map((value) => {
      const key = value as keyof typeof BudgetCategoryEnum;
      return {
        itemValue: BudgetCategoryEnum[key],
        itemLabel: BudgetCategoryEnum[key],
        status: !usedBudgets
          .map((budget) => budget.category)
          .includes(BudgetCategoryEnum[key])
          ? ModalDropdownItemStatus.Ready
          : ModalDropdownItemStatus.Selected,
        onSelect: (selectedCategory: string) => {
          if (form.value) {
            form.value.category = selectedCategory as BudgetCategoryEnum;
          }
        },
      };
    }),
  },
  [ModalDropdownEnumType.Color]: {
    type: ModalDropdownEnumType.Color,
    options: Object.keys(Color).map((value) => {
      const key = value as keyof typeof BudgetColorThemeEnum;
      return {
        itemValue: key,
        itemLabel: value,
        status: !usedBudgets
          .map((budget) => budget.colorTheme)
          .includes(BudgetColorThemeEnum[key])
          ? ModalDropdownItemStatus.Ready
          : ModalDropdownItemStatus.Selected,
        onSelect: (selectedColorKey: string) => {
          if (form.value) {
            form.value.theme =
              BudgetColorThemeEnum[
                selectedColorKey as keyof typeof BudgetColorThemeEnum
              ];
          }
        },
      };
    }),
  },
};

// const handleS
</script>
<style lang="scss" scoped>
.budget-modal {
  &_form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
}
</style>
