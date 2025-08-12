<template>
  <hgroup class="budgets_heading">
    <shared-page-heading />
    <shared-button
      class="budgets_heading_button--add-new"
      type="button"
      :appearance="ButtonAppearanceEnum.Primary"
      :on-click="openAddNewModal"
    >
      + Add New Budget
    </shared-button>
  </hgroup>
  <section
    :class="{
      budgets_content: true,
      'is-loading': !budgets,
    }"
  >
    <section v-if="budgets" class="budgets_content_spending-summary">
      <shared-doughnut-chart
        v-if="chartData"
        class="budgets_content_spending-summary_chart"
        :overlay-number="budgets?.totalSpent || 0"
        :data="chartData"
        :total-number="budgets?.totalMaximum || 0"
      />
      <div class="budgets_content_spending-summary_wrapper">
        <h2 class="budgets_content_spending-summary_heading">
          Spending Summary
        </h2>
        <ul class="budgets_content_spending-summary_list">
          <budgets-spending-summary-item
            v-for="(budget, index) in budgets?.representBudgets"
            :key="budget.category + index"
            class="budgets_content_spending-summary_list_item"
            :color-theme="budget.colorTheme"
            :category="budget.category"
            :maximum-with-currency="budget.maximumWithCurrency"
            :spent-with-currency="budget.spentWithCurrency"
            :maximum="budget.maximum"
            :spent="budget.spent"
            :represent-transactions="budget.representTransactions"
          />
        </ul>
      </div>
    </section>
    <ul class="budgets_content_budgets-detail-list">
      <li
        v-for="(budget, index) in budgets?.representBudgets"
        :key="budget.category + index"
        class="budgets_content_budgets-detail-list_item"
      >
        <budgets-content-card :dropdown-options="[]" :budget-info="budget" />
      </li>
    </ul>
  </section>
  <budgets-modal
    v-if="budgets"
    :targetBudgetCategory="budgetCategory"
    :type="currentOpeningModal || BudgetModalTypeEnum.AddNew"
    :is-shown="!!currentOpeningModal"
    :used-budgets="budgets.representBudgets"
    v-on:on-close-modal="onCloseModal"
  />
</template>

<script setup lang="ts">
import type { ChartData } from "chart.js";
import { BudgetCategoryEnum } from "~/api/data-contracts";
import {
  BudgetModalTypeEnum,
  type IBudgetContent,
} from "~/interfaces/budgets.interface";
import { ButtonAppearanceEnum } from "~/interfaces/shared.interface";
import { getBudgets } from "~/services/budgets.service";
const budgets = ref<IBudgetContent>();
const chartData = ref<ChartData>();
const budgetCategory = ref<BudgetCategoryEnum>();
const currentOpeningModal = ref<BudgetModalTypeEnum | undefined>();
const openAddNewModal = () => {
  currentOpeningModal.value = BudgetModalTypeEnum.AddNew;
};

const setBudgetsData = (budgetsData: IBudgetContent) => {
  budgets.value = { ...budgetsData };

  chartData.value = {
    datasets: [
      {
        data: budgets.value.representBudgets.map((item) => item.maximum) || [],
        backgroundColor:
          budgets.value.representBudgets.map((item) => item.colorTheme) || [],
        hoverOffset: 4,
      },
    ],
  };
};
getBudgets().then(setBudgetsData);

const onCloseModal = (fetchData?: boolean) => {
  currentOpeningModal.value = undefined;
  if (fetchData) {
    getBudgets().then(setBudgetsData);
  }
};
</script>

<style lang="scss" scoped>
$gap: 1.5rem;

.budgets {
  &_heading {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  &_content {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: $gap;
    &_spending-summary {
      @include card-spacing-style;
      &_wrapper {
        min-width: 18.5rem;
      }
      &_heading {
        @include text-preset-2;
        margin-bottom: 1.5rem;
      }

      &_list {
        list-style-type: none;
        display: flex;
        flex-direction: column;
        gap: 1rem;
        &_item {
          padding-bottom: 1rem;
          border-bottom: solid 1px var(--grey-100);
          &:last-child {
            padding-bottom: 0;
            border: none;
          }
        }
      }

      &_chart {
        max-width: 15rem;
        margin-inline: auto;
        padding-block: 1.25rem;
        margin-bottom: 2rem;
      }
    }

    &_budgets-detail-list {
      list-style-type: none;
      display: flex;
      flex-direction: column;
      gap: $gap;
    }
  }
}

@media screen and (min-width: 48rem) {
  .budgets {
    &_content {
      &_spending-summary {
        display: flex;
        align-items: center;
        justify-content: space-between;
        &_chart {
          margin-block: 0;
          margin-inline: auto;
        }
      }
    }
  }
}

@media screen and (min-width: 90rem) {
  .budgets {
    &_content {
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      grid-template-rows: repeat(4, min-content);

      &_spending-summary {
        display: unset;
        grid-column: 1 / span 5;
      }

      &_budgets-detail-list {
        grid-column: 6 / -1;
        grid-row: 1 / -1;
      }
    }
  }
}
</style>
