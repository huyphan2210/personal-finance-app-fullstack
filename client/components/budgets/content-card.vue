<template>
  <shared-content-card
    :heading="heading"
    :color-theme="colorTheme"
    :dropdown-options="dropdownOptions.concat(defaultBudgetDropdownOptions)"
  >
    <section class="budget-info">
      <span class="budget-info_maximum">
        Maximum of {{ budgetInfo.maximumWithCurrency }}
      </span>
      <progress
        ref="budgetBar"
        class="budget-info_bar"
        :value="budgetInfo.spent"
        :max="budgetInfo.maximum"
      ></progress>
    </section>
  </shared-content-card>
</template>
<script lang="ts" setup>
import { type IBudgetContentCard } from "~/interfaces/budgets.interface";
import type { IDropdownOption } from "~/interfaces/shared.interface";
import { Color } from "~/types/color";

const { heading, colorTheme, dropdownOptions, budgetInfo } =
  defineProps<IBudgetContentCard>();
const budgetBar = ref<HTMLProgressElement>();
const openEditBudgetModal = () => {};
const openDeleteBudgetModal = () => {};
const defaultBudgetDropdownOptions: IDropdownOption[] = [
  {
    content: "Edit Budget",
    onClick: openEditBudgetModal,
  },
  {
    content: "Delete Budget",
    contentColor: Color.Red,
    onClick: openDeleteBudgetModal,
  },
];
</script>
<style lang="scss" scoped>
.budget-info {
  margin-top: 1.25rem;
  &_maximum {
    @include text-preset-4;
    color: var(--grey-500);
  }

  &_bar {
    --corner: 0.25rem;
    display: block;
    width: 100%;
    height: 2rem;
    padding: 0.25rem;
    appearance: none;
    background-color: var(--beige-100);
    border-radius: calc(var(--corner) * 2);

    &::-webkit-progress-bar {
      background-color: inherit;
      border-radius: var(--corner);
    }

    &::-webkit-progress-value {
      background-color: var(--green);
      border-radius: var(--corner);
    }

    &::-moz-progress-bar {
      background-color: inherit;
    }

    &:focus-visible {
      outline: none;
    }
  }
}
</style>
