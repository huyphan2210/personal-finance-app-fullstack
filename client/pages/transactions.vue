<template>
  <shared-page-heading />
  <form
    ref="form"
    role="search"
    class="transactions"
    @submit="searchTransactions"
  >
    <fieldset class="transactions_filter">
      <shared-input
        class="transactions_filter_search-field-wrapper"
        :type="InputEnumType.Search"
        :custom-input-handler="handleSearchString"
        placeholder="Search by Name or Amount"
      >
        <button type="button">
          <img
            src="../assets/images/search.svg"
            loading="lazy"
            alt="Search Icon"
          />
        </button>
      </shared-input>
      <div class="transactions_filter_dropdowns">
        <shared-dropdown
          v-for="filter in filters"
          :mobile-icon="filter.mobileIcon"
          :label="filter.label"
          :options="filter.options"
          :on-selection="filter.onSelection"
          :for-field="filter.forField"
          :pre-selected-option="filter.preSelectedOption"
          :class="{
            'category-dropdown': filter.forField === 'category',
          }"
        />
      </div>
    </fieldset>
    <transactions-table
      :data="transactionItems"
      :class="{
        'is-loading': isLoading === true,
      }"
    />
    <transactions-table-nav
      :pre-selected-page="formValues.page"
      :number-of-pages="pageNumber"
      :setPage="setCurrentPage"
    />
  </form>
</template>

<script setup lang="ts">
import { type IDropdown } from "~/interfaces/shared.interface";
import sortIcon from "../assets/images/sort.svg";
import categoryIcon from "../assets/images/category.svg";
import type {
  FormFieldTypes,
  ITransactionItem,
  ITransactionSearchForm,
} from "~/interfaces/transactions.interface";
import { getTransactions } from "~/services/transactions.service";
import {
  TransactionCategoryEnum,
  type Transaction,
} from "~/api/data-contracts";
import { InputEnumType } from "~/interfaces/shared.interface";
import { sortOptions } from "~/services/base.service";

const categoryOptions = [
  "All Transactions",
  ...Object.values(TransactionCategoryEnum),
];

const router = useRouter();
const route = useRoute();
const {
  search,
  sortBy,
  category,
  page,
}: { search?: string; sortBy?: string; category?: string; page?: string } =
  route.query;

const pageInteger = parseInt(page || "1");
const errorStore = useErrorStore();
const form = ref<HTMLFormElement>();
const searchTimeout = ref<NodeJS.Timeout>();
const transactionItems = ref<ITransactionItem[]>([]);
const isLoading = ref<boolean>(true);
const pageNumber = ref<number>(1);
const formValues = reactive<ITransactionSearchForm>({
  searchString: search,
  sortBy: sortOptions.find((option) => option === sortBy) ?? sortOptions[0],
  category: categoryOptions.find((option) => option === category),
  page: isNaN(pageInteger) || pageInteger <= 0 ? 1 : pageInteger,
});

const handleFilter = (field: FormFieldTypes, value?: string) => {
  switch (field) {
    case "category":
      formValues.page = 1;
      if (value === "All Transactions") {
        value = undefined;
      }
      break;
    default:
      break;
  }

  formValues[field] = value;
  searchTransactions();
};

const filters: IDropdown[] = [
  {
    mobileIcon: sortIcon,
    label: "Sort by",
    options: sortOptions,
    onSelection: handleFilter,
    forField: "sortBy",
    preSelectedOption: formValues.sortBy,
  },
  {
    mobileIcon: categoryIcon,
    label: "Category",
    options: categoryOptions,
    onSelection: handleFilter,
    forField: "category",
    preSelectedOption: formValues.category,
  },
];

const setCurrentPage = (page: number) => {
  formValues.page = page;
  searchTransactions();
};

onBeforeMount(() => searchTransactions());

const handleSearchString = (event?: Event) => {
  clearTimeout(searchTimeout.value);
  const value = (event?.currentTarget as HTMLInputElement)?.value || undefined;
  formValues.searchString = value;
  formValues.page = 1;
  searchTimeout.value = setTimeout(() => {
    searchTransactions();
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

    router.push({
      query: {
        page: formValues.page,
        search: formValues.searchString,
        sortBy: formValues.sortBy,
        category: formValues.category,
      },
    });

    transactionItems.value = transactionsContent.transactions.map(
      (transaction: Transaction) => ({
        name: transaction.user,
        avatarUrl: transaction.avatarUrl,
        category: transaction.category,
        amount: transaction.amount,
        transactionDate: transaction.date,
      })
    );

    pageNumber.value = transactionsContent.numberOfPages;
    formValues.page = transactionsContent.currentPage;
    window.scroll({
      top: 0,
      behavior: "smooth",
    });
  } catch (error) {
    if (error instanceof Error) {
      errorStore.setErrorMessage(error.message);
    } else {
      errorStore.setDefaultErrorMessage();
    }
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
