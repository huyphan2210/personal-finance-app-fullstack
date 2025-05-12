<template>
  <shared-page-heading />
  <section class="overview_summary">
    <overview-summary-card v-for="card in overviewContent?.summaryCardsContent" :class="{ main: card.isMainCard }"
      :card-heading="card.cardHeading" :card-content="card.cardContent" />
  </section>
  <section class="overview_content">
    <overview-section-card class="overview_content_pots" :heading="pageHeadings[Page.Pots]" :navigate-to="Page.Pots"
      nav-content="See Details">
      <overview-pot-item v-for="potItem in overviewContent?.potsCardContent.potItems" :label="potItem.name"
        :content="potItem.total.toString()" />
    </overview-section-card>
    <overview-section-card class="overview_content_transactions" :heading="pageHeadings[Page.Transactions]"
      :navigate-to="Page.Transactions">

    </overview-section-card>
    <overview-section-card class="overview_content_budgets" :heading="pageHeadings[Page.Budgets]"
      :navigate-to="Page.Budgets">

    </overview-section-card>
    <overview-section-card class="overview_content_recurring-bills" :heading="pageHeadings[Page.RecurringBills]"
      :navigate-to="Page.RecurringBills">

    </overview-section-card>
  </section>

</template>

<script setup lang="ts">
import { getSummaryContent, type IOverviewPageContent } from '~/services/overview.service';

const overviewContent = ref<IOverviewPageContent>();
getSummaryContent().then(content => overviewContent.value = content)
</script>

<style lang="scss">
.overview {

  &_summary,
  &_content {
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
