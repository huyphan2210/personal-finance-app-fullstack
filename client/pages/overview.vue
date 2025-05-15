<template>
  <shared-page-heading />
  <section class="overview_summary">
    <overview-summary-card
      v-for="card in overviewContent?.summaryCardsContent"
      :class="{ main: card.isMainCard }"
      :card-heading="card.cardHeading"
      :card-content="card.cardContent"
    />
  </section>
  <section class="overview_content">
    <overview-pot-card :pots-card-content="overviewContent?.potsCardContent" />
    <overview-transactions-card />
    <overview-budgets-card />
    <overview-recurring-bills-card />
  </section>
</template>

<script setup lang="ts">
import {
  getSummaryContent,
  type IOverviewPageContent,
} from "~/services/overview.service";

const overviewContent = ref<IOverviewPageContent>();
getSummaryContent().then((content) => (overviewContent.value = content));
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

@media screen and (min-width: 64rem) {
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
      grid-template-rows: repeat(2, min-content) repeat(2, 1fr);
      &--pots {
        grid-area: pots;
      }

      &--transactions {
        grid-area: transactions;
      }

      &--budgets {
        grid-area: budgets;
      }

      &--recurring-bills {
        grid-area: recurring-bills;
      }
    }
  }
}
</style>
