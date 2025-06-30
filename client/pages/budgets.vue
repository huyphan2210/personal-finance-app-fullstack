<template>
  <hgroup class="budgets_heading">
    <shared-page-heading />
    <button class="budgets_heading_button--add-new" type="button">
      + Add New Budget
    </button>
  </hgroup>
  <section class="budgets_content">
    <section class="budgets_content_spending-summary"></section>
  </section>
</template>

<script setup lang="ts"></script>

<style lang="scss" scoped>
.budgets {
  &_heading {
    display: flex;
    justify-content: space-between;
    &_button {
      &--add-new {
        padding: 1rem;
        border-radius: 0.5rem;
        color: var(--white);
        background-color: var(--grey-900);
        @include text-preset-4-bold;
      }
    }
  }
}
</style>
