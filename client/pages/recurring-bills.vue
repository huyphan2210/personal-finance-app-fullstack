<template>
  <shared-page-heading />
  <section class="recurring-bills">
    <section class="recurring-bills_summary">
      <div class="recurring-bills_summary_total">
        <img src="../assets/images/bills.svg" loading="lazy" alt="Bills" />
        <div class="recurring-bills_summary_total_number">
          <div class="recurring-bills_summary_total_number_monthly">
            <h2>Total monthly bills</h2>
            <span>
              {{ enUSFormatter.format(subscriptionContent?.totalMonthly || 0) }}
            </span>
          </div>
          <div class="recurring-bills_summary_total_number_yearly">
            <h2>Total yearly bills</h2>
            <span>
              {{ enUSFormatter.format(subscriptionContent?.totalYearly || 0) }}
            </span>
          </div>
        </div>
      </div>
      <div class="recurring-bills_summary_monthly">
        <h2>Monthly summary</h2>
        <ul class="recurring-bills_summary_monthly_list">
          <li
            v-for="item in monthlySummaryItems"
            :key="item.content"
            :class="[
              'recurring-bills_summary_monthly_list_item',
              item.className,
            ]"
          >
            <span>{{ item.label }}</span>
            <span>
              {{ item.content }}
            </span>
          </li>
        </ul>
      </div>
    </section>
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
        :data="subscriptionContent?.subscriptions || []"
        :class="{
          'is-loading': isLoading === true,
        }"
      />
    </form>
  </section>
</template>

<script lang="ts" setup>
import type { SubscriptionsContent } from "~/api/data-contracts";
import sortIcon from "../assets/images/sort.svg";
import { InputEnumType, type IDropdown } from "~/interfaces/shared.interface";
import type {
  ISubscriptionMonthlySummary,
  ISubscriptionSearchForm,
} from "~/interfaces/subscriptions.interface";
import type { FormFieldTypes } from "~/interfaces/transactions.interface";
import { enUSFormatter, sortOptions } from "~/services/base.service";
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
const subscriptionContent = ref<SubscriptionsContent>();
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

const monthlySummaryItems = ref<ISubscriptionMonthlySummary[]>([]);

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

    subscriptionContent.value = subscriptionsContent;
    monthlySummaryItems.value = [
      {
        label: "Paid Bills",
        content: `${
          subscriptionContent.value.monthlySummary.numOfPaidSubscriptions
        }(${enUSFormatter.format(
          subscriptionContent.value?.monthlySummary.paidAmount || 0
        )})`,
        className: "paid",
      },
      {
        label: "Unpaid Bills",
        content: `${
          subscriptionContent.value.monthlySummary.numOfUnpaidSubscriptions
        }(${enUSFormatter.format(
          subscriptionContent.value?.monthlySummary.unpaidAmount || 0
        )})`,
        className: "unpaid",
      },
      {
        label: "Total Upcoming",
        content: `${
          subscriptionContent.value.monthlySummary.numOfUpcomingSubscriptions
        }(${enUSFormatter.format(
          subscriptionContent.value?.monthlySummary.totalUpcomingAmount || 0
        )})`,
        className: "upcoming",
      },
      {
        label: "Due Soon",
        content: `${
          subscriptionContent.value.monthlySummary.numOfDueSoonSubscriptions
        }(${enUSFormatter.format(
          subscriptionContent.value?.monthlySummary.dueSoonAmount || 0
        )})`,
        className: "due-soon",
      },
    ];
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
  display: flex;
  flex-direction: column;
  gap: 1.5rem;

  &_summary {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    &_total {
      display: flex;
      gap: 1.5rem;
      background-color: var(--grey-900);
      color: var(--white);
      border-radius: 0.5rem;
      padding: 1.5rem 1.25rem;
      &_number {
        display: flex;
        flex-direction: column;
        gap: 1.5rem;
        &_monthly,
        &_yearly {
          margin-top: max(auto, 1.5rem);
          h2 {
            @include text-preset-4;
            margin-bottom: 11px;
          }
          span {
            @include text-preset-1;
          }
        }
      }
    }

    &_monthly {
      background-color: var(--white);
      border-radius: 0.75rem;
      padding: 1.25rem;
      h2 {
        @include text-preset-3;
        color: var(--grey-900);
      }
      &_list {
        list-style-type: none;
        display: flex;
        flex-direction: column;
        gap: 1rem;
        margin-top: 1.25rem;
        &_item {
          display: flex;
          justify-content: space-between;
          align-items: center;
          color: var(--grey-500);
          padding-bottom: 1rem;
          border-bottom: solid 1px
            color-mix(in srgb, var(--grey-500), transparent 85%);
          &:last-child {
            padding-bottom: 0;
            border-bottom: 0;
          }

          span {
            @include text-preset-5;
            &:last-child {
              @include text-preset-5-bold;
              color: var(--grey-900);
            }
          }

          &.paid {
            color: var(--green);
            span {
              color: inherit;
            }
          }

          &.unpaid {
            color: var(--red);
            span {
              color: inherit;
            }
          }

          &.due-soon {
            color: var(--gold);
            span {
              color: inherit;
            }
          }
        }
      }
    }
  }

  &_form {
    flex: 1;
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

@media screen and (min-width: 48rem) {
  .recurring-bills {
    &_summary {
      flex-direction: unset;
      &_total {
        padding: 1.5rem;
        flex: 1;
        flex-direction: column;
        align-items: self-start;
        gap: 2rem;
      }
      &_monthly {
        flex: 1;
      }
    }

    &_form {
      padding: 2rem;
    }
  }
}

@media screen and (min-width: 90rem) {
  .recurring-bills {
    display: grid;
    gap: 1.5rem;
    grid-template-columns: repeat(12, 1fr);
    &_summary {
      grid-column: 1 / 5;
      flex-direction: column;
      height: min-content;
    }

    &_form {
      grid-column: 5 / -1;
    }
  }
}
</style>
