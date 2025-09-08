<template>
  <shared-page-heading />
  <section class="recurring-bills">
    <section class="recurring-bills_total-and-summary"></section>
    <form
      ref="form"
      role="search"
      class="recurring-bills_form"
      @submit="searchSubscriptions"
    >
      <fieldset class="recurring-bills_form_filter">
        <shared-input
          class="recurring-bills_form_filter_search-field-wrapper"
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
        <div class="recurring-bills_form_filter_dropdowns">
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
      <recurring-bills-table
        :data="subscriptionItems"
        :class="{
          'is-loading': isLoading === true,
        }"
      />
      <!-- <subscriptions-table-nav
        :pre-selected-page="formValues.page"
        :number-of-pages="pageNumber"
        :setPage="setCurrentPage"
      /> -->
    </form>
  </section>
</template>

<script lang="ts" setup>
import sortIcon from "../assets/images/sort.svg";
import { InputEnumType, type IDropdown } from "~/interfaces/shared.interface";
import type {
  ISubscriptionItem,
  ISubscriptionSearchForm,
} from "~/interfaces/subscriptions.interface";
import type { FormFieldTypes } from "~/interfaces/transactions.interface";
import { sortOptions } from "~/services/base.service";
import { getSubscriptions } from "~/services/subscription.service";

const router = useRouter();
const route = useRoute();
const {
  search,
  sortBy,
  page,
}: { search?: string; sortBy?: string; page?: string } = route.query;
const pageInteger = parseInt(page || "1");

const errorStore = useErrorStore();
const isLoading = ref<boolean>(true);
const subscriptionItems = ref<ISubscriptionItem[]>([]);
const pageNumber = ref<number>(1);
const formValues = reactive<ISubscriptionSearchForm>({
  searchString: search,
  sortBy: sortOptions.find((option) => option === sortBy) ?? sortOptions[0],
  page: isNaN(pageInteger) || pageInteger <= 0 ? 1 : pageInteger,
});
let searchTimeout: NodeJS.Timeout;

const handleFilter = (field: FormFieldTypes, value?: string) => {
  if (field === "sortBy") {
    formValues.sortBy = value;
  }

  searchSubscriptions();
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
];

const handleSearchString = (event?: Event) => {
  clearTimeout(searchTimeout);
  const value = (event?.currentTarget as HTMLInputElement)?.value || undefined;
  formValues.searchString = value;
  formValues.page = 1;
  searchTimeout = setTimeout(() => {
    searchSubscriptions();
  }, 300);
};

const searchSubscriptions = async (event?: Event) => {
  event?.preventDefault();
  try {
    isLoading.value = true;
    const subscriptionsContent = await getSubscriptions(
      formValues.page,
      formValues.searchString,
      formValues.sortBy
    );

    router.push({
      query: {
        page: formValues.page,
        search: formValues.searchString,
        sortBy: formValues.sortBy,
      },
    });

    subscriptionItems.value = subscriptionsContent.subscriptions;

    pageNumber.value = subscriptionsContent.numberOfPages;
    formValues.page = subscriptionsContent.currentPage;
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
searchSubscriptions();
</script>

<style lang="scss" scoped>
.recurring-bills {
  flex: 1;
  &_form {
    background-color: var(--white);
    padding: 1.5rem 1.25rem;
    border-radius: 0.75rem;
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    &_filter {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1.5rem;
      &_search-field-wrapper {
        position: relative;
        flex: 1;
        max-width: 20rem;

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
    }
  }
}
@media screen and (min-width: 90rem) {
  .recurring-bills {
    display: grid;
    gap: 1.5rem;
    grid-template-columns: repeat(12, 1fr);
    &_form {
      grid-column: 5 / -1;
    }
  }
}
</style>
