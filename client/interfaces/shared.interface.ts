import type {
  BudgetColorThemeEnum,
  PotColorThemeEnum,
} from "~/api/data-contracts";

export interface IContentCard {
  heading: string;
  colorTheme: BudgetColorThemeEnum | PotColorThemeEnum;
  dropdownOptions: IDropdownOption[];
}

export interface IDropdownOption {
  content: string;
  contentColor?: string;
  onClick: () => void;
}
