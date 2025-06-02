<template>
  <div class="doughnut-chart_wrapper">
    <canvas ref="chartRef"></canvas>
    <span>${{ overlayNumber }} <small>of ${{ totalNumber }} limit</small> </span>
  </div>
</template>
<script lang="ts" setup>
import {
  Chart,
  ArcElement,
  Tooltip,
  Legend,
  DoughnutController,
  type ChartConfiguration,
} from "chart.js";
import { type IDoughnutChart } from "./dougnut-chart.model";

Chart.register(ArcElement, Tooltip, Legend, DoughnutController);

const { data, overlayNumber, totalNumber } = defineProps<IDoughnutChart>();

const chartRef = ref<HTMLCanvasElement>();
const chartConfig: ChartConfiguration = {
  type: "doughnut",
  data,
};

onMounted(() => {
  new Chart(chartRef.value!, chartConfig);
});
</script>
<style lang="scss" scoped>
.doughnut-chart_wrapper {
  position: relative;
  span {
    position: absolute;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    text-align: center;
    top: 52%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 100%;
    height: 100%;
    max-width: 187.5px;
    max-height: 187.5px;
    border-radius: 50%;
    background-color: rgba(255, 255, 255, 0.25);
    color: var(--grey-900);
    @include text-preset-1;
    small {
      color: var(--grey-500);
      @include text-preset-5;
    }
  }
}
</style>
