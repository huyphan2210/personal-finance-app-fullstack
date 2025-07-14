<template>
  <section class="content-card">
    <hgroup class="content-card_heading-wrapper">
      <h2 ref="cardHeading" class="content-card_heading-wrapper_heading">
        {{ heading }}
      </h2>
      <div class="content-card_heading-wrapper_dropdown-wrapper">
        <button
          @click="openDropdownMenu"
          title="Open-Dropdown Button"
          type="button"
          class="content-card_heading-wrapper_dropdown-wrapper_button"
        >
          <svg
            width="14"
            height="4"
            viewBox="0 0 14 4"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M8.75 2C8.75 2.34612 8.64736 2.68446 8.45507 2.97225C8.26278 3.26003 7.98947 3.48434 7.6697 3.61679C7.34993 3.74924 6.99806 3.7839 6.65859 3.71637C6.31913 3.64885 6.00731 3.48218 5.76256 3.23744C5.51782 2.9927 5.35115 2.68087 5.28363 2.34141C5.2161 2.00194 5.25076 1.65007 5.38321 1.3303C5.51567 1.01053 5.73997 0.737221 6.02775 0.544928C6.31554 0.352636 6.65388 0.25 7 0.25C7.46413 0.25 7.90925 0.434375 8.23744 0.762563C8.56563 1.09075 8.75 1.53587 8.75 2ZM2 0.25C1.65388 0.25 1.31554 0.352636 1.02775 0.544928C0.739967 0.737221 0.515665 1.01053 0.383212 1.3303C0.250758 1.65007 0.216102 2.00194 0.283627 2.34141C0.351151 2.68087 0.517822 2.9927 0.762564 3.23744C1.00731 3.48218 1.31913 3.64885 1.65859 3.71637C1.99806 3.7839 2.34993 3.74924 2.6697 3.61679C2.98947 3.48434 3.26278 3.26003 3.45507 2.97225C3.64737 2.68446 3.75 2.34612 3.75 2C3.75 1.53587 3.56563 1.09075 3.23744 0.762563C2.90925 0.434375 2.46413 0.25 2 0.25ZM12 0.25C11.6539 0.25 11.3155 0.352636 11.0278 0.544928C10.74 0.737221 10.5157 1.01053 10.3832 1.3303C10.2508 1.65007 10.2161 2.00194 10.2836 2.34141C10.3512 2.68087 10.5178 2.9927 10.7626 3.23744C11.0073 3.48218 11.3191 3.64885 11.6586 3.71637C11.9981 3.7839 12.3499 3.74924 12.6697 3.61679C12.9895 3.48434 13.2628 3.26003 13.4551 2.97225C13.6474 2.68446 13.75 2.34612 13.75 2C13.75 1.77019 13.7047 1.54262 13.6168 1.3303C13.5288 1.11798 13.3999 0.925066 13.2374 0.762563C13.0749 0.600061 12.882 0.471156 12.6697 0.383211C12.4574 0.295265 12.2298 0.25 12 0.25Z"
              fill="var(--grey-300)"
            />
          </svg>
          <ul class="content-card_heading-wrapper_dropdown-wrapper_options">
            <li v-for="option in dropdownOptions">
              <button type="button" title="Option">{{ option.content }}</button>
            </li>
          </ul>
        </button>
      </div>
    </hgroup>
    <slot />
  </section>
</template>

<script lang="ts" setup>
import { BudgetColorThemeEnum } from "~/api/data-contracts";
import type { IContentCard } from "~/interfaces/shared.interface";

const { heading, colorTheme, dropdownOptions } = defineProps<IContentCard>();

const cardHeading = ref<HTMLHeadingElement>();
const colorObject = Object.fromEntries(
  Object.entries(BudgetColorThemeEnum).map(([key, value]) => [value, key])
);

onMounted(() => {
  if (colorObject[colorTheme]) {
    cardHeading.value?.classList.add(
      `theme-${colorObject[colorTheme].toLowerCase()}`
    );
  }
});

const openDropdownMenu = () => {};
</script>

<style lang="scss" scoped>
.content-card {
  @include card-spacing-style;

  &_heading-wrapper {
    display: flex;
    align-items: center;
    justify-content: space-between;
    &_heading {
      @include text-preset-2;
      color: var(--grey-900);
      display: flex;
      align-items: center;
      gap: 1rem;
      &::before {
        content: "";
        display: block;
        width: 1rem;
        height: 1rem;
        border-radius: 50%;
      }

      &.theme-green {
        &::before {
          background-color: var(--green);
        }
      }

      &.theme-purple {
        &::before {
          background-color: var(--purple);
        }
      }

      &.theme-cyan {
        &::before {
          background-color: var(--cyan);
        }
      }

      &.theme-navy {
        &::before {
          background-color: var(--navy);
        }
      }

      &.theme-yellow {
        &::before {
          background-color: var(--yellow);
        }
      }
    }

    &_dropdown-wrapper {
      position: relative;
      &_button {
        display: flex;
      }
    }
  }
}
</style>
