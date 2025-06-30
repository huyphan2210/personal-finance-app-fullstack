/* eslint-disable */
/* tslint:disable */
// @ts-nocheck
/*
 * ---------------------------------------------------------------
 * ## THIS FILE WAS GENERATED VIA SWAGGER-TYPESCRIPT-API        ##
 * ##                                                           ##
 * ## AUTHOR: acacode                                           ##
 * ## SOURCE: https://github.com/acacode/swagger-typescript-api ##
 * ---------------------------------------------------------------
 */

export interface OverviewContent {
  balance: Balance;
  pots: Pot[];
  budgets: BudgetOverviewContent;
  transactions: Transaction[];
  recurringBillsSummary: RecurringBillsSummary;
}

export interface Balance {
  current: number;
  income: number;
  expenses: number;
}

export interface Pot {
  name: string;
  target: number;
  total: number;
  /**
   * One of: ['#82c9d7', '#277c78', '#626070', '#f2cdac', '#826CB0']
   * @example "#82c9d7"
   */
  colorTheme: PotColorThemeEnum;
}

export interface BudgetOverviewContent {
  totalSpent: number;
  totalMaximum: number;
  representBudgets: Budget[];
}

export interface Budget {
  maximum: number;
  /**
   * One of: ['Entertainment', 'Bills', 'Dining Out', 'Personal Care', 'General', 'Groceries', 'Transportation', 'Lifestyle', 'Education', 'Shopping']
   * @example "Entertainment"
   */
  category: BudgetCategoryEnum;
  /**
   * One of: ['#82c9d7', '#277c78', '#626070', '#f2cdac', '#826CB0']
   * @example "#82c9d7"
   */
  colorTheme: BudgetColorThemeEnum;
}

export interface Transaction {
  avatarUrl: string;
  user: string;
  /**
   * One of: ['Entertainment', 'Bills', 'Dining Out', 'Personal Care', 'General', 'Groceries', 'Transportation', 'Lifestyle', 'Education', 'Shopping']
   * @example "Entertainment"
   */
  category: TransactionCategoryEnum;
  date: string;
  amount: number;
  recurring: boolean;
}

export interface RecurringBillsSummary {
  paidAmount: number;
  totalUpcomingAmount: number;
  dueSoonAmount: number;
}

export interface TransactionsContent {
  transactions: Transaction[];
  numberOfPages: number;
  currentPage: number;
}

export interface Pots {
  pots: Pot[];
}

/**
 * One of: ['#82c9d7', '#277c78', '#626070', '#f2cdac', '#826CB0']
 * @example "#82c9d7"
 */
export enum PotColorThemeEnum {
  Value82C9D7 = "#82c9d7",
  Value277C78 = "#277c78",
  Value626070 = "#626070",
  ValueF2Cdac = "#f2cdac",
  Value826CB0 = "#826CB0",
}

/**
 * One of: ['Entertainment', 'Bills', 'Dining Out', 'Personal Care', 'General', 'Groceries', 'Transportation', 'Lifestyle', 'Education', 'Shopping']
 * @example "Entertainment"
 */
export enum BudgetCategoryEnum {
  Entertainment = "Entertainment",
  Bills = "Bills",
  DiningOut = "Dining Out",
  PersonalCare = "Personal Care",
  General = "General",
  Groceries = "Groceries",
  Transportation = "Transportation",
  Lifestyle = "Lifestyle",
  Education = "Education",
  Shopping = "Shopping",
}

/**
 * One of: ['#82c9d7', '#277c78', '#626070', '#f2cdac', '#826CB0']
 * @example "#82c9d7"
 */
export enum BudgetColorThemeEnum {
  Value82C9D7 = "#82c9d7",
  Value277C78 = "#277c78",
  Value626070 = "#626070",
  ValueF2Cdac = "#f2cdac",
  Value826CB0 = "#826CB0",
}

/**
 * One of: ['Entertainment', 'Bills', 'Dining Out', 'Personal Care', 'General', 'Groceries', 'Transportation', 'Lifestyle', 'Education', 'Shopping']
 * @example "Entertainment"
 */
export enum TransactionCategoryEnum {
  Entertainment = "Entertainment",
  Bills = "Bills",
  DiningOut = "Dining Out",
  PersonalCare = "Personal Care",
  General = "General",
  Groceries = "Groceries",
  Transportation = "Transportation",
  Lifestyle = "Lifestyle",
  Education = "Education",
  Shopping = "Shopping",
}
