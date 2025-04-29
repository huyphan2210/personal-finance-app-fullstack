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
const summaryCards = [{
  cardHeading: "Current Balance",
  cardContent: "$4,836.00",
  isMainCard: true,
},
{
  cardHeading: "Income",
  cardContent: "$3,814.25"
},
{
  cardHeading: "Expenses",
  cardContent: "$1,700.50"
}]
</script>

<style lang="scss">
.overview {
  &_summary {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }
}
</style>
