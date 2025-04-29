<template>
  <div class="summary-card">
    <small>{{ cardHeading }}</small>
    <span>{{ cardContent }}</span>
  </div>
</template>

<script lang="ts" setup>
const { cardHeading, cardContent } = defineProps<{
  cardHeading: string,
  cardContent: string
}>();
</script>

<style lang="scss" scoped>
.summary-card {
  background-color: var(--white);
  padding: 1.25rem;
  border-radius: 0.75rem;

  small {
    color: var(--grey-500);
    @include text-preset-4;
  }

  span {
    color: var(--grey-900);
    display: block;
    margin-top: 0.75rem;
    @include text-preset-1;
  }

  &.main {
    background-color: var(--grey-900);

    small {
      color: var(--white);
    }

    span {
      color: var(--white);
    }
  }
}
</style>
