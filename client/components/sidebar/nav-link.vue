<template>
  <li>
    <NuxtLink
      @mouseover="handleMouseOver"
      @mouseleave="handleMouseLeave"
      :to="page"
    >
      <shared-icon :type="type" :state="currentState" />
      <span>{{ pageHeadings[page] }}</span>
    </NuxtLink>
  </li>
</template>

<script lang="ts" setup>
import { IconType, IconState } from "~/types/icons";
import { usePageStore, pageHeadings, Page } from "../../stores/pages.store";

const { page } = defineProps<{
  page: Page;
}>();

const iconRecords: Record<Page, IconType> = {
  [Page.Overview]: IconType.Home,
  [Page.Home]: IconType.Home,
  [Page.Transactions]: IconType.Transactions,
  [Page.Budgets]: IconType.Budgets,
  [Page.Pots]: IconType.Pots,
  [Page.RecurringBills]: IconType.RecurringBills,
  [Page.Login]: IconType.Home,
  [Page.Signup]: IconType.Home,
};

const pageStore = usePageStore();

const currentState = ref<IconState>(
  pageStore.currentPage === page ? IconState.Active : IconState.Default
);

const type = ref<IconType>(iconRecords[page]);

const handleMouseOver = (e: MouseEvent) => {
  const link = e.currentTarget as HTMLAnchorElement;
  if (link.href.includes(pageStore.currentPage)) {
    return;
  }
  currentState.value = IconState.Hovered;
};

const handleMouseLeave = (e: MouseEvent) => {
  const link = e.currentTarget as HTMLAnchorElement;
  if (link.href.includes(pageStore.currentPage)) {
    return;
  }
  currentState.value = IconState.Default;
};

watch(
  () => pageStore.currentPage,
  (currentPage) => {
    currentState.value =
      currentPage === page ? IconState.Active : IconState.Default;
  }
);
</script>

<style lang="scss" scoped>
li {
  a {
    display: flex;
    flex-direction: column;
    align-items: center;
    min-width: 68.6px;
    padding-block: 0.5rem 0.75rem;
    position: relative;
    text-decoration: none;
    color: var(--grey-300);
    gap: 0.25rem;

    &:hover {
      color: var(--grey-100);
    }

    &.router-link-active.router-link-exact-active {
      color: var(--grey-900);
      background-color: var(--beige-100);
      border-radius: 0.5rem 0.5rem 0 0;

      &:hover {
        color: unset;
      }

      &::after {
        background-color: var(--green);
      }
    }

    &::after {
      position: absolute;
      content: "";
      left: 0;
      bottom: 0;
      width: 100%;
      height: 0.25rem;
      transition: 0.3s;
    }

    span {
      display: none;
      @include text-preset-5-bold;
    }
  }
}

@media screen and (min-width: 48rem) {
  li {
    a {
      min-width: 6.5rem;

      span {
        display: unset;
      }
    }
  }
}

@media screen and (min-width: 80rem) {
  li {
    a {
      flex-direction: unset;
      padding: 1rem 2rem;
      gap: 1rem;
      min-width: unset;

      &.router-link-active.router-link-exact-active {
        border-radius: 0 0.75rem 0.75rem 0;

        &::after {
          background-color: var(--green);
        }
      }

      &::after {
        top: 0;
        bottom: unset;
        width: 0.25rem;
        height: 100%;
      }

      span {
        @include text-preset-3;
      }
    }

    &.minimize {
      a {
        span {
          display: none;
        }
      }
    }
  }
}
</style>
