<template>
  <hgroup class="budgets_heading">
    <shared-page-heading />
    <button class="budgets_heading_button--add-new" type="button">
      + Add New Budget
    </button>
  </hgroup>
  <section class="budgets_content">
    <section class="budgets_content_spending-summary">
      <shared-doughnut-chart
        v-if="chartData"
        class="budgets_content_spending-summary_chart"
        :overlay-number="budgets?.totalSpent || 0"
        :data="chartData"
        :total-number="budgets?.totalMaximum || 0"
      />
    </section>
  </section>
</template>

<script setup lang="ts">
import type { ChartData } from "chart.js";
import { type BudgetContent } from "~/api/data-contracts";
import { getBudgets } from "~/services/budgets.service";
const budgets = ref<BudgetContent>();
const chartData = ref<ChartData>();
getBudgets().then((response) => {
  budgets.value = response;
  chartData.value = {
    datasets: [
      {
        data: response.representBudgets.map((item) => item.maximum) || [],
        backgroundColor:
          response.representBudgets.map((item) => item.colorTheme) || [],
        hoverOffset: 4,
      },
    ],
  };
});
</script>

<style lang="scss" scoped>
.budgets {
  &_heading {
    display: flex;
    justify-content: space-between;
    &_button {
      &--add-new {
        padding: 1rem;
        border-radius: 0.5rem;
        color: var(--white);
        background-color: var(--grey-900);
        @include text-preset-4-bold;
      }
    }
  }
  &_content {
    flex: 1;
    &_spending-summary {
      background-color: var(--white);
      border-radius: 0.75rem;

      &_chart {
        max-width: 15rem;
        margin-inline: auto;
      }
    }
  }
}
</style>
