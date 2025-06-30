import type { Budget } from "~/api/data-contracts";

export interface IOverviewBudgetsCard {
  budgetsCardContent?: {
    spentBudget: number;
    totalBudget: number;
    budgetItems: Budget[];
  };
}
