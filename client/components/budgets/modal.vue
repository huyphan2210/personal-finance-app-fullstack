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
      <shared-button
        class="budget-modal_form_btn"
        type="submit"
        :is-loading="isLoading"
        :appearance="ButtonAppearanceEnum.Primary"
      >
        Add Budget
      </shared-button>
    </form>
  </shared-modal>
</template>
<script lang="ts" setup>
import {
  ModalDropdownEnumType,
  ButtonAppearanceEnum,
  type IModalDropdownItem,
} from "~/interfaces/shared.interface";
import {
  BudgetCategoryEnum,
  BudgetColorThemeEnum,
  CreateBudgetCategoryEnum,
  CreateBudgetColorThemeEnum,
  type CreateBudget,
} from "~/api/data-contracts";
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
  createBudget,
} from "~/services/budgets.service";
import { Color } from "~/types/color";

const CLOSE_BUDGET_MODAL_EVENT = "on-close-modal";

const { isShown, type, targetBudgetCategory, usedBudgets } =
  defineProps<IBudgetModal>();
const emits = defineEmits([CLOSE_BUDGET_MODAL_EVENT]);
const errorStore = useErrorStore();
const form = ref<CreateBudget>({
  category: CreateBudgetCategoryEnum.Bills,
  maximum: 0,
  colorTheme: CreateBudgetColorThemeEnum.Cyan,
});

const isLoading = ref<boolean>(false);

const onCloseModal = (isClosed: boolean, fetchData?: boolean) => {
  emits(CLOSE_BUDGET_MODAL_EVENT, fetchData);
};

const addNewBudget = (e: Event) => {
  e.preventDefault();
  isLoading.value = true;
  createBudget(form.value)
    .then(() => onCloseModal(true, true))
    .catch((message) => errorStore.setErrorMessage(message))
    .finally(() => (isLoading.value = false));
};

const setMaximumSpend = (e?: Event) => {
  if (form.value) {
    form.value.maximum = parseFloat(
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
    options: Object.keys(CreateBudgetCategoryEnum)
      .map((value) => {
        const key = value as keyof typeof CreateBudgetCategoryEnum;
        const status = !usedBudgets
          .map((budget) => budget.category)
          .includes(BudgetCategoryEnum[key])
          ? CreateBudgetCategoryEnum[key] === form.value?.category
            ? ModalDropdownItemStatus.Selected
            : ModalDropdownItemStatus.Ready
          : ModalDropdownItemStatus.Used;
        if (status === ModalDropdownItemStatus.Selected) {
          form.value.category = CreateBudgetCategoryEnum[key];
        }
        return {
          itemValue: CreateBudgetCategoryEnum[key],
          itemLabel: CreateBudgetCategoryEnum[key],
          status,
          onSelect: (selectedCategory: string) => {
            if (form.value) {
              form.value.category =
                selectedCategory as CreateBudgetCategoryEnum;
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
        const key = value as keyof typeof CreateBudgetColorThemeEnum;
        const status = !usedBudgets
          .map((budget) => budget.colorTheme)
          .includes(BudgetColorThemeEnum[key])
          ? CreateBudgetColorThemeEnum[key] === form.value.colorTheme
            ? ModalDropdownItemStatus.Selected
            : ModalDropdownItemStatus.Ready
          : ModalDropdownItemStatus.Used;

        if (status === ModalDropdownItemStatus.Selected) {
          form.value.colorTheme = CreateBudgetColorThemeEnum[key];
        }
        return {
          itemValue: key,
          itemLabel: value,
          status: !usedBudgets
            .map((budget) => budget.colorTheme)
            .includes(BudgetColorThemeEnum[key])
            ? CreateBudgetColorThemeEnum[key] === form.value.colorTheme
              ? ModalDropdownItemStatus.Selected
              : ModalDropdownItemStatus.Ready
            : ModalDropdownItemStatus.Used,
          onSelect: (selectedColorKey: string) => {
            if (form.value) {
              form.value.colorTheme =
                CreateBudgetColorThemeEnum[
                  selectedColorKey as keyof typeof CreateBudgetColorThemeEnum
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
    &_btn {
      margin-top: 0.25rem;
    }
  }
}
</style>
