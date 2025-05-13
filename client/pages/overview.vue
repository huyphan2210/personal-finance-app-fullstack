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
    <overview-section-card
      class="overview_content--pots"
      :heading="pageHeadings[Page.Pots]"
      :navigate-to="Page.Pots"
      nav-content="See Details"
    >
      <section class="overview_content--pots_total-saved">
        <img
          src="../assets/images/pots.svg"
          loading="lazy"
          alt="Total Saved Icon"
        />
        <div class="overview_content--pots_total-saved_text">
          <small>Total Saved</small>
          <span>{{ overviewContent?.potsCardContent.totalSaved }}</span>
        </div>
      </section>
      <section class="overview_content--pots_items">
        <overview-pot-item
          v-for="(potItem, index) in overviewContent?.potsCardContent.potItems"
          :label="potItem.name"
          :content="potItem.total.toString()"
          :class="{
            'border-green': index % 4 === 0,
            'border-cyan': index % 4 === 1,
            'border-navy': index % 4 === 2,
            'border-yellow': index % 4 === 3,
          }"
        />
      </section>
    </overview-section-card>
    <overview-section-card
      class="overview_content--transactions"
      :heading="pageHeadings[Page.Transactions]"
      :navigate-to="Page.Transactions"
    >
    </overview-section-card>
    <overview-section-card
      class="overview_content--budgets"
      :heading="pageHeadings[Page.Budgets]"
      :navigate-to="Page.Budgets"
    >
    </overview-section-card>
    <overview-section-card
      class="overview_content--recurring-bills"
      :heading="pageHeadings[Page.RecurringBills]"
      :navigate-to="Page.RecurringBills"
    >
    </overview-section-card>
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

  &_content {
    &--pots {
      display: flex;
      flex-direction: column;
      gap: 1.25rem;

      &_total-saved {
        padding: 1rem;
        background-color: var(--beige-100);
        border-radius: 1rem;
      }
      &_items {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        gap: 1rem;
      }
    }
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
