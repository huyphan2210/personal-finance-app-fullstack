<template>
  <li class="card-item">
    <small>{{ label }}</small>
    <span>${{ content }}</span>
  </li>
</template>

<script lang="ts" setup>
import type { ICardItem } from "./card-item.model";

const { label, content, colorTheme } = defineProps<ICardItem>();
</script>

<style lang="scss" scoped>
.card-item {
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

  &.border-green {
    &::before {
      background-color: var(--green);
    }
  }

  &.border-cyan {
    &::before {
      background-color: var(--cyan);
    }
  }

  &.border-navy {
    &::before {
      background-color: var(--navy);
    }
  }

  &.border-yellow {
    &::before {
      background-color: var(--yellow);
    }
  }
}
</style>
