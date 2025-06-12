<template>
  <nav class="transactions_pagination">
    <ul class="transactions_pagination_list">
      <li class="transactions_pagination_list_item prev">
        <button
          type="button"
          :disabled="currentPage === 1"
          @click="setCurrentPage(currentPage - 1)"
        >
          <svg
            width="16"
            height="16"
            viewBox="0 0 16 16"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M10.1467 12.8541L5.14674 7.85414C5.10025 7.80771 5.06337 7.75256 5.03821 7.69186C5.01305 7.63117 5.0001 7.5661 5.0001 7.50039C5.0001 7.43469 5.01305 7.36962 5.03821 7.30892C5.06337 7.24823 5.10025 7.19308 5.14674 7.14664L10.1467 2.14664C10.2167 2.07664 10.3058 2.02895 10.4028 2.00963C10.4999 1.9903 10.6005 2.00021 10.6919 2.03808C10.7833 2.07596 10.8614 2.14011 10.9163 2.2224C10.9713 2.3047 11.0006 2.40145 11.0005 2.50039L11.0005 12.5004C11.0006 12.5993 10.9713 12.6961 10.9163 12.7784C10.8614 12.8607 10.7833 12.9248 10.6919 12.9627C10.6005 13.0006 10.4999 13.0105 10.4028 12.9912C10.3058 12.9718 10.2167 12.9242 10.1467 12.8541Z"
              fill="#696868"
            />
          </svg>
          <span>Prev</span>
        </button>
      </li>
      <li
        v-for="(content, index) in pagination"
        :class="{
          transactions_pagination_list_item: true,
          current: currentPage === content,
        }"
      >
        <button
          type="button"
          :disabled="content === '...'"
          @click="setCurrentPage(typeof content === 'number' ? content : 0)"
        >
          {{ content }}
        </button>
      </li>
      <li class="transactions_pagination_list_item next">
        <button
          type="button"
          :disabled="currentPage === numberOfPages"
          @click="setCurrentPage(currentPage + 1)"
        >
          <span>Next</span>
          <svg
            width="16"
            height="16"
            viewBox="0 0 16 16"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M5.85375 3.14585L10.8537 8.14586C10.9002 8.19229 10.9371 8.24744 10.9623 8.30814C10.9874 8.36883 11.0004 8.4339 11.0004 8.49961C11.0004 8.56531 10.9874 8.63038 10.9623 8.69108C10.9371 8.75177 10.9002 8.80692 10.8538 8.85336L5.85375 13.8534C5.78382 13.9234 5.6947 13.971 5.59765 13.9904C5.50061 14.0097 5.40002 13.9998 5.3086 13.9619C5.21719 13.924 5.13908 13.8599 5.08414 13.7776C5.0292 13.6953 4.99992 13.5986 5 13.4996L5 3.49961C4.99992 3.40066 5.0292 3.30391 5.08414 3.22161C5.13907 3.13932 5.21719 3.07517 5.3086 3.03729C5.40002 2.99942 5.50061 2.98952 5.59765 3.00884C5.6947 3.02817 5.78382 3.07585 5.85375 3.14585Z"
              fill="#696868"
            />
          </svg>
        </button>
      </li>
    </ul>
  </nav>
</template>
<script lang="ts" setup>
import type { ITransactionsNavigation } from "~/interfaces/transactions.interface";

const { numberOfPages, setPage } = defineProps<ITransactionsNavigation>();
const currentPage = ref<number>(1);
const pagination = ref<(number | string)[]>([1]);
let pageAroundCurrent = 0;

const setCurrentPage = (page: number) => {
  if (page === currentPage.value || page === 0) {
    return;
  }
  currentPage.value = page;
  handlePagination();
  setPage(currentPage.value);
};

const handlePagination = (): void => {
  const range: (number | string)[] = [];
  if (window.innerWidth >= 768 && numberOfPages <= 10) {
    pageAroundCurrent = 2;
    for (let i = 1; i <= numberOfPages; i++) {
      range.push(i);
    }
  } else {
    if (window.innerWidth >= 768) {
      pageAroundCurrent = 1;
    } else {
      pageAroundCurrent = 0;
    }

    const left = Math.max(2, currentPage.value - pageAroundCurrent);
    const right = Math.min(
      numberOfPages - 1,
      currentPage.value + pageAroundCurrent
    );

    range.push(1);

    if (left > 2) {
      range.push("...");
    }

    for (let i = left; i <= right; i++) {
      range.push(i);
    }

    if (right < numberOfPages - 1) {
      range.push("...");
    }

    range.push(numberOfPages);
  }

  pagination.value = range;
};
watch(
  () => numberOfPages,
  () => handlePagination()
);

window.addEventListener("resize", handlePagination);

onUnmounted(() => {
  window.removeEventListener("resize", handlePagination);
});
</script>
<style lang="scss" scoped>
.transactions_pagination {
  margin-top: auto;
  &_list {
    display: flex;
    gap: 0.5rem;
    &_item {
      display: block;

      &.current {
        button {
          background-color: var(--grey-900);
          color: var(--white);
        }
      }

      button {
        border: solid 1px var(--beige-500);
        padding: 0.75rem 1.25rem;
        position: relative;
        display: flex;
        align-items: center;
        gap: 1rem;
        border-radius: 0.5rem;

        span {
          display: none;
        }

        &:hover:not(.current) {
          background-color: var(--beige-500);
          color: var(--white);
          svg {
            path {
              fill: var(--white);
            }
          }

          &:disabled {
            cursor: not-allowed;
          }
        }
      }

      &.prev {
        margin-right: auto;
      }

      &.next {
        margin-left: auto;
      }
    }
  }
}
</style>
