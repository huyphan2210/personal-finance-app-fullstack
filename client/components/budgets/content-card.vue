<template>
  <shared-content-card
    :heading="budgetInfo.category"
    :color-theme="budgetInfo.colorTheme"
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
      <section class="budget-info_latest-spending">
        <hgroup>
          <h3>Lastest Spending</h3>
          <NuxtLink
            @mouseover="handleMouseOver"
            @mouseleave="handleMouseLeave"
            :to="
              Page.Transactions +
              `?page=1&sortBy=Latest&category=${budgetInfo.category}`
            "
          >
            See Details
            <svg
              width="12"
              height="12"
              viewBox="0 0 12 12"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M4.76531 1.98468L8.51531 5.73468C8.55018 5.76951 8.57784 5.81087 8.59671 5.85639C8.61558 5.90192 8.62529 5.95071 8.62529 5.99999C8.62529 6.04927 8.61558 6.09807 8.59671 6.1436C8.57784 6.18912 8.55018 6.23048 8.51531 6.26531L4.76531 10.0153C4.71287 10.0678 4.64602 10.1036 4.57324 10.1181C4.50046 10.1326 4.42501 10.1251 4.35645 10.0967C4.28789 10.0683 4.22931 10.0202 4.1881 9.95849C4.1469 9.89677 4.12494 9.82421 4.125 9.74999L4.125 2.24999C4.12494 2.17578 4.1469 2.10322 4.1881 2.0415C4.22931 1.97978 4.28789 1.93167 4.35645 1.90326C4.42501 1.87485 4.50046 1.86743 4.57324 1.88192C4.64602 1.89641 4.71287 1.93218 4.76531 1.98468Z"
                :fill="svgFillColorRef"
              />
            </svg>
          </NuxtLink>
        </hgroup>
        <ul class="budget-info_latest-spending_list">
          <budgets-transaction-item
            v-for="{
              avatarUrl,
              user,
              amount,
              date,
              category,
              recurring,
            } in budgetInfo.representTransactions"
            :avatar-url="avatarUrl"
            :user="user"
            :amount="amount"
            :date="date"
            :category="category"
            :recurring="recurring"
          ></budgets-transaction-item>
        </ul>
      </section>
    </section>
  </shared-content-card>
</template>
<script lang="ts" setup>
import { BudgetColorThemeEnum } from "~/api/data-contracts";
import { type IBudgetContentCard } from "~/interfaces/budgets.interface";
import type { IDropdownOption } from "~/interfaces/shared.interface";
import { enUSFormatter } from "~/services/base.service";
import { Color } from "~/types/color";

const { dropdownOptions, budgetInfo } = defineProps<IBudgetContentCard>();

const budget = ref<HTMLElement>();
const openEditBudgetModal = () => {};
const openDeleteBudgetModal = () => {};

const svgFillColorRef = ref("var(--grey-500)");

const handleMouseOver = () => {
  svgFillColorRef.value = "var(--grey-900)";
};

const handleMouseLeave = () => {
  svgFillColorRef.value = "var(--grey-500)";
};

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
  if (colorObject[budgetInfo.colorTheme]) {
    budget.value?.classList.add(
      `${colorObject[budgetInfo.colorTheme].toLowerCase()}`
    );
  }
});
</script>
<style lang="scss" scoped>
.budget-info {
  $colors: "green", "cyan", "yellow", "navy";
  @mixin content-color($color-name) {
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
    @include content-color($color);
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

  &_latest-spending {
    background-color: var(--beige-100);
    padding: 1rem;
    border-radius: 0.75rem;
    margin-top: 1.25rem;
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
    hgroup {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
      a {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        color: var(--grey-500);
        text-decoration: none;

        @include text-preset-4;

        &:hover {
          color: var(--grey-900);
        }
        &:focus-visible {
          outline-offset: 0.25rem;
          outline-color: var(--grey-900);
        }
      }
    }

    &_list {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }
  }
}
</style>
