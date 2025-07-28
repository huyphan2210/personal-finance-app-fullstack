<template>
  <div ref="dropdownWrapper" class="modal-dropdown-wrapper">
    <label class="modal-dropdown-wrapper_label" :for="INPUT_ID">
      {{ label }}
    </label>
    <button
      class="modal-dropdown-wrapper_button"
      title="Open dropdown button"
      type="button"
      :id="INPUT_ID"
      @click="openDropdown"
    ></button>
    <ul class="modal-dropdown-wrapper_options"></ul>
  </div>
</template>
<script lang="ts" setup>
import type {
  IModalDropdown,
  ModalDropdownEnumType,
} from "~/interfaces/shared.interface";

const INPUT_ID = Math.random().toString();

const { settings, label } = defineProps<IModalDropdown>();
const dropdownWrapper = ref<HTMLDivElement>();

const openDropdown = () => {
  dropdownWrapper.value?.classList.add("open");
};
</script>
<style lang="scss" scoped>
.modal-dropdown-wrapper {
  position: relative;

  &_label {
    @include label-style;
  }

  &_button {
    @include input-wrapper-style;
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
  }

  &_options {
    position: absolute;
    top: 100%;
    width: 100%;
    list-style-type: none;
  }
}
</style>
