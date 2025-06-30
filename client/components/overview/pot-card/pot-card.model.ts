import { type Pot } from "~/api/data-contracts";

export interface IOverviewPotCard {
  potsCardContent?: {
    totalSaved: number;
    potItems: Pot[];
  };
}
