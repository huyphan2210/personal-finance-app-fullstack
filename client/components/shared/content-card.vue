<template>
  <section class="content_card">
    <hgroup>
      <h2>{{ heading }}</h2>
    </hgroup>
    <slot />
  </section>
</template>

<script lang="ts" setup>
import type { IContentCard } from "~/interfaces/shared.interface";

const { heading, colorTheme } = defineProps<IContentCard>();

const svgFillColorRef = ref("var(--grey-500)");

const handleMouseOver = () => {
  svgFillColorRef.value = "var(--grey-900)";
};

const handleMouseLeave = () => {
  svgFillColorRef.value = "var(--grey-500)";
};
</script>

<style lang="scss" scoped>
.content_card {
  @include card-spacing-style;
}
</style>
