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
        :key="form.category"
        :settings="categoryDropdownSettings"
        :is-disabled="true"
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
        :key="form.colorTheme"
        :settings="colorDropdownSettings"
        :is-disabled="true"
        label="Color Tag"
      />
      <shared-button
        class="budget-modal_form_btn"
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
} from "~/interfaces/shared.interface";
import {
  CreateBudgetCategoryEnum,
  CreateBudgetColorThemeEnum,
  type CreateBudget,
} from "~/api/data-contracts";
import { type IBudgetEditModal } from "~/interfaces/budgets.interface";
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

const { isShown, type, targetBudgetCategory, editBudgetInfo } =
  defineProps<IBudgetEditModal>();
const emits = defineEmits([CLOSE_BUDGET_MODAL_EVENT]);
const errorStore = useErrorStore();
const form = ref<CreateBudget>({
  category: (editBudgetInfo?.category ||
    CreateBudgetCategoryEnum.Bills) as CreateBudgetCategoryEnum,
  maximum: editBudgetInfo?.maximum || 0,
  colorTheme: (editBudgetInfo?.colorTheme ||
    CreateBudgetColorThemeEnum.Cyan) as CreateBudgetColorThemeEnum,
});

const isLoading = ref<boolean>(false);

const onCloseModal = (isClosed: boolean, fetchData?: boolean) => {
  emits(CLOSE_BUDGET_MODAL_EVENT, fetchData);
};

const addNewBudget = (e: Event) => {
  e.preventDefault();
  isLoading.value = true;
  // createBudget(form.value)
  //   .then(() => onCloseModal(true, true))
  //   .catch((message) => errorStore.setErrorMessage(message))
  //   .finally(() => {
  //     isLoading.value = false;
  //   });
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

  return false;
};

const dropdownSettingsRecords: Record<
  ModalDropdownEnumType,
  () => IModalColorDropdownSettings | IModalTextDropdownSettings
> = {
  [ModalDropdownEnumType.Text]: () => ({
    type: ModalDropdownEnumType.Text,
    options: [
      {
        itemValue: form.value.category,
        itemLabel:
          Object.keys(CreateBudgetCategoryEnum).find(
            (key) =>
              CreateBudgetCategoryEnum[
                key as keyof typeof CreateBudgetCategoryEnum
              ] === form.value.category
          ) ?? Object.keys(CreateBudgetCategoryEnum)[0],
        status: ModalDropdownItemStatus.Selected,
        onSelect: () => {},
      },
    ],
  }),
  [ModalDropdownEnumType.Color]: () => ({
    type: ModalDropdownEnumType.Color,
    options: [
      {
        itemValue: (Object.keys(CreateBudgetColorThemeEnum).find(
          (key) =>
            CreateBudgetColorThemeEnum[
              key as keyof typeof CreateBudgetColorThemeEnum
            ] === form.value.colorTheme
        ) || "Cyan") as keyof typeof CreateBudgetColorThemeEnum,
        itemLabel:
          Object.keys(CreateBudgetColorThemeEnum).find(
            (key) =>
              CreateBudgetColorThemeEnum[
                key as keyof typeof CreateBudgetColorThemeEnum
              ] === form.value.colorTheme
          ) || "Cyan",
        status: ModalDropdownItemStatus.Selected,
        onSelect: () => {},
      },
    ],
  }),
};

const colorDropdownSettings = ref<IModalColorDropdownSettings>(
  dropdownSettingsRecords[
    ModalDropdownEnumType.Color
  ]() as IModalColorDropdownSettings
);
const categoryDropdownSettings = ref<IModalTextDropdownSettings>(
  dropdownSettingsRecords[
    ModalDropdownEnumType.Text
  ]() as IModalTextDropdownSettings
);

const reassignValuesToForm = () => {
  form.value = {
    category: (editBudgetInfo?.category ||
      CreateBudgetCategoryEnum.Bills) as CreateBudgetCategoryEnum,
    maximum: editBudgetInfo?.maximum || 0,
    colorTheme: (editBudgetInfo?.colorTheme ||
      CreateBudgetColorThemeEnum.Cyan) as CreateBudgetColorThemeEnum,
  };
  colorDropdownSettings.value = dropdownSettingsRecords[
    ModalDropdownEnumType.Color
  ]() as IModalColorDropdownSettings;
  categoryDropdownSettings.value = dropdownSettingsRecords[
    ModalDropdownEnumType.Text
  ]() as IModalTextDropdownSettings;
};

watch(() => editBudgetInfo, reassignValuesToForm);
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
