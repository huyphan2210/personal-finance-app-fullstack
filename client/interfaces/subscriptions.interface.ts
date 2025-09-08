import type { Subscription } from "~/api/data-contracts";

export interface ISubscriptionSearchForm {
  searchString?: string;
  sortBy?: string;
  page: number;
}

export interface ISubscriptionItem extends Subscription {}

export interface ISubscriptionTable {
  data: ISubscriptionItem[]
}
