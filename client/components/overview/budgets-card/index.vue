<template>
  <overview-section-card
    class="overview_content--budgets"
    :heading="pageHeadings[Page.Budgets]"
    :navigate-to="Page.Budgets"
  >
    <div class="overview_content--budgets_content">
      <shared-doughnut-chart
        v-if="chartDataRef"
        class="overview_content--budgets_content_chart"
        :overlay-number="budgetsCardContent?.spentBudget || 0"
        :data="chartDataRef"
        :total-number="budgetsCardContent?.budgetItems.reduce((prev, next) => ({
          maximum: prev.maximum + next.maximum,
          category: EnumBudgetCategory.Bills
        }), {
          maximum: 0
        }).maximum || 0"
      />
      <ul class="overview_content--budgets_content_list">
        <overview-card-item
          class="budget-item"
          v-for="(item, index) in budgetsCardContent?.budgetItems"
          :label="item.category"
          :content="item.maximum.toFixed(2)"
          :class="{
            'border-green': index % 4 === 0,
            'border-cyan': index % 4 === 1,
            'border-yellow': index % 4 === 2,
            'border-navy': index % 4 === 3,
          }"
        />
      </ul>
    </div>
  </overview-section-card>
</template>

<script lang="ts" setup>
import type { ChartData } from "chart.js";
import { Color } from "~/types/color";
import type { IOverviewBudgetsCard } from "./budgets-card.model";
import { EnumBudgetCategory } from "~/api";

const { budgetsCardContent } = defineProps<IOverviewBudgetsCard>();

const chartDataRef = ref<ChartData>();
watch(
  () => budgetsCardContent,
  (content) => {
    chartDataRef.value = {
      datasets: [
        {
          data: content?.budgetItems.map((item) => item.maximum) || [],
          backgroundColor: [Color.Green, Color.Cyan, Color.Yellow, Color.Navy],
          hoverOffset: 4,
        },
      ],
    };
  }
);
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
