import { type BudgetContent } from "~/api/data-contracts";
import { budgetApi, enUSFormatter, handleResponse } from "./base.service";
import type { IBudget, IBudgetContent } from "~/interfaces/budgets.interface";

export const getBudgets = async () => {
  const response = await handleResponse<BudgetContent>(budgetApi.getBudgetsApi);
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
