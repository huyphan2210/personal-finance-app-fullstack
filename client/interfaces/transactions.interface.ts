import type { EnumTransactionCategory } from "~/api";

export interface ITransactionItem {
  category: EnumTransactionCategory;
  transactionDate: string;
  amount: number;
  name: string;
  avatarUrl: string;
}

export interface ITransactionSearchForm {
  searchString?: string;
  sortBy?: string;
  category?: string;
  page: 1;
}

export interface ITransactionsTable {
  data: ITransactionItem[];
}

export interface ITransactionsNavigation {
  numberOfPages: number;
}
