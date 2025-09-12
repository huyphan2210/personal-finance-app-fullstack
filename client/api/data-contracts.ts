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

export interface CreatePot {
  /**
   * Pot color theme
   * @example "#7f9161"
   */
  colorTheme: CreatePotColorThemeEnum;
  /**
   * Name of the pot
   * @minLength 1
   * @maxLength 30
   */
  name: string;
  /** Maximum target of the pot */
  target: number;
  /** Total of the pot */
  total?: number;
}

export interface DeleteBudget {
  /** Budget ID (UUID) */
  id: string;
}

export interface DeletePot {
  /** Pot ID (UUID) */
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
  numOfDueSoonSubscriptions: number;
  numOfPaidSubscriptions: number;
  numOfUnpaidSubscriptions: number;
  numOfUpcomingSubscriptions: number;
  paidAmount: number;
  totalUpcomingAmount: number;
  unpaidAmount: number;
}

export interface Subscription {
  amount: number;
  avatarUrl: string;
  dueDate: string;
  /**
   * One of: ['DueSoon', 'Paid', 'Unpaid', 'Upcoming']
   * @example "DueSoon"
   */
  paidStatus: SubscriptionPaidStatusEnum;
  /**
   * One of: ['Monthly', 'Yearly']
   * @example "Monthly"
   */
  recurrence: SubscriptionRecurrenceEnum;
  /**
   * One of: ['Active', 'Inactive']
   * @example "Active"
   */
  status: SubscriptionStatusEnum;
  user: string;
}

export interface SubscriptionsContent {
  currentPage: number;
  monthlySummary: RecurringBillsSummary;
  numberOfPages: number;
  subscriptions: Subscription[];
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
  subscriptionId?: string;
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

export interface UpdatePot {
  /**
   * Pot color theme
   * @example "#7f9161"
   */
  colorTheme?: UpdatePotColorThemeEnum;
  /** Pot ID (UUID) */
  id: string;
  /**
   * Name of the pot
   * @minLength 1
   * @maxLength 30
   */
  name?: string;
  /** Maximum target of the pot */
  target?: number;
  /** Total of the pot */
  total?: number;
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
 * Pot color theme
 * @example "#7f9161"
 */
export enum CreatePotColorThemeEnum {
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
 * One of: ['DueSoon', 'Paid', 'Unpaid', 'Upcoming']
 * @example "DueSoon"
 */
export enum SubscriptionPaidStatusEnum {
  DueSoon = "DueSoon",
  Paid = "Paid",
  Unpaid = "Unpaid",
  Upcoming = "Upcoming",
}

/**
 * One of: ['Monthly', 'Yearly']
 * @example "Monthly"
 */
export enum SubscriptionRecurrenceEnum {
  Monthly = "Monthly",
  Yearly = "Yearly",
}

/**
 * One of: ['Active', 'Inactive']
 * @example "Active"
 */
export enum SubscriptionStatusEnum {
  Active = "Active",
  Inactive = "Inactive",
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

/**
 * Pot color theme
 * @example "#7f9161"
 */
export enum UpdatePotColorThemeEnum {
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
