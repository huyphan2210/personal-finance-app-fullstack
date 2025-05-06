<template>
  <aside ref="sidebarRef" class="sidebar">
    <nav>
      <shared-logo class="logo" />
      <ul ref="navListRef">
        <sidebar-nav-link ref="listItems" v-for="nav in listOfNavigations" :page="nav" />
      </ul>
    </nav>
    <button @mouseenter="() => isButtonHovered = true" @mouseleave="() => isButtonHovered = false"
      @click="handleSizeOfBar" class="sidebar_minimize-button" type="button">
      <shared-icon class="sidebar_minimize-button_icon--right" :type="IconType.ArrowRight"
        :state="isButtonHovered ? IconState.Hovered : IconState.Default" />
      <shared-icon class=" sidebar_minimize-button_icon--left" :type="IconType.ArrowLeft"
        :state="isButtonHovered ? IconState.Hovered : IconState.Default" />
      <span>Minimize Menu</span>
    </button>
  </aside>
</template>

<script setup lang="ts">
import type { SidebarNavLink } from '#components';
import { IconState, IconType } from '~/types/icons';

const sidebarRef = ref<HTMLElement>();
const navListRef = ref<HTMLUListElement>();

const isButtonHovered = ref(false);

const listOfNavigations: Page[] = [
  Page.Overview,
  Page.Transactions,
  Page.Budgets,
  Page.Pots,
  Page.RecurringBills,
];

const handleSizeOfBar = (e: MouseEvent) => {
  const sidebarElement = sidebarRef.value;
  const navListElement = navListRef.value;
  const minimizeButton = e.currentTarget as HTMLButtonElement;
  const minimizeClass = "minimize";

  if (sidebarElement && navListElement) {
    minimizeButton.classList.toggle(minimizeClass);
    sidebarElement.classList.toggle(minimizeClass);
    const links = navListElement.getElementsByTagName("li");
    for (let i = 0; i < links.length; i++) {
      links[i].classList.toggle(minimizeClass);
    }
  }
}
</script>

<style lang="scss" scoped>
.sidebar {
  display: flex;
  background-color: var(--grey-900);
  border-radius: 0.5rem 0.5rem 0 0;
  padding-top: 0.5rem;
  padding-inline: 1rem;
  position: sticky;
  left: 0;
  bottom: 0;

  .logo {
    display: none;
    padding: 2.5rem 2rem;
  }

  nav {
    flex: 1;
    display: flex;

    ul {
      flex: 1;
      display: flex;
      justify-content: space-between;
      list-style: none;
    }
  }

  &_minimize-button {
    display: none;
    margin-top: auto;
    border: 0;
    background-color: transparent;
    padding: 1rem 2rem;
    color: var(--grey-300);
    @include text-preset-3;

    &:hover {
      cursor: pointer;
      color: var(--grey-100);
    }
  }
}

@media screen and (min-width: 64rem) {
  .sidebar {
    width: 18.75rem;
    padding: 0;
    padding-bottom: 1.5rem;
    flex-direction: column;
    gap: 1.5rem;

    &.minimize {
      width: 5.5rem;
      overflow: hidden;

      .logo {
        display: flex;
        justify-content: center;
        align-items: center;
      }

      nav {
        padding-right: 0;

        ul {
          padding-right: 0.5rem;
        }
      }

      .sidebar_minimize-button {
        display: flex;
        align-items: center;
        gap: 1rem;

        &_icon {
          &--right {
            display: unset;
          }

          &--left {
            display: none;
          }
        }
      }
    }

    .logo {
      display: unset;
    }

    nav {
      flex-direction: column;
      flex: unset;
      gap: 1.5rem;
      padding-right: 1.5rem;

      ul {
        flex-direction: column;
        justify-content: start;
      }
    }

    &_minimize-button {
      display: flex;
      align-items: center;
      gap: 1rem;

      &_icon {
        &--right {
          display: none;
        }
      }

      &.minimize {
        span {
          display: none;
        }
      }
    }
  }
}
</style>
