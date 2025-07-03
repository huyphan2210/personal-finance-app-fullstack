import { type BudgetContent } from "~/api/data-contracts";
import { budgetApi, handleResponse } from "./base.service";

export const getBudgets = async () => {
  const budgets = await handleResponse<BudgetContent>(budgetApi.getBudgetsApi);
  return budgets;
};
