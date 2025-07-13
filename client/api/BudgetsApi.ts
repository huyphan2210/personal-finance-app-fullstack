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

import type { BudgetContent } from "./data-contracts";
import { HttpClient, type RequestParams } from "./http-client";

export class BudgetsApi<
  SecurityDataType = unknown,
> extends HttpClient<SecurityDataType> {
  /**
   * @description Get the budgets data
   *
   * @tags budgets-api
   * @name GetBudgetsApi
   * @request GET:/budgets-api
   */
  getBudgetsApi = (params: RequestParams = {}) =>
    this.request<BudgetContent, any>({
      path: `/budgets-api`,
      method: "GET",
      format: "json",
      ...params,
    });
}
