<template>
  <shared-page-heading />
  <form
    ref="formRef"
    role="search"
    class="transactions"
    @submit="searchTransactions"
  >
    <fieldset class="transactions_filter">
      <div class="transactions_filter_search-field-wrapper">
        <input
          class="search-input"
          aria-label="Search fields for Transactions"
          type="search"
          name="Search Transactions"
          placeholder="Search Transactions"
          @input="handleSearchString"
        />
        <button type="button">
          <img
            src="../assets/images/search.svg"
            loading="lazy"
            alt="Search Icon"
          />
        </button>
      </div>
      <div class="transactions_filter_dropdowns">
        <shared-dropdown
          v-for="filter in filters"
          :mobile-icon="filter.mobileIcon"
          :label="filter.label"
          :options="filter.options"
        />
      </div>
    </fieldset>
    <transactions-table :data="transactionItems" />
    <transactions-table-nav
      :current-page="paginationData.currentPage"
      :number-of-pages="paginationData.numberOfPages"
    />
  </form>
</template>

<script setup lang="ts">
import type { IDropdown } from "~/components/shared/dropdown/dropdown.modal";
import sortIcon from "../assets/images/sort.svg";
import categoryIcon from "../assets/images/category.svg";
import { EnumTransactionCategory } from "~/api";
import type {
  ITransactionItem,
  ITransactionsNavigation,
} from "~/interfaces/transactions.interface";

const filters: IDropdown[] = [
  {
    mobileIcon: sortIcon,
    label: "Sort by",
    options: ["Latest", "Oldest", "A to Z", "Z to A", "Highest", "Lowest"],
  },
  {
    mobileIcon: categoryIcon,
    label: "Category",
    options: ["All Transactions", ...Object.values(EnumTransactionCategory)],
  },
];

const formRef = ref<HTMLFormElement>();
const searchTimeout = ref<number>(0);

const transactionItems: ITransactionItem[] = [
  {
    name: "Emma Richardson",
    avatarUrl:
      "https://res.cloudinary.com/dejteftxn/image/upload/v1747793082/emma-richardson_b0zi3o.jpg",
    category: EnumTransactionCategory.General,
    transactionDate: "2024-08-19T14:23:11+00:00",
    amount: 75.5,
  },
];

const paginationData: ITransactionsNavigation = {
  currentPage: 1,
  numberOfPages: 5,
};

const formValues = reactive({
  searchString: "",
  sortBy: "Lastest",
  category: "All Transactions",
  page: 1,
});

onBeforeMount(() => searchTransactions);

const handleSearchString = (event: Event) => {
  clearTimeout(searchTimeout.value);
  formValues.searchString = (event.currentTarget as HTMLInputElement).value;
  searchTimeout.value = setTimeout(() => {
    formRef.value?.requestSubmit();
  }, 300);
};

const searchTransactions = (event?: Event) => {
  event?.preventDefault();
  // TODO: Call Transactions API
};
</script>

<style lang="scss" scoped>
.transactions {
  flex: 1;
  background-color: var(--white);
  border-radius: 0.75rem;
  padding: 1.5rem 1.25rem;
  &_filter {
    display: flex;
    justify-content: space-between;
    gap: 1.5rem;
    margin-bottom: 1.5rem;

    &_search-field-wrapper {
      position: relative;
      flex: 1;
      max-width: 20rem;
      .search-input {
        width: 100%;
        padding-right: 3.25rem !important;
        &::-webkit-search-decoration,
        &::-webkit-search-cancel-button,
        &::-webkit-search-results-button,
        &::-webkit-search-results-decoration {
          display: none;
        }
      }

      button {
        position: absolute;
        top: 50%;
        right: 1.25rem;
        transform: translateY(-50%);

        img {
          vertical-align: top;
        }
      }
    }

    &_dropdowns {
      display: flex;
      gap: 1.5rem;
    }
  }
}

@media screen and (min-width: 48rem) {
  .transactions {
    padding: 2rem;
  }
}
</style>
