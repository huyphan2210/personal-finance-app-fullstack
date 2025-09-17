<template>
  <h1>{{ pageStore.currentPageHeading }}</h1>
</template>

<script setup lang="ts">
import { usePageStore } from "../../stores/pages.store";
const pageStore = usePageStore();

const assignHead = () =>
  useHead({
    title: pageStore.currentPageHeading,
    meta: [
      {
        name: pageStore.currentPageHeading,
        content: `This is my page for ${pageStore.currentPageHeading}`,
      },
    ],
  });
assignHead();
watch(
  () => pageStore.currentPageHeading,
  () => assignHead()
);
</script>
