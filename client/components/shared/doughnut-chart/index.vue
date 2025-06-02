<template>
  <div class="doughnut-chart_wrapper">
    <canvas ref="chartRef"></canvas>
    <span>{{ overlayNumber }}</span>
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

const { data, overlayNumber } = defineProps<IDoughnutChart>();

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
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 100%;
    height: 100%;
    max-width: 214px;
    max-height: 214px;
  }
}
</style>
