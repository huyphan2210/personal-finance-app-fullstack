import { defineStore } from "pinia";

export enum Page {
  Home = "/",
  Transactions = "/transactions",
  Budgets = "/budgets",
  Pots = "/pots",
  RecurringBills = "/recurring-bills",
  Login = "/login",
  Signup = "/sign-up",
}

interface PageStoreState {
  currentPage: Page;
  currentPageHeading: string;
}

export const pageHeadings: Record<Page, string> = {
  [Page.Home]: "Overview",
  [Page.Transactions]: "Transactions",
  [Page.Budgets]: "Budgets",
  [Page.Pots]: "Pots",
  [Page.RecurringBills]: "Recurring Bills",
  [Page.Login]: "Login",
  [Page.Signup]: " Sign Up",
};

export const usePageStore = defineStore("page", {
  state: (): PageStoreState => ({
    currentPage: Page.Home,
    currentPageHeading: "Overview",
  }),
  actions: {
    setCurrentPage(page: Page) {
      this.currentPage = page;
      this.currentPageHeading = pageHeadings[page];
    },
  },
});
