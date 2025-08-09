<template>
  <button
    :class="{
      button: true,
      primary: appearance === ButtonAppearanceEnum.Primary,
      secondary: appearance === ButtonAppearanceEnum.Secondary,
      danger: appearance === ButtonAppearanceEnum.Danger,
    }"
    :type="type"
  >
    <slot></slot>
  </button>
</template>
<script lang="ts" setup>
import {
  ButtonAppearanceEnum,
  type IButton,
} from "~/interfaces/shared.interface";

const { type, appearance } = defineProps<IButton>();
</script>
<style lang="scss" scoped>
.button {
}
</style>
