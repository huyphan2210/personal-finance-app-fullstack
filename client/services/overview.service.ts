import { OverviewService } from "~/api";
import type { IOverviewBudgetsCard } from "~/components/overview/budgets-card/budgets-card.model";
import type { IOverviewPotCard } from "~/components/overview/pot-card/pot-card.model";
import type { IOverviewSummaryCard } from "~/components/overview/summary-card/summary-card.model";
import type { IOverviewTransactionsCard } from "~/components/overview/transactions-card/transactions-card.model";

export interface IOverviewPageContent
  extends IOverviewPotCard,
    IOverviewBudgetsCard,
    IOverviewTransactionsCard {
  summaryCardsContent: IOverviewSummaryCard[];
}

export const getSummaryContent: () => Promise<IOverviewPageContent> =
  async () => {
    const overviewContent = await OverviewService.getOverview();
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

    const budgets = overviewContent.budgets;

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
        spentBudget: 338,
        budgetItems: budgets,
      },
      transactionsCardContent: {
        transactions: overviewContent.transactions,
      },
    };

    return overviewPageContent;
  };
