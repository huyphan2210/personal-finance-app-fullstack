import type { Budget } from "~/api";

export interface IOverviewBudgetsCard {
  budgetsCardContent?: {
    spentBudget: number;
    totalBudget: number;
    budgetItems: Budget[];
  };
}
