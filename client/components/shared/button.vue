<template>
  <button
    :class="{
      btn: true,
      primary: appearance === ButtonAppearanceEnum.Primary,
      secondary: appearance === ButtonAppearanceEnum.Secondary,
      danger: appearance === ButtonAppearanceEnum.Danger,
    }"
    :type="type"
    :disabled="isDisabled"
    @click="onClick"
  >
    <slot></slot>
  </button>
</template>
<script lang="ts" setup>
import {
  ButtonAppearanceEnum,
  type IButton,
} from "~/interfaces/shared.interface";

const { type, appearance, isDisabled, onClick } = defineProps<IButton>();
</script>
<style lang="scss" scoped>
.btn {
  @include text-preset-4-bold;
  padding: 1rem;
  border-radius: 0.5rem;

  &.primary {
    color: var(--white);
    background-color: var(--grey-900);

    &:hover {
      background-color: var(--grey-500);
    }
  }

  &.secondary {
    @include text-preset-4;
    color: var(--grey-500);
    padding: 0;

    &:hover {
      color: var(--grey-900);
    }
  }

  &.danger {
    background-color: var(--red);
    color: var(--white);

    &:hover {
      background-color: color-mix(in srgb, var(--red), transparent 20%);
    }
  }
}
</style>
