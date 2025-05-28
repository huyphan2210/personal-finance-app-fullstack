<template>
  <overview-section-card
    class="overview_content--recurring-bills"
    :heading="pageHeadings[Page.RecurringBills]"
    :navigate-to="Page.RecurringBills"
  >
    <ul class="overview_content--recurring-bills_list">
      <overview-recurring-bills-card-item
        v-for="({ label, amount }, index) in recurringItems"
        :class="{
          'border-green': index % 3 === 0,
          'border-yellow': index % 3 === 1,
          'border-cyan': index % 3 === 2,
        }"
        :label="label"
        :amount="amount"
      />
    </ul>
  </overview-section-card>
</template>
<script lang="ts" setup>
import type {
  IOverviewRecurringBillsCard,
  IRecurringBillSummaryItem,
} from "./recurring-bills-card.model";

const { recurringBillsCardContent } =
  defineProps<IOverviewRecurringBillsCard>();

const recurringItems = ref<IRecurringBillSummaryItem[]>();
watch(
  () => recurringBillsCardContent,
  (content) => {
    if (!content) {
      return;
    }

    recurringItems.value = [
      {
        label: "Paid Bills",
        amount: content?.paidAmount,
      },
      {
        label: "Total Upcoming",
        amount: content?.totalUpcomingAmount,
      },
      {
        label: "Due Soon",
        amount: content?.dueSoonAmount,
      },
    ];
  }
);
</script>
<style lang="scss" scoped>
.overview_content--recurring-bills {
  &_list {
    margin-top: 2rem;
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }
}
</style>
