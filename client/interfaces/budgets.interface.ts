import type {
  Budget,
  BudgetCategoryEnum,
  BudgetContent,
} from "~/api/data-contracts";
import type { IContentCardDropdownOption } from "./shared.interface";

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
  onEditModal: (budget: IBudget) => void;
}

export enum BudgetModalTypeEnum {
  AddNew = 1,
  Edit = 2,
  Delete = 3,
}

export interface IBudgetModal {
  isShown: boolean;
  type: BudgetModalTypeEnum;
  targetBudgetCategory?: BudgetCategoryEnum;
  usedBudgets: IBudget[];
}

export interface IBudgetEditModal extends IBudgetModal {
  editBudgetInfo?: IBudget;
}
