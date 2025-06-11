<template>
  <shared-page-heading />
  <form
    ref="form"
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
    <transactions-table
      :data="transactionItems"
      :class="{
        'is-loading': isLoading === true,
      }"
    />
    <transactions-table-nav :number-of-pages="paginationData.numberOfPages" />
  </form>
</template>

<script setup lang="ts">
import type { IDropdown } from "~/components/shared/dropdown/dropdown.modal";
import sortIcon from "../assets/images/sort.svg";
import categoryIcon from "../assets/images/category.svg";
import { EnumTransactionCategory } from "~/api";
import type {
  ITransactionItem,
  ITransactionSearchForm,
  ITransactionsNavigation,
} from "~/interfaces/transactions.interface";
import { getTransactions } from "~/services/transaction.service";

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

const formValues = reactive<ITransactionSearchForm>({
  searchString: undefined,
  sortBy: "Lastest",
  category: undefined,
  page: 1,
});

const form = ref<HTMLFormElement>();
const searchTimeout = ref<number>(0);
const transactionItems = ref<ITransactionItem[]>([]);
const isLoading = ref<boolean>(true);

const paginationData = ref<ITransactionsNavigation>({
  numberOfPages: 1,
});

onBeforeMount(() => searchTransactions());

const handleSearchString = (event: Event) => {
  clearTimeout(searchTimeout.value);
  formValues.searchString = (event.currentTarget as HTMLInputElement).value;
  searchTimeout.value = setTimeout(() => {
    form.value?.requestSubmit();
  }, 300);
};

const searchTransactions = async (event?: Event) => {
  event?.preventDefault();
  try {
    isLoading.value = true;
    const transactionsContent = await getTransactions(
      formValues.page,
      formValues.searchString,
      formValues.category,
      formValues.sortBy
    );

    transactionItems.value = transactionsContent.transactions.map(
      (transaction) => ({
        name: transaction.user,
        avatarUrl: transaction.avatarUrl,
        category: transaction.category,
        amount: transaction.amount,
        transactionDate: transaction.date,
      })
    );

    paginationData.value = {
      numberOfPages: transactionsContent.numberOfPages,
    };
  } catch (error) {
  } finally {
    isLoading.value = false;
  }
};
</script>

<style lang="scss" scoped>
.transactions {
  display: flex;
  flex-direction: column;
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
