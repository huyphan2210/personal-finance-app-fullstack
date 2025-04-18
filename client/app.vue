<script setup lang="ts">
import Sidebar from "./components/sidebar.vue";
import { Page, usePageStore } from "./stores/pages.store";
const route = useRoute();
const pageStore = usePageStore();
pageStore.setCurrentPage(route.path as Page);
watch(
  () => route.path,
  (newPath) => {
    pageStore.setCurrentPage(newPath as Page);
  }
);
</script>

<template>
  <NuxtRouteAnnouncer />
  <main :class="{ second: pageStore.currentPage == Page.Login || pageStore.currentPage == Page.Signup }">
    <NuxtPage />
  </main>
  <Sidebar v-if="pageStore.currentPage !== Page.Login && pageStore.currentPage !== Page.Signup" />
  <Illustration v-else />
  <footer>
    Created by
    <a href="https://github.com/huyphan2210/" target="_blank">Huy Phan</a>
  </footer>
</template>

<style lang="scss" scoped>
.second {
  order: 2;

  @media screen and (min-width: 64rem) {
    order: unset;
  }
}
</style>
