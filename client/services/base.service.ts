import { type HttpResponse, type RequestParams } from "~/api/http-client";
import { OverviewApi } from "~/api/OverviewApi";
import { TransactionsApi } from "~/api/TransactionsApi";
import { PotsApi } from "~/api/PotsApi";
import { BudgetsApi } from "~/api/BudgetsApi";

const config = useRuntimeConfig();

export const overviewApi = new OverviewApi({
  baseUrl: config.public.apiBase,
});

export const budgetApi = new BudgetsApi({
  baseUrl: config.public.apiBase,
});

export const transactionsApi = new TransactionsApi({
  baseUrl: config.public.apiBase,
});

export const potsApi = new PotsApi({
  baseUrl: config.public.apiBase,
});

export const handleGetResponse = async <T = any>(
  responsePromise: (params?: RequestParams) => Promise<HttpResponse<T, any>>
): Promise<T> => {
  try {
    const response = await responsePromise();
    const json = await response.json();
    return json;
  } catch (error) {
    const message =
      error instanceof Response ? await error.text() : DEFAULT_ERROR_MESSAGE;
    throw new Error(message);
  }
};

export const enUSFormatter = new Intl.NumberFormat("en-US", {
  style: "currency",
  currency: "USD",
});
