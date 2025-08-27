<template>
  <shared-modal
    :heading="potModalHeadings[type]()"
    :message="potModalInstruction[type]"
    class="pot-modal--update-total"
    :is-modal-shown="isShown"
    v-on:on-close-modal="onCloseModal"
  >
    <form class="pot-modal--update-total_form" @submit="updateTotalPot">
      <shared-input
        :type="InputEnumType.Number"
        prefix="$"
        label="Target"
        placeholder="e.g. 2000"
        :value="form.amount?.toString()"
        :custom-input-handler="setTotal"
        :max-value="targetPot.target - targetPot.total"
      />
      <shared-button
        class="pot-modal--update-total_form_btn"
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
} from "~/interfaces/shared.interface";
import {
  potModalHeadings,
  potModalInstruction,
  potModalPrimaryButtonContent,
  updatePot,
} from "~/services/pots.service";
import {
  PotModalTypeEnum,
  type IUpdateTotalPotModal,
} from "~/interfaces/pots.interface";

const CLOSE_POT_MODAL_EVENT = "on-close-modal";
const { isShown, type, targetPot } = defineProps<IUpdateTotalPotModal>();
const emits = defineEmits([CLOSE_POT_MODAL_EVENT]);
const form = ref({
  id: targetPot?.id || "",
  amount: 0,
});
let originalFormValue = { ...form.value };

const errorStore = useErrorStore();
const isLoading = ref(false);

const onCloseModal = (isClosed: boolean, fetchData?: boolean) => {
  emits(CLOSE_POT_MODAL_EVENT, fetchData);
};

const updateTotalPot = (e?: Event) => {
  e?.preventDefault();
  isLoading.value = true;
  const total =
    targetPot.total +
    (type === PotModalTypeEnum.AddToPot
      ? form.value.amount
      : -form.value.amount);
  updatePot({
    id: form.value.id,
    total,
  })
    .then(() => onCloseModal(true, true))
    .catch((message) => errorStore.setErrorMessage(message))
    .finally(() => (isLoading.value = false));
};

const setTotal = (e?: Event) => {
  const value = (e?.currentTarget as HTMLInputElement)?.value;
  form.value.amount =
    type === PotModalTypeEnum.AddToPot ? parseFloat(value) : -parseFloat(value);
};

const isButtonDisabled = () => {
  if (!form.value.amount || form.value.amount <= 0) {
    return true;
  }

  return false;
};

watch(
  () => targetPot,
  (value) => {
    form.value = {
      id: value?.id || "",
      amount: 0,
    };
    originalFormValue = { ...form.value };
  }
);
</script>
<style lang="scss" scoped>
.pot-modal--update-total {
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
