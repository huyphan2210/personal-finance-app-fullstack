import type { ChartData } from "chart.js";
import type {
  BudgetColorThemeEnum,
  PotColorThemeEnum,
} from "~/api/data-contracts";
import type { FormFieldTypes } from "./transactions.interface";
import type { Color } from "~/types/color";

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
}

export enum ModalDropdownItemStatus {
  Ready = 1,
  Selected = 2,
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
