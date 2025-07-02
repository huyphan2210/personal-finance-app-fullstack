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

import type { TransactionsContent } from "./data-contracts";
import { HttpClient, type RequestParams } from "./http-client";

export class TransactionsApi<
  SecurityDataType = unknown,
> extends HttpClient<SecurityDataType> {
  /**
   * @description Get the transactions data
   *
   * @tags transactions-api
   * @name GetTransactionsApi
   * @request GET:/transactions-api
   */
  getTransactionsApi = (
    query?: {
      /** @default 1 */
      page?: number;
      /** @default "" */
      search?: string;
      /** @default "" */
      category?: string;
      /** @default "" */
      sortBy?: string;
    },
    params: RequestParams = {},
  ) =>
    this.request<TransactionsContent, any>({
      path: `/transactions-api`,
      method: "GET",
      query: query,
      format: "json",
      ...params,
    });
}
