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
   * One of: ['#82c9d7', '#277c78', '#626070', '#f2cdac', '#826CB0', '#c94736']
   * @example "#82c9d7"
   */
  colorTheme: BudgetColorThemeEnum;
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
   * @example "#82c9d7"
   */
  colorTheme: CreateBudgetColorThemeEnum;
  /** Maximum allowed budget */
  maximum: number;
}

export interface OverviewContent {
  balance: Balance;
  budgets: BudgetContent;
  pots: Pot[];
  recurringBillsSummary: RecurringBillsSummary;
  transactions: Transaction[];
}

export interface Pot {
  /**
   * One of: ['#82c9d7', '#277c78', '#626070', '#f2cdac', '#826CB0', '#c94736']
   * @example "#82c9d7"
   */
  colorTheme: PotColorThemeEnum;
  name: string;
  target: number;
  total: number;
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
 * One of: ['#82c9d7', '#277c78', '#626070', '#f2cdac', '#826CB0', '#c94736']
 * @example "#82c9d7"
 */
export enum BudgetColorThemeEnum {
  Cyan = "#82c9d7",
  Green = "#277c78",
  Navy = "#626070",
  Yellow = "#f2cdac",
  Purple = "#826CB0",
  Red = "#c94736",
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
 * @example "#82c9d7"
 */
export enum CreateBudgetColorThemeEnum {
  Cyan = "#82c9d7",
  Green = "#277c78",
  Navy = "#626070",
  Yellow = "#f2cdac",
  Purple = "#826CB0",
  Red = "#c94736",
}

/**
 * One of: ['#82c9d7', '#277c78', '#626070', '#f2cdac', '#826CB0', '#c94736']
 * @example "#82c9d7"
 */
export enum PotColorThemeEnum {
  Cyan = "#82c9d7",
  Green = "#277c78",
  Navy = "#626070",
  Yellow = "#f2cdac",
  Purple = "#826CB0",
  Red = "#c94736",
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
