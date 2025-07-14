<template>
  <shared-content-card
    :heading="heading"
    :color-theme="colorTheme"
    :dropdown-options="dropdownOptions"
  ></shared-content-card>
</template>
<script lang="ts" setup>
import { type IBudgetContentCard } from "~/interfaces/budgets.interface";

const { heading, colorTheme, dropdownOptions } =
  defineProps<IBudgetContentCard>();
</script>
<style lang="scss" scoped></style>
