import type { ChartData } from "chart.js";
import type {
  BudgetColorThemeEnum,
  PotColorThemeEnum,
} from "~/api/data-contracts";
import type { FormFieldTypes } from "./transactions.interface";
import type { Color } from "~/types/color";

export enum ButtonAppearanceEnum {
  Primary = 1,
  Secondary = 2,
  Danger = 3,
}

export interface IButton {
  type: "submit" | "reset" | "button";
  appearance: ButtonAppearanceEnum;
  isDisabled?: boolean;
  isLoading?: boolean;
  onClick?: (e: Event) => void;
}

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

export interface IDoughnutChart {
  data: ChartData;
  overlayNumber: number;
  totalNumber: number;
}

export interface IDropdown {
  preSelectedOption?: string;
  mobileIcon?: string;
  options: string[];
  label: string;
  forField: FormFieldTypes;
  onSelection: (field: FormFieldTypes, value: string) => void;
}

export enum InputEnumType {
  Text = 1,
  Email = 2,
  Password = 3,
  Number = 4,
  Search = 5,
}

export enum ModalDropdownEnumType {
  Color = 1,
  Text = 2,
}

export interface IInput {
  label?: string;
  value?: string;
  placeholder?: string;
  prefix?: string;
  type: InputEnumType;
  customInputHandler?: (e?: Event) => void;
}

export interface IModalTextDropdownSettings {
  type: ModalDropdownEnumType.Text;
  options: IModalDropdownItem[];
}

export interface IModalColorDropdownSettings {
  type: ModalDropdownEnumType.Color;
  options: IModalDropdownColorItem[];
}

export interface IModalDropdown {
  label?: string;
  settings: IModalColorDropdownSettings | IModalTextDropdownSettings;
  isDisabled?: boolean;
}

export enum ModalDropdownItemStatus {
  Selected = 1,
  Ready = 2,
  Used = 3,
}

export interface IModalDropdownItem {
  onSelect?: (value: string) => void;
  itemLabel: string;
  itemValue: string;
  status: ModalDropdownItemStatus;
}

export interface IModalDropdownColorItem extends IModalDropdownItem {
  itemValue: keyof typeof Color;
}
