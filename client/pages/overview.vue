<template>
  <shared-page-heading />
  <section
    :class="{
      overview_summary: true,
      'is-loading': isLoading,
    }"
  >
    <overview-summary-card
      v-for="card in overviewContent?.summaryCardsContent"
      :class="{ main: card.isMainCard }"
      :card-heading="card.cardHeading"
      :card-content="card.cardContent"
    />
  </section>
  <section
    :class="{
      overview_content: true,
      'is-loading': isLoading,
    }"
  >
    <template v-if="!isLoading">
      <overview-pot-card
        :pots-card-content="overviewContent?.potsCardContent"
      />
      <overview-transactions-card
        :transactions-card-content="overviewContent?.transactionsCardContent"
      />
      <overview-budgets-card
        :budgets-card-content="overviewContent?.budgetsCardContent"
      />
      <overview-recurring-bills-card
        :recurring-bills-card-content="
          overviewContent?.recurringBillsCardContent
        "
      />
    </template>
  </section>
</template>

<script setup lang="ts">
import {
  getSummaryContent,
  type IOverviewPageContent,
} from "~/services/overview.service";

const errorStore = useErrorStore();
const isLoading = ref<boolean>(true);
const overviewContent = ref<IOverviewPageContent>();

onBeforeMount(async () => {
  try {
    overviewContent.value = await getSummaryContent();
  } catch (error) {
    if (error instanceof Error) {
      errorStore.setErrorMessage(error.message);
    } else {
      errorStore.setDefaultErrorMessage();
    }
  } finally {
    isLoading.value = false;
  }
});
</script>

<style lang="scss">
.overview {
  &_summary,
  &_content {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    &.is-loading {
      flex: 1;
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

@media screen and (min-width: 90rem) {
  .overview {
    &_content {
      flex: 1;
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      grid-template-rows: repeat(2, min-content) repeat(2, 1fr);

      &--pots {
        grid-column: 1 / span 7;
        grid-row: 1;
      }

      &--budgets {
        grid-column: 8 / -1;
        grid-row: 1 / span 2;
      }

      &--transactions {
        grid-column: 1 / span 7;
        grid-row: 2 / -1;
      }

      &--recurring-bills {
        grid-column: 8 / -1;
        grid-row: 3 / -1;
      }
    }
  }
}
</style>
