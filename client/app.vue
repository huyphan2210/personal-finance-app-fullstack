<script setup lang="ts">
import Sidebar from "./components/sidebar/index.vue";
import { Page, usePageStore } from "./stores/pages.store";
import axios from "axios";
import { serviceOptions } from "~/api";

const authenticationRoutes = [Page.Login, Page.Signup];

const route = useRoute();
const pageStore = usePageStore();
pageStore.setCurrentPage(route.path as Page);
watch(
  () => route.path,
  (newPath) => {
    pageStore.setCurrentPage(newPath as Page);
  }
);

const config = useRuntimeConfig();
serviceOptions.axios = axios.create({
  baseURL: config.public.apiBase,
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
});
</script>

<template>
  <NuxtRouteAnnouncer />
  <main
    :class="{ second: authenticationRoutes.includes(pageStore.currentPage) }"
  >
    <NuxtPage />
  </main>
  <Sidebar
    v-if="
      !authenticationRoutes.includes(pageStore.currentPage) &&
      pageStore.currentPage !== Page.Home
    "
  />
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

  @media screen and (min-width: 90rem) {
    order: unset;
  }
}
</style>
