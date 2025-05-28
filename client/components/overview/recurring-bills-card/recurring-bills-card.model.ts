import type { RecurringBillsSummary } from "~/api";

export interface IOverviewRecurringBillsCard {
  recurringBillsCardContent?: RecurringBillsSummary;
}

export interface IRecurringBillSummaryItem {
  label: string;
  amount?: number;
}
