import type { Transaction } from "~/api/data-contracts";

export interface IOverviewTransactionsCard {
  transactionsCardContent?: {
    transactions: Transaction[];
  };
}
