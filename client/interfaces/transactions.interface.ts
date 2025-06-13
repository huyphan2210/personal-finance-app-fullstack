import type { EnumTransactionCategory } from "~/api";

export type FormFieldTypes = 'sortBy' | 'category';
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
  page: number;
}

export interface ITransactionsTable {
  data: ITransactionItem[];
}

export interface ITransactionsNavigation {
  preSelectedPage?: number;
  numberOfPages: number;
  setPage: (page: number) => void
}
