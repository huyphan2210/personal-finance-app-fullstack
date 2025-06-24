<template>
  <overview-section-card
    class="overview_content--budgets"
    :heading="pageHeadings[Page.Budgets]"
    :navigate-to="Page.Budgets"
  >
    <div class="overview_content--budgets_content">
      <shared-doughnut-chart
        v-if="chartData"
        class="overview_content--budgets_content_chart"
        :overlay-number="budgetsCardContent?.spentBudget || 0"
        :data="chartData"
        :total-number="budgetsCardContent?.totalBudget || 0"
      />
      <ul class="overview_content--budgets_content_list">
        <overview-card-item
          class="budget-item"
          v-for="item in budgetsCardContent?.budgetItems"
          :label="item.category"
          :content="item.maximum.toFixed(2)"
          :color-theme="item.colorTheme"
        />
      </ul>
    </div>
  </overview-section-card>
</template>

<script lang="ts" setup>
import type { ChartData } from "chart.js";
import type { IOverviewBudgetsCard } from "./budgets-card.model";

const { budgetsCardContent } = defineProps<IOverviewBudgetsCard>();

const chartData = ref<ChartData>();
chartData.value = {
  datasets: [
    {
      data: budgetsCardContent?.budgetItems.map((item) => item.maximum) || [],
      backgroundColor:
        budgetsCardContent?.budgetItems.map((item) => item.colorTheme) || [],
      hoverOffset: 4,
    },
  ],
};
</script>
<style lang="scss" scoped>
.overview_content--budgets {
  &_content {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    margin-top: 1.25rem;
    gap: 1rem;
    &_chart {
      width: 100% !important;
      height: 100% !important;
      max-width: 15rem;
      max-height: 15rem;
      margin-inline: auto;
    }

    &_list {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      gap: 1rem;
    }
  }
}

@media screen and (min-width: 48rem) {
  .overview_content--budgets {
    &_content {
      flex-direction: unset;
      padding-block: 31px;
      &_list {
        flex-direction: column;
        .budget-item {
          width: unset;
        }
      }
    }
  }
}
</style>
