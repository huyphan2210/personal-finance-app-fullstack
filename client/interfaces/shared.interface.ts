import type {
  BudgetColorThemeEnum,
  PotColorThemeEnum,
} from "~/api/data-contracts";

export interface IContentCard {
  heading: string;
  colorTheme: BudgetColorThemeEnum | PotColorThemeEnum;
  dropdownOptions: IContentCardDropdownOption[];
}

export interface IContentCardDropdownOption {
  content: string;
  contentColor?: string;
  onClick: () => void;
}

export enum InputEnumType {
  Text = 1,
  Email = 2,
  Password = 3,
  Number = 4,
}

export interface IInput {
  label?: string;
  placeholder?: string;
  prefix?: string;
  type: InputEnumType;
}
