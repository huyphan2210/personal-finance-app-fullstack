<template>
  <li ref="cardItem" class="card-item">
    <small>{{ label }}</small>
    <span>${{ content }}</span>
  </li>
</template>

<script lang="ts" setup>
import type { ICardItem } from "./card-item.model";
import { BudgetColorThemeEnum } from "~/api/data-contracts";

const { label, content, colorTheme } = defineProps<ICardItem>();
const cardItem = ref<HTMLLIElement>();
const colorObject = Object.fromEntries(
  Object.entries(BudgetColorThemeEnum).map(([key, value]) => [value, key])
);

onMounted(() => {
  if (colorObject[colorTheme]) {
    cardItem.value?.classList.add(
      `border-${colorObject[colorTheme].toLowerCase()}`
    );
  }
});
</script>

<style lang="scss" scoped>
@mixin border-color($color) {
  &.border-#{$color} {
    &::before {
      background-color: var(--#{$color});
    }
  }
}
.card-item {
  @each $color in $colors {
    @include border-color($color);
  }
  
  display: block;
  position: relative;
  padding-left: 1.25rem;
  width: calc(50% - 1.75rem);
  min-width: 81px;

  &::before {
    content: "";
    position: absolute;
    height: 100%;
    width: 0.25rem;
    border-radius: 0.5rem;
    top: 0;
    left: 0;
  }

  small {
    color: var(--grey-500);

    @include text-preset-5;
  }

  span {
    display: block;
    color: var(--grey-900);
    margin-top: 0.25rem;

    @include text-preset-4-bold;
  }
}
</style>
