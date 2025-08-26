<template>
  <shared-modal
    :heading="potModalHeadings[type]()"
    :message="potModalInstruction[type]"
    class="pot-modal--edit"
    :is-modal-shown="isShown"
    v-on:on-close-modal="onCloseModal"
  >
    <form class="pot-modal--edit_form" @submit="editPot">
      <shared-input
        :type="InputEnumType.Text"
        :max-length="30"
        label="Pot Name"
        :value="form.name"
        :custom-input-handler="setPotName"
        placeholder="e.g. Rainy Days"
      >
        <small class="pot-modal--edit_form_field_tip">
          {{ POT_NAME_MAX_LENGTH - (form.name?.length || 0) }}
          character{{
            POT_NAME_MAX_LENGTH - (form.name?.length || 0) > 1 ? "s" : ""
          }}
          left
        </small>
      </shared-input>
      <shared-input
        :type="InputEnumType.Number"
        prefix="$"
        label="Target"
        placeholder="e.g. 2000"
        :value="form.target?.toString()"
        :custom-input-handler="setTarget"
      />
      <shared-modal-dropdown
        :key="targetPot?.id"
        :settings="colorDropdownSettings"
        label="Theme"
      />
      <shared-button
        class="pot-modal--edit_form_btn"
        type="submit"
        :is-loading="isLoading"
        :appearance="ButtonAppearanceEnum.Primary"
        :is-disabled="isButtonDisabled()"
      >
        {{ potModalPrimaryButtonContent[type] }}
      </shared-button>
    </form>
  </shared-modal>
</template>
<script lang="ts" setup>
import {
  InputEnumType,
  ButtonAppearanceEnum,
  ModalDropdownEnumType,
  ModalDropdownItemStatus,
  type IModalDropdownItem,
  type IModalColorDropdownSettings,
  type IModalDropdownColorItem,
} from "~/interfaces/shared.interface";
import type { IEditPotModal } from "~/interfaces/pots.interface";
import {
  potModalHeadings,
  potModalInstruction,
  potModalPrimaryButtonContent,
  updatePot,
} from "~/services/pots.service";
import {
  UpdatePotColorThemeEnum,
  PotColorThemeEnum,
  type UpdatePot,
} from "~/api/data-contracts";
const CLOSE_POT_MODAL_EVENT = "on-close-modal";
const POT_NAME_MAX_LENGTH = 30;
const { isShown, type, usedPots, targetPot } = defineProps<IEditPotModal>();
const emits = defineEmits([CLOSE_POT_MODAL_EVENT]);

const errorStore = useErrorStore();
const isLoading = ref(false);

const onCloseModal = (isClosed: boolean, fetchData?: boolean) => {
  emits(CLOSE_POT_MODAL_EVENT, fetchData);
};

const form = ref<UpdatePot>({
  id: targetPot?.id || "",
  name: targetPot?.name,
  target: targetPot?.target,
  colorTheme:
    (targetPot?.colorTheme as unknown as UpdatePotColorThemeEnum) ??
    UpdatePotColorThemeEnum.Cyan,
});
let originalFormValue = { ...form.value };

const sortItems = (
  firstItem: IModalDropdownItem,
  secondItem: IModalDropdownItem
) => {
  const statusCompare = firstItem.status - secondItem.status;
  if (statusCompare !== 0) return statusCompare;
  return firstItem.itemLabel.localeCompare(secondItem.itemLabel);
};

const getColorDropdownSettings = (): IModalColorDropdownSettings => ({
  type: ModalDropdownEnumType.Color,
  options: Object.keys(PotColorThemeEnum)
    .map((value) => {
      const key = value as keyof typeof PotColorThemeEnum;
      const usedColors = usedPots.map((pot) => pot.colorTheme);
      let status = ModalDropdownItemStatus.Ready;
      if (
        usedColors.includes(PotColorThemeEnum[key]) &&
        form.value.colorTheme === UpdatePotColorThemeEnum[key]
      ) {
        status = ModalDropdownItemStatus.Selected;
      } else if (usedColors.includes(PotColorThemeEnum[key])) {
        status = ModalDropdownItemStatus.Used;
      }

      return {
        itemValue: key,
        itemLabel: value,
        status,
        onSelect: (selectedColorKey: string) => {
          if (form.value) {
            form.value.colorTheme =
              UpdatePotColorThemeEnum[
                selectedColorKey as keyof typeof UpdatePotColorThemeEnum
              ];
          }
        },
      };
    })
    .sort(sortItems),
});

const colorDropdownSettings = ref<IModalColorDropdownSettings>(
  getColorDropdownSettings()
);

const isButtonDisabled = () => {
  if (!form.value.name || !form.value.target || form.value.target <= 0) {
    return true;
  }

  if (
    colorDropdownSettings.value.options.find(
      (option) =>
        UpdatePotColorThemeEnum[option.itemValue] === form.value.colorTheme &&
        option.status === ModalDropdownItemStatus.Used
    )
  ) {
    return true;
  }

  if (JSON.stringify(form.value) === JSON.stringify(originalFormValue)) {
    return true;
  }
  
  return false;
};

const setTarget = (e?: Event) => {
  const value = (e?.currentTarget as HTMLInputElement)?.value;
  form.value.target = parseFloat(value);
};
const setPotName = (e?: Event) => {
  const value = (e?.currentTarget as HTMLInputElement)?.value;
  form.value.name = value;
};
const editPot = (e?: Event) => {
  e?.preventDefault();
  isLoading.value = true;
  updatePot(form.value)
    .then(() => onCloseModal(true, true))
    .catch((message) => errorStore.setErrorMessage(message))
    .finally(() => (isLoading.value = false));
};

watch(
  () => targetPot,
  (value) => {
    form.value = {
      id: value?.id || "",
      name: value?.name,
      target: value?.target,
      colorTheme:
        (value?.colorTheme as unknown as UpdatePotColorThemeEnum) ??
        UpdatePotColorThemeEnum.Cyan,
    };
    originalFormValue = { ...form.value };
    colorDropdownSettings.value = getColorDropdownSettings();
  }
);
</script>
<style lang="scss" scoped>
.pot-modal--edit {
  &_form {
    display: flex;
    flex-direction: column;
    gap: 1rem;

    &_btn {
      margin-top: 0.25rem;
    }

    &_field {
      &_tip {
        @include text-preset-5;
        display: block;
        text-align: right;
        margin-top: 0.25rem;
        color: var(--grey-500);
      }
    }
  }
}
</style>
