import type {
  Budget,
  BudgetCategoryEnum,
  BudgetContent,
} from "~/api/data-contracts";
import type { IContentCard } from "./shared.interface";

export interface IBudget extends Budget {
  maximumWithCurrency: string;
  spentWithCurrency: string;
}

export interface IBudgetContent extends BudgetContent {
  representBudgets: IBudget[];
}

export interface IBudgetContentCard extends IContentCard {
  heading: BudgetCategoryEnum;
}
