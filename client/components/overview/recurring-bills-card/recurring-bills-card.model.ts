import { type RecurringBillsSummary } from "~/api/data-contracts";

export interface IOverviewRecurringBillsCard {
  recurringBillsCardContent?: RecurringBillsSummary;
}

export interface IRecurringBillSummaryItem {
  label: string;
  amount?: number;
}
