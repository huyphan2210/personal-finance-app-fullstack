<template>
  <li ref="cardItem">
    <span>{{ category }}</span>
    <span>
      {{ spentWithCurrency }} <small> of {{ maximumWithCurrency }}</small>
    </span>
  </li>
</template>
<script lang="ts" setup>
import { BudgetColorThemeEnum } from "~/api/data-contracts";
import type { IBudget } from "~/interfaces/budgets.interface";

const { colorTheme, category, spentWithCurrency, maximumWithCurrency } =
  defineProps<IBudget>();
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

li {
  display: flex;
  justify-content: space-between;
  padding-left: 1.25rem;
  position: relative;
  span {
    &:first-child {
      @include text-preset-4;
      color: var(--grey-500);
    }
    &:last-child {
      @include text-preset-3;
      color: var(--grey-900);
      small {
        @include text-preset-5;
        color: var(--grey-500);
      }
    }
  }

  &::before {
    content: "";
    position: absolute;
    height: 100%;
    max-height: 21px;
    width: 0.25rem;
    border-radius: 0.5rem;
    top: 0;
    left: 0;
  }

  @each $color in $colors {
    @include border-color($color);
  }
}
</style>
