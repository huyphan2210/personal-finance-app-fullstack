<template>
  <div class="pot-item">
    <small>{{ label }}</small>
    <span>{{ content }}</span>
  </div>
</template>

<script lang="ts" setup>
import type { IPotItem } from "./pot-item.model";

const { label, content } = defineProps<IPotItem>();
</script>

<style lang="scss" scoped>
.pot-item {
  position: relative;
  padding-left: 1.25rem;
  width: calc(50% - 1.75rem);

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
