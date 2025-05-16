<template>
  <overview-section-card
    class="overview_content--budgets"
    :heading="pageHeadings[Page.Budgets]"
    :navigate-to="Page.Budgets"
  >
    <shared-doughnut-chart
      v-if="chartDataRef"
      class="overview_content--budgets_chart"
      :data="chartDataRef"
    />
  </overview-section-card>
</template>

<script lang="ts" setup>
import type { ChartData } from "chart.js";
import { Color } from "~/types/color";
import type { IOverviewBudgetsCard } from "./budgets-card.model";

const { budgetsCardContent } = defineProps<IOverviewBudgetsCard>();

const chartDataRef = ref<ChartData>();
watch(
  () => budgetsCardContent,
  (content) => {
    chartDataRef.value = {
      datasets: [
        {
          data: content?.budgetItems.map((item) => item.maximum) || [],
          backgroundColor: [Color.Cyan, Color.Yellow, Color.Navy, Color.Green],
          hoverOffset: 4,
        },
      ],
    };
  }
);
</script>
<style lang="scss" scoped>
.overview_content--budgets {
  &_chart {
    width: 15rem !important;
    height: 15rem !important;
  }
}
</style>
