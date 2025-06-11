import { TransactionsService, type TransactionsContent } from "~/api";

export const getTransactions = async (
  page: number,
  searchString?: string,
  category?: string,
  sortBy?: string
): Promise<TransactionsContent> => {
  const transactionsContent = await TransactionsService.getTransactions({
    page: page,
    search: searchString,
    category,
    sortBy,
  });

  return transactionsContent;
};
