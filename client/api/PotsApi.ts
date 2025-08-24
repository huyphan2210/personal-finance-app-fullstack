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

import type { CreatePot, DeletePot, Pots, UpdatePot } from "./data-contracts";
import { ContentType, HttpClient, type RequestParams } from "./http-client";

export class PotsApi<
  SecurityDataType = unknown,
> extends HttpClient<SecurityDataType> {
  /**
   * @description Delete pot
   *
   * @tags pots-api
   * @name DeletePotsApi
   * @request DELETE:/pots-api
   */
  deletePotsApi = (payload: DeletePot, params: RequestParams = {}) =>
    this.request<void, void>({
      path: `/pots-api`,
      method: "DELETE",
      body: payload,
      type: ContentType.Json,
      ...params,
    });
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
  /**
   * @description Update pot
   *
   * @tags pots-api
   * @name PatchPotsApi
   * @request PATCH:/pots-api
   */
  patchPotsApi = (payload: UpdatePot, params: RequestParams = {}) =>
    this.request<void, void>({
      path: `/pots-api`,
      method: "PATCH",
      body: payload,
      type: ContentType.Json,
      ...params,
    });
  /**
   * @description Create new pot
   *
   * @tags pots-api
   * @name PostPotsApi
   * @request POST:/pots-api
   */
  postPotsApi = (payload: CreatePot, params: RequestParams = {}) =>
    this.request<void, void>({
      path: `/pots-api`,
      method: "POST",
      body: payload,
      type: ContentType.Json,
      ...params,
    });
}
