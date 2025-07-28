<template>
  <li class="modal-dropdown-item">
    <button class="modal-dropdown-item_button" type="button">
      <slot></slot>
    </button>
  </li>
</template>
<script lang="ts">
import type { IModalDropdownItem } from "~/interfaces/shared.interface";

const props = defineProps<IModalDropdownItem>();
</script>
<style lang="scss" scoped></style>
