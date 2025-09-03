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

import type { Subscription } from "./data-contracts";
import { HttpClient, type RequestParams } from "./http-client";

export class SubscriptionsApi<
  SecurityDataType = unknown,
> extends HttpClient<SecurityDataType> {
  /**
   * @description Get the transactions data
   *
   * @tags subscriptions-api
   * @name GetSubscriptionsApi
   * @request GET:/subscriptions-api
   */
  getSubscriptionsApi = (
    query?: {
      /** @default 1 */
      page?: number;
      /** @default "" */
      search?: string;
      /** @default "" */
      sortBy?: string;
    },
    params: RequestParams = {},
  ) =>
    this.request<Subscription, any>({
      path: `/subscriptions-api`,
      method: "GET",
      query: query,
      format: "json",
      ...params,
    });
}
