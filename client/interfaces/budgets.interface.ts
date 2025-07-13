import type { Budget, BudgetContent } from "~/api/data-contracts";

export interface IBudget extends Budget {
  maximumWithCurrency: string;
  spentWithCurrency: string;
}

export interface IBudgetContent extends BudgetContent {
  representBudgets: IBudget[]
}