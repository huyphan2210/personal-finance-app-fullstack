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

export interface Balance {
  current: number;
  expenses: number;
  income: number;
}

export interface Budget {
  /**
   * One of: ['Entertainment', 'Bills', 'Dining Out', 'Personal Care', 'General', 'Groceries', 'Transportation', 'Lifestyle', 'Education', 'Shopping']
   * @example "Entertainment"
   */
  category: BudgetCategoryEnum;
  /**
   * One of: ['#7f9161', '#3f82b2', '#93674f', '#82c9d7', '#cab361', '#277c78', '#97a0ac', '#934f6f', '#626070', '#be6c49', '#af81ba', '#826cb0', '#c94736', '#597c7c', '#f2cdac']
   * @example "#7f9161"
   */
  colorTheme: BudgetColorThemeEnum;
  id: string;
  maximum: number;
  representTransactions: Transaction[];
  spent: number;
}

export interface BudgetContent {
  representBudgets: Budget[];
  totalMaximum: number;
  totalSpent: number;
}

export interface CreateBudget {
  /**
   * Budget category
   * @example "Entertainment"
   */
  category: CreateBudgetCategoryEnum;
  /**
   * Budget color theme
   * @example "#7f9161"
   */
  colorTheme: CreateBudgetColorThemeEnum;
  /** Maximum allowed budget */
  maximum: number;
}

export interface DeleteBudget {
  /** Budget ID (UUID) */
  id: string;
}

export interface OverviewContent {
  balance: Balance;
  budgets: BudgetContent;
  pots: PotOverview;
  recurringBillsSummary: RecurringBillsSummary;
  transactions: Transaction[];
}

export interface Pot {
  /**
   * One of: ['#7f9161', '#3f82b2', '#93674f', '#82c9d7', '#cab361', '#277c78', '#97a0ac', '#934f6f', '#626070', '#be6c49', '#af81ba', '#826cb0', '#c94736', '#597c7c', '#f2cdac']
   * @example "#7f9161"
   */
  colorTheme: PotColorThemeEnum;
  id: string;
  name: string;
  target: number;
  total: number;
}

export interface PotOverview {
  pots: Pot[];
  totalSaved: number;
}

export interface Pots {
  pots: Pot[];
}

export interface RecurringBillsSummary {
  dueSoonAmount: number;
  paidAmount: number;
  totalUpcomingAmount: number;
}

export interface Transaction {
  amount: number;
  avatarUrl: string;
  /**
   * One of: ['Entertainment', 'Bills', 'Dining Out', 'Personal Care', 'General', 'Groceries', 'Transportation', 'Lifestyle', 'Education', 'Shopping']
   * @example "Entertainment"
   */
  category: TransactionCategoryEnum;
  date: string;
  recurring: boolean;
  user: string;
}

export interface TransactionsContent {
  currentPage: number;
  numberOfPages: number;
  transactions: Transaction[];
}

export interface UpdateBudget {
  /**
   * Budget category
   * @example "Entertainment"
   */
  category: UpdateBudgetCategoryEnum;
  /**
   * Budget color theme
   * @example "#7f9161"
   */
  colorTheme: UpdateBudgetColorThemeEnum;
  /** Budget ID (UUID) */
  id: string;
  /** Maximum allowed budget */
  maximum: number;
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
 * One of: ['#7f9161', '#3f82b2', '#93674f', '#82c9d7', '#cab361', '#277c78', '#97a0ac', '#934f6f', '#626070', '#be6c49', '#af81ba', '#826cb0', '#c94736', '#597c7c', '#f2cdac']
 * @example "#7f9161"
 */
export enum BudgetColorThemeEnum {
  Army = "#7f9161",
  Blue = "#3f82b2",
  Brown = "#93674f",
  Cyan = "#82c9d7",
  Gold = "#cab361",
  Green = "#277c78",
  Grey = "#97a0ac",
  Magenta = "#934f6f",
  Navy = "#626070",
  Orange = "#be6c49",
  Pink = "#af81ba",
  Purple = "#826cb0",
  Red = "#c94736",
  Turquois = "#597c7c",
  Yellow = "#f2cdac",
}

/**
 * Budget category
 * @example "Entertainment"
 */
export enum CreateBudgetCategoryEnum {
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
 * Budget color theme
 * @example "#7f9161"
 */
export enum CreateBudgetColorThemeEnum {
  Army = "#7f9161",
  Blue = "#3f82b2",
  Brown = "#93674f",
  Cyan = "#82c9d7",
  Gold = "#cab361",
  Green = "#277c78",
  Grey = "#97a0ac",
  Magenta = "#934f6f",
  Navy = "#626070",
  Orange = "#be6c49",
  Pink = "#af81ba",
  Purple = "#826cb0",
  Red = "#c94736",
  Turquois = "#597c7c",
  Yellow = "#f2cdac",
}

/**
 * One of: ['#7f9161', '#3f82b2', '#93674f', '#82c9d7', '#cab361', '#277c78', '#97a0ac', '#934f6f', '#626070', '#be6c49', '#af81ba', '#826cb0', '#c94736', '#597c7c', '#f2cdac']
 * @example "#7f9161"
 */
export enum PotColorThemeEnum {
  Army = "#7f9161",
  Blue = "#3f82b2",
  Brown = "#93674f",
  Cyan = "#82c9d7",
  Gold = "#cab361",
  Green = "#277c78",
  Grey = "#97a0ac",
  Magenta = "#934f6f",
  Navy = "#626070",
  Orange = "#be6c49",
  Pink = "#af81ba",
  Purple = "#826cb0",
  Red = "#c94736",
  Turquois = "#597c7c",
  Yellow = "#f2cdac",
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

/**
 * Budget category
 * @example "Entertainment"
 */
export enum UpdateBudgetCategoryEnum {
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
 * Budget color theme
 * @example "#7f9161"
 */
export enum UpdateBudgetColorThemeEnum {
  Army = "#7f9161",
  Blue = "#3f82b2",
  Brown = "#93674f",
  Cyan = "#82c9d7",
  Gold = "#cab361",
  Green = "#277c78",
  Grey = "#97a0ac",
  Magenta = "#934f6f",
  Navy = "#626070",
  Orange = "#be6c49",
  Pink = "#af81ba",
  Purple = "#826cb0",
  Red = "#c94736",
  Turquois = "#597c7c",
  Yellow = "#f2cdac",
}
