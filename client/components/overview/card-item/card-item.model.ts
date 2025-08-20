import type {
  BudgetColorThemeEnum,
  PotColorThemeEnum,
} from "~/api/data-contracts";

export interface ICardItem {
  label: string;
  content: string;
  colorTheme: BudgetColorThemeEnum | PotColorThemeEnum;
}
