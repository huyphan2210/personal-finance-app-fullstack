<script setup lang="ts">
import Sidebar from "./components/sidebar/index.vue";
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

const authenticationRoutes = [Page.Login, Page.Signup]
</script>

<template>
  <NuxtRouteAnnouncer />
  <main :class="{ second: authenticationRoutes.includes(pageStore.currentPage) }">
    <NuxtPage />
  </main>
  <Sidebar v-if="!authenticationRoutes.includes(pageStore.currentPage) && pageStore.currentPage !== Page.Home" />
  <Illustration v-else />
  <footer>
    Created by
    <a href="https://github.com/huyphan2210/" target="_blank">Huy Phan</a>
  </footer>
  <SharedErrorModal />
</template>

<style lang="scss" scoped>
.second {
  order: 2;

  @media screen and (min-width: 64rem) {
    order: unset;
  }
}
</style>
