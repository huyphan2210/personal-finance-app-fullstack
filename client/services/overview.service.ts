import type { IOverviewBudgetsCard } from "~/components/overview/budgets-card/budgets-card.model";
import type { IOverviewPotCard } from "~/components/overview/pot-card/pot-card.model";
import type { IOverviewRecurringBillsCard } from "~/components/overview/recurring-bills-card/recurring-bills-card.model";
import type { IOverviewSummaryCard } from "~/components/overview/summary-card/summary-card.model";
import type { IOverviewTransactionsCard } from "~/components/overview/transactions-card/transactions-card.model";
import { type OverviewContent } from "~/api/data-contracts";
import { handleResponse, overviewApi } from "./base.service";

export interface IOverviewPageContent
  extends IOverviewPotCard,
    IOverviewBudgetsCard,
    IOverviewTransactionsCard,
    IOverviewRecurringBillsCard {
  summaryCardsContent: IOverviewSummaryCard[];
}

export const getSummaryContent: () => Promise<IOverviewPageContent> =
  async () => {
    const overviewContent = await handleResponse<OverviewContent>(
      overviewApi.getOverviewApi
    );

    const enUSFormatter = new Intl.NumberFormat("en-US", {
      style: "currency",
      currency: "USD",
    });

    const potsTotalSaved = overviewContent.pots.reduce(
      (prev, current) => ({
        target: 0,
        total: prev.total + current.total,
      }),
      {
        total: 0,
      }
    ).total;

    const overviewPageContent: IOverviewPageContent = {
      summaryCardsContent: [
        {
          cardHeading: "Current Balance",
          cardContent: enUSFormatter.format(
            overviewContent.balance?.current || 0
          ),
          isMainCard: true,
        },
        {
          cardHeading: "Income",
          cardContent: enUSFormatter.format(
            overviewContent.balance?.income || 0
          ),
        },
        {
          cardHeading: "Expenses",
          cardContent: enUSFormatter.format(
            overviewContent.balance?.expenses || 0
          ),
        },
      ],
      potsCardContent: {
        totalSaved: potsTotalSaved,
        potItems: [...overviewContent.pots].slice(0, 4),
      },
      budgetsCardContent: {
        spentBudget: overviewContent.budgets.totalSpent,
        totalBudget: overviewContent.budgets.totalMaximum,
        budgetItems: overviewContent.budgets.representBudgets,
      },
      transactionsCardContent: {
        transactions: overviewContent.transactions,
      },
      recurringBillsCardContent: overviewContent.recurringBillsSummary,
    };

    return overviewPageContent;
  };
