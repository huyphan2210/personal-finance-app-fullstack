<template>
  <li class="transaction-item">
    <figure class="transaction-item_user">
      <img :src="avatarUrl" loading="lazy" :alt="user" />
      <figcaption>{{ user }}</figcaption>
    </figure>
    <div class="transaction-item_detail">
      <span>{{ enUSFormatter.format(amount) }}</span>
      <span>{{ day }} {{ month }} {{ year }}</span>
    </div>
  </li>
</template>

<script lang="ts" setup>
import type { Transaction } from "~/api";

const { avatarUrl, amount, user, date } = defineProps<Transaction>();

const enUSFormatter = new Intl.NumberFormat("en-US", {
  style: "currency",
  currency: "USD",
});

const transactionDate = new Date(date);
const day = transactionDate.getUTCDate().toString().padStart(2, "0");
const month = transactionDate.toLocaleString("en-GB", {
  month: "short",
  timeZone: "UTC",
});
const year = transactionDate.getUTCFullYear();
</script>

<style lang="scss" scoped>
.transaction-item {
  display: flex;
  &_user {
    display: flex;
    align-items: center;
    gap: 1rem;
    flex: 1;
    img {
      width: 2rem;
      border-radius: 50%;
    }

    @include text-preset-4-bold;
  }
  &_detail {
    span {
      display: block;
    }
  }
}
</style>
