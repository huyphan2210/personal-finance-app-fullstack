<template>
  <h1>{{ pageStore.currentPageHeading }}</h1>
</template>

<script setup lang="ts">
import { usePageStore } from "../../stores/pages.store";
const pageStore = usePageStore();
</script>
