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

import type {
  BudgetContent,
  CreateBudget,
  DeleteBudget,
  UpdateBudget,
} from "./data-contracts";
import { ContentType, HttpClient, type RequestParams } from "./http-client";

export class BudgetsApi<
  SecurityDataType = unknown,
> extends HttpClient<SecurityDataType> {
  /**
   * @description Delete budget
   *
   * @tags budgets-api
   * @name DeleteBudgetsApi
   * @request DELETE:/budgets-api
   */
  deleteBudgetsApi = (payload: DeleteBudget, params: RequestParams = {}) =>
    this.request<void, void>({
      path: `/budgets-api`,
      method: "DELETE",
      body: payload,
      type: ContentType.Json,
      ...params,
    });
  /**
   * @description Get the budgets data
   *
   * @tags budgets-api
   * @name GetBudgetsApi
   * @request GET:/budgets-api
   */
  getBudgetsApi = (params: RequestParams = {}) =>
    this.request<BudgetContent, void>({
      path: `/budgets-api`,
      method: "GET",
      format: "json",
      ...params,
    });
  /**
   * @description Edit budget
   *
   * @tags budgets-api
   * @name PatchBudgetsApi
   * @request PATCH:/budgets-api
   */
  patchBudgetsApi = (payload: UpdateBudget, params: RequestParams = {}) =>
    this.request<void, void>({
      path: `/budgets-api`,
      method: "PATCH",
      body: payload,
      type: ContentType.Json,
      ...params,
    });
  /**
   * @description Create new budget
   *
   * @tags budgets-api
   * @name PostBudgetsApi
   * @request POST:/budgets-api
   */
  postBudgetsApi = (payload: CreateBudget, params: RequestParams = {}) =>
    this.request<void, void>({
      path: `/budgets-api`,
      method: "POST",
      body: payload,
      type: ContentType.Json,
      ...params,
    });
}
