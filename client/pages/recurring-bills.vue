<template>
  <shared-page-heading />
  <section class="recurring-bills_total-and-summary"></section>
</template>

<script lang="ts" setup>
import type { Subscription } from "~/api/data-contracts";
import type {
  ISubscriptionItem,
  ISubscriptionSearchForm,
} from "~/interfaces/subscriptions.interface";
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

<style lang="scss" scoped></style>
