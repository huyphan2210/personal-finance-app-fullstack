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

import type { Pots } from "./data-contracts";
import { HttpClient, type RequestParams } from "./http-client";

export class PotsApi<
  SecurityDataType = unknown,
> extends HttpClient<SecurityDataType> {
  /**
   * @description Get the pots data
   *
   * @tags pots-api
   * @name GetPotsApi
   * @request GET:/pots-api
   */
  getPotsApi = (params: RequestParams = {}) =>
    this.request<Pots, any>({
      path: `/pots-api`,
      method: "GET",
      format: "json",
      ...params,
    });
}
