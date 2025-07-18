import type {
  Budget,
  BudgetCategoryEnum,
  BudgetContent,
} from "~/api/data-contracts";
import type { IContentCard, IDropdownOption } from "./shared.interface";

export interface IBudget extends Budget {
  maximumWithCurrency: string;
  spentWithCurrency: string;
}

export interface IBudgetContent extends BudgetContent {
  representBudgets: IBudget[];
}

export interface IBudgetContentCard {
  budgetInfo: IBudget;
  dropdownOptions: IDropdownOption[];
}

export interface IBudgetModal {
  isShown: boolean;
}

export interface IBudgetAddNewModal extends IBudgetModal {}
