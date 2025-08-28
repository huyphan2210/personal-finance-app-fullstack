<template>
  <shared-modal
    :heading="potModalHeadings[type](targetPot?.name)"
    :message="potModalInstruction[type](enUSFormatter.format(form.maxAmount))"
    class="pot-modal--update-total"
    :is-modal-shown="isShown"
    v-on:on-close-modal="onCloseModal"
  >
    <div class="pot-modal--update-total_progress">
      <div class="pot-modal--update-total_progress_saved">
        <small>Total Saved</small>
        <span>{{ enUSFormatter.format(targetPot?.total || "+Infinity") }}</span>
      </div>
      <div class="pot-modal--update-total_progress_bar-wrapper">
        <progress
          :class="{
            'pot-modal--update-total_progress_bar-wrapper_primary': true,
            'add-money': type === PotModalTypeEnum.AddToPot,
            withdraw: type === PotModalTypeEnum.Withdraw,
          }"
          :value="
            type === PotModalTypeEnum.AddToPot
              ? (targetPot?.total || 0) + (form.amount || 0)
              : targetPot?.total || 0
          "
          :max="targetPot?.target"
        ></progress>
        <progress
          :class="{
            'pot-modal--update-total_progress_bar-wrapper_secondary': true,
            'add-money': type === PotModalTypeEnum.AddToPot,
            withdraw: type === PotModalTypeEnum.Withdraw,
          }"
          :value="
            type === PotModalTypeEnum.Withdraw
              ? (targetPot?.total || 0) - (form.amount || 0)
              : targetPot?.total || 0
          "
          :max="targetPot?.target"
        ></progress>
        <span
          ref="divider"
          class="pot-modal--update-total_progress_bar-wrapper_divider"
        >
        </span>
      </div>
      <div class="pot-modal--update-total_progress_target">
        <small
          :class="{
            danger: form.percentage < originalFormValue.percentage,
            good: form.percentage > originalFormValue.percentage,
          }"
        >
          {{ form.percentage.toFixed(2) }}%
        </small>
        <span>
          Target of {{ enUSFormatter.format(targetPot?.target || "+Infinity") }}
        </span>
      </div>
    </div>
    <form class="pot-modal--update-total_form" @submit="updateTotalPot">
      <shared-input
        :type="InputEnumType.Number"
        prefix="$"
        :label="`Amount to ${
          type === PotModalTypeEnum.AddToPot ? 'Add' : 'Withdraw'
        }`"
        placeholder="e.g. 2000"
        :value="form.amount?.toString()"
        :custom-input-handler="setTotal"
        :max-value="form.maxAmount"
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
import { enUSFormatter } from "~/services/base.service";

const CLOSE_POT_MODAL_EVENT = "on-close-modal";
const { isShown, type, targetPot } = defineProps<IUpdateTotalPotModal>();
const emits = defineEmits([CLOSE_POT_MODAL_EVENT]);
const divider = ref<HTMLSpanElement>();
const form = ref({
  id: targetPot?.id || "",
  amount: 0,
  maxAmount:
    type === PotModalTypeEnum.AddToPot
      ? (targetPot?.target || 0) - (targetPot?.total || 0)
      : targetPot?.total || 0,
  percentage: ((targetPot?.total || 0) / (targetPot?.target || 1)) * 100,
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
    (targetPot?.total || 0) +
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
  form.value.amount = parseFloat(value);
  const newTotal =
    (targetPot?.total || 0) +
    (type === PotModalTypeEnum.AddToPot
      ? form.value.amount || 0
      : -(form.value.amount || 0));
  form.value.percentage = ((newTotal || 0) / (targetPot?.target || 1)) * 100;
  if (divider.value && type === PotModalTypeEnum.Withdraw) {
    divider.value.style.left = `calc(${form.value.percentage}% - 0.125rem)`;
  }
};

const isButtonDisabled = () => {
  if (
    !form.value.amount ||
    form.value.amount <= 0 ||
    form.value.amount > form.value.maxAmount
  ) {
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
      maxAmount:
        type === PotModalTypeEnum.AddToPot
          ? (value?.target || 0) - (value?.total || 0)
          : value?.total || 0,
      percentage: ((value?.total || 0) / (value?.target || 1)) * 100,
    };
    if (divider.value) {
      divider.value.style.left = `calc(${form.value.percentage}% - 0.125rem)`;
    }

    originalFormValue = { ...form.value };
  }
);
</script>
<style lang="scss" scoped>
.pot-modal--update-total {
  &_progress {
    padding-block: 10.5px;
    &_saved {
      display: flex;
      justify-content: space-between;
      align-items: center;

      small {
        @include text-preset-4;
        color: var(--grey-500);
      }
      span {
        @include text-preset-1;
        color: var(--grey-900);
      }
    }
    &_bar-wrapper {
      --corner: 0.25rem;
      position: relative;
      margin-block: 1rem 13px;
      &_divider {
        position: absolute;
        top: 0;
        background-color: var(--grey-100);
        width: 0.125rem;
        height: 100%;
        transition: none;
      }
      &_primary,
      &_secondary {
        display: block;
        width: 100%;
        height: 0.5rem;
        appearance: none;
        border-radius: var(--corner);
        background-color: var(--beige-100);

        &::-webkit-progress-bar {
          background-color: inherit;
          border-radius: var(--corner);
        }

        &::-webkit-progress-value {
          border-radius: var(--corner);
        }

        &::-moz-progress-bar {
          background-color: inherit;
        }

        &:focus-visible {
          outline: none;
        }
      }

      &_primary {
        &.add-money {
          &::-webkit-progress-value {
            background-color: var(--green);
          }
        }
        &.withdraw {
          &::-webkit-progress-value {
            background-color: var(--red);
          }
        }
      }
      &_secondary {
        position: absolute;
        width: 100%;
        top: 0;
        background-color: transparent;
        &.add-money {
          &::-webkit-progress-value {
            background-color: var(--grey-900);
          }
        }

        &.withdraw {
          &::-webkit-progress-value {
            background-color: var(--grey-900);
          }
        }
      }
    }

    &_target {
      display: flex;
      justify-content: space-between;
      align-items: center;

      small {
        @include text-preset-5-bold;
        color: var(--grey-500);

        &.danger {
          color: var(--red);
        }

        &.good {
          color: var(--green);
        }
      }

      span {
        @include text-preset-5;
        color: var(--grey-500);
      }
    }
  }
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
