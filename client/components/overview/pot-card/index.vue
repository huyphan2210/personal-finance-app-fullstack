<template>
  <overview-section-card
    class="overview_content--pots"
    :heading="pageHeadings[Page.Pots]"
    :navigate-to="Page.Pots"
    nav-content="See Details"
  >
    <div class="overview_content--pots_wrapper">
      <section class="overview_content--pots_wrapper_total-saved">
        <img
          src="../../../assets/images/pots.svg"
          loading="lazy"
          alt="Total Saved Icon"
        />
        <div class="overview_content--pots_wrapper_total-saved_text">
          <small>Total Saved</small>
          <span>${{ potsCardContent?.totalSaved }}</span>
        </div>
      </section>
      <ul class="overview_content--pots_wrapper_items">
        <overview-card-item
          class="pot-item"
          v-for="(potItem, index) in potsCardContent?.potItems"
          :label="potItem.name"
          :content="potItem.total.toString()"
          :class="{
            'border-green': index % 4 === 0,
            'border-cyan': index % 4 === 1,
            'border-navy': index % 4 === 2,
            'border-yellow': index % 4 === 3,
          }"
        />
      </ul>
    </div>
  </overview-section-card>
</template>

<script lang="ts" setup>
import type { IOverviewPotCard } from "./pot-card.model";

const { potsCardContent } = defineProps<IOverviewPotCard>();
</script>

<style lang="scss" scoped>
.overview_content--pots {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
  &_wrapper {
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
    &_total-saved {
      flex: 1;
      padding: 1rem;
      background-color: var(--beige-100);
      border-radius: 1rem;
      display: flex;
      align-items: center;
      gap: 1rem;

      &_text {
        small {
          color: var(--grey-500);
          @include text-preset-4;
        }

        span {
          display: block;
          margin-top: 11px;
          color: var(--grey-900);
          @include text-preset-1;
        }
      }
    }

    &_items {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      gap: 1rem;
    }
  }
}

@media screen and (min-width: 48rem) {
  .overview_content--pots {
    &_wrapper {
      flex-direction: unset;
      &_total-saved {
        min-width: 247px;
      }
    }
  }
}

@media screen and (min-width: 80rem) {
  .overview_content--pots {
    &_wrapper {
      &_items {
        max-width: 277px;
        .pot-item {
          width: unset;
        }
      }
    }
  }
}
</style>
