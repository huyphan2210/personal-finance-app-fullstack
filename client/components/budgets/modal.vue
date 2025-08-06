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
        :custom-input-handler="setMaximumSpend"
      />
      <shared-modal-dropdown
        :settings="dropdownSettingsRecords[ModalDropdownEnumType.Color]"
        label="Color Tag"
      />
    </form>
  </shared-modal>
</template>
<script lang="ts" setup>
import {
  ModalDropdownEnumType,
  type IModalDropdownItem,
} from "~/interfaces/shared.interface";
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
}>({
  category: BudgetCategoryEnum.Bills,
  maximumSpend: 0,
  theme: BudgetColorThemeEnum.Cyan,
});

const onCloseModal = (isClosed: boolean) => {
  emits(CLOSE_BUDGET_MODAL_EVENT, isClosed);
};

const addNewBudget = (e: Event) => {
  e.preventDefault();
};

const setMaximumSpend = (e?: Event) => {
  if (form.value) {
    form.value.maximumSpend = parseFloat(
      (e?.currentTarget as HTMLInputElement).value
    );
  }
};

const sortItems = (
  firstItem: IModalDropdownItem,
  secondItem: IModalDropdownItem
) => {
  const statusCompare = firstItem.status - secondItem.status;
  if (statusCompare !== 0) return statusCompare;
  return firstItem.itemLabel.localeCompare(secondItem.itemLabel);
};

const dropdownSettingsRecords: Record<
  ModalDropdownEnumType,
  IModalColorDropdownSettings | IModalTextDropdownSettings
> = {
  [ModalDropdownEnumType.Text]: {
    type: ModalDropdownEnumType.Text,
    options: Object.keys(BudgetCategoryEnum)
      .map((value) => {
        const key = value as keyof typeof BudgetCategoryEnum;
        const status = !usedBudgets
          .map((budget) => budget.category)
          .includes(BudgetCategoryEnum[key])
          ? BudgetCategoryEnum[key] === form.value?.category
            ? ModalDropdownItemStatus.Selected
            : ModalDropdownItemStatus.Ready
          : ModalDropdownItemStatus.Used;
        if (status === ModalDropdownItemStatus.Selected) {
          form.value.category = BudgetCategoryEnum[key];
        }
        return {
          itemValue: BudgetCategoryEnum[key],
          itemLabel: BudgetCategoryEnum[key],
          status,
          onSelect: (selectedCategory: string) => {
            if (form.value) {
              form.value.category = selectedCategory as BudgetCategoryEnum;
            }
          },
        };
      })
      .sort(sortItems),
  },
  [ModalDropdownEnumType.Color]: {
    type: ModalDropdownEnumType.Color,
    options: Object.keys(Color)
      .map((value) => {
        const key = value as keyof typeof BudgetColorThemeEnum;
        const status = !usedBudgets
          .map((budget) => budget.colorTheme)
          .includes(BudgetColorThemeEnum[key])
          ? BudgetColorThemeEnum[key] === form.value.theme
            ? ModalDropdownItemStatus.Selected
            : ModalDropdownItemStatus.Ready
          : ModalDropdownItemStatus.Used;

        if (status === ModalDropdownItemStatus.Selected) {
          form.value.theme = BudgetColorThemeEnum[key];
        }
        return {
          itemValue: key,
          itemLabel: value,
          status: !usedBudgets
            .map((budget) => budget.colorTheme)
            .includes(BudgetColorThemeEnum[key])
            ? BudgetColorThemeEnum[key] === form.value.theme
              ? ModalDropdownItemStatus.Selected
              : ModalDropdownItemStatus.Ready
            : ModalDropdownItemStatus.Used,
          onSelect: (selectedColorKey: string) => {
            if (form.value) {
              form.value.theme =
                BudgetColorThemeEnum[
                  selectedColorKey as keyof typeof BudgetColorThemeEnum
                ];
            }
          },
        };
      })
      .sort(sortItems),
  },
};
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
