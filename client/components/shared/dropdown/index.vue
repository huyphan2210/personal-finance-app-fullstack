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
        <svg
          class="dropdown-wrapper_button_content_current-icon"
          width="12"
          height="6"
          viewBox="0 0 12 6"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M11.3538 0.85375L6.35378 5.85375C6.30734 5.90024 6.2522 5.93712 6.1915 5.96228C6.1308 5.98744 6.06574 6.00039 6.00003 6.00039C5.93432 6.00039 5.86926 5.98744 5.80856 5.96228C5.74786 5.93712 5.69271 5.90024 5.64628 5.85375L0.646278 0.85375C0.576272 0.783823 0.528588 0.694696 0.509263 0.597654C0.489938 0.500611 0.49984 0.400016 0.537716 0.308605C0.575593 0.217193 0.63974 0.139075 0.722036 0.08414C0.804333 0.0292046 0.90108 -7.77138e-05 1.00003 1.549e-07L11 1.549e-07C11.099 -7.77138e-05 11.1957 0.0292046 11.278 0.08414C11.3603 0.139075 11.4245 0.217193 11.4623 0.308605C11.5002 0.400016 11.5101 0.500611 11.4908 0.597654C11.4715 0.694696 11.4238 0.783823 11.3538 0.85375Z"
            fill="#201F24"
          />
        </svg>
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
import { type IDropdown } from "./dropdown.modal";

const { mobileIcon, options, label } = defineProps<IDropdown>();
const dropdownWrapperRef = ref<HTMLDivElement>();
const optionListRef = ref<HTMLUListElement>();
const currentOption = ref<string>(options[0] || "");

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
    background-color: transparent !important;
    padding: 0 !important;

    &_content {
      display: none;
      &_current-option {
        color: var(--grey-900);
        font-weight: 400;
      }
    }

    img {
      vertical-align: top;
    }
  }

  &_option-list {
    background-color: var(--white);
    position: absolute;
    top: calc(100% + 1rem);
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
          padding-bottom: 0 !important;
        }
      }

      &_button {
        color: var(--grey-900) !important;
        background-color: transparent !important;
        text-align: left;
        padding: 0.75rem 0 !important;
        font-weight: 400 !important;

        &:hover,
        &.current {
          font-weight: 700 !important;
        }
      }
    }
  }
  &.open {
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
      border: solid 1px var(--beige-500) !important;
      padding: 0.75rem 1.25rem !important;
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
  }
}
</style>
