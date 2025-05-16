import type { Pot } from "~/api";

export interface IOverviewPotCard {
  potsCardContent?: {
    totalSaved: number;
    potItems: Pot[];
  };
}
