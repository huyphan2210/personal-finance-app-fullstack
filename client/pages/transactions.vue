<template>
  <shared-page-heading />
  <form role="search" class="transactions">
    <fieldset class="transactions_filter">
      <div class="transactions_filter_search-field-wrapper">
        <input
          class="search-input"
          aria-label="Search fields for Transactions"
          type="search"
          name="Search Transactions"
          placeholder="Search Transactions"
        />
        <img
          src="../assets/images/search.svg"
          loading="lazy"
          alt="Search Icon"
        />
      </div>
    </fieldset>
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
    <nav class="transactions_pagination"></nav>
  </form>
</template>

<script setup lang="ts"></script>

<style lang="scss" scoped>
.transactions {
  flex: 1;
  background-color: var(--white);
  border-radius: 0.75rem;
  padding: 1.5rem 1.25rem;
  &_filter {
    display: flex;
    justify-content: space-between;
    gap: 1.5rem;
    &_search-field-wrapper {
      position: relative;
      .search-input {
        width: 100%;
        &::-webkit-search-decoration,
        &::-webkit-search-cancel-button,
        &::-webkit-search-results-button,
        &::-webkit-search-results-decoration {
          display: none;
        }
      }

      img {
        position: absolute;
        top: 50%;
        right: 1.25rem;
        transform: translateY(-50%);
      }
    }
  }
  &_table {
    table-layout: fixed;
    width: 100%;
    th,
    td {
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
