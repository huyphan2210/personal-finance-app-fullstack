<template>
  <li class="modal-dropdown-item">
    <button
      @click="() => onSelect && onSelect(itemValue)"
      :class="{
        'modal-dropdown-item_button': true,
        selected: status === ModalDropdownItemStatus.Selected,
      }"
      type="button"
      :disabled="status === ModalDropdownItemStatus.Used"
    >
      <slot></slot>
    </button>
  </li>
</template>
<script lang="ts" setup>
import {
  ModalDropdownItemStatus,
  type IModalDropdownItem,
} from "~/interfaces/shared.interface";

const { onSelect, itemValue, status } = defineProps<IModalDropdownItem>();
</script>
<style lang="scss" scoped>
.modal-dropdown-item {
  padding-bottom: 0.75rem;
  border-bottom: solid 1px var(--grey-100);

  button {
    width: 100%;
    text-align: start;
    &:disabled {
      cursor: not-allowed;
    }
  }

  &:last-child {
    padding-bottom: 0;
    border-bottom: none;
  }
}
</style>
