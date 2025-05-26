<template>
  <overview-section-card
    class="overview_content--transactions"
    :heading="pageHeadings[Page.Transactions]"
    :navigate-to="Page.Transactions"
    :nav-content="'View All'"
  >
    <ul class="overview_content--transactions_list">
      <overview-transactions-card-item
        v-for="(
          { avatarUrl, user, date, amount, recurring, category }, index
        ) in transactionsCardContent?.transactions"
        :class="
          index === transactionsCardContent!.transactions.length - 1
            ? 'last-item'
            : ''
        "
        :avatar-url="avatarUrl"
        :user="user"
        :date="date"
        :amount="amount"
        :recurring="recurring"
        :category="category"
      />
    </ul>
  </overview-section-card>
</template>
<script lang="ts" setup>
import { type IOverviewTransactionsCard } from "./transactions-card.model";

const { transactionsCardContent } = defineProps<IOverviewTransactionsCard>();
</script>
<style lang="scss" scoped>
.overview_content--transactions {
  &_list {
    margin-top: 2rem;
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
  }
}
</style>
