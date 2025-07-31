<template>
  <div ref="dropdownWrapperRef" class="dropdown-wrapper">
    <span class="dropdown-wrapper_label">{{ label }}</span>
    <button
      class="dropdown-wrapper_button"
      type="button"
      @click="handleDropdown"
    >
      <div class="dropdown-wrapper_button_content">
        <span class="dropdown-wrapper_button_content_current-option">
          {{ currentOption }}
        </span>
        <img
          src="../../assets/images/dropdown-triangle.svg"
          loading="lazy"
          alt="Dropdown Triangle"
        />
      </div>
      <img
        class="dropdown-wrapper_icon"
        :src="mobileIcon"
        loading="lazy"
        :alt="label"
      />
      <ul ref="optionListRef" class="dropdown-wrapper_option-list">
        <li class="dropdown-wrapper_option-list_label">{{ label }}</li>
        <li
          v-for="(option, index) in options"
          :class="{
            'dropdown-wrapper_option-list_item': true,
            'first-option': index === 0,
            'last-option': index === options.length - 1,
          }"
        >
          <button
            :class="{
              'dropdown-wrapper_option-list_item_button': true,
              current: currentOption === option,
            }"
            type="button"
            @click="() => handleOption(option)"
          >
            {{ option }}
          </button>
        </li>
      </ul>
    </button>
  </div>
</template>
<script lang="ts" setup>
import { type IDropdown } from "~/interfaces/shared.interface";

const { preSelectedOption, mobileIcon, options, label, onSelection, forField } =
  defineProps<IDropdown>();
const dropdownWrapperRef = ref<HTMLDivElement>();
const optionListRef = ref<HTMLUListElement>();
const currentOption = ref<string>(preSelectedOption || options[0] || "");

const handleDropdown = (e: MouseEvent) => {
  if (optionListRef.value?.contains(e.srcElement as Node)) {
    return;
  }

  document
    .querySelectorAll(".dropdown-wrapper")
    .forEach((list) => list.classList.remove("open"));

  if (!dropdownWrapperRef.value?.classList.contains("open")) {
    dropdownWrapperRef.value?.classList.add("open");
  }
};

const closeDropdown = (event: MouseEvent) => {
  if (!dropdownWrapperRef.value?.contains(event.target as Node)) {
    dropdownWrapperRef.value?.classList.remove("open");
  }
};

const handleOption = (option: string) => {
  currentOption.value = option;
  onSelection(forField, option);
  dropdownWrapperRef.value?.classList.remove("open");
};

onMounted(() => {
  document.addEventListener("click", closeDropdown);
});
</script>
<style lang="scss" scoped>
.dropdown-wrapper {
  position: relative;
  display: flex;
  align-items: center;
  gap: 0.5rem;

  &_label {
    display: none;
    white-space: nowrap;
    color: var(--grey-500);
    @include text-preset-4;
  }

  &_button {
    border-radius: 0.5rem;
    &:hover {
      cursor: auto;
    }

    &_content {
      display: none;
      &:hover {
        cursor: pointer;
      }
      &_current-option {
        color: var(--grey-900);
        font-weight: 400;
      }
    }

    img {
      vertical-align: top;
      &:hover {
        cursor: pointer;
      }
    }
  }

  &_option-list {
    background-color: var(--white);
    position: absolute;
    top: calc(100% + 1rem);
    text-align: left;
    right: 0;
    transform: scaleY(0);
    padding: 0.75rem 1.25rem;
    transform-origin: top;
    border-radius: 0.5rem;
    box-shadow: 0 0.25rem 1.5rem rgba(0, 0, 0, 0.25);
    &_label,
    &_item {
      display: block;
      width: 100%;
      min-width: 74px;
      white-space: nowrap;
      @include text-preset-4;
    }

    &_label {
      color: var(--grey-500);
      padding-bottom: 0.75rem;
      pointer-events: none;
      border-bottom: solid 1px var(--grey-100);
    }

    &_item {
      border-top: solid 1px var(--grey-100);

      &.first-option {
        border-top: none;
      }

      &.last-option {
        .dropdown-wrapper_option-list_item_button {
          padding-bottom: 0;
        }
      }

      &_button {
        display: block;
        width: 100%;
        color: var(--grey-900);
        background-color: transparent;
        text-align: left;
        padding: 0.75rem 0;
        font-weight: 400;

        &:hover,
        &.current {
          font-weight: 700;
        }
      }
    }
  }
  &.open {
    .dropdown-wrapper_button_content {
      img {
        transform: rotate(180deg);
      }
    }
    .dropdown-wrapper_option-list {
      transform: scaleY(1);
    }
  }
}

@media screen and (min-width: 48rem) {
  .dropdown-wrapper {
    &_label {
      display: unset;
    }

    &_icon {
      display: none;
    }

    &_button {
      &:hover {
        cursor: pointer;
      }
      border: solid 1px var(--beige-500);
      padding: 0.75rem 1.25rem;
      position: relative;
      &_content {
        display: flex;
        align-items: center;
        gap: 1rem;
      }
    }

    &_option-list {
      width: calc(100% - 2.5rem);
      &_label {
        display: none;
      }
    }

    &.category-dropdown {
      .dropdown-wrapper {
        &_button {
          &_content {
            justify-content: space-between;
            min-width: 8rem;
          }
        }
      }
    }
  }
}
</style>
