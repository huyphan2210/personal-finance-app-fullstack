import type { Transaction } from "~/api";

export interface IOverviewTransactionsCard {
  transactionsCardContent?: {
    transactions: Transaction[];
  };
}
