<template>
  <aside class="sidebar">
    <nav>
      <ul>
        <SidebarNavLink
          v-for="nav in listOfNavigations"
          :page="nav"
        ></SidebarNavLink>
      </ul>
    </nav>
    <button class="sidebar_minimize-button" type="button">Minimize Menu</button>
  </aside>
</template>

<script setup lang="ts">
const listOfNavigations: Page[] = [
  Page.Overview,
  Page.Transactions,
  Page.Budgets,
  Page.Pots,
  Page.RecurringBills,
];
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
    }
  }

  &_minimize-button {
    display: none;
  }
}
</style>
