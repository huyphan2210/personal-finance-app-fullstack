<template>
  <overview-section-card
    class="overview_content--transactions"
    :heading="pageHeadings[Page.Transactions]"
    :navigate-to="Page.Transactions"
  >
    <ul class="overview_content--transactions_list">
      <overview-transactions-card-item
        v-for="{
          avatarUrl,
          user,
          date,
          amount,
          recurring,
          category,
        } in transactionsCardContent?.transactions"
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
