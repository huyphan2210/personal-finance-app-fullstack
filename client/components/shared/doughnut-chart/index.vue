<template>
  <canvas ref="chartRef"></canvas>
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

const { data } = defineProps<IDoughnutChart>();

const chartRef = ref<HTMLCanvasElement>();
const chartConfig: ChartConfiguration = {
  type: "doughnut",
  data,
};

onMounted(() => {
  new Chart(chartRef.value!, chartConfig);
});
</script>
