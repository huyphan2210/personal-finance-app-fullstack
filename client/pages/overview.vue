<template>
  <shared-page-heading />
  <section class="overview_summary">
    <overview_summary-card v-for="card in summaryCards" :class="{ main: card.isMainCard }"
      :card-heading="card.cardHeading" :card-content="card.cardContent" />
  </section>
  <section class="overview_content">
    <section class="overview_content_pots"></section>
    <section class="overview_content_transactions"></section>
    <section class="overview_content_budgets"></section>
    <section class="overview_content_recurring-bills"></section>
  </section>

</template>

<script setup lang="ts">
import { OverviewService, type OverviewSummary } from '~/api';
import { type IOverviewSummaryCard } from '~/components/overview/summary-card/summary-card.model';

const summaryCards = ref<IOverviewSummaryCard[]>();

OverviewService.getOverviewApi().then((summaryInfo: OverviewSummary) => {
  const enUSFormatter = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
  })

  summaryCards.value = [{
    cardHeading: "Current Balance",
    cardContent: enUSFormatter.format(summaryInfo.balance?.current || 0),
    isMainCard: true,
  },
  {
    cardHeading: "Income",
    cardContent: enUSFormatter.format(summaryInfo.balance?.income || 0)
  },
  {
    cardHeading: "Expenses",
    cardContent: enUSFormatter.format(summaryInfo.balance?.expenses || 0)
  }]
})
</script>

<style lang="scss">
.overview {
  &_summary {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }
}

@media screen and (min-width: 48rem) {
  .overview {
    &_summary {
      flex-direction: unset;
      gap: 1.5rem;
    }
  }
}
</style>
