import type {
  Budget,
  BudgetCategoryEnum,
  BudgetContent,
} from "~/api/data-contracts";
import type {
  IContentCard,
  IContentCardDropdownOption,
} from "./shared.interface";
import type { Category } from "~/types/category";

export interface IBudget extends Budget {
  maximumWithCurrency: string;
  spentWithCurrency: string;
}

export interface IBudgetContent extends BudgetContent {
  representBudgets: IBudget[];
}

export interface IBudgetContentCard {
  budgetInfo: IBudget;
  dropdownOptions: IContentCardDropdownOption[];
}

export enum BudgetModalTypeEnum {
  AddNew = 1,
  Edit = 2,
  Delete = 3,
}

export interface IBudgetModal {
  isShown: boolean;
  type: BudgetModalTypeEnum;
  budgetCategory?: BudgetCategoryEnum;
}
