<template>
  <shared-page-heading />
  <section class="overview_summary">
    <overview-summary-card v-for="card in summaryCards" :class="{ main: card.isMainCard }"
      :card-heading="card.cardHeading" :card-content="card.cardContent" />
  </section>
  <section class="overview_content">
    <overview-section-card
      class="overview_content_pots"
      :heading="pageHeadings[Page.Pots]"
      :navigate-to="Page.Pots"
      nav-content="See Details"
    >

    </overview-section-card>
    <overview-section-card
      class="overview_content_transactions"
      :heading="pageHeadings[Page.Transactions]"
      :navigate-to="Page.Transactions"
    >

    </overview-section-card>
    <overview-section-card
      class="overview_content_budgets"
      :heading="pageHeadings[Page.Budgets]"
      :navigate-to="Page.Budgets"
    >

    </overview-section-card>
    <overview-section-card
      class="overview_content_recurring-bills"
      :heading="pageHeadings[Page.RecurringBills]"
      :navigate-to="Page.RecurringBills">

    </overview-section-card>
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
  &_summary, &_content {
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

    &_content {
      gap: 1.5rem;
    }
  }
}

@media screen and (min-width:64rem) {
  .overview {
    &_content {
      flex: 1;
      display: grid;
      grid-template-columns: calc(60% - 1.5rem) 40%;
      grid-template-areas:
        "pots budgets"
        "transactions budgets"
        "transactions recurring-bills"
        "transactions recurring-bills";

      &_pots {
        grid-area: pots;
      }
      &_transactions {
        grid-area: transactions;
      }
      &_budgets {
        grid-area: budgets;
      }
      &_recurring-bills {
        grid-area: recurring-bills;
      }
    }
  }
}
</style>
