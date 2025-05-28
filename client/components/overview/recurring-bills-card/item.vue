<template>
  <li class="recurring-bill-summary-item">
    <span>{{ label }}</span>
    <span>{{ enUSFormatter.format(amount) }}</span>
  </li>
</template>
<script lang="ts" setup>
import type { IRecurringBillSummaryItem } from "./recurring-bills-card.model";

const { label, amount } = defineProps<IRecurringBillSummaryItem>();
const enUSFormatter = new Intl.NumberFormat("en-US", {
  style: "currency",
  currency: "USD",
});
</script>
<style lang="scss" scoped>
.recurring-bill-summary-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: var(--beige-100);
  padding: 1.25rem 1rem;
  border-radius: 0.5rem;
  border-left: solid 0.25rem;

  &.border-green {
    border-color: var(--green);
  }

  &.border-yellow {
    border-color: var(--yellow);
  }

  &.border-cyan {
    border-color: var(--cyan);
  }

  span {
    &:first-child {
      color: var(--grey-500);
      @include text-preset-4;
    }

    &:last-child {
      color: var(--grey-900);
      @include text-preset-4-bold;
    }
  }
}
</style>
