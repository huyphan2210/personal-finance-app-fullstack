<template>
  <shared-page-heading />
  <section class="transactions">
    <section class="transactions_filter"></section>
    <table class="transactions_table">
      <thead>
        <tr>
          <th>Recipient / Sender</th>
          <th>Category</th>
          <th>Transaction Date</th>
          <th>Amount</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>Recipient / Sender</th>
          <th>Category</th>
          <th>Transaction Date</th>
          <th>Amount</th>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<script setup lang="ts"></script>

<style lang="scss" scoped>
.transactions {
  flex: 1;
  background-color: var(--white);
  border-radius: 0.75rem;
  padding: 1.5rem 1.25rem;
  &_table {
    table-layout: fixed;
    width: 100%;
    th, td {
      text-align: start;
      color: var(--grey-500);
      @include text-preset-5;

      &:last-child {
        text-align: end;
      }

      &:not(:last-child):not(:first-child) {
        display: none;
      }
    }

    thead {
      display: none;
    }
  }
}
</style>
