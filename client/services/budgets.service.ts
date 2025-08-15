import {
  BudgetCategoryEnum,
  type BudgetContent,
  type CreateBudget,
} from "~/api/data-contracts";
import { budgetApi, enUSFormatter, handleGetResponse } from "./base.service";
import {
  BudgetModalTypeEnum,
  type IBudget,
  type IBudgetContent,
} from "~/interfaces/budgets.interface";

export const getBudgets = async () => {
  const response = await handleGetResponse<BudgetContent>(
    budgetApi.getBudgetsApi
  );
  const budgets: IBudget[] = response.representBudgets.map(
    (budget) =>
      ({
        ...budget,
        maximumWithCurrency: enUSFormatter.format(budget.maximum),
        spentWithCurrency: enUSFormatter.format(budget.spent),
      } as IBudget)
  );
  const budgetContent: IBudgetContent = {
    ...response,
    representBudgets: budgets,
  };
  return budgetContent;
};

export const createBudget = async (payload: CreateBudget) => {
  try {
    await budgetApi.postBudgetsApi(payload);
  } catch (error) {
    const message =
      error instanceof Response
        ? await error.text()
        : "Something wrong happened";
    throw new Error(message);
  }
};

export const budgetModalHeadings: Record<
  BudgetModalTypeEnum,
  (category?: BudgetCategoryEnum) => string
> = {
  [BudgetModalTypeEnum.AddNew]: () => "Add New Budget",
  [BudgetModalTypeEnum.Edit]: () => "Edit Budget",
  [BudgetModalTypeEnum.Delete]: (category) => `Delete '${category}'?`,
};

export const budgetModalInstruction: Record<BudgetModalTypeEnum, string> = {
  [BudgetModalTypeEnum.AddNew]:
    "Choose a category to set a spending budget. These categories can help you monitor spending.",
  [BudgetModalTypeEnum.Edit]:
    "As your budgets change, feel free to update your spending limits.",
  [BudgetModalTypeEnum.Delete]:
    "Are you sure you want to delete this budget? This action cannot be reversed, and all the data inside it will be removed forever.",
};

export const budgetModalPrimaryButtonContent: Record<
  BudgetModalTypeEnum,
  string
> = {
  [BudgetModalTypeEnum.AddNew]: "Add Budget",
  [BudgetModalTypeEnum.Edit]: "Save Changes",
  [BudgetModalTypeEnum.Delete]: "Yes, Confirm Deletion",
};
