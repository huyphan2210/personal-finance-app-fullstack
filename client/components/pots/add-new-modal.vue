<template>
  <shared-modal
    :heading="potModalHeadings[type]()"
    :message="potModalInstruction[type]"
    class="pot-modal--add-new"
    :is-modal-shown="isShown"
    v-on:on-close-modal="onCloseModal"
  >
    <form class="pot-modal--add-new_form" @submit="addNewPot">
      <shared-input
        :type="InputEnumType.Text"
        :max-length="30"
        label="Pot Name"
        :value="form.potName"
        :custom-input-handler="setPotName"
        placeholder="e.g. Rainy Days"
      >
        <small class="pot-modal--add-new_form_field_tip">
          {{ POT_NAME_MAX_LENGTH - form.potName.length }}
          character{{
            POT_NAME_MAX_LENGTH - form.potName.length > 1 ? "s" : ""
          }}
          left
        </small>
      </shared-input>
      <shared-input
        :type="InputEnumType.Number"
        prefix="$"
        label="Target"
        placeholder="e.g. 2000"
        :value="form.target.toString()"
        :custom-input-handler="setTarget"
      />
      <shared-modal-dropdown :settings="colorDropdownSettings" label="Theme" />
      <shared-button
        class="pot-modal--add-new_form_btn"
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
} from "~/interfaces/shared.interface";
import type { IPotModal } from "~/interfaces/pots.interface";
import {
  potModalHeadings,
  potModalInstruction,
  potModalPrimaryButtonContent,
} from "~/services/pots.service";
import { PotColorThemeEnum } from "~/api/data-contracts";
const CLOSE_POT_MODAL_EVENT = "on-close-modal";
const POT_NAME_MAX_LENGTH = 30;
const { isShown, type, usedPots } = defineProps<IPotModal>();
const emits = defineEmits([CLOSE_POT_MODAL_EVENT]);
const isLoading = ref(false);

const onCloseModal = (isClosed: boolean, fetchData?: boolean) => {
  emits(CLOSE_POT_MODAL_EVENT, fetchData);
};

const form = ref({
  potName: "",
  target: 0,
  colorTheme: PotColorThemeEnum.Cyan,
});

const sortItems = (
  firstItem: IModalDropdownItem,
  secondItem: IModalDropdownItem
) => {
  const statusCompare = firstItem.status - secondItem.status;
  if (statusCompare !== 0) return statusCompare;
  return firstItem.itemLabel.localeCompare(secondItem.itemLabel);
};

const colorDropdownSettings = {
  type: ModalDropdownEnumType.Color,
  options: Object.keys(PotColorThemeEnum)
    .map((value) => {
      const key = value as keyof typeof PotColorThemeEnum;
      const status = !usedPots
        .map((pot) => pot.colorTheme)
        .includes(PotColorThemeEnum[key])
        ? PotColorThemeEnum[key] === form.value.colorTheme
          ? ModalDropdownItemStatus.Selected
          : ModalDropdownItemStatus.Ready
        : ModalDropdownItemStatus.Used;

      if (status === ModalDropdownItemStatus.Selected) {
        form.value.colorTheme = PotColorThemeEnum[key];
      }
      return {
        itemValue: key,
        itemLabel: value,
        status: !usedPots
          .map((pot) => pot.colorTheme)
          .includes(PotColorThemeEnum[key])
          ? PotColorThemeEnum[key] === form.value.colorTheme
            ? ModalDropdownItemStatus.Selected
            : ModalDropdownItemStatus.Ready
          : ModalDropdownItemStatus.Used,
        onSelect: (selectedColorKey: string) => {
          if (form.value) {
            form.value.colorTheme =
              PotColorThemeEnum[
                selectedColorKey as keyof typeof PotColorThemeEnum
              ];
          }
        },
      };
    })
    .sort(sortItems),
};

const isButtonDisabled = () => {
  if (!form.value.potName || !form.value.target || form.value.target <= 0) {
    return true;
  }

  if (
    colorDropdownSettings.options.find(
      (option) =>
        PotColorThemeEnum[option.itemValue] === form.value.colorTheme &&
        option.status === ModalDropdownItemStatus.Used
    )
  ) {
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
  form.value.potName = value;
};
const addNewPot = (e?: Event) => {
  e?.preventDefault();
};
</script>
<style lang="scss" scoped>
.pot-modal--add-new {
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
