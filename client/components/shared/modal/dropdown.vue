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
      :disabled="isDisabled"
      @click="openDropdown"
    >
      <template v-if="settings.type === ModalDropdownEnumType.Text">
        {{ selectedOption }}
      </template>
      <template v-else-if="settings.type === ModalDropdownEnumType.Color">
        <span
          :class="[
            'modal-dropdown-wrapper_button_color',
            selectedOption?.toLocaleLowerCase(),
          ]"
        >
          {{ selectedOption }}
        </span>
      </template>
      <img
        class="modal-dropdown-wrapper_button_triangle"
        src="../../../assets/images/dropdown-triangle.svg"
        loading="lazy"
        alt="Dropdown Triangle"
      />
    </button>
    <ul class="modal-dropdown-wrapper_options">
      <shared-modal-dropdown-item
        :status="option.status"
        :on-select="(value: string) => {
          if (option.onSelect) {
            option.onSelect(value)
          }
          setSelectedOption(value)
        }"
        :item-value="option.itemValue"
        :item-label="option.itemLabel"
        v-for="option in settings.options"
      >
        <template v-if="settings.type === ModalDropdownEnumType.Text">
          {{ option.itemLabel }}
        </template>
        <template v-else-if="settings.type === ModalDropdownEnumType.Color">
          <span
            :class="[
              'modal-dropdown-item_content',
              option.itemLabel.toLocaleLowerCase(),
              option.status === ModalDropdownItemStatus.Used ? 'disabled' : '',
            ]"
          >
            {{ option.itemLabel }}
          </span>
        </template>
      </shared-modal-dropdown-item>
    </ul>
  </div>
</template>
<script lang="ts" setup>
import {
  ModalDropdownEnumType,
  ModalDropdownItemStatus,
  type IModalDropdown,
} from "~/interfaces/shared.interface";

const INPUT_ID = Math.random().toString();

const { settings, label, isDisabled } = defineProps<IModalDropdown>();
const dropdownWrapper = ref<HTMLDivElement>();

const selectedOption = ref<string>();

const setSelectedOption = (value: string) => {
  selectedOption.value = value;
  settings.options
    .filter((option) => option.status !== ModalDropdownItemStatus.Used)
    .forEach((option) => {
      if (option.itemLabel === selectedOption.value) {
        option.status = ModalDropdownItemStatus.Selected;
        return;
      }
      option.status = ModalDropdownItemStatus.Ready;
    });
  dropdownWrapper.value?.classList.remove("open");
};

const openDropdown = () => {
  dropdownWrapper.value?.classList.add("open");
};

const closeDropdown = (e: Event) => {
  if (!dropdownWrapper.value?.contains(e.target as Node)) {
    dropdownWrapper.value?.classList.remove("open");
  }
};

setSelectedOption(settings.options[0].itemValue);
if (settings.options[0].onSelect) {
  settings.options[0].onSelect(settings.options[0].itemValue);
}

onMounted(() => document.addEventListener("click", closeDropdown));
onUnmounted(() => document.removeEventListener("click", closeDropdown));
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
    color: var(--grey-900);
    &:disabled {
      background-color: var(--grey-100);
      cursor: not-allowed;
    }

    &_color {
      display: flex;
      gap: 0.75rem;
      align-items: center;
      &::before {
        content: "";
        width: 1rem;
        height: 1rem;
        border-radius: 50%;
      }

      @mixin button-prefix-color($color-name) {
        &.#{$color-name} {
          &::before {
            background-color: var(--#{$color-name});
          }
        }
      }
      @each $color in $colors {
        @include button-prefix-color($color);
      }
    }
  }

  &_options {
    position: absolute;
    z-index: 1;
    top: calc(100% + 1rem);
    width: calc(100% - 2.5rem);
    max-height: 17.25rem;
    list-style-type: none;
    background-color: var(--white);
    padding: 0.75rem 1.25rem;
    border-radius: 0.5rem;
    display: none;
    overflow: auto;
    box-shadow: 0 0.25rem 1.5rem rgba(0, 0, 0, 0.25);

    .modal-dropdown-item {
      &_content {
        display: flex;
        gap: 0.75rem;
        align-items: center;
        &::before {
          content: "";
          width: 1rem;
          height: 1rem;
          border-radius: 50%;
        }

        &.disabled {
          &::before {
            opacity: 0.25;
          }
        }

        @mixin prefix-color($color-name) {
          &.#{$color-name} {
            &::before {
              background-color: var(--#{$color-name});
            }
          }
        }
        @each $color in $colors {
          @include prefix-color($color);
        }
      }
    }
  }

  &.open {
    .modal-dropdown-wrapper {
      &_button {
        &_triangle {
          transform: rotate(180deg);
        }
      }

      &_options {
        transform-origin: top;
        display: flex;
        flex-direction: column;
        gap: 0.75rem;
        animation: show-dropdown ease-in-out 0.3s forwards;
      }
    }
  }
}
@keyframes show-dropdown {
  0% {
    transform: scaleY(0);
  }

  100% {
    transform: scaleY(1);
  }
}
</style>
