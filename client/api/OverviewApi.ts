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

import { OverviewContent } from "./data-contracts";
import { HttpClient, RequestParams } from "./http-client";

export class OverviewApi<
  SecurityDataType = unknown
> extends HttpClient<SecurityDataType> {
  /**
   * @description Get the overview data
   *
   * @tags overview-api
   * @name GetOverviewApi
   * @request GET:/overview-api
   */
  getOverviewApi = (params: RequestParams = {}) =>
    this.request<OverviewContent, any>({
      path: `/overview-api`,
      method: "GET",
      format: "json",
      ...params,
    });
}
