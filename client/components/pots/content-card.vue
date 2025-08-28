<template>
  <shared-content-card
    class="pot-content-card"
    :heading="potInfo.name"
    :color-theme="potInfo.colorTheme"
    :dropdown-options="dropdownOptions.concat(defaultPotDropdownOptions)"
  >
    <div class="pot-content-card_progress">
      <div class="pot-content-card_progress_saved">
        <small>Total Saved</small>
        <span>{{ enUSFormatter.format(potInfo.total) }}</span>
      </div>
      <progress
        ref="progressBar"
        class="pot-content-card_progress_bar"
        :value="potInfo.total"
        :max="potInfo.target"
      ></progress>
      <div class="pot-content-card_progress_target">
        <small>
          {{ ((potInfo.total / potInfo.target) * 100).toFixed(2) }}%
        </small>
        <span>Target of {{ enUSFormatter.format(potInfo.target) }}</span>
      </div>
    </div>
    <div class="pot-content-card_btn-group">
      <button
        class="pot-content-card_btn-group_btn"
        type="button"
        @click="() => onAddToTotal(potInfo)"
        :disabled="potInfo.total >= potInfo.target"
      >
        + Add Money
      </button>
      <button
        class="pot-content-card_btn-group_btn"
        type="button"
        :disabled="potInfo.total <= 0"
        @click="() => onWithdraw(potInfo)"
      >
        Withdraw
      </button>
    </div>
  </shared-content-card>
</template>
<script lang="ts" setup>
import { PotColorThemeEnum } from "~/api/data-contracts";
import type { IPotContentCard } from "~/interfaces/pots.interface";
import type { IContentCardDropdownOption } from "~/interfaces/shared.interface";
import { enUSFormatter } from "~/services/base.service";
import { Color } from "~/types/color";

const {
  potInfo,
  dropdownOptions,
  onDeleteModal,
  onEditModal,
  onAddToTotal,
  onWithdraw,
} = defineProps<IPotContentCard>();
const progressBar = ref<HTMLProgressElement>();

const defaultPotDropdownOptions: IContentCardDropdownOption[] = [
  {
    content: "Edit Pot",
    onClick: () => {
      onEditModal(potInfo);
    },
  },
  {
    content: "Delete Pot",
    contentColor: Color.Red,
    onClick: () => {
      onDeleteModal(potInfo);
    },
  },
];

const colorObject = Object.fromEntries(
  Object.entries(PotColorThemeEnum).map(([key, value]) => [value, key])
);

onMounted(() => {
  if (colorObject[potInfo.colorTheme]) {
    progressBar.value?.classList.add(
      `${colorObject[potInfo.colorTheme].toLowerCase()}`
    );
  }
});
</script>
<style lang="scss" scoped>
@mixin bar-color($color-name) {
  &.#{$color-name} {
    &::-webkit-progress-value {
      background-color: var(--#{$color-name});
    }
  }
}
.pot-content-card {
  display: flex;
  flex-direction: column;
  gap: 2rem;
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
    &_bar {
      @each $color in $colors {
        @include bar-color($color);
      }
      --corner: 0.25rem;
      display: block;
      width: 100%;
      height: 0.5rem;
      appearance: none;
      border-radius: var(--corner);
      background-color: var(--beige-100);
      margin-block: 1rem 13px;

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

    &_target {
      display: flex;
      justify-content: space-between;
      align-items: center;

      small {
        @include text-preset-5-bold;
        color: var(--grey-500);
      }

      span {
        @include text-preset-5;
        color: var(--grey-500);
      }
    }
  }
  &_btn-group {
    display: flex;
    justify-content: space-between;
    gap: 1rem;
    &_btn {
      @include text-preset-4-bold;
      flex: 1;
      background-color: var(--beige-100);
      padding: 15px;
      color: var(--grey-900);
      border-radius: 0.5rem;
      border: solid 1px var(--beige-100);
      &:hover {
        background-color: transparent;
        border-color: var(--beige-500);
      }

       &:disabled {
        background-color: var(--grey-300);
        border-color: var(--grey-300);
        color: var(--grey-500);
        cursor: not-allowed;
      }
    }
  }
}
</style>
