<template>
  <aside class="sidebar">
    <nav>
      <ul>
        <li :class="{ active: pageStore.currentPage === Page.Home }">
          <NuxtLink :to="Page.Home">{{ pageHeadings[Page.Home] }}</NuxtLink>
        </li>
        <li :class="{ active: pageStore.currentPage === Page.Transactions }">
          <NuxtLink :to="Page.Transactions">{{
            pageHeadings[Page.Transactions]
          }}</NuxtLink>
        </li>
        <li :class="{ active: pageStore.currentPage === Page.Budgets }">
          <NuxtLink :to="Page.Budgets">{{
            pageHeadings[Page.Budgets]
          }}</NuxtLink>
        </li>
        <li :class="{ active: pageStore.currentPage === Page.Pots }">
          <NuxtLink :to="Page.Pots">{{ pageHeadings[Page.Pots] }}</NuxtLink>
        </li>
        <li :class="{ active: pageStore.currentPage === Page.RecurringBills }">
          <NuxtLink :to="Page.RecurringBills">{{
            pageHeadings[Page.RecurringBills]
          }}</NuxtLink>
        </li>
      </ul>
    </nav>
    <button type="button">Minimize Menu</button>
  </aside>
</template>

<script setup lang="ts">
import { usePageStore, pageHeadings } from "../stores/pages.store";
const pageStore = usePageStore();
</script>

<style lang="scss" scoped>
a {
  &.router-link-active.router-link-exact-active {
    color: var(--grey-900);
  }
}
</style>
