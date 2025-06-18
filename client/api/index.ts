/** Generate by swagger-axios-codegen */
// @ts-nocheck
/* eslint-disable */

/** Generate by swagger-axios-codegen */
/* eslint-disable */
// @ts-nocheck
import axiosStatic, { type AxiosInstance, type AxiosRequestConfig } from 'axios';

export interface IRequestOptions extends AxiosRequestConfig {
  /**
   * show loading status
   */
  loading?: boolean;
  /**
   * display error message
   */
  showError?: boolean;
  /**
   * indicates whether Authorization credentials are required for the request
   * @default true
   */
  withAuthorization?: boolean;
}

export interface IRequestConfig {
  method?: any;
  headers?: any;
  url?: any;
  data?: any;
  params?: any;
}

// Add options interface
export interface ServiceOptions {
  axios?: AxiosInstance;
  /** only in axios interceptor config*/
  loading: boolean;
  showError: boolean;
}

// Add default options
export const serviceOptions: ServiceOptions = {};

// Instance selector
export function axios(configs: IRequestConfig, resolve: (p: any) => void, reject: (p: any) => void): Promise<any> {
  if (serviceOptions.axios) {
    return serviceOptions.axios
      .request(configs)
      .then((res) => {
        resolve(res.data);
      })
      .catch((err) => {
        reject(err);
      });
  } else {
    throw new Error('please inject yourself instance like axios  ');
  }
}

export function getConfigs(method: string, contentType: string, url: string, options: any): IRequestConfig {
  const configs: IRequestConfig = {
    loading: serviceOptions.loading,
    showError: serviceOptions.showError,
    ...options,
    method,
    url
  };
  configs.headers = {
    ...options.headers,
    'Content-Type': contentType
  };
  return configs;
}

export const basePath = '/api';

export interface IList<T> extends Array<T> {}
export interface List<T> extends Array<T> {}
export interface IDictionary<TValue> {
  [key: string]: TValue;
}
export interface Dictionary<TValue> extends IDictionary<TValue> {}

export interface IListResult<T> {
  items?: T[];
}

export class ListResultDto<T> implements IListResult<T> {
  items?: T[];
}

export interface IPagedResult<T> extends IListResult<T> {
  totalCount?: number;
  items?: T[];
}

export class PagedResultDto<T = any> implements IPagedResult<T> {
  totalCount?: number;
  items?: T[];
}

// customer definition
// empty

export class OverviewService {
  /**
   *
   */
  static getOverview(options: IRequestOptions = {}): Promise<OverviewContent> {
    return new Promise((resolve, reject) => {
      let url = basePath + '/overview';

      const configs: IRequestConfig = getConfigs('get', 'application/json', url, options);

      axios(configs, resolve, reject);
    });
  }
}

export class PotsService {
  /**
   *
   */
  static getPots(options: IRequestOptions = {}): Promise<Pots> {
    return new Promise((resolve, reject) => {
      let url = basePath + '/pots';

      const configs: IRequestConfig = getConfigs('get', 'application/json', url, options);

      axios(configs, resolve, reject);
    });
  }
}

export class TransactionsService {
  /**
   *
   */
  static getTransactions(
    params: {
      /**  */
      page?: number;
      /**  */
      search?: string;
      /**  */
      category?: string;
      /**  */
      sortBy?: string;
    } = {} as any,
    options: IRequestOptions = {}
  ): Promise<TransactionsContent> {
    return new Promise((resolve, reject) => {
      let url = basePath + '/transactions';

      const configs: IRequestConfig = getConfigs('get', 'application/json', url, options);
      configs.params = {
        page: params['page'],
        search: params['search'],
        category: params['category'],
        sortBy: params['sortBy']
      };

      axios(configs, resolve, reject);
    });
  }
}

/** OverviewContent */
export interface OverviewContent {
  /**  */
  balance: Balance;

  /**  */
  pots: Pot[];

  /**  */
  budgets: Budget[];

  /**  */
  transactions: Transaction[];

  /**  */
  recurringBillsSummary: RecurringBillsSummary;
}

/** Balance */
export interface Balance {
  /**  */
  current: number;

  /**  */
  income: number;

  /**  */
  expenses: number;
}

/** Pot */
export interface Pot {
  /**  */
  name: string;

  /**  */
  target: number;

  /**  */
  total: number;
}

/** Budget */
export interface Budget {
  /**  */
  maximum: number;

  /** One of: ['Entertainment', 'Bills', 'Dining Out', 'Personal Care', 'General', 'Groceries', 'Transportation', 'Lifestyle', 'Education', 'Shopping'] */
  category: EnumBudgetCategory;
}

/** Transaction */
export interface Transaction {
  /**  */
  avatarUrl: string;

  /**  */
  user: string;

  /** One of: ['Entertainment', 'Bills', 'Dining Out', 'Personal Care', 'General', 'Groceries', 'Transportation', 'Lifestyle', 'Education', 'Shopping'] */
  category: EnumTransactionCategory;

  /**  */
  date: string;

  /**  */
  amount: number;

  /**  */
  recurring: boolean;
}

/** RecurringBillsSummary */
export interface RecurringBillsSummary {
  /**  */
  paidAmount: number;

  /**  */
  totalUpcomingAmount: number;

  /**  */
  dueSoonAmount: number;
}

/** TransactionsContent */
export interface TransactionsContent {
  /**  */
  transactions: Transaction[];

  /**  */
  numberOfPages: number;

  /**  */
  currentPage: number;
}

/** Pots */
export interface Pots {
  /**  */
  pots: Pot[];
}
export enum EnumBudgetCategory {
  'Entertainment' = 'Entertainment',
  'Bills' = 'Bills',
  'Dining Out' = 'Dining Out',
  'Personal Care' = 'Personal Care',
  'General' = 'General',
  'Groceries' = 'Groceries',
  'Transportation' = 'Transportation',
  'Lifestyle' = 'Lifestyle',
  'Education' = 'Education',
  'Shopping' = 'Shopping'
}
export enum EnumTransactionCategory {
  'Entertainment' = 'Entertainment',
  'Bills' = 'Bills',
  'Dining Out' = 'Dining Out',
  'Personal Care' = 'Personal Care',
  'General' = 'General',
  'Groceries' = 'Groceries',
  'Transportation' = 'Transportation',
  'Lifestyle' = 'Lifestyle',
  'Education' = 'Education',
  'Shopping' = 'Shopping'
}
