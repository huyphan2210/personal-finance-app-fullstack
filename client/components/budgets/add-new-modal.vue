<template>
  <shared-modal
    :heading="budgetModalHeadings[type]()"
    :message="budgetModalInstruction[type]"
    class="budget-modal--add-new"
    :is-modal-shown="isShown"
    v-on:on-close-modal="onCloseModal"
  >
    <form class="budget-modal--add-new_form" @submit="addNewBudget">
      <shared-modal-dropdown
        :settings="categoryDropdownSettings"
        label="Category"
      />
      <shared-input
        :type="InputEnumType.Number"
        prefix="$"
        label="Maximum Spending"
        :value="form.maximum.toString()"
        :custom-input-handler="setMaximumSpend"
      />
      <shared-modal-dropdown
        :settings="colorDropdownSettings"
        label="Color Tag"
      />
      <shared-button
        class="budget-modal--add-new_form_btn"
        type="submit"
        :is-loading="isLoading"
        :appearance="ButtonAppearanceEnum.Primary"
        :is-disabled="isButtonDisabled()"
      >
        {{ budgetModalPrimaryButtonContent[type] }}
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
  budgetModalPrimaryButtonContent,
  createBudget,
} from "~/services/budgets.service";

const CLOSE_BUDGET_MODAL_EVENT = "on-close-modal";

const { isShown, type, usedBudgets } = defineProps<IBudgetModal>();
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
    .finally(() => {
      isLoading.value = false;
    });
};

const setMaximumSpend = (e?: Event) => {
  if (form.value) {
    form.value.maximum = parseFloat(
      (e?.currentTarget as HTMLInputElement).value
    );
  }
};

const isButtonDisabled = () => {
  if (!form.value.maximum || form.value.maximum <= 0) {
    return true;
  }

  if (
    categoryDropdownSettings.value.options.find(
      (option) =>
        option.itemValue === form.value.category &&
        option.status === ModalDropdownItemStatus.Used
    )
  ) {
    return true;
  }

  if (
    colorDropdownSettings.value.options.find(
      (option) =>
        CreateBudgetColorThemeEnum[option.itemValue] ===
          form.value.colorTheme &&
        option.status === ModalDropdownItemStatus.Used
    )
  ) {
    return true;
  }

  return false;
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
    options: Object.keys(CreateBudgetColorThemeEnum)
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

const colorDropdownSettings = ref<IModalColorDropdownSettings>(
  dropdownSettingsRecords[
    ModalDropdownEnumType.Color
  ] as IModalColorDropdownSettings
);
const categoryDropdownSettings = ref<IModalTextDropdownSettings>(
  dropdownSettingsRecords[
    ModalDropdownEnumType.Text
  ] as IModalTextDropdownSettings
);
</script>
<style lang="scss" scoped>
.budget-modal--add-new {
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
