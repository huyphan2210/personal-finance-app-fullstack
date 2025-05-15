import type { Pot } from "~/api";

export interface IOverviewPotSection {
  potsCardContent?: {
    totalSaved: number;
    potItems: Pot[];
  };
}
