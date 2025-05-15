import { OverviewService, type OverviewContent, type Pot } from "~/api";
import type { IOverviewPotSection } from "~/components/overview/pot-card/pot-section.model";
import type { IOverviewSummaryCard } from "~/components/overview/summary-card/summary-card.model";

export interface IOverviewPageContent extends IOverviewPotSection {
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
    };

    return overviewPageContent;
  };
