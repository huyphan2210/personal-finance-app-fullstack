import { defineStore } from "pinia";

export enum Page {
  Overview = "/overview",
  Transactions = "/transactions",
  Budgets = "/budgets",
  Pots = "/pots",
  RecurringBills = "/recurring-bills",
  Login = "/login",
  Signup = "/sign-up",
}

export const pageHeadings: Record<Page, string> = {
  [Page.Overview]: "Overview",
  [Page.Transactions]: "Transactions",
  [Page.Budgets]: "Budgets",
  [Page.Pots]: "Pots",
  [Page.RecurringBills]: "Recurring Bills",
  [Page.Login]: "Login",
  [Page.Signup]: " Sign Up",
};

interface PageStoreState {
  currentPage: Page;
  currentPageHeading: string;
}

export const usePageStore = defineStore("page", {
  state: (): PageStoreState => ({
    currentPage: Page.Overview,
    currentPageHeading: "Overview",
  }),
  actions: {
    setCurrentPage(page: Page) {
      this.currentPage = page;
      this.currentPageHeading = pageHeadings[page];
    },
  },
});
