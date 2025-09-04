import { type SubscriptionsContent } from "~/api/data-contracts";
import { handleGetResponse, subscriptionsApi } from "./base.service";

export const getSubscriptions = async (
  page: number,
  searchString?: string,
  sortBy?: string
) => {
  const subscriptionsContent = await handleGetResponse<SubscriptionsContent>(
    () =>
      subscriptionsApi.getSubscriptionsApi({
        page,
        search: searchString,
        sortBy,
      })
  );

  return subscriptionsContent;
};
