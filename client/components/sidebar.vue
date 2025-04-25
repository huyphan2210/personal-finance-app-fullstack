<template>
  <aside class="sidebar">
    <nav>
      <ul>
        <li :class="{ active: pageStore.currentPage === Page.Overview }">
          <NuxtLink @mouseover="handleMouseOver" :to="Page.Overview">
            <SharedIcon :type="IconType.Home"
              :state="pageStore.currentPage === Page.Overview ? IconState.Active : IconState.Default" />
            <span>{{ pageHeadings[Page.Overview] }}</span>
          </NuxtLink>
        </li>
        <li :class="{ active: pageStore.currentPage === Page.Transactions }">
          <NuxtLink @mouseover="handleMouseOver" :to="Page.Transactions">
            <SharedIcon :type="IconType.Transactions"
              :state="pageStore.currentPage === Page.Transactions ? IconState.Active : IconState.Default" />
            <span>{{ pageHeadings[Page.Transactions] }}</span>
          </NuxtLink>
        </li>
        <li :class="{ active: pageStore.currentPage === Page.Budgets }">
          <NuxtLink @mouseover="handleMouseOver" :to="Page.Budgets">
            <SharedIcon :type="IconType.Budgets"
              :state="pageStore.currentPage === Page.Budgets ? IconState.Active : IconState.Default" />
            <span>{{ pageHeadings[Page.Budgets] }}</span>
          </NuxtLink>
        </li>
        <li :class="{ active: pageStore.currentPage === Page.Pots }">
          <NuxtLink @mouseover="handleMouseOver" :to="Page.Pots">
            <SharedIcon :type="IconType.Pots"
              :state="pageStore.currentPage === Page.Pots ? IconState.Active : IconState.Default" />
            <span>{{ pageHeadings[Page.Pots] }}</span>
          </NuxtLink>
        </li>
        <li :class="{ active: pageStore.currentPage === Page.RecurringBills }">
          <NuxtLink @mouseover="handleMouseOver" :to="Page.RecurringBills">
            <SharedIcon :type="IconType.RecurringBills"
              :state="pageStore.currentPage === Page.RecurringBills ? IconState.Active : IconState.Default" />
            <span>{{ pageHeadings[Page.RecurringBills] }}</span>
          </NuxtLink>
        </li>
      </ul>
    </nav>
    <button class="sidebar_minimize-button" type="button">Minimize Menu</button>
  </aside>
</template>

<script setup lang="ts">
import { usePageStore, pageHeadings } from "../stores/pages.store";
import { IconType, IconState } from "../types/icons";
const pageStore = usePageStore();

const handleMouseOver = (e: MouseEvent) => {
  const link = e.currentTarget as HTMLAnchorElement;
}

</script>

<style lang="scss" scoped>
.sidebar {
  display: flex;
  background-color: var(--grey-900);
  border-radius: 0.5rem 0.5rem 0 0;
  padding-top: 0.5rem;
  padding-inline: 1rem;
  position: sticky;
  left: 0;
  bottom: 0;

  nav {
    flex: 1;
    display: flex;

    ul {
      flex: 1;
      display: flex;
      justify-content: space-between;
      list-style: none;

      li {
        a {
          display: flex;
          flex-direction: column;
          align-items: center;
          min-width: 68.6px;
          padding-block: 0.5rem 0.75rem;
          position: relative;

          &.router-link-active.router-link-exact-active {
            color: var(--grey-900);
            background-color: var(--beige-100);
            border-radius: 0.5rem 0.5rem 0 0;

            &::after {
              background-color: var(--green);
            }
          }

          &::after {
            position: absolute;
            content: '';
            left: 0;
            bottom: 0;
            width: 100%;
            height: 0.25rem;
            transition: 0.3s;
          }

          span {
            display: none;
          }
        }
      }
    }
  }

  &_minimize-button {
    display: none;
  }
}
</style>
