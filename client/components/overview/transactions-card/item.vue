<template>
  <li :class="['transaction-item', amount > 0 ? 'incoming' : 'outgoing']">
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
import type { Transaction } from "~/api/data-contracts";

const { avatarUrl, amount, user, date } = defineProps<Transaction>();

const enUSFormatter = new Intl.NumberFormat("en-US", {
  style: "currency",
  currency: "USD",
  signDisplay: "always",
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
  padding-bottom: 1.25rem;
  border-bottom: solid 1px var(--grey-100);

  &.last-item {
    padding-bottom: 0;
    border: none;
  }

  &.incoming {
    .transaction-item_detail {
      span {
        color: var(--green);
      }
    }
  }

  &.incoming {
    .transaction-item_detail {
      span {
        &:first-child {
          color: var(--green);
        }
        &:last-child {
          color: var(--grey-500);
        }
      }
    }
  }

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
    text-align: end;
    span {
      display: block;
      color: var(--grey-900);

      &:first-child {
        margin-bottom: 0.5rem;
        @include text-preset-4-bold;
      }

      &:last-child {
        color: var(--grey-500);
        @include text-preset-5;
      }
    }
  }
}

@media screen and (min-width: 48rem) {
  .transaction-item {
    &_user {
      img {
        width: 2.5rem;
      }
    }
  }
}
</style>
