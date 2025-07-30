<template>
  <li class="modal-dropdown-item">
    <button
      @click="() => onSelect(itemValue)"
      class="modal-dropdown-item_button"
      type="button"
    >
      <slot></slot>
    </button>
  </li>
</template>
<script lang="ts" setup>
import type { IModalDropdownItem } from "~/interfaces/shared.interface";

const { onSelect, itemValue } = defineProps<IModalDropdownItem>();
</script>
<style lang="scss" scoped>
.modal-dropdown-item {
  padding-bottom: 0.75rem;
  border-bottom: solid 1px var(--grey-100);

  button {
    width: 100%;
    text-align: start;
  }
  &:last-child {
    padding-bottom: 0;
    border-bottom: none;
  }
}
</style>
