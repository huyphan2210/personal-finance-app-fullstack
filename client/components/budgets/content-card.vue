<template>
  <shared-content-card
    :heading="heading"
    :color-theme="colorTheme"
    :dropdown-options="dropdownOptions.concat(defaultBudgetDropdownOptions)"
  >
    <section ref="budget" class="budget-info">
      <span class="budget-info_maximum">
        Maximum of {{ budgetInfo.maximumWithCurrency }}
      </span>
      <progress
        class="budget-info_bar"
        :value="budgetInfo.spent"
        :max="budgetInfo.maximum"
      ></progress>
      <ul class="budget-info_details">
        <li class="budget-info_details_item spent">
          <span>Spent</span>
          <b>{{ budgetInfo.spentWithCurrency }}</b>
        </li>
        <li class="budget-info_details_item">
          <span>Remaining</span>
          <b>{{
            enUSFormatter.format(budgetInfo.maximum - budgetInfo.spent)
          }}</b>
        </li>
      </ul>
    </section>
  </shared-content-card>
</template>
<script lang="ts" setup>
import { BudgetColorThemeEnum } from "~/api/data-contracts";
import { type IBudgetContentCard } from "~/interfaces/budgets.interface";
import type { IDropdownOption } from "~/interfaces/shared.interface";
import { enUSFormatter } from "~/services/base.service";
import { Color } from "~/types/color";

const { heading, colorTheme, dropdownOptions, budgetInfo } =
  defineProps<IBudgetContentCard>();

const budget = ref<HTMLElement>();
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

const colorObject = Object.fromEntries(
  Object.entries(BudgetColorThemeEnum).map(([key, value]) => [value, key])
);

onMounted(() => {
  if (colorObject[colorTheme]) {
    budget.value?.classList.add(`${colorObject[colorTheme].toLowerCase()}`);
  }
});
</script>
<style lang="scss" scoped>
.budget-info {
  $colors: "green", "cyan", "yellow", "navy";
  @mixin bar-color($color-name) {
    &.#{$color-name} {
      .budget-info {
        &_bar {
          &::-webkit-progress-value {
            background-color: var(--#{$color-name});
          }
        }

        &_details {
          &_item {
            &.spent {
              &::before {
                background-color: var(--#{$color-name});
              }
            }
          }
        }
      }
    }
  }
  @each $color in $colors {
    @include bar-color($color);
  }

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
    margin-block: 1rem;

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

  &_details {
    list-style-type: none;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
    &_item {
      position: relative;
      padding-left: 1.25rem;
      span {
        @include text-preset-5;
        color: var(--grey-500);
        display: block;
        margin-bottom: 0.25rem;
      }

      b {
        @include text-preset-4-bold;
        color: var(--grey-900);
      }

      &::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        height: 100%;
        width: 0.25rem;
        border-radius: 0.5rem;
        background-color: var(--beige-100);
      }
    }
  }
}
</style>
