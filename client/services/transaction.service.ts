import type { TransactionsContent } from "~/api/data-contracts";
import { handleGetResponse, transactionsApi } from "./base.service";

export const getTransactions = async (
  page: number,
  searchString?: string,
  category?: string,
  sortBy?: string
): Promise<TransactionsContent> => {
  const transactionsContent = await handleGetResponse<TransactionsContent>(() =>
    transactionsApi.getTransactionsApi({
      page: page,
      search: searchString,
      category,
      sortBy,
    })
  );

  return transactionsContent;
};
